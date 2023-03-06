class ItemDatabase:

    def __init__(self):
        self.item_db = {'Apple': 2.0,
                        'Orange': 1.0,
                        'Onion': 1.5
                        }

    def get_item_value(self, item: str) -> float:
        return self.item_db[item]

    def get_all_items(self):
        return self.item_db

    def create_item(self, item: str, cost: float):
        self.item_db[item] = cost

    def update_item(self, item: str, cost: float):
        if item in self.item_db.keys():
            self.item_db[item] = cost
        else:
            return 'Item not found'

    def delete_item(self, item: str):
        self.item_db.pop(item)
