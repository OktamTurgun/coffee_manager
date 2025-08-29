from getpass import getpass

class User:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role  # 'admin' yoki 'kassir'

    def __str__(self):
        return f"{self.username} ({self.role})"

# Demo foydalanuvchilar
USERS = [
    User("admin", "admin123", "admin"),
    User("kassir1", "kassir123", "kassir")
]

def login():
    """Login funksiyasi: foydalanuvchi nomi va parol so‘raydi"""
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()

    user = next((u for u in USERS if u.username == username and u.password == password), None)
    if user:
        print(f"✅ Xush kelibsiz, {user.username}! Rol: {user.role}")
        return user
    else:
        print("❌ Noto‘g‘ri username yoki parol!")
        return None
