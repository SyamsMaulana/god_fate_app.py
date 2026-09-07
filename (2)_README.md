# God of FATE Operations

> *Inverted Pyramid Framework & Al-Haqq Protocol*  
> Author / Creator: Syams Maulana / ICAM (GOD•MauL)

## 📌 Deskripsi Sistem
**God of FATE Operations** adalah sistem manajemen operasional berbasis Command Line Interface (CLI) yang dirancang untuk administrasi guild Trading Card Game (TCG), pencatatan rekor pertandingan, penyelenggaraan turnamen sistem Swiss-Pairing, serta modul analisis kecerdasan buatan (*TCG AI*) berbasis probabilitas hipergeometrik.

## 🚀 Fitur Utama
1. **Sistem Utama (`god_fate_app.py`):**
   - Registrasi Tim & Agen serta pemantauan *archetype* deck andalan.
   - Pencatatan rekor duel dan *match history* secara *real-time*.
   - Kalkulator win-rate dan leaderboard agen guild.
   - Manajemen peserta turnamen dan generator Swiss-Pairing otomatis dengan sistem *Bye*.
   - Ekspor data laporan ke format CSV.

2. **Modul TCG AI (`tcg_ai_module.py`):**
   - Simulator peluang *opening hand* menggunakan distribusi hipergeometrik.
   - Analisis taktik dan rekomendasi strategi *deck archetype*.
   - Generator laporan analitis berwatermark digital *Al-Haqq Protocol*.

## 🛠️ Cara Menjalankan
Pastikan Python telah terpasang di perangkatmu (Termux / Desktop), lalu jalankan perintah berikut:
```bash
# Menjalankan menu operasional utama guild
python god_fate_app.py

# Menjalankan modul analisis TCG AI
python tcg_ai_module.py
