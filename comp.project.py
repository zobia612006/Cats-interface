def CloseAnswerWins():
    import random 
    points=0
    CHOICE= "yes"
    choice= input("Welcome! Are you ready to play this game? \n " )
    if  str.lower(choice)== CHOICE:
        print("Great! Here are the rules of the game...")
        print(" 1: CALCULATORS ARE NOT ALLOWED since this game tests your mental math skills \n 2: You will be given two 2-digit numbers to multiply. \n 3: Of course it is difficult to perform such a large calculation without using a calculator, so you will have to give an approximate value \n 4: If the answer is within +-100 of the actual answer it will deemed as correct! \n 5: There will be ten rounds in total. Good luck!")
        for i in range(0,10):
            num1= random.randint(10,99)
            num2= random.randint(10,99)
            num12= str(num1) + " x "
            num22= str(num2) + "?"
            answer= int(input("What is " + num12 +num22 + "\n" ))
            if answer>= (num1*num2)-100 and answer<= (num1*num2)+100:
                print("Correct!")
                points=points+1
            else:
                print("Incorrect")
        if points==0:
            print("Your score is 0/10!")
        elif points==1:
            print("Your score is 1/10!")
        elif points==2:
            print("Your score is 2/10!")
        elif points==3:
            print("Your score is 3/10!")
        elif points==4:
            print("Your score is 4/10!")
        elif points==5:
            print("Your score is 5/10!")
        elif points==6:
            print("Your score is 6/10!")
        elif points==7:
            print("Your score is 7/10!")
        elif points==8:
            print("Your score is 8/10!")
        elif points==9:
            print("Your score is 9/10!")
        else:
            print("Your score is 10/10!")
            
    else:
        print("Okay! Come back when you are ready.")

def LoadFireBlock():
    import random
    user_wins=0
    computer_wins=0
    CHOICE= "yes"
    choice= input("Welcome! Are you ready to play this game? \n " )
    if  str.lower(choice)== CHOICE:
        print("Great! Here are the rules of the game...")
        print(" 1: Fire is not possible without any load \n 2: Block cancels the effect of fire \n 3: The number of fires with which you can attack is equal to the number of loads you have \n 4: Using fire means minus 1 load \n 5:Fire covers load given that you had a load otherwise you lose \n 6: There will be three rounds in total!")
            
        for i in range(0,3):
            user_load= 0
            computer_load=0
            um= False
            while um!= True:
                user_action= input("Enter a choice: load, fire or block\n " )
                possible_actions= ["load" , "fire" , "block"]
                computer_action= random.choice(possible_actions)
                print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
                if user_action== "load":
                    if computer_action== "load":
                        computer_load= computer_load+1
                        user_load= user_load+1
                        print("Both sides gain one load!")
                    elif computer_action== "fire":
                        if computer_load== 0:
                            print("You win because fire is not possible without any load!")
                            um= True
                            user_wins= user_wins+1
                        else:
                            print("You lose since fire covers load!")
                            um= True
                            computer_wins= computer_wins +1
                    else:
                        user_load= user_load+1
                        print("You gain one load!")
                elif user_action== "fire":
                    if user_load==0:
                        print("You lose since fire is not possible without any load!")
                        um= True
                        computer_wins= computer_wins+1
                    else:
                        if computer_action== "load":
                            print("You win wince fire covers load!")
                            user_wins= user_wins+1
                            um= True
                        elif computer_action== "fire":
                            if computer_load==0:
                                print("You win since fire without load is not possible without any load!")
                                um= True
                                user_wins= user_wins+1
                            else:
                                print("Both sides lost one load....let's continue!")
                                user_load= user_load-1
                                computer_load= computer_load-1
                        else:
                            user_load= user_load -1
                            print("Your fire was blocked so you lose one load!")
                else:
                    if computer_action== "load":
                        computer_load= computer_load+1
                        print("The other side gains one load!")
                    elif computer_action== "fire":
                        if computer_load==0:
                            print("You win since fire is not possible without any load!")
                            user_wins= user_wins+1
                            um= True
                        else:
                            print("You blocked the fire so the other side loses one load!")
                            computer_load= computer_load-1
                    else:
                        print("Nothing happened...let's continue!")
                
        if user_wins==0:
            print("3:0, you lose!")
        elif user_wins==1:
            print("2:1, you lose!")
        elif user_wins==2:
            print("2:1, you win!")
        else:
            print("3:0, you win!")
    else:
        print("Okay! Come back when you are ready!")

def OrderGuessingGame():
    import random
    points=0
    CHOICE= "yes"
    choice= input("Welcome! Are you ready to play this game? \n " )
    if  str.lower(choice)== CHOICE:
        print("Great! Here are the rules of the game...")
        print(" 1: I will think of three numbers in a specific order \n 2: You will be told the numbers but not the order, that is for you to guess! \n 3: If you guess the correct order you get a point \n 4: There will be 5 rounds in total and you will be given five chances in each round \n 5: This game is based on pure luck!")
        for i in range(0,5):
            num1= random.randint(0,99)
            num2= random.randint(0,99)
            num3= random.randint(0,99)
            print("The three numbers are " + str(num1)  + ", " + str(num2) + " and " + str(num3) + ". What do you think is the order I chose for these numbers?")
            nums= [num1, num2, num3]
            random.shuffle(nums)
            num12= str(nums[0])
            num22 = str(nums[1])
            num32= str(nums[2])
            first= input("1st: ")
            second= input("2nd: ")
            third= input("3rd: ")
            index=0
            while (first!= num12 or second!= num22 or third!= num32) and index!= 4:
                print("Incorrect. Try again")
                index= index +1
                first= input("1st: ")
                second= input("2nd: ")
                third= input("3rd: ")

            if index==4:
                print("Incorrect")
            else:
                print("Correct!")
                points= points+1

            
            

        if points==0:
            print("Your score is 0/5!")
        elif points==1:
            print("Your score is 1/5!")
        elif points==2:
            print("Your score is 2/5!")
        elif points==3:
            print("Your score is 3/5!")
        elif points==4:
            print("Your score is 4/5!")
        else:
            print("Your score is 5/5!")         
    else:
        print("Okay! Come back when you are ready.")




game_choice=0
while game_choice!=4: 
    game_choice= int(input("Press 1 to play the 'Close Answer Wins' game, press 2 to play the 'Load Fire Block' game, press 3 to play the 'Order Guessing Game' or press 4 if you don't want to play \n"))
    if game_choice==1:
        CloseAnswerWins()
    elif game_choice==2:
        LoadFireBlock()
    elif game_choice==3:
        OrderGuessingGame()


