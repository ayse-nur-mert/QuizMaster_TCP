import socket

# Joker (Sunucu) uygulaması
class JokerServer:
    def __init__(self, host='127.0.0.1', port=4338):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f'Joker sunucu {self.host}:{self.port} adresinde dinliyor.')

    def accept_program_server(self):
        program_socket, program_address = self.server_socket.accept()
        print(f'Bağlantı kabul edildi: {program_address}')
        return program_socket

    def process_joker_request(self, program_socket):
        try:
            request = program_socket.recv(1024).decode()
            # Joker işlemi burada yapılacak
            response = "A) 1991 (%40) B) 2000 (%25) C) 1989 (%30) D) 2010 (%5)"  # Örnek yanıt
            program_socket.sendall(response.encode())
        except Exception as e:
            print(f'Joker isteği işleme hatası: {e}')

    def close(self):
        self.server_socket.close()
        print('Joker sunucu kapatıldı.')

# Örnek kullanım
if __name__ == "__main__":
    joker_server = JokerServer()
    program_socket = joker_server.accept_program_server()
    joker_server.process_joker_request(program_socket)
    joker_server.close() 