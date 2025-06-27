import json


class SortDishes:
    def __init__(self, selected_dlcs: list = None):
        if selected_dlcs is None:
            self.selected_dlcs = ['basic']
        else:
            self.selected_dlcs = selected_dlcs
        self.filtered_data = []

    def sort_by_dlc(self):
        try:
            with open("../Dishes.json", "r", encoding="utf-8") as file:
                data = json.load(file)

        except Exception as e:
            print(f"Błąd wczytywania JSON: {e}")
            return []

        self.filtered_data = [dlc for dlc in data if dlc["DLC_name"] in self.selected_dlcs]
        print(self.filtered_data)
        return self.filtered_data

    def result(self):
        for dlc in self.filtered_data:
            print(f"\nDLC {dlc['DLC_name']}")
            for dish in dlc["Dishes"]:
                print(f"- {dish['name']}")
