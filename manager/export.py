import csv
import os
from openpyxl import Workbook


def export_to_csv(products, filename="products.csv"):
    """Mahsulotlarni CSV faylga eksport qilish"""
    if not products:
        print("❌ Eksport uchun mahsulotlar mavjud emas.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Sarlavhalar
        writer.writerow(["ID", "Nomi", "Narxi", "Soni", "Kategoriya"])
        # Mahsulotlarni yozish
        for idx, p in enumerate(products, start=1):
            writer.writerow([idx, p.name, p.price, p.quantity, p.category.name if p.category else "Yo'q"])

    print(f"✅ Mahsulotlar CSV faylga saqlandi: {os.path.abspath(filename)}")


def export_to_excel(products, filename="products.xlsx"):
    """Mahsulotlarni Excel faylga eksport qilish"""
    if not products:
        print("❌ Eksport uchun mahsulotlar mavjud emas.")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Mahsulotlar"

    # Sarlavhalar
    ws.append(["ID", "Nomi", "Narxi", "Soni", "Kategoriya"])

    # Mahsulotlar yozish
    for idx, p in enumerate(products, start=1):
        ws.append([idx, p.name, p.price, p.quantity, p.category.name if p.category else "Yo'q"])

    wb.save(filename)
    print(f"✅ Mahsulotlar Excel faylga saqlandi: {os.path.abspath(filename)}")
