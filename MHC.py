from tabulate import tabulate 

#totalScore is to add up total score for each question

def quiz():
    totalScore = 0
    print("Lets see your mood for today")
    print("Please answer the following questions so we can determine you mood on a scale from 1 to 10")
    input("Click Enter to continue")
    print("____________________________________________")


    #question 1
    print("Question 1")
    while(True):
        try:
            scoreinp = input("What would you rate your past week mentally 0-10?: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + scoreinp
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Next question")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")

    #question 2
    print("Question 2")
    while(True):
        try:
            scoreinp = input("What would you rate your past week physically 0-10?: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + scoreinp
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Next question")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")

    #question 3
    print("Question 3")
    while(True):
        try:
            scoreinp = input("How would you rate your anxiety level from 0-10?: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + (10 - scoreinp) 
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Next question")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")

    #question 4
    print("Question 4")
    while(True):
        try:
            scoreinp = input("How would you rate your nutritional level from 0-10?: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + scoreinp
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Next question")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")
        
    #question 5
    print("Question 5")
    while(True):
        try:
            scoreinp = input("Rate your stress level for the past month: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + (10 - scoreinp)
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Next question")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")

    #question 6
    print("Question 6")
    while(True):
        try:
            scoreinp = input("How would rate your interactions with others this past week from 0-10?: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + scoreinp
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Next question")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")

    #question 7
    print("Question 7")
    while(True):
        try:
            scoreinp = input("Rate your productivity level for the past month from 0-10: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + scoreinp
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Next question")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")

    #question 8
    print("Question 8")
    while(True):
        try:
            scoreinp = input("Rate your motivational level for the past month from 0-10: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + scoreinp
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Next question")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")

    #question 9
    print("Question 9")
    while(True):
        try:
            scoreinp = input("How would you rate your feelings about your environment on a scale from 0-10?: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + scoreinp
            print("Your current score: ", totalScore)
            print("____________________________________________")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")

    #question 10
    print("Last question!")
    print("Question 10")
    while(True):
        try:
            scoreinp = input("How would you rate your sleep schedule?: ")
            scoreinp = float(scoreinp)
            if (scoreinp < 0 or scoreinp > 10):
                raise ValueError()
            totalScore = totalScore + scoreinp
            print("Your current score: ", totalScore)
            print("____________________________________________")
            print("Thanks for taking our quiz")
            break
        except ValueError:
            print("____________________________________________")
            print("Looks like this is an invalid input, Please try again")
            print("Please enter a number from 1-10")
           
    averageScore = totalScore/10 
    print("Your average score was ", averageScore)
    print(" ")
    if(averageScore <= 10 and averageScore >= 9):
        print("Amazing! Seems like your doing well!")
    elif(averageScore < 9 and averageScore >= 7):
        print("Great! Seems like your managing just fine!")
    elif(averageScore < 7 and averageScore >= 5):
        print("Mhmm you could do better, Reach out for some help if needed!")
    elif(averageScore < 5 and averageScore >= 3):
        print("Stay strong! Don't Hesistate to reach out for help!")
    elif(averageScore < 3 and averageScore >= 0):
        print("Looks like your not doing well, You should ask for help! It's always right to seek the aid when you really need it!")
    print("____________________________________________")
    intro()

def scale():
    print("____________________________________________")
    scale = [['Assesment', 'Score'],
             ['Amazing', '9-10'],
             ['Great', '7-8'],
             ['Managing', '5-6'],
             ['Gloomy', '3-4'],
             ['Need Support', '0-2']]

    print(tabulate(scale, headers ="firstrow", tablefmt = "psql"))
    print("Here is our scale!")
    print("____________________________________________")
    intro()

def exit():
    print("Thanks again for taking our quiz! Feel free to take our quiz anytime. Take care!")

def intro():
    print("Hey there! Come answer 10 questions to see how your mental health is!")
    print("If you want to take our quiz enter 'y'")
    print("If you want to see our scale enter 's'")
    print("If you to exit enter 'e'")
    inp = input("Choose an option!: ")
    print("____________________________________________")
    if (inp == 'y' or inp == 'Y'):
        quiz()
    elif (inp == 's' or inp == 'S'):
        scale()
    elif( inp == 'e'or inp == 'E'):
        exit()
    else:
        print("Invalid Option, Please try again")
        introRetry()

def introRetry():
    print("____________________________________________")
    print("If you want to take our quiz enter 'y'")
    print("If you want to see our scale enter 's'")
    print("If you to exit enter 'e'")
    inp = input("Choose an option!: ")
    print("____________________________________________")
    if (inp == 'y' or inp == 'Y'):
        quiz()
    elif (inp == 's' or inp == 'S'):
        scale()
    elif( inp == 'e'or inp == 'E'):
        exit()
    else:
        print("Invalid Option, Please try again")
        introRetry()

intro()