from unittest import mock
from unittest.mock import patch
from menu_classes import ProductMenu, CourierMenu, OrderMenu
import csv
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
    print_product_list_has_been_called = False
    create_product_has_been_called = False
    update_product_has_been_called = False
    delete_product_has_been_called = False

    def __init__(self, product_list):
        self.product_list = product_list

    def save_list_to_csv(self):
        self.save_list_to_csv_has_been_called = True
        header = ['name', 'price']

        with open('fake_order_for_test.csv', 'w') as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(self.product_list)


    def print_product_list(self):
        self.print_product_list_has_been_called = True

    def update_product(self):
        self.update_product_has_been_called = True

    def delete_product(self):
        self.delete_product_has_been_called = True
        temp_list = ["Latte", "Cappuccino", "Americano"]

        try:
            thing_to_delete = int(input(f"Please pick a product to delete or enter 'b' to return: "))
            if thing_to_delete == 'b':
                return "main_menu"
            else:
                del temp_list[thing_to_delete - 1]
                self.save_list_to_csv()
                return temp_list

        except (ValueError, IndexError):
            return '\nInvalid input.\n'

    def create_product(self, new_product_name, new_product_price):
        self.create_product_has_been_called = True
        if not isinstance(new_product_price, float):
            raise TypeError
        if not isinstance(new_product_name, str):
            raise TypeError
        new_item = {'name': new_product_name, 'price': new_product_price}
        self.product_list.append(new_item)

        self.save_list_to_csv()

    def show_product_menu(self):

        command = input(f"Please enter your command.\n"
                        f"0. Go back to main menu.\n"
                        f"1. Print product list.\n"
                        f"2. Create new product\n"
                        f"3. Update product\n"
                        f"4. Delete product\n")
        if command == '1':
            self.print_product_list()
        elif command == '2':
            self.create_product()
        elif command == '3':
            self.update_product()
        elif command == '4':
            self.delete_product()
        elif command == '0':
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


@mock.patch("builtins.input")
def test_product_menu_1_print_product_list(mock_input):
    mock_input.side_effect = ["1"]
    product_menu_under_test = FakeProductMenu([])
    assert product_menu_under_test.print_product_list_has_been_called == False

    product_menu_under_test.show_product_menu()

    assert product_menu_under_test.print_product_list_has_been_called == True
    assert mock_input.call_count == 1


@mock.patch("builtins.input")
def test_product_menu_3_update_product(mock_input):
    mock_input.side_effect = ["3"]
    product_menu_under_test = FakeProductMenu([])
    assert product_menu_under_test.update_product_has_been_called == False

    product_menu_under_test.show_product_menu()

    assert product_menu_under_test.update_product_has_been_called == True
    assert mock_input.call_count == 1



@mock.patch("builtins.input")
def test_product_menu_delete_product_method(mock_input):
    mock_input.side_effect = ["2"]
    product_menu_under_test = FakeProductMenu([])
    expected = ["Latte", "Americano"]
    action = product_menu_under_test.delete_product()
    assert action == expected

    mock_input.side_effect = ["1"]
    product_menu_under_test = FakeProductMenu([])
    expected = ["Cappuccino", "Americano"]
    action = product_menu_under_test.delete_product()
    assert action == expected

    mock_input.side_effect = ["abc"]
    product_menu_under_test = FakeProductMenu([])
    expected = "\nInvalid input.\n"
    action = product_menu_under_test.delete_product()
    assert action == expected


def _read_repository_save(file_path):
    temp_list = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            temp_list.append(item)
    return temp_list


def test_save_list_to_csv():
    products = {'name': 'americano', 'price': 2.5}
    product_list = []
    product_menu_under_test = FakeProductMenu(product_list)
    file_path = "fake_order_for_test.csv"
    # product_file_repository = ProductFileRepository(file_path)

    read_product_lines = _read_repository_save(file_path)
    assert read_product_lines == []

    product_menu_under_test.product_list.append(products)
    product_menu_under_test.save_list_to_csv()

    read_product_lines = _read_repository_save(file_path)
    assert read_product_lines == [{'name': 'americano', 'price': '2.5'}]

    # product_file_repository.save(products)
    #
    # read_product_lines = _read_repository_save(file_path)
    # assert read_product_lines == ["Product(Fanta)", "Product(Pepsi)"]
    # open(file_path, "w").close()
