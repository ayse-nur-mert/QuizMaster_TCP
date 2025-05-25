# QuizMaster\_TCP

**QuizMaster\_TCP**, TCP soket programlama ile yazılmış basit bir bilgi yarışması (quiz) oyunudur. Bir sunucu (server) ve birden fazla istemci (client) arasında çalışır.

## 📌 Proje Hakkında

* Sunucu, istemcileri dinler ve soruları gönderir.
* İstemciler, sunucuya bağlanıp soruları cevaplar.
* Her doğru cevap puan kazandırır.
* Oyun sonunda puanlar gösterilir.

## 🛠️ Kullanılan Teknolojiler

* C programlama dili
* TCP soketleri
* Terminal tabanlı çalışma

## 🚀 Nasıl Çalıştırılır?

### 1. Sunucuyu Derleyip Başlat:

```bash
gcc server.c -o server
./server [port]
```

### 2. İstemciyi Derleyip Başlat:

```bash
gcc client.c -o client
./client [IP adresi] [port]
```

### Örnek:

```bash
./server 8080
./client 127.0.0.1 8080
```

## 📁 Dosyalar

* `server.c` → Sunucu kodu
* `client.c` → İstemci kodu
* `questions.txt` → Quiz soruları
