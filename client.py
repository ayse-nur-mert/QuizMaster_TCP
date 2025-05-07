import socket

# Yarışmacı (İstemci) uygulaması
class YarismaciClient:
    def __init__(self, host='127.0.0.1', port=4337):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print('Sunucuya bağlanıldı.')
        except ConnectionError as e:
            print(f'Bağlantı hatası: {e}')

    def close(self):
        self.client_socket.close()
        print('Bağlantı kapatıldı.')

    def send_answer(self, answer):
        try:
            self.client_socket.sendall(answer.encode())
        except Exception as e:
            print(f'Cevap gönderme hatası: {e}')

    def receive_question(self):
        try:
            question = self.client_socket.recv(1024).decode()
            return question
        except Exception as e:
            print(f'Soru alma hatası: {e}')
            return None

# Örnek kullanım
if __name__ == "__main__":
    client = YarismaciClient()
    client.connect()
    while True:
        question = client.receive_question()
        if question:
            print(f'Soru: {question}')
            user_answer = input("Cevabınızı girin (A, B, C, D): ")
            client.send_answer(user_answer)  # Kullanıcıdan alınan cevap
        else:
            print('Sunucu ile bağlantı kesildi.')
            break  # Bağlantı kesilirse döngüden çık
    client.close() 