from unittest import mock
from tests.fake_classes import FakeProductMenu, FakeCourierMenu, FakeOrderMenu
import csv
import pytest


def _read_from_csv(file_path):
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

    read_product_lines = _read_from_csv(file_path)
    assert read_product_lines == []

    product_menu_under_test.product_list.append(products)
    product_menu_under_test.save_list_to_csv()

    read_product_lines = _read_from_csv(file_path)
    assert read_product_lines == [{'name': 'americano', 'price': '2.5'}]


def test_product_menu_create_product_raise_type_error():
    # Assembly
    products = [{"name": "Fanta", "price": 100}]
    product_menu_under_test = FakeProductMenu(products)

    # Action / Assertion
    with pytest.raises(TypeError):
        product_menu_under_test.create_product("Pepsi", 100)


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


def test_product_menu_1_print_product_list(monkeypatch):
    fake_input = iter(["1"])
    monkeypatch.setattr('builtins.input', lambda _: next(fake_input, None))
    product_menu_under_test = FakeProductMenu([])
    assert product_menu_under_test.print_product_list_has_been_called == False

    product_menu_under_test.show_product_menu()

    assert product_menu_under_test.print_product_list_has_been_called == True


def test_product_menu_3_update_product(monkeypatch):
    fake_input = iter(["3"])
    monkeypatch.setattr('builtins.input', lambda _: next(fake_input, None))
    product_menu_under_test = FakeProductMenu([])
    assert product_menu_under_test.update_product_has_been_called == False

    product_menu_under_test.show_product_menu()

    assert product_menu_under_test.update_product_has_been_called == True


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


# tests for Courier


def test_product_menu_create_courier_raise_type_error():
    # Assembly
    courier_info = [{"name": "Test_Courier", "phone": "1834633"}]
    product_menu_under_test = FakeCourierMenu(courier_info)

    # Action / Assertion
    with pytest.raises(TypeError):
        product_menu_under_test.create_courier('Pepsi', 100)


def test_courier_menu_create_courier():
    # Assembly
    courier_info = [{"name": "Frank", "phone": "1834633"}]
    courier_menu_under_test = FakeCourierMenu(courier_info)
    assert len(courier_menu_under_test.courier_list) == 1
    assert courier_menu_under_test.save_list_to_csv_has_been_called == False

    # # Action
    courier_menu_under_test.create_courier("Rick", "1878200")
    #
    # # Assertion
    assert len(courier_menu_under_test.courier_list) == 2
    assert courier_menu_under_test.save_list_to_csv_has_been_called == True


def test_courier_menu_1_print_courier_list(monkeypatch):
    fake_input = iter(["1"])
    monkeypatch.setattr('builtins.input', lambda _: next(fake_input, None))
    courier_menu_under_test = FakeCourierMenu([])
    assert courier_menu_under_test.print_courier_list_has_been_called == False

    courier_menu_under_test.show_courier_menu()

    assert courier_menu_under_test.print_courier_list_has_been_called == True


def test_courier_menu_3_update_courier(monkeypatch):
    fake_input = iter(["3"])
    monkeypatch.setattr('builtins.input', lambda _: next(fake_input, None))
    courier_menu_under_test = FakeCourierMenu([])
    assert courier_menu_under_test.update_courier_has_been_called == False

    courier_menu_under_test.show_courier_menu()

    assert courier_menu_under_test.update_courier_has_been_called == True


def test_order_menu_update_status(monkeypatch):
    fake_input = iter(["2", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(fake_input, None))

    orders = [
        {'customer_name': 'Nathan', 'customer_address': 'sitting room', 'customer_phone': '8193212', 'courier': '3',
         'status': 'Dispatched', 'items': '2,3,1,'},
        {'customer_name': 'Heather', 'customer_address': '456, H road', 'customer_phone': '667124819', 'courier': '2',
         'status': 'PREPARING', 'items': '1,2'},
        {'customer_name': 'Sheikh', 'customer_address': '123,london,321', 'customer_phone': '98127412', 'courier': '3',
         'status': 'Dispatched', 'items': '1,1'}]

    order_menu_under_test = FakeOrderMenu(orders)
    assert order_menu_under_test.order_list[1]['status'] == 'PREPARING'

    order_menu_under_test.update_order()

    assert order_menu_under_test.order_list[1]['status'] == 'Delivered'

