# Seat Manager

A command line tool to manage the seat allocation for a library(self study point or lab).This will be my project for  Vityathi Python essential course.

## Features 
 i. Register simple users(id, name etc.)
 ii. Allocate the seat to a user 
 iii. Vacant a seat 
 iv. Save and load data from local json files.

## How can we run the program ?

First we have to open a terminal inside the project folder then we habe to run a command 
        "python src/main.py"

## Features:
    Then we will get a list:-

    1. Create User
    2. List Users  
    3. List Seats
    4. Allocate Seat
    5. Release Seat
    6. Save & Exit
    0. Exit Without Saving


then we have to choose the Number Accordingly which we need to do.

## Requirements 
-Python 3.14.0
-no any library

## Data saving location
  data/users.json
  data/seats.json

-It can be easily opened in any text editor and from there, we can easily read and analyse.

## Project Structure 
```
vityarthi_python/
│
├── src/
│ ├── main.py
│ ├── users.py
│ ├── seats.py
│ └── storage.py
│
├── data/
│ ├── users.json
│ └── seats.json
│
├── tests/
│ ├── test_users.py
│ └── test_seats.py
│
├── README.md
├── report.md
├── statement.md
|
├── images/
|   └──screenshots
│      ├── List_and_allocation_seats.png
|      ├── menu_usercreation.png
|      ├── release_seats.png
|      ├── save_exit.png
│      └── testing.png
├── logs
```
## Instruction for testing
    To test the project you just have to run the command inside the terminal of the project folder:
        "python -m unittest discover tests"

## Screen Shots 

### MENU AND USER CREATION
![menu_usercreation](/images/screenshots/menu_usercreation.png)    

### LIST AND ALLOCATION SEATS
![list_allocation](/images/screenshots/List_and_allocation_seats.png)    

### RELEASE SEATS 
![release_seats](/images/screenshots/release_seats.png)

### Save and Exit
![save_exit](/images/screenshots/save_exit.png)

### Testing
![testing](/images/screenshots/testing.png)

