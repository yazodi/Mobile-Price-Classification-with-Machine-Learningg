# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Veriyi oku
df = pd.read_csv("mobile_prices.csv")

# Özellikleri ve hedefi ayır
X = df.drop("price_range", axis=1)
y = df["price_range"]

# Eğitim-test bölmesi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğit
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Doğruluk
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Modeli kaydet
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
