# ☕ Coffee Bar Manager

![Coffee Bar](https://img.shields.io/badge/Project-CoffeeBarManager-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

## Loyihaning maqsadi

**Coffee Bar Manager** — bu kichik kafe yoki coffee bar uchun mahsulotlarni boshqarish, savdolarni kuzatish va xarajatlarni nazorat qilish dasturi.  

Loyiha o'quv maqsadida yozilgan bo'lib, Python modullaridan foydalanishni, fayllar bilan ishlashni va dasturiy arxitekturani yaxshiroq tushunishga yordam beradi.

---

## Funksiyalar

✅ Mahsulot qo'shish, yangilash va o'chirish  
✅ Savdolarni qayd etish (sana, mahsulot va miqdor)  
✅ Xarajatlarni qo'shish va kuzatish  
✅ Hisobotlarni ko'rish (sotuv va xarajatlar)  
✅ JSON fayllarda ma'lumotlarni saqlash  

---

## Loyihaning tuzilishi

```bash
coffee_bar_project/
│── data/                # Ma'lumotlar (JSON fayllar)
│   ├── data.json
│   ├── expenses.json
│   └── sales.json
│
│── manager/             # Asosiy modullar
│   ├── __init__.py
│   ├── storage.py       # Mahsulotlarni saqlash
│   ├── sales.py         # Savdo funksiyalari
│   ├── expenses.py      # Xarajat funksiyalari
│   └── menu.py          # Asosiy menyu
│
│── tests/               # Test fayllar
│
│── main.py              # Loyihani ishga tushirish fayli
│── README.md            # Loyihaning tavsifi
```

---

## Ishga tushirish

1. **Loyihani yuklab oling:**
   ```bash
   git clone https://github.com/OktamTurgun/coffee_manager.git
   cd coffee_bar_project
   ```

2. **Virtual muhit yaratib o'rnating:**
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

3. **Dasturni ishga tushiring:**
   ```bash
   python main.py
   ```

---

## Kelajak rejalar (Coffee Bar Manager 2.0)

**2.0 versiyada qo'shiladigan imkoniyatlar:**

📊 Diagrammalar orqali vizual hisobot (Matplotlib / Plotly bilan)  
🛠️ Mahsulotlarni kategoriyalarga bo'lish (ichimliklar, shirinliklar va hokazo)  
📦 Ombor (storage) optimallashtirish va minimal miqdordan kam bo'lsa ogohlantirish  
🌐 Django yoki FastAPI asosida veb-versiya  
👥 Bir nechta foydalanuvchilar (admin, kassir) bilan ishlash  

---

## Muallif

👤 **Uktam Turgunov**  
📧 **Aloqa:** <uktamturgunov30@gmail.com>

⭐ Agar loyiha sizga yoqqan bo'lsa, GitHub'da star bosishni unutmang!
