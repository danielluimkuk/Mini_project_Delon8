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

