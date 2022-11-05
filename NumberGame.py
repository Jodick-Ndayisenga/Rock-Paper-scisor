import random
names = []
attempts = 0
y = input('Welcome to the game. Click Q if you do not want to play but rather quit and anything to continue: ').lower()
if y == 'q':
    print('Goodbye')
    quit()

else:

    name1 = str(input('What is you last name? ').lower())
    names.append(name1)
    name2 = str(input("Write any other name of your choice: ").lower())
    names.append(name2)
    name3 = str(input("finally, write any other name on your choice: ").lower())
    names.append(name3)



print(names)

while True:
    random_number = random.randint(0,2)
    computer_pick = names[random_number]

    choice = input('Now, pick one name from the list above and see if it matches with what the computer has picked: ').lower()

    if choice not in names:
        print('Please choose only one name from: ', names)
        continue
    

    elif choice in names:

        attempts += 1
        
        if choice != computer_pick:
            print('Sorry, you lost. Try again.')
            continue

        else:
            print('Congratulations, you won in ', attempts, 'attempts!')
            print('You won because the computer had also picked', computer_pick,'.')
            break

            

