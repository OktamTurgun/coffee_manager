from manager.storage import Storage
from manager.product import Product
from manager.category import Category
from manager.sales import sell, show_sales
from manager.expenses import add_expense, show_expenses
from manager.reports import show_report
from manager.export import export_to_csv, export_to_excel
from manager.users import login

def run_menu():
    storage = Storage()

    # Kirish
    current_user = None
    while not current_user:
        current_user = login()

    while True:
        print("\n=== Coffee Bar Manager ===")
        # Menu variantlari rolga qarab
        if current_user.role == "admin":
            print("1. Mahsulot qo‘shish")
            print("2. Mahsulotlar ro‘yxati")
            print("3. Sotish")
            print("4. Sotuvlar tarixi")
            print("5. Mahsulotni yangilash")
            print("6. Mahsulotni o‘chirish")
            print("7. Harajat qo‘shish")
            print("8. Harajatlar ro‘yxati")
            print("9. Hisobot")
            print("10. Mahsulotlarni CSV/Excel ga eksport qilish")
        elif current_user.role == "kassir":
            print("1. Mahsulot qo‘shish")
            print("2. Mahsulotlar ro‘yxati")
            print("3. Sotish")
        print("0. Chiqish")

        choice = input("Tanlang: ").strip()

        # Kassir uchun cheklov
        if current_user.role == "kassir" and choice not in ["1", "2", "3", "0"]:
            print("❌ Sizda bu amalni bajarish huquqi yo‘q!")
            continue

        # === Tanlovlar ===
        if choice == "1":
            # Mahsulot qo‘shish
            name = input("Mahsulot nomi: ").strip()
            try:
                price = int(input("Narxi: ").strip())
                qty = int(input("Miqdori: ").strip())
            except ValueError:
                print("❌ Narx va miqdor butun son bo‘lishi kerak.")
                continue

            # Kategoriya tanlash/yaratish
            print("\n📂 Kategoriya tanlang yoki yangi kiriting:")
            if not hasattr(storage, "categories"):
                storage.categories = []

            if storage.categories:
                for c in storage.categories:
                    print(c)

            kat_input = input("Kategoriya nomi (yangi yoki mavjud): ").strip()
            if kat_input:
                existing = next((c for c in storage.categories if c.name.lower() == kat_input.lower()), None)
                if existing:
                    category_name = existing.name
                else:
                    new_cat = Category(kat_input)
                    storage.categories.append(new_cat)
                    category_name = new_cat.name
            else:
                category_name = None

            storage.add_product(Product(name, price, qty, category_name))
            storage.save()
            print(f"✅ {name} qo‘shildi!")

        elif choice == "2":
            storage.list_products()

        elif choice == "3":
            sell(storage)

        elif choice == "4" and current_user.role == "admin":
            show_sales(storage)

        elif choice == "5" and current_user.role == "admin":
            storage.list_products()
            eski_nom = input("Qaysi mahsulotni yangilamoqchisiz (nomini kiriting): ").strip()
            if not eski_nom:
                print("❌ Mahsulot nomi bo‘sh bo‘lishi mumkin emas.")
                continue
            yangi_nom = input("Yangi nom (bo‘sh qoldirsangiz o‘zgarmaydi): ").strip()
            try:
                yangi_narx_input = input("Yangi narx (bo‘sh qoldirsangiz o‘zgarmaydi): ").strip()
                yangi_narx = int(yangi_narx_input) if yangi_narx_input else None
                yangi_soni_input = input("Yangi miqdor (bo‘sh qoldirsangiz o‘zgarmaydi): ").strip()
                yangi_soni = int(yangi_soni_input) if yangi_soni_input else None
            except ValueError:
                print("❌ Narx va miqdor butun son bo‘lishi kerak.")
                continue

            if storage.edit_product(eski_nom, yangi_nom, yangi_narx, yangi_soni):
                print(f"✅ {eski_nom} yangilandi!")
            else:
                print("❌ Bunday mahsulot topilmadi.")

        elif choice == "6" and current_user.role == "admin":
            storage.list_products()
            nom = input("Qaysi mahsulotni o‘chirmoqchisiz (nomini kiriting): ").strip()
            if not nom:
                print("❌ Mahsulot nomi bo‘sh bo‘lishi mumkin emas.")
                continue
            confirm = input(f"{nom} ni o‘chirmoqchimisiz? (ha/yo‘q): ").strip().lower()
            if confirm == "ha":
                storage.delete_product(nom)
                print(f"✅ {nom} o‘chirildi!")
            else:
                print("❌ O‘chirish bekor qilindi.")

        elif choice == "7" and current_user.role == "admin":
            add_expense(storage)

        elif choice == "8" and current_user.role == "admin":
            show_expenses(storage)

        elif choice == "9" and current_user.role == "admin":
            show_report(storage)

        elif choice == "10" and current_user.role == "admin":
            products = storage.products
            export_to_csv(products)
            export_to_excel(products)

        elif choice == "0":
            print("Dastur tugadi. 👋")
            break

        else:
            print("❌ Noto‘g‘ri tanlov, qaytadan urinib ko‘ring.")
