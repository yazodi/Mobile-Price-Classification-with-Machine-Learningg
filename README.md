# 📱 Mobile Price Classification with Machine Learning

Bu proje, bir cep telefonunun donanımsal özelliklerine göre hangi fiyat aralığında olduğunu tahmin eden bir makine öğrenmesi modelidir.  
Streamlit arayüzü ile kullanıcı, telefonun teknik özelliklerini girerek tahmini fiyat aralığını öğrenebilir.

---

## 🔍 Problem Tanımı

Cep telefonları farklı donanım seviyelerinde sunulur. Bu proje, çeşitli teknik özelliklere bakarak bir telefonun fiyat segmentini (0: en düşük, 3: en yüksek) sınıflandırmayı amaçlar.

---

## 📦 Kullanılan Veri Seti

- Dataset: [`mobile_prices.csv`](./mobile_prices.csv)
- Sütun Sayısı: 21 (20 giriş + 1 hedef)
- Hedef (target): `price_range`

---

## 🛠 Kullanılan Özellikler

- `battery_power`, `ram`, `px_height`, `px_width`, `fc`, `pc`
- `bluetooth`, `dual_sim`, `four_g`, `three_g`, `wifi`
- `n_cores`, `int_memory`, `mobile_wt`
- `sc_h`, `sc_w`, `talk_time`, `clock_speed`, `touch_screen`

---

## 🔧 Kullanılan Kütüphaneler

- `pandas`
- `numpy`
- `scikit-learn`
- `streamlit`
- `pickle`

---

## 🤖 Model Bilgisi

- Algoritma: `RandomForestClassifier`
- Doğruluk: %X (eğitim sırasında çıktı)
- Model dosyası: [`model.pkl`](./model.pkl)

---

## 🚀 Nasıl Çalıştırılır?

### 1. Gerekli paketleri yükle:
```bash
pip install -r requirements.txt



Streamlit uygulamasını başlat
Demo (Opsiyonel)
Model Hugging Face'e yüklendiyse burada paylaşılabilir:

🔗 https://huggingface.co/yazodi


📦 Mobile Price Classification
 ┣ 📜 mobile_prices.csv
 ┣ 📜 model.pkl
 ┣ 📜 model.py
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md



kendiniz olşturun
 Örnek Girdi (sample_input.json)

{
  "battery_power": 1200,
  "blue": 1,
  "clock_speed": 1.6,
  "dual_sim": 1,
  "fc": 5,
  "four_g": 1,
  "int_memory": 32,
  "mobile_wt": 150,
  "n_cores": 4,
  "pc": 13,
  "px_height": 800,
  "px_width": 1200,
  "ram": 2048,
  "sc_h": 14,
  "sc_w": 7,
  "talk_time": 10,
  "three_g": 1,
  "touch_screen": 1,
  "wifi": 1
}



📌 Notlar
Eğitim amaçlı hazırlanmıştır.

Gerçek ticari modellerde daha fazla veri ve hiperparametre optimizasyonu gerekebilir.


🪪 Lisans
MIT License