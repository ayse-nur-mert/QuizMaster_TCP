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
    
    # 5 adet soru sor
    for question_data in questions_data['questions']:
        question_text = f"{question_data['question']}\n"
        for option, text in question_data['options'].items():
            question_text += f"{option}) {text} "
        server.send_question(client_socket, question_text)
        answer = server.receive_answer(client_socket)
        if answer:
            if answer.upper() == question_data['answer']:
                print("Doğru cevap!")
                continue  # Doğru cevap verildiğinde bir sonraki soruya geç
            else:
                print("Yanlış cevap. Doğru cevap: ", question_data['answer'])
                break  # Yanlış cevap verildiğinde döngüden çık
        else:
            print('Cevap alınamadı.')
            break  # Bağlantı kesilirse döngüden çık

    server.close() 