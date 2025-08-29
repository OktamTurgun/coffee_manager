def add_expense(storage):
    """Harajat qo‘shish"""
    name = input("Harajat nomi: ").strip()
    if not name:
        print("❌ Harajat nomi bo‘sh bo‘lishi mumkin emas.")
        return
    try:
        amount = int(input("Summasi (so‘m): ").strip())
    except ValueError:
        print("❌ Summani butun son kiriting.")
        return
    if amount <= 0:
        print("❌ Summasi musbat bo‘lsin.")
        return

    storage.record_expense(name, amount)  # ✅ endi Storage dagi metoddan foydalanadi
    print(f"✅ Harajat qo‘shildi: {name} — {amount:,} so‘m")


def show_expenses(storage):
    """Harajatlar ro‘yxatini chiqarish"""
    if not storage.expenses:
        print("📭 Hali harajatlar yo‘q.")
        return

    print("\n💸 Harajatlar:")
    for e in storage.expenses:
        print(f"{e['date']} | {e['name']} — {e['amount']:,} so‘m")
