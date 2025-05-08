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
    
    # Ödül mesajları - program sonlandığında kontrol için
    reward_messages = [
        "Linç Yükleniyor",
        "Önemli olan katılmaktı",
        "İki birden büyüktür",
        "Buralara kolay gelmedik",
        "Sen bu işi biliyorsun",
        "Harikasın"
    ]
    
    print("Bilgi Yarışmasına Hoş Geldiniz!")
    print("Toplam 5 soru sorulacak ve 2 joker hakkınız var:")
    print("- Seyirciye Sorma (S): Seyircilerin tahminlerini gösterir")
    print("- Yarı Yarıya (Y): İki yanlış şıkkı eler")
    print("İyi şanslar!\n")
    
    try:
        while True:
            question = client.receive_question()
            if question:
                # Program sonlandırma mesajı
                if question == "Program sonlandırılıyor.":
                    print("Program sonlandırılıyor...")
                    break
                    
                # Ödül mesajı kontrolü
                if any(message in question for message in reward_messages):
                    print(f"Yarışma sonucu: {question}")
                    break
                    
                # Normal soru veya joker cevabı
                print(f'{question}')
                user_answer = input()
                client.send_answer(user_answer)
            else:
                print('Sunucu ile bağlantı kesildi.')
                break
    except KeyboardInterrupt:
        print("\nYarışmadan çıkılıyor...")
    finally:
        client.close() 