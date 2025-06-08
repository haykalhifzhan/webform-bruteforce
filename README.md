# 🛡️ Web Form Brute Force Tool

Sebuah tools sederhana yang saya buat untuk kebutuhan pembelajaran dan simulasi keamanan web — khususnya dalam melakukan **brute force** pada form login berbasis HTML.

> ❗ Tools ini hanya untuk tujuan edukasi dan **tidak boleh digunakan untuk menyerang sistem tanpa izin**.

## 🚀 Fitur
- Mencoba kombinasi username dan password dari wordlist
- Mendukung input melalui file eksternal
- Deteksi keberhasilan login berdasarkan teks respon (misal: "Login Failed")

## 🧠 Cara Pakai
1. Siapkan target URL login form.
2. Masukkan username dan password wordlist ke `usernames.txt` dan `passwords.txt`.
3. Jalankan script:

```bash
python bruteforce_login.py
