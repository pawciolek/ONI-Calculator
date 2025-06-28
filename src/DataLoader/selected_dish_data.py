class Selected_dish_data:
    def __init__(self, selected_dish: list = None):
        self.selected_dish = selected_dish if selected_dish is not None else []

    def set_selected_dish(self, dish):
        self.selected_dish = [dish]

    def get_selected(self):
        return self.selected_dish[0] if self.selected_dish else None

    def clear(self):
        self.selected_dish = []

    def exists(self):
        return bool(self.selected_dish)

    def has_dish_name(self, name: str):
        return self.exists() and self.selected_dish[0]["name"] == name

    def checkData(self):
        print(f"sprawdzanie klasy: {self.selected_dish}")
