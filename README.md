# QuizMaster\_TCP

**QuizMaster\_TCP**, Python kullanılarak geliştirilen basit bir bilgi yarışması oyunudur. Oyunda üç ana bileşen vardır:

* 🎲 **Joker** (Yardım sunucusu)
* 🖥️ **Sunucu**
* 👤 **İstemciler**

## 📌 Nasıl Çalışır?

* **Joker**, oyuncuların kullanabileceği yardım seçeneklerini yönetir.
* **Sunucu**, istemcilerle iletişim kurar, soruları gönderir ve cevapları değerlendirir.
* **İstemciler**, sunucuya bağlanır, soruları yanıtlar ve isterse joker kullanır.

## ⚙️ Çalıştırma Sırası

Projeyi çalıştırmak için üç ayrı terminal açıp şu sırayla başlatmanız yeterlidir:

1. `joker.py`
2. `server.py`
3. `client.py`

### Örnek:

```bash
python joker.py
python server.py
python client.py
```

Her şey otomatik çalışır, ekstra soket ayarı yapmanıza gerek yoktur.

## 📁 Dosyalar

* `joker.py` → Joker sunucusu
* `server.py` → Ana quiz sunucusu
* `client.py` → Oyuncu istemcisi
* `questions.txt` → Soruların bulunduğu dosya

## ✅ Gereksinimler

* Python 3
