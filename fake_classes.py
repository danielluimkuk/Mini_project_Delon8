import csv


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


class FakeCourierMenu():
    # save_list_to_csv_has_been_called = False
    print_courier_list_has_been_called = False
    create_courier_has_been_called = False
    update_courier_has_been_called = False
    delete_courier_has_been_called = False
    save_list_to_csv_has_been_called = False

    def __init__(self, courier_list):
        self.courier_list = courier_list

    def show_courier_menu(self):

        command = input(f"Please enter your command.\n"
                        f"0. Go back to main menu.\n"
                        f"1. Print courier list.\n"
                        f"2. Create new courier\n"
                        f"3. Update courier\n"
                        f"4. Delete courier\n")
        if command == '1':
            self.print_courier_list()
        elif command == '2':
            self.create_courier()
        elif command == '3':
            self.update_courier()
        elif command == '4':
            self.delete_courier()
        elif command == '0':
            pass

    def save_list_to_csv(self):
        self.save_list_to_csv_has_been_called = True
        header = ['name', 'phone']

        with open('fake_courier.csv', 'w') as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(self.courier_list)

    def print_courier_list(self):
        self.print_courier_list_has_been_called = True

    def create_courier(self, new_courier_name, new_courier_num):
        self.create_courier_has_been_called = True
        if not isinstance(new_courier_num, str):
            raise TypeError
        if not isinstance(new_courier_name, str):
            raise TypeError
        new_item = {'name': new_courier_name, 'phone': new_courier_num}
        self.courier_list.append(new_item)
        self.save_list_to_csv()

    def update_courier(self):
        self.update_courier_has_been_called = True

    def delete_courier(self):
        temp_list = self.courier_list
        for count, value in enumerate(self.courier_list):
            print(count + 1, value)
        try:
            thing_to_delete = int(input(f"Please pick a product to delete or enter 'b' to return: "))
            if thing_to_delete == 'b':
                self.show_courier_menu()
            else:
                del temp_list[thing_to_delete - 1]
                self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.delete_courier()


class FakeOrderMenu:
    def __init__(self, order_list):
        self.order_list = order_list

    def update_order(self):
        temp_list = self.order_list
        # for count, value in enumerate(self.order_list):
        #     print(count + 1, value)
        try:
            index_of_thing_to_update = int(input(f'Please pick an order to update: '))


            new_thing = temp_list[index_of_thing_to_update - 1]
            choice = input(f"Please choose a status:\n"
                           f"1. Preparing\n"
                           f"2. Dispatched\n"
                           f"3. Delivered\n"
                           f"4. Cancelled\n")
            if choice == '1':
                choice = 'Preparing'
            elif choice == '2':
                choice = 'Dispatched'
            elif choice == '3':
                choice = 'Delivered'
            elif choice == '4':
                choice = 'Cancelled'

            new_thing['status'] = choice

            temp_list[index_of_thing_to_update - 1] = new_thing
            self.order_list = temp_list
            # self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
