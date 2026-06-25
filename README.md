# ⚡ SportMax — Sport Do'koni

O'zbekiston bozori uchun to'liq sport marketplace veb-sayti.  
Streamlit + sof HTML/CSS/JS bilan qurilgan.

---

## ✨ Funksiyalar

| Bo'lim | Tavsif |
|--------|--------|
| **Kategoriyalar** | 6 tab: Trenajorlar, Sport Kiyim, Aksessuarlar, Sport Ovqat, Futbol, Tennis — har birida 6 ta mahsulot |
| **Savat (Cart)** | Mahsulot qo'shish, miqdorini o'zgartirish, o'chirish — real vaqtda summa hisoblanadi |
| **Buyurtma** | Savatdagi mahsulotlar bilan to'liq buyurtma formasi |
| **Top 10** | Eng ko'p sotilgan 10 ta mahsulot ranking badge bilan |
| **Porsiya Kalkulyatori** | Necha kunga yetishi, 1 porsiya narxi, kunlik va oylik xarajat |
| **Kaloriya Kalkulyatori** | BMR, TDEE, massa terish / yog' yoqish normalari + makro diagramma |
| **Protein Kalkulyatori** | Vazn va maqsad bo'yicha kunlik protein norma + qo'shimchadan kerak miqdor |
| **Xizmatlar** | Yetkazib berish, to'lov, kafolat, sport maslahati |

---

## 🚀 Ishga tushirish

```bash
# 1. Repozitoriyani klonlash
git clone https://github.com/YOUR_USERNAME/sportmax.git
cd sportmax

# 2. Virtual muhit (tavsiya etiladi)
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Streamlit o'rnatish
pip install streamlit

# 4. Ilovani ishga tushirish
streamlit run app.py
```

Brauzerda avtomatik ochiladi: `http://localhost:8501`

---

## 📁 Fayl Tuzilmasi

```
sportmax/
├── app.py          # Streamlit ilovasi (index.html ni yuklaydi)
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

- **Font**: Barlow Condensed (sarlavhalar) + Inter (matn)
- **Rang palitasi**: Yashil #22c55e + Qora #0a0a0a + Oq #ffffff
- **Responsive**: Mobil (600px), planshet (900px), desktop (1200px)

---

## 🌐 GitHub Pages (faqat HTML)

1. `index.html` ni GitHub reposiga yuklang
2. Settings → Pages → Source: `main` branch `/root`
3. Saytingiz `https://YOUR_USERNAME.github.io/sportmax/` da ochiladi

---

## 📞 Aloqa

- **Sayt**: sportmax.uz
- **Telefon**: +998 71 234-56-78
- **Email**: info@sportmax.uz

---

© 2026 SportMax. Barcha huquqlar himoyalangan.
