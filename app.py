import streamlit as st
import numpy as np
import joblib
import pandas as pd
from sklearn.datasets import load_breast_cancer

# Load model
model = joblib.load('random_forest_model.pkl')

# Load feature names dari dataset breast cancer
data = load_breast_cancer()
feature_names = data.feature_names

# Judul aplikasi
st.title("Prediksi Kanker Payudara")

# Input fitur oleh pengguna
st.sidebar.header("Masukkan Nilai Fitur")

# Buat inputan sesuai jumlah fitur
user_input = []
for feature in feature_names:
    value = st.sidebar.number_input(f"{feature}", min_value=0.0, step=0.1)
    user_input.append(value)

# Ubah input ke dalam bentuk array numpy
input_data = np.array(user_input).reshape(1, -1)

# Prediksi saat tombol ditekan
if st.sidebar.button("Prediksi"):
    prediction = model.predict(input_data)
    prediksi_label = "Jinak" if prediction[0] == 0 else "Ganas"
    
    # Tampilkan hasil
    st.subheader("Hasil Prediksi")
    st.write(f"Model memprediksi bahwa tumor tersebut bersifat: **{prediksi_label}**")
