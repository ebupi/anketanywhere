# Quiz Uygulaması

Bu proje, Python ve Flask kullanılarak geliştirilmiş basit bir quiz uygulamasıdır. Kullanıcılar, AI, makine öğrenimi, bilgisayar görüşü ve NLP (Doğal Dil İşleme) gibi konularda soruları yanıtlayabilir ve puanlarını görebilirler. Ayrıca, kullanıcıların isim-soyisim ve hobiler gibi kişisel bilgilerini de kaydedebilir.

## Özellikler

- **Çoktan Seçmeli Sorular:** Kullanıcılar, 8 farklı soruyu yanıtlayabilir.
- **Puan Hesaplama:** Her doğru cevap için 12.5 puan eklenir ve toplam puan hesaplanır.
- **En Yüksek Puan:** Uygulama, şimdiye kadar alınan en yüksek puanı gösterir.
- **Kişisel Bilgiler:** Kullanıcılar, isim-soyisim ve hobiler gibi bilgilerini girebilir.
- **Veritabanı Kaydı:** Kullanıcıların cevapları ve puanları SQLite veritabanında saklanır.

## Kurulum

1. **Gereksinimler:**
   - Python 3.x
   - Flask
   - Flask-SQLAlchemy

2. **Bağımlılıkları Yükle:**
   Proje klasöründe terminali açın ve aşağıdaki komutu çalıştırın:
   ```bash
   pip install flask flask-sqlalchemy
   ```

3. **Uygulamayı Çalıştır:**
   Terminalde aşağıdaki komutu çalıştırarak Flask uygulamasını başlatın:
   ```bash
   python app.py
   ```

4. **Tarayıcıda Aç:**
   Uygulama başladıktan sonra, tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

## Klasör Yapısı

```
quiz-app/
│
├── app.py                  # Flask uygulamasının ana dosyası
├── instance/               # Özel dosyalar için Flask'ın varsayılan klasörü
│   └── data.db             # SQLite veritabanı (otomatik oluşturulur)
├── templates/              # HTML şablonlarının bulunduğu klasör
│   └── index.html          # Quiz formunun HTML şablonu
├── static/                 # Statik dosyaların bulunduğu klasör
│   └── style.css           # Stil dosyası
└── requirements.txt        # Bağımlılıkların listesi
```

## Katkıda Bulunma

Bu proje açık kaynaklıdır. Katkıda bulunmak isterseniz, lütfen bir "pull request" gönderin. Önerileriniz ve geri bildirimleriniz her zaman memnuniyetle karşılanır!
