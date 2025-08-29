from datetime import datetime

def show_report(storage):
    """Umumiy hisobot: mahsulotlar, sotuvlar, harajatlar, foyda"""
    print("\n📦 MAHSULOTLAR RO‘YXATI 📦")
    if not storage.products:
        print("📭 Hozircha mahsulot yo‘q.")
    else:
        for p in storage.products:
            print(f"- {p.name} | {p.quantity} dona | {p.price:,} so‘m")

    print("\n🧾 SOTUVLAR TARIXI 🧾")
    if not storage.sales:
        print("📭 Sotuvlar hali yo‘q.")
    else:
        total_sales = 0
        for s in storage.sales:
            total_sales += s['total']
            print(f"{s['date']} | {s['name']} x{s['qty']} | "
                  f"{s['unit_price']:,} so‘m | Jami: {s['total']:,} so‘m")
        print(f"💰 Sotuvlar jami: {total_sales:,} so‘m")

    print("\n💸 HARAJATLAR 💸")
    if not storage.expenses:
        print("📭 Harajatlar hali yo‘q.")
        total_expenses = 0
    else:
        total_expenses = 0
        for e in storage.expenses:
            total_expenses += e['amount']
            print(f"{e['date']} | {e['name']} — {e['amount']:,} so‘m")
        print(f"💸 Harajatlar jami: {total_expenses:,} so‘m")

    # Foyda hisoblash
    profit = total_sales - total_expenses
    print("\n📊 FOYDA / ZARAR 📊")
    if profit > 0:
        print(f"✅ Foyda: {profit:,} so‘m")
    elif profit < 0:
        print(f"❌ Zarar: {abs(profit):,} so‘m")
    else:
        print("⚖️ Natija: 0 so‘m")

