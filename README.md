# ⚙ QurilishMart — Qurilish Mollari Internet Do'koni

O'zbekiston bozori uchun to'liq qurilish mollari veb-sayti.  
Streamlit + sof HTML/CSS/JS bilan qurilgan.

---

## ✨ Funksiyalar

| Bo'lim | Tavsif |
|--------|--------|
| **Kategoriyalar** | 4 ta tab: Sement, Kafel, Bo'yoq, Laminat — har birida 6 ta mahsulot, rasm va narx bilan |
| **Savat (Cart)** | Mahsulot qo'shish, miqdorini o'zgartirish, o'chirish — real vaqtda summa hisoblanadi |
| **B2B Buyurtma** | Savatdagi mahsulotlar rasmlari, narxlari va jami summa bilan ko'rsatiladi; buyurtma berish formasi |
| **Tavsiyalar** | Eng ko'p sotilgan 10 ta mahsulot (har toifadan), ranking badge bilan |
| **Kalkulyator** | Kafel maydoni, bo'yoq litri, sement kilogrami — uchta alohida hisoblash vositasi |
| **Xizmatlar** | Yetkazib berish, to'lov, kafolat, maslahat |

---

## 🚀 Ishga tushirish

### Talab qilinadigan muhit
- Python 3.8+
- pip

### O'rnatish

```bash
# 1. Repozitoriyani klonlash
git clone https://github.com/YOUR_USERNAME/qurilishmart.git
cd qurilishmart

# 2. Virtual muhit (ixtiyoriy, tavsiya etiladi)
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Kutubxonalarni o'rnatish
pip install streamlit

# 4. Ilovani ishga tushirish
streamlit run app.py
```

Brauzerda avtomatik ochiladi: `http://localhost:8501`

---

## 📁 Fayl Tuzilmasi

```
qurilishmart/
├── app.py          # Streamlit ilovasi (HTML ni yuklaydi)
├── index.html      # Butun frontend (HTML + CSS + JS)
├── README.md       # Ushbu fayl
└── requirements.txt
```

---

## 📦 requirements.txt

```
streamlit>=1.32.0
```

---

## 🎨 Dizayn

- **Font**: Space Grotesk (sarlavhalar) + Inter (matn)
- **Rang palitasi**: Ildiz o'rtuvi (#f97316) + Qora (#111827) + Oq (#ffffff)
- **Responsive**: Mobil (600px), planshet (900px), desktop (1200px)

---

## 🌐 GitHub Pages (faqat HTML)

Agar faqat HTML versiyasini joylashtirmoqchi bo'lsangiz:

1. `index.html` ni GitHub reposiga yuklang
2. Settings → Pages → Source: `main` branch `/root`
3. Saytingiz `https://YOUR_USERNAME.github.io/qurilishmart/` da ochiladi

---

## 📞 Aloqa

- **Sayt**: qurilishmart.uz
- **Telefon**: +998 71 234-56-78
- **Email**: info@qurilishmart.uz

---

© 2026 QurilishMart. Barcha huquqlar himoyalangan.
