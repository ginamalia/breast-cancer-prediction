# 🌟 Breast Cancer Prediction

Aplikasi prediksi kanker payudara menggunakan **Machine Learning (Random Forest Classifier)** dengan **Streamlit** sebagai GUI. Model dilatih menggunakan dataset **Breast Cancer Wisconsin** dari Scikit-Learn.

## 📚 Dataset
Dataset yang digunakan adalah **Breast Cancer Wisconsin** dari **scikit-learn**, yang berisi informasi karakteristik tumor untuk menentukan apakah tumor tersebut **jinak (benign)** atau **ganas (malignant)**.

- **Fitur**: 30 fitur numerik terkait karakteristik tumor.
- **Target**:
  - `0` = Benign (Jinak)
  - `1` = Malignant (Ganas)

## 🛠️ Instalasi
Pastikan Anda sudah menginstal **Python 3.x** dan **pip**. Jika ingin menggunakan virtual environment, jalankan:

```sh
python -m venv venv
```
Aktifkan environment:
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

Kemudian, install dependensi:
```sh
pip install -r requirements.txt
```

## 👨‍💻 Cara Menjalankan Aplikasi
1. **Clone repository ini**:
   ```sh
   git clone https://github.com/ginamalia/breast-cancer-prediction.git
   cd breast-cancer-prediction
   ```

2. **Jalankan Streamlit**:
   ```sh
   streamlit run app.py
   ```

3. **Akses aplikasi di browser**: `http://localhost:8501`

## 🔢 Fitur
- ✅ **Input Manual Fitur Tumor** melalui GUI.
- ✅ **Prediksi Kanker Payudara** (Jinak/Ganas) dengan **Random Forest**.
- ✅ **Akurasi Model Ditampilkan** setelah pelatihan.
- ✅ **Confusion Matrix untuk Evaluasi Model**.
- ✅ **Visualisasi Data dengan Seaborn & Matplotlib**.

## 💻 Teknologi yang Digunakan
- **Python** (3.x)
- **Scikit-Learn** (Machine Learning Model)
- **Pandas & NumPy** (Data Processing)
- **Streamlit** (GUI/Frontend)
- **Matplotlib & Seaborn** (Visualisasi)
- **GitHub** (Version Control)

## 📊 Hasil Evaluasi Model
Model **Random Forest Classifier** mencapai akurasi sekitar **94%** berdasarkan data uji.

## 🔧 Pengembangan Selanjutnya
- [ ] Menambahkan opsi untuk memilih model ML lain (KNN, SVM, dll.).
- [ ] Mengimplementasikan **Feature Importance** untuk analisis lebih lanjut.
- [ ] Menambahkan opsi **upload CSV** untuk batch prediksi.
- [ ] Deploy aplikasi ke **Streamlit Cloud** atau **Heroku**.

## 🌟 Kontribusi
Pull Request dipersilakan! Pastikan untuk membuat branch baru sebelum mengirim PR.

---
Dibuat dengan ❤ oleh Ridhaka Gina Amalia
