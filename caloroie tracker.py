import os
from datetime import datetime

now = datetime.now()
tdee = 0
calorie = 0
protein = 0
fat = 0
carb = 0
date = now.strftime("%m %d %Y")
food = ''
def confirmtdee():
    if os.path.exists("tdee.txt"):
        try:
            with open("tdee.txt")  as f:
                lines = f.readlines()
                print('Continue with tdee ' + str(lines[0]) + '?(Y/N)')
                tdeeconfirm = None
                while tdeeconfirm is None:
                        print('Enter Y/N')
                        tdeeconfirm = input().upper()
                        if tdeeconfirm == 'Y' or tdeeconfirm == 'N':
                            if tdeeconfirm == 'Y':
                                global tdee
                                tdee = lines[0]
                                askOption()
                            else:
                                tdeeconfirm = True
                                maketdee()
                        else:
                            tdeeconfirm = None
                            pass
                            
        except IndexError:
            os.remove('tdee.txt')
            pass
            5
    else:
        askOption()

def askOption():
    print('[1] To enter a custom food\n[2] To use saved food\n[3] To open food list\n[4] View macros\n[5]\
 Save food to list\n[6] To remove food from list\n[7] Foods eaten today\n[8] Change tdee')
    choice = input()
    if choice.isdigit():
        if choice == '1':
            foodName()
        elif choice == '2':
            addFood()
        elif choice == '3':
            openFoodList()
        elif choice == '4':
            macrosLeft()
        elif choice == '5':
            saveFood()
        elif choice == '6':
            deleteFood()
        elif choice == '7':
            foodsEaten()
        elif choice == '8':
            maketdee()
        else:
            askOption()
    else:
        askOption()
        
           


def maketdee():
    tdee1 = None
    while tdee1 is None:

        try:
            print('Enter tdee')
            tdee1 = int(input())
        except ValueError:
            print('Please type a number')
            pass
    confirmation = None
    while confirmation is None:
            print('Your tdee is ' + str(tdee1) + '. Confirm? (Y/N)')
            confirmation = input().upper()
            if confirmation == 'Y' or confirmation == 'N':
                if confirmation == 'Y':
                    global tdee
                    tdee = tdee1
                    text_file = open(("tdee.txt") , "w")
                    text_file.write(str(tdee))
                    text_file.close()
                    askOption()
                else:
                    maketdee()


        

def foodName():
    spam = True
    while spam == True:
        print('Enter food name')
        global food
        food = input()
        if food.isalpha():
            calorie()
        else:
            foodName()


    calorie()

def calorie():
    spam = True
    while spam == True:
        print('Enter food calorie')
        global calorie
        calorie = input()
        if calorie.isdigit():
            protein()
        else:
            calorie()


def protein():
    spam = True
    while spam == True:
        print('Enter food protein')
        global protein
        protein = input()
        if protein.isdigit():
            fat()
        else:
            protein()

def fat():
    spam = True
    while spam == True:
        print('Enter food fat')
        global fat
        fat = input()
        if protein.isdigit():
            carb()
        else:
            fat()

def carb():
    spam = True
    while spam == True:
        print('Enter food carb')
        global carb
        carb = input()
        if protein.isdigit():
            print(food + '\n' + 'calorie ' + calorie + '\n' + 'protein ' + protein +
                  '\n' + 'fat ' + fat + '\n' + 'carb ' + carb +
                    '\n' + 'Confirm? Y/N\n [0] For main menu')
            confirmation = input().upper()
            if confirmation == 'Y':
                save()
            elif confirmation == '0':
                askOption()
            else:
                foodName()
            
        else:
            carb()
    
def save():
    text_file = open(("tdee " + date + ".txt"), "a")
    text_file.write('' + "\n")
    text_file.write(food + "\n")
    text_file.write('cal ' + calorie + "\n")
    text_file.write('protein ' + protein + "\n")
    text_file.write('fat ' + fat + "\n")
    text_file.write('carb ' + carb + "\n")
    text_file.close()

    calLeft()

def calLeft():
    with open("tdee " + date + ".txt") as file:
        cal = 0


        for line in file:
            if 'cal' in line:
                cal = cal + int(line[4:])
        print('You have eaten ' + str(cal) + ' calories today.')
        print(str(int(tdee) - int(cal)) + ' calories left')
        askOption()
        
def saveFood():
    print('Enter food name')
    foodNameS = input().upper()
    print('Enter calories')
    foodCalS = input()
    print('Enter protein')
    foodProteinS = input()
    print('Enter fat')
    foodFatS = input()
    print('Enter carb')
    foodCarbS = input()
    print(foodNameS + '\n' + 'calorie ' + foodCalS + '\n' + 'protein ' + 
          foodProteinS + '\n' + 'fat ' + foodFatS + '\n' + 'carbs ' + foodCarbS)
    print('Confirm? Y/N')
    while True:
            confirmation = input().upper()
            if confirmation == 'Y' or confirmation == 'N':
                if confirmation == 'Y':
                    text_file = open(("FoodList.txt") , "a")
                    text_file.write('' + "\n")
                    text_file.write('\n' + 'Food: ' + foodNameS.lower() + "\n")
                    text_file.write('cal ' + foodCalS + "\n")
                    text_file.write('protein ' + foodProteinS + "\n")
                    text_file.write('fat ' + foodFatS + "\n")
                    text_file.write('carb ' + foodCarbS)
                    text_file.close()
                    askOption()
                    break
                else:
                    askOption()
                
def openFoodList():
    with open("FoodList.txt")  as f:
        lines = f.readlines()
        for i in range(len(lines)-1):
            if 'Food:' in lines[i]:
                print(lines[i], end='')
                print(lines[i+1], end='')
                print(lines[i+2], end='')
                print(lines[i+3], end='')
                print(lines[i+4])

    input('Press enter to go to main menu')
    askOption()
    
def addFood():
    print('Enter food name')
    food = input().upper()
    with open("FoodList.txt")  as f:
        lines = f.readlines()
        for i in range(len(lines)-1):
            if food in lines[i]:

                
                print(lines[i], end='')
                print(lines[i+1], end='')
                print(lines[i+2], end='')
                print(lines[i+3], end='')
                print(lines[i+4], end='')
                print('Confirm? (Y/N)')
                confirmation = input().upper()
                if confirmation == 'Y' or confirmation == 'N':
                    if confirmation == 'Y':
                        text_file = open(("tdee " + date + ".txt") , "a")
                        text_file.write('' + "\n")
                        text_file.write('Food' + "\n")
                        text_file.write(lines[i] )
                        text_file.write(lines[i+1])
                        text_file.write(lines[i+2])
                        text_file.write(lines[i+3])
                        text_file.write(lines[i+4])
                        text_file.close()
                        print('Succesfully added ' + lines[i].lower(), end="")
                        calLeft()
                    else:
                        break
    
    print('[0] To go to main menu')
    option = input()
    while True:
        if option == '0':
            askOption()
            break
        else:
            print('Try again')

def macrosLeft():
    try:
        with open("tdee " + date + ".txt" , "r") as file:
            protein = 0
            carb = 0
            fat = 0
            cal = 0
            for line in file:
                if 'protein' in line:
                    protein = protein + int(line[7:])
                elif 'carb' in line:
                    carb = carb + int(line[5:])
                elif 'fat' in line:
                    fat = fat + int(line[4:])
                elif 'cal' in line:
                    cal = cal + int(line[4:])
            print('Cal = ' + str(cal))
            print('Protein = ' + str(protein))
            print('Fat = ' + str(fat))
            print('Carbs = ' + str(carb))
            input("Press Enter to continue...")
            askOption()
    except FileNotFoundError:
        input('No entries yet')
        askOption()


def deleteFood():
    print('Enter food name')
    dfood = input().lower()
    if len(dfood) == 0:
        deleteFood()
    else:
        with open("FoodList.txt", "r") as f:
            content = f.read()
            if ('Food: ' + dfood) in content:
                new_text = ""
                with open("FoodList.txt", "r") as f:
                    lines = f.readlines()
                    i = 0
                    while i < len(lines):
                        if dfood in lines[i]:
                            print('Deleting ' + lines[i] + lines[i + 1] + lines[i + 2] + lines[i + 3] + 'Confirm? Y/N')
                            confirmation = input().upper()
                            while True:
                                if confirmation in ["YES", "Y"]:
                                    i += 5
                                    break
                                elif confirmation in ["NO", "N"]:
                                    new_text += lines[i]
                                    i += 1
                                    break
                                else:
                                    deleteFood()
                        else:
                            new_text += lines[i]
                            i += 1
                with open("FoodList.txt", "w") as f:
                     f.write(new_text)
                askOption()
            
            else:
                print('food not found')
                input('press enter to go back to menu')
                askOption()
def foodsEaten():
    with open(("tdee " + date + ".txt"), "r") as f:
        lines = f.read()
        print(lines)
confirmtdee()
