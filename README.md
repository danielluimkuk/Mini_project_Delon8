# Mini-Project for Data Engineer program of Generation UK
# Building a program that runs on the command line (CLI).

## Overview

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

## Project Outline
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
