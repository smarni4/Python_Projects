from shopping_cart import ShoppingCart
from Item_database import ItemDatabase
import pytest


@pytest.fixture()
def cart():
    """ returns shopping cart class """
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    """ Tests the adding items to the cart function """
    cart.add("Apple", 1)
    assert "Apple" in cart.get_all_items(), 'Item is not added'


def test_when_add_more_than_max_size(cart):
    """ Tests the overflow error """
    with pytest.raises(OverflowError):
        for _ in range(7):
            cart.add('Apple', 3)


def test_can_get_total_price(cart):
    """ Tests the total price calculating function """
    cart.add('Apple', 3)
    cart.add('Onion', 2)
    cart.add('Orange', 4)
    item = ItemDatabase()
    item_db = item.item_db
    assert cart.get_total_price(item_db) == 13, 'Calculated total price is incorrect.'
