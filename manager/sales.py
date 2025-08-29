from datetime import datetime

def _choose_product(storage):
    """Indeks yoki nom bo‘yicha mahsulot tanlash"""
    if not storage.products:
        print("📭 Mahsulot yo‘q!")
        return None

    print("\n📦 Mahsulotlar:")
    for i, p in enumerate(storage.products, 1):
        print(f"{i}. {p.name} — {p.price:,} so‘m (qoldiq: {p.quantity})")

    choice = input("Mahsulot raqami yoki nomi: ").strip()

    # Agar raqam kiritilsa
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(storage.products):
            return storage.products[idx]
        print("❌ Noto‘g‘ri indeks.")
        return None

    # Nom bo‘yicha qidirish
    for p in storage.products:
        if p.name.lower() == choice.lower():
            return p

    print("❌ Bunday mahsulot topilmadi.")
    return None


def sell(storage):
    """Mahsulot sotish"""
    product = _choose_product(storage)
    if not product:
        return

    try:
        qty = int(input("Soni (dona): ").strip())
    except ValueError:
        print("❌ Soni butun son bo‘lishi kerak.")
        return

    if qty <= 0:
        print("❌ Soni musbat bo‘lishi kerak.")
        return

    if qty > product.quantity:
        print("❌ Yetarli qoldiq yo‘q.")
        return

    total = product.price * qty
    product.quantity -= qty  # qoldiqdan ayiramiz

    # ✅ endi Storage dagi record_sale dan foydalanamiz
    storage.record_sale(product.name, qty, product.price, total)

    storage.save()  # mahsulot qoldig‘ini saqlash
    print(f"✅ Sotildi: {product.name} x{qty} = {total:,} so‘m")


def show_sales(storage):
    """Sotuvlar tarixini ko‘rsatish"""
    if not storage.sales:
        print("📭 Sotuvlar tarixi bo‘sh.")
        return

    print("\n🧾 Sotuvlar tarixi:")
    for s in storage.sales:
        print(f"{s['date']} | {s['name']} x{s['qty']} | "
              f"{s['unit_price']:,} so‘m | Jami: {s['total']:,} so‘m")
