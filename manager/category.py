class Category:
    _id_counter = 1

    def __init__(self, name: str):
        self.id = Category._id_counter
        Category._id_counter += 1
        self.name = name

    def __str__(self):
        return f"{self.id}. {self.name}"
