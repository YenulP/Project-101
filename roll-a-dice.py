import random

response = input("Do you want to roll a dice? If so, please answer with y")

while response == "y":
    no = random.randint(1,6)
    
    if no == 1:
        print("[- - - - -]")
        print("[         ]")
        print("[    0    ]")
        print("[         ]")
        print("[- - - - -]")
        response = input("Would you like to continue? y or n")

    if no == 2:
        print("[- - - - -]")
        print("[0        ]")
        print("[         ]")
        print("[        0]")
        print("[- - - - -]")
        response = input("Would you like to continue? y or n")

    if no == 3:
        print("[- - - - -]")
        print("[0        ]")
        print("[    0    ]")
        print("[        0]")
        print("[- - - - -]")
        response = input("Would you like to continue? y or n")

    if no == 4:
        print("[- - - - -]")
        print("[0       0]")
        print("[         ]")
        print("[0       0]")
        print("[- - - - -]")
        response = input("Would you like to continue? y or n")

    if no == 5:
        print("[- - - - -]")
        print("[0       0]")
        print("[    0    ]")
        print("[0       0]")
        print("[- - - - -]")
        response = input("Would you like to continue? y or n") 

    if no == 6:
        print("[- - - - -]")
        print("[0       0]")
        print("[0       0]")
        print("[0       0]")
        print("[- - - - -]")
        response = input("Would you like to continue? y or n")