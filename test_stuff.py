from menu_classes import ProductMenu, CourierMenu, OrderMenu

# from unittest.mock import Mock, patch
import pytest

product_menu = ProductMenu()
courier_menu = CourierMenu()
order_menu = OrderMenu()

# @patch('builtins.input')
# def test_print_product_list(mock_input):
#     product_menu.print_product_list()
#     mock_input.return_value = [{'name': 'latte', 'price': '3.0'}, {'name': 'americano', 'price': '2.0'}]


class FakeProductMenu:
    save_list_to_csv_has_been_called = False

    def __init__(self, product_list):
        self.product_list = product_list

    def save_list_to_csv(self):
        self.save_list_to_csv_has_been_called = True

    def create_product(self, new_product_name, new_product_price):
        if not isinstance(new_product_price, float):
            raise TypeError
        if not isinstance(new_product_name, str):
            raise TypeError
        new_item = {'name': new_product_name, 'price': new_product_price}
        self.product_list.append(new_item)
        print("The product is created!!")
        self.save_list_to_csv()

    def save_list_to_csv(self):
        pass

def test_product_menu_create_product_raise_type_error():
    # Assembly
    products = [{"name": "Fanta", "price": 100}]
    product_menu_under_test = FakeProductMenu(products)
    assert len(product_menu_under_test.product_list) == 1

    # Action / Assertion
    with pytest.raises(TypeError):
        product_menu_under_test.create_product('Pepsi', 100)


def test_product_menu_create_product():
    # Assembly
    products = [{"name": "Fanta", "price": 100}]
    product_menu_under_test = FakeProductMenu(products)
    assert len(product_menu_under_test.product_list) == 1
    assert product_menu_under_test.save_list_to_csv_has_been_called == False

    # Action
    product_menu_under_test.create_product("Pepsi", 10.0)

    # Assertion
    assert len(product_menu_under_test.product_list) == 2
    assert product_menu_under_test.save_list_to_csv_has_been_called == True


# def test_product_menu_update_product():
#     pass

def _read_repository_save(file_path):
    with open(file_path, "r") as f:
        product_lines = f.read().splitlines()
        return product_lines

def test_product_file_repository_save():
    products = {'name': 'americano', 'price': 2.5}
    file_path = "fake_order_for_test.csv"
    product_file_repository = ProductFileRepository(file_path)

    read_product_lines = _read_repository_save(file_path)
    assert read_product_lines == []

    product_file_repository.save(products)

    read_product_lines = _read_repository_save(file_path)
    assert read_product_lines == ["Product(Fanta)", "Product(Pepsi)"]
    open(file_path, "w").close()