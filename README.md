# Coffee Bar Manager

Python terminal dasturi bo'lib, kafe mahsulotlarini boshqarish uchun mo'ljallangan.

## Funksiyalar

- Mahsulot qo'shish, ko'rish, yangilash, o'chirish
- Kategoriya bilan integratsiya
- Sotuvlar va harajatlarni kuzatish
- Hisobotlar (foyda, zarar)
- CSV / Excel eksport
- Parol bilan kirish (admin / kassir)

## Talablar

- Python 3.11+
- Kutubxonalar: `openpyxl`

## O'rnatish

```bash
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Ishga tushirish

```bash
python main.py
```

## Testlar

`tests/` papkasi ichida mini test fayllari mavjud.
Siz pytest yoki unittest yordamida testlarni ishga tushirishingiz mumkin:

```bash
python -m unittest discover tests
```

## Litsenziya

Ushbu loyiha MIT litsenziyasi ostida tarqatiladi. Batafsil `LICENSE` faylga qarang.

## Muallif

**GitHub:** [OktamTurgun](https://github.com/OktamTurgun)