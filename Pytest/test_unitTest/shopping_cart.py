from typing import List
from Item_database import ItemDatabase


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.cart_list = []
        self.max_size = max_size
        self.item = ItemDatabase()
        self.item_db = self.item.item_db

    def add(self, item: str, count: int):
        if self.size() > self.max_size:
            raise OverflowError
        self.cart_list.append([item, count])

    def size(self) -> int:
        return len(self.cart_list)

    def get_item(self, get_item: str) -> List:
        for item in self.cart_list:
            if item[0] == get_item:
                return item[0]

    def get_all_items(self):
        items = []
        for item in self.cart_list:
            items.append(item[0])
        return items

    def get_total_price(self, price_map: dict):
        total_price = 0
        for item in self.cart_list:
            if item[0] in self.item_db.keys():
                for key, value in price_map.items():
                    if item[0] == key:
                        total_price += int(item[1])*self.item.get_item_value(item[0])
        return total_price


# cart = ShoppingCart()
# print(cart.add('Apple', 2))
# print(cart.size())
# print(cart.add('Onion', 3))
# print(cart.size())
# print(cart.get_item('Onion'))
# print(cart.get_total_price({'Apple': 20, 'Onion': 10}))

