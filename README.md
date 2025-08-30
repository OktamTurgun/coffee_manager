# ☕ Coffee Bar Manager

![Coffee Bar](https://img.shields.io/badge/Project-CoffeeBarManager-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0-orange?style=for-the-badge)

## Loyihaning maqsadi

**Coffee Bar Manager** — bu kichik kafe yoki coffee bar uchun mahsulotlarni boshqarish, savdolarni kuzatish va xarajatlarni nazorat qilish dasturi.  
Loyiha o'quv maqsadida yozilgan bo'lib, Python modullaridan foydalanishni, fayllar bilan ishlashni va dasturiy arxitekturani yaxshiroq tushunishga yordam beradi.

---

## Funksiyalar

### ✅ Asosiy imkoniyatlar:
- ✅ Mahsulotlar bilan to'liq ishlash (qo'shish, yangilash, o'chirish)
- ✅ Mahsulotlarni kategoriyalarga ajratish (ichimliklar, shirinliklar va h.k.)
- ✅ Savdolarni qayd etish (sana, mahsulot va miqdor)
- ✅ Xarajatlarni qo'shish va kuzatish
- ✅ Batafsil hisobotlarni ko'rish (sotuv va xarajatlar)
- ✅ Ma'lumotlarni eksport qilish
- ✅ Bir nechta foydalanuvchilar bilan ishlash (admin, kassir)
- ✅ JSON fayllarda xavfsiz ma'lumot saqlash

### 🧪 Sifat nazorati:
- ✅ Har bir modul uchun test fayllar
- ✅ Professional kod arxitekturasi
- ✅ Modullar bo'yicha ajratilgan funksiyalar

---

## Loyihaning tuzilishi

```bash
coffee_manager/
├── data/                    # 📁 Ma'lumotlar (JSON fayllar, .gitignore bilan himoyalangan)
│   ├── data.json           # 📄 Mahsulotlar ma'lumotlari  
│   ├── expenses.json       # 📄 Xarajatlar ma'lumotlari
│   └── sales.json          # 📄 Savdo ma'lumotlari
│
├── manager/                 # 📂 Asosiy modullar
│   ├── __init__.py         # 📄 Python paket fayli
│   ├── category.py         # 📄 Mahsulot kategoriyalari
│   ├── product.py          # 📄 Mahsulotlar bilan ishlash
│   ├── storage.py          # 📄 Mahsulotlarni saqlash
│   ├── sales.py            # 📄 Savdo funksiyalari
│   ├── expenses.py         # 📄 Xarajat funksiyalari
│   ├── reports.py          # 📄 Hisobotlar moduli
│   ├── export.py           # 📄 Ma'lumotlarni eksport qilish
│   ├── users.py            # 📄 Foydalanuvchilar boshqaruvi
│   └── menu.py             # 📄 Asosiy menyu
│
├── tests/                   # 🧪 Test fayllar
│   ├── test_category.py    # 🧪 Kategoriya testlari
│   ├── test_product.py     # 🧪 Mahsulot testlari
│   ├── test_storage.py     # 🧪 Saqlash testlari
│   ├── test_sales.py       # 🧪 Savdo testlari
│   └── test_expenses.py    # 🧪 Xarajat testlari
│
├── .gitignore              # ⚙️ Git e'tiborsiz fayllar
├── LICENSE                 # 📜 Loyiha litsenziyasi
├── requirements.txt        # 📦 Python kutubxonalar ro'yxati
├── main.py                 # 🚀 Loyihani ishga tushirish fayli
└── README.md               # 📖 Loyihaning tavsifi
```

---

## Ishga tushirish

1. **Loyihani yuklab oling:**
   ```bash
   git clone https://github.com/OktamTurgun/coffee_manager.git
   cd coffee_manager
   ```

2. **Kerakli kutubxonalarni o'rnating:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Virtual muhit yaratish (ixtiyoriy):**
   ```bash
   python -m venv coffee_env
   source coffee_env/bin/activate  # Linux/Mac
   # yoki
   coffee_env\Scripts\activate     # Windows
   ```

4. **Dasturni ishga tushiring:**
   ```bash
   python main.py
   ```

5. **Testlarni ishga tushirish:**
   ```bash
   python -m pytest tests/
   ```

---

## Texnologiyalar va kutubxonalar

- **Python 3.10+** - Asosiy dasturlash tili
- **JSON** - Ma'lumotlarni saqlash
- **Pytest** - Testlar uchun
- **Datetime** - Sana va vaqt bilan ishlash
- **OS/Path** - Fayl tizimi bilan ishlash

---

## Kelajak rejalar (3.0 versiya)

**Keyingi versiyalarda qo'shiladigan imkoniyatlar:**

📊 **Vizualizatsiya:**
- Diagrammalar orqali vizual hisobot (Matplotlib / Plotly bilan)
- Grafik ko'rinishdagi savdo tahlili

📦 **Ilg'or xususiyatlar:**
- Ombor (storage) optimallashtirish va minimal miqdordan kam bo'lsa ogohlantirish
- Avtomatik buyurtma berish tizimi
- QR kod yaratish va skanerlash

🌐 **Veb-versiya:**
- Django yoki FastAPI asosida veb-interfeys
- REST API yaratish
- Real-time ma'lumotlar yangilanishi

🔐 **Xavfsizlik:**
- Foydalanuvchi autentifikatsiyasi
- Rollar va ruxsatlar tizimi
- Ma'lumotlarni shifrlash

---

## Hissa qo'shish

Bu loyihaga hissa qo'shishni xohlaysizmi? Quyidagi qadamlarni bajaring:

1. Repository'ni fork qiling
2. Yangi branch yarating (`git checkout -b feature/yangi-xususiyat`)
3. O'zgarishlaringizni commit qiling (`git commit -am 'Yangi xususiyat qo'shildi'`)
4. Branch'ni push qiling (`git push origin feature/yangi-xususiyat`)
5. Pull Request yarating

---

## Litsenziya

Bu loyiha [LICENSE](LICENSE) fayli ostida litsenziyalangan.

---

## Muallif

👤 **Uktam Turgunov**  
📧 **Aloqa:** uktamturgunov30@gmail.com  
🐙 **GitHub:** [@OktamTurgun](https://github.com/OktamTurgun)

---

⭐ **Agar loyiha sizga yoqqan bo'lsa, GitHub'da star bosishni unutmang!**

💡 **Savol va takliflar uchun Issues bo'limidan foydalaning**