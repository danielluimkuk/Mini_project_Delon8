# Mini-Project for Data Engineer program of Generation UK  --- Building a program that runs on the command line (CLI).   

## Project Background

Your client has launched a pop-up café in a busy business district. 

They are offering home-made lunches and refreshments to the surrounding offices. 

As such, they require a software application which helps them to log and track orders.  

## Requirements as a business:

• I want to maintain a collection of products and couriers.

• When a customer makes a new order,I need to create this on the system.

• I need to be able to update the status of an order i.e:preparing, out-for-delivery, delivered.

• When I exit my app, I need all data to be persisted and not lost.

• When I start myapp, I need to load all persisted data.

• I need to be sure my app has been tested and proven to work well.

• I need to receive regular software updates.  


# Requirements

## Week 1

-   create a product (string) and add it to a list
-   view all products with an index attached
-   STRETCH update or delete a product using an index value to choose

Finished the requirement and stretch goal however I did not have TDD in mind at all.
Finished it without any OOP and the functions were bit lengthy.

## Week 2

-   create a product,  **courier or order**  and add it to a list
-   view all products,  **couriers or orders**  index attached
-   **add data persitence**  using text files
-   STRETCH update or delete a product,  **courier or order**  by choosing its index

Orders were required to be stored as dictionaries with the following structure { "customer_name": "John", "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER", "customer_phone": "0789887334", "status": "preparing" }

There was some confusion this week because we got two different sets of requirements.

Rewrote the whole app and implemented some OOP to reuse the code, as the functions required for products and couriers are identical but their name and file path.
Added the functions to add, update and delete couriers and orders and added code to read and write from/to txt files.

The dictionary type for order made the code not reusable thus some repetitive functions were made. However functionality wise , it is functional and met the requirements.



## Week 3

-   create a product, courier or order and add it to a list
-   view all products, couriers or orders
-   add data persistence using text files  **- update the status of an order**
-   STRETCH update or delete a product, courier or order by index

As we were required to persist data with txt file, I imagined we would be required to persist it on csv file later on. So I took the initiative to do it earlier and made all three of the items persist-able in csv files.
Requirements are met and exceeded. (might not be a good practice)

## Week 4

-   create a product, courier or order and add it to a list
-   view all products, couriers or orders
-   add data persistence using  **csv files**
-   update the status of an order
-   **BONUS list orders by status or courier**

Rewrote the program again to try adopting the repository pattern and making classes like objects of order, product, courier. However when I tried to loop through these objects, some bugs were found and I retreat back to using dictionaries instead.



## Project Outline

![Screenshot 2022-11-23 at 11 06 43 AM](https://user-images.githubusercontent.com/108125998/203532038-2e3fa99e-cb30-4b18-813e-75edf56721dc.png)

• The functions of the project are encapsulated in three classes. ProductMenu, CourierMenu and OrderMenu.  

• Each of the objects have their own CRUD functions and CSV file for data persistance.  

• When each of them is called, data in the form of lists will be called from the CSV file or one will be created.  

• Whenever a CRUD function is called, data will be loaded and persisted to the CSV file.  
## Screenshots of the CLI APP
#### The app on the main menu. 
![Screenshot 2022-11-18 at 12 13 25 PM](https://user-images.githubusercontent.com/108125998/202704677-cb735e45-3ac6-46de-8ee3-74007d307146.png)
#### Number input to navigate through the menus and showing product list.
![Screenshot 2022-11-18 at 12 13 45 PM](https://user-images.githubusercontent.com/108125998/202704655-0959f650-f2e6-4e27-aafc-448e5fcb986a.png)  
#### Creating a new product.
![Screenshot 2022-11-18 at 12 14 21 PM](https://user-images.githubusercontent.com/108125998/202704631-e43547f2-c725-455e-a63c-2da1b52a7147.png)  
#### A typical order would require multiple inputs from prompts.
![Screenshot 2022-11-18 at 12 14 48 PM](https://user-images.githubusercontent.com/108125998/202704619-43a2a9b1-c322-4616-829d-99286fe65549.png)  
#### Choice of products would be displayed as number, separated by commas and would not accept otherwise.
![Screenshot 2022-11-18 at 12 16 19 PM](https://user-images.githubusercontent.com/108125998/202704585-3eea437f-f439-491a-ae7a-ecceedc59fb4.png)  
#### After an update, the old item and the new item will be shown for user to compare the changes.
![Screenshot 2022-11-18 at 12 18 03 PM](https://user-images.githubusercontent.com/108125998/202704553-d16847a0-7517-4b5a-860c-eb60802992b5.png)  
#### A look on the CSV file.
![Screenshot 2022-11-18 at 1 33 05 PM](https://user-images.githubusercontent.com/108125998/202716799-c34c2e41-e9c6-4dcf-8f28-86a3f8d8f6da.png)

## Meeting the requirements -- Testing
Apart from doing manuel testing to ensure the app meeting the requirements.  
Some unit testings are also done.   
11 Tests were made at this point of time.  
One is used to test the save list to csv function.  

![Screenshot 2022-11-23 at 12 24 36 PM](https://user-images.githubusercontent.com/108125998/203546372-dd8d9afd-03ee-4ed1-af64-03cd17509274.png)

Two are used to test if the create product function will raise type error for unknown inputs and successfully append the item to the list.   

![Screenshot 2022-11-23 at 12 22 49 PM](https://user-images.githubusercontent.com/108125998/203546061-ff63c065-847e-407a-9777-302ef06a8394.png)

Another one is used to test the delete function and two other were used to test if the app can navigate through different menus from number command.  
Two similar tests for the courier menu.
One last test for update status function of the order menu as it is a lengthy dictionary.  

Tests were made with the assistance of fake classes as some of them do not return any objects to be tested.  

![Screenshot 2022-11-23 at 12 25 25 AM](https://user-images.githubusercontent.com/108125998/203447393-b35f2753-42f1-4d73-a6e0-883ef320318f.png)


## Potential improvements  
#### Better UI
Commands like "os.system('clear')" can be used to refresh the terminal whenever a menu is called or a page is turned, it is removed to make the program lighter and more reader-friendly.  
#### Better use of classes and OOP
Individual products, couriers and orders can be sorted to their own class with their own specific attributes to form their own dictionaries.
A repository layer should be used to better handle the filing of CSVs and data base interaction.  
Variables such as PATH and HEADER can be used to reduce repetitive code for file handling.  
The code can be further refractor to meet the clean code standard.

#### Too wet
###### DRY (Don't Repeat Youself)  
It is best practice however the code is a bit repetitive to be honest.  
#### Testability
Although the app logic is quite straight forward, the functions are not neat enough to be tested individually without some modifications, for example creating fake classes and fake functions.

## Things I enjoyed most.
It is a wonderful experience to practice my OOP concepts, logic, file handling and exception handling.  
If I have to pick one thing I learnt from this project, is the importance of TDD.
When I was writing the tests for the app, it was so hard to make tests for made applications and functions.
It was a painful lesson but definitely worth while.  

## KEY TAKEAWAY
1. Documentation
2. Testability
3. Sticking to requirement


