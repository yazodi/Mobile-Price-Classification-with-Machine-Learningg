import streamlit as st
import pickle
import numpy as np

# Modeli yükle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📱 Mobile Price Range Prediction")
st.write("Telefon özelliklerine göre fiyat aralığını tahmin edin. (0: En düşük, 3: En yüksek)")

# 20 özelliği kullanıcıdan alalım:
battery_power = st.slider("🔋 Battery Power (mAh)", 500, 2000, 1000)
blue = st.selectbox("📶 Bluetooth Var mı?", [0, 1])
clock_speed = st.slider("⏱ Clock Speed (GHz)", 0.5, 3.0, 1.5)
dual_sim = st.selectbox("📱 Çift SIM Var mı?", [0, 1])
fc = st.slider("🤳 Ön Kamera (MP)", 0, 20, 5)
four_g = st.selectbox("📡 4G Desteği", [0, 1])
int_memory = st.slider("💾 Dahili Hafıza (GB)", 2, 64, 16)
mobile_wt = st.slider("⚖️ Ağırlık (gram)", 80, 250, 150)
n_cores = st.slider("🧠 İşlemci Çekirdek Sayısı", 1, 8, 4)
pc = st.slider("📸 Arka Kamera (MP)", 0, 20, 13)
px_height = st.slider("🔳 Piksel Yüksekliği", 0, 1960, 500)
px_width = st.slider("🔲 Piksel Genişliği", 0, 2000, 800)
ram = st.slider("🧠 RAM (MB)", 256, 4000, 1024)
sc_h = st.slider("📱 Ekran Yüksekliği (cm)", 5, 20, 12)
sc_w = st.slider("📱 Ekran Genişliği (cm)", 0, 18, 7)
talk_time = st.slider("📞 Konuşma Süresi (saat)", 2, 20, 10)
three_g = st.selectbox("📡 3G Var mı?", [0, 1])
touch_screen = st.selectbox("🖱 Dokunmatik Ekran Var mı?", [0, 1])
wifi = st.selectbox("📶 Wi-Fi Desteği", [0, 1])

# Girdi vektörü (20 özellik)
input_data = np.array([[battery_power, blue, clock_speed, dual_sim, fc,
                        four_g, int_memory, mobile_wt, n_cores, pc,
                        px_height, px_width, ram, sc_h, sc_w,
                        talk_time, three_g, touch_screen, wifi]])

# Tahmin
if st.button("Tahmin Et"):
    prediction = model.predict(input_data)[0]
    st.success(f"📊 Tahmini Fiyat Aralığı: {prediction} (0: düşük, 3: yüksek)")
