import sqlite3

# Veritabanı bağlantısı oluşturalım
conn = sqlite3.connect('veritabani.db')
cursor = conn.cursor()

# Konular tablosu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS konular (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        konu TEXT NOT NULL
    )
''')

# Sorular tablosu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sorular (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        konu_id INTEGER NOT NULL,
        soru TEXT NOT NULL,
        cevap_a TEXT NOT NULL,
        cevap_b TEXT NOT NULL,
        cevap_c TEXT NOT NULL,
        cevap_d TEXT NOT NULL,
        dogru_cevap TEXT NOT NULL,
        FOREIGN KEY (konu_id) REFERENCES konular (id)
    )
''')


# Sınav konularımız
konular = [
    "Python'da AI Geliştirme",
    "Bilgisayar Görüşü",
    "NLP (Nöro-dilbilim)",
    "Python Uygulamalarında AI Modelleri Uygulama"
]

# Konuları SQLite veritabanına ekliyoruz
for konu in konular:
    cursor.execute('''
        INSERT INTO konular (konu)
        VALUES (?)
    ''', (konu,))

# Konu id'lerini alıyoruz
cursor.execute('SELECT * FROM konular')
konu_rows = cursor.fetchall()

# Tuple'ları sözlüğe dönüştürelim
konu_dict = {row[1]: row[0] for row in konu_rows}



# Sorularımız
sorular = {
    "Python'da AI Geliştirme": [
        {
            "soru": "Python'da bir yapay zeka programı yazmak için hangi kütüphaneyi kullanabilirsin?",
            "cevap_a": "TensorFlow",
            "cevap_b": "Photoshop",
            "cevap_c": "Excel",
            "cevap_d": "Minecraft 🙂",
            "dogru_cevap": "a"
        },
        {
            "soru": "Makine öğrenmesi, bilgisayarların ne yapmasını sağlar?",
            "cevap_a": "Kendi kendine yeni şeyler öğrenmesini",
            "cevap_b": "Daha hızlı çalışmasını",
            "cevap_c": "Daha az enerji harcamasını",
            "cevap_d": "İnternete bağlanmasını",
            "dogru_cevap": "a"
        },
        {
            "soru": "Hangisi bir yapay zeka uygulaması için kullanılan bir algoritma türüdür?",
            "cevap_a": "Toplama",
            "cevap_b": "Çıkarma",
            "cevap_c": "Karar Ağacı",
            "cevap_d": "Çarpma",
            "dogru_cevap": "c"
        },
        {
            "soru": "Yapay zeka programları hangi alanlarda kullanılabilir?",
            "cevap_a": "Sağlık, oyun, otomotiv",
            "cevap_b": "Eğitim, sanat, müzik",
            "cevap_c": "Hepsi",
            "cevap_d": "Hiçbiri",
            "dogru_cevap": "c"
        },
        {
            "soru": "Python'da bir yapay zeka projesine başlamadan önce ne yapmalısın?",
            "cevap_a": "Bilgisayarını kapatmalısın.",
            "cevap_b": "Bir oyun oynamalısın.",
            "cevap_c": "Bir problem belirlemeli ve veri toplamalısın.",
            "cevap_d": "Televizyon izlemelisin.",
            "dogru_cevap": "c"
        }
    ],
    "Bilgisayar Görüşü": [
        {
            "soru": "Bilgisayar görüşü, bilgisayarların ne yapmasını sağlar?",
            "cevap_a": "Görüntüleri ve videoları anlamasını",
            "cevap_b": "Daha hızlı çalışmasını",
            "cevap_c": "Daha az enerji harcamasını",
            "cevap_d": "İnternete bağlanmasını",
            "dogru_cevap": "a"
        },
        {
            "soru": "Hangisi bir bilgisayar görüşü uygulaması örneğidir?",
            "cevap_a": "Yüz tanıma",
            "cevap_b": "Müzik çalma",
            "cevap_c": "Metin yazma",
            "cevap_d": "Hesaplama yapma",
            "dogru_cevap": "a"
        },
        {
            "soru": "Bilgisayar görüşü hangi alanlarda kullanılabilir?",
            "cevap_a": "Otonom araçlar",
            "cevap_b": "Tıbbi görüntüleme",
            "cevap_c": "Güvenlik sistemleri",
            "cevap_d": "Hepsi",
            "dogru_cevap": "d"
        },
        {
            "soru": "Bilgisayar görüşü sistemleri nasıl eğitilir?",
            "cevap_a": "Ona bol miktarda resim ve video göstererek",
            "cevap_b": "Ona kitap okuyarak",
            "cevap_c": "Ona müzik dinleterek",
            "cevap_d": "Ona film izleterek",
            "dogru_cevap": "a"
        },
        {
            "soru": "Bilgisayar görüşü ile ne tür problemler çözülebilir?",
            "cevap_a": "Nesne tanıma, görüntü sınıflandırma, hareket takibi",
            "cevap_b": "Duygu analizi, metin çevirisi, özetleme",
            "cevap_c": "Ses tanıma, konuşma sentezi, sesli asistanlar",
            "cevap_d": "Hiçbiri",
            "dogru_cevap": "a"
        }
    ],
    "NLP (Nöro-dilbilim)": [
        {
            "soru": "NLP, bilgisayarların ne yapmasını sağlar?",
            "cevap_a": "İnsan dilini anlamasını ve işlemesini",
            "cevap_b": "Daha hızlı çalışmasını",
            "cevap_c": "Daha az enerji harcamasını",
            "cevap_d": "İnternete bağlanmasını",
            "dogru_cevap": "a"
        },
        {
            "soru": "Hangisi bir NLP uygulaması örneğidir?",
            "cevap_a": "Çeviri uygulamaları",
            "cevap_b": "Hesap makineleri",
            "cevap_c": "Oyunlar",
            "cevap_d": "Resim düzenleme programları",
            "dogru_cevap": "a"
        },
        {
            "soru": "NLP hangi alanlarda kullanılabilir?",
            "cevap_a": "Müşteri hizmetleri chatbotları",
            "cevap_b": "Sosyal medya analizi",
            "cevap_c": "Duygu analizi",
            "cevap_d": "Hepsi",
            "dogru_cevap": "d"
        },
        {
            "soru": "NLP'de bir metni analiz etmek için hangi yöntemler kullanılır?",
            "cevap_a": "Kelimelerin sayılması",
            "cevap_b": "Cümlelerin uzunluğunun ölçülmesi",
            "cevap_c": "Kelimelerin anlamsal ilişkilerinin incelenmesi",
            "cevap_d": "Hepsi",
            "dogru_cevap": "d"
        },
        {
            "soru": "NLP ile ne tür problemler çözülebilir?",
            "cevap_a": "Spam filtreleme, otomatik metin özetleme, dil çevirisi",
            "cevap_b": "Görüntü sınıflandırma, nesne tanıma, yüz tanıma",
            "cevap_c": "Ses tanıma, konuşma sentezi, sesli asistanlar",
            "cevap_d": "Hiçbiri",
            "dogru_cevap": "a"
        }
    ],
    "Python Uygulamalarında AI Modelleri Uygulama": [
        {
            "soru": "Eğittiğiniz bir yapay zeka modelini nasıl kullanabilirsiniz?",
            "cevap_a": "Bir web sitesine entegre ederek",
            "cevap_b": "Bir mobil uygulamaya ekleyerek",
            "cevap_c": "Bir cihazda çalıştırarak",
            "cevap_d": "Hepsi",
            "dogru_cevap": "d"
        },
        {
            "soru": "Bir yapay zeka modelini eğitmek için neden çok fazla veriye ihtiyaç duyarsınız?",
            "cevap_a": "Daha doğru ve güvenilir sonuçlar elde etmek için",
            "cevap_b": "Daha hızlı çalışması için",
            "cevap_c": "Daha az enerji harcaması için",
            "cevap_d": "İnternete bağlanması için",
            "dogru_cevap": "a"
        },
        {
            "soru": "Bir yapay zeka modelinin başarısını nasıl ölçersiniz?",
            "cevap_a": "Doğru tahminlerin sayısına bakarak",
            "cevap_b": "Ne kadar hızlı çalıştığına bakarak",
            "cevap_c": "Ne kadar az enerji harcadığına bakarak",
            "cevap_d": "Ne kadar çok veri kullandığına bakarak",
            "dogru_cevap": "a"
        },
        {
            "soru": "Yapay zeka modelleri hangi sektörlerde kullanılabilir?",
            "cevap_a": "Sağlık, finans, perakende",
            "cevap_b": "Ulaşım, eğitim, eğlence",
            "cevap_c": "Hepsi",
            "cevap_d": "Hiçbiri",
            "dogru_cevap": "c"
        },
        {
            "soru": "Yapay zeka modellerini kullanmanın etik sonuçları nelerdir?",
                "cevap_a": "Önyargı, ayrımcılık, gizlilik",
                "cevap_b": "İşsizlik, güvenlik riskleri, kontrol kaybı",
                "cevap_c": "Hepsi",
                "cevap_d": "Hiçbiri",
                "dogru_cevap": "c"
            }
        ]
    }

# Konu ID'lerini kullanarak
for konu_adi, sorular_listesi in sorular.items():
    konu_id = konu_dict[konu_adi]  # Konu adına göre ID'yi al
    for soru_dict in sorular_listesi:
        cursor.execute('''
            INSERT INTO sorular (konu_id, soru, cevap_a, cevap_b, cevap_c, cevap_d, dogru_cevap)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (konu_id, soru_dict["soru"], soru_dict["cevap_a"], soru_dict["cevap_b"], soru_dict["cevap_c"], soru_dict["cevap_d"], soru_dict["dogru_cevap"]))

conn.commit()
conn.close()
print("Sorular başarıyla veritabanına eklendi!")
