import json
import socket

# JSON dosyasından soruları yükle
with open('questions.json', 'r') as file:
    questions_data = json.load(file)

# Program Sunucusu (Sunucu-İstemci) uygulaması
class ProgramServer:
    def __init__(self, host='127.0.0.1', port=4337):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f'Sunucu {self.host}:{self.port} adresinde dinliyor.')

    def accept_client(self):
        client_socket, client_address = self.server_socket.accept()
        print(f'Bağlantı kabul edildi: {client_address}')
        return client_socket

    def send_question(self, client_socket, question):
        try:
            client_socket.sendall(question.encode())
        except Exception as e:
            print(f'Soru gönderme hatası: {e}')

    def receive_answer(self, client_socket):
        try:
            answer = client_socket.recv(1024).decode()
            return answer
        except Exception as e:
            print(f'Cevap alma hatası: {e}')
            return None

    def close(self):
        self.server_socket.close()
        print('Sunucu kapatıldı.')

# Örnek kullanım
if __name__ == "__main__":
    server = ProgramServer()
    client_socket = server.accept_client()
    
    # Ödül mesajları
    reward_messages = [
        "Linç Yükleniyor",
        "Önemli olan katılmaktı",
        "İki birden büyüktür",
        "Buralara kolay gelmedik",
        "Sen bu işi biliyorsun",
        "Harikasın"
    ]
    
    # 5 adet soru sor
    for index, question_data in enumerate(questions_data['questions']):
        question_text = f"{question_data['question']}\n"
        for option, text in question_data['options'].items():
            question_text += f"{option}) {text} "
        server.send_question(client_socket, question_text)
        answer = server.receive_answer(client_socket)
        if answer:
            if answer.upper() == question_data['answer']:
                print("Doğru cevap!")
                if index == len(questions_data['questions']) - 1:
                    server.send_question(client_socket, reward_messages[index + 1])  # Tüm sorular doğruysa en yüksek ödül
                    server.send_question(client_socket, "Program sonlandırılıyor.")  # Program sonlandırma mesajı
                    break  # Tüm sorular doğruysa döngüden çık
            else:
                print("Yanlış cevap. Doğru cevap: ", question_data['answer'])
                server.send_question(client_socket, "Önemli olan katılmaktı")  # Yanlış cevap verildiğinde sadece bu mesaj
                break  # Yanlış cevap verildiğinde döngüden çık
        else:
            print('Cevap alınamadı.')
            break  # Bağlantı kesilirse döngüden çık

    # İstemciye kapanış sinyali gönder
    server.send_question(client_socket, "Program sonlandırılıyor.")
    server.close()  # Programı sonlandır
    exit()  # Çıkış yap 