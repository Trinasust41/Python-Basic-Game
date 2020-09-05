import random
while True:
    
    flag=True
    while flag:
        number=input("Plz type a number for an upper bound to play the game! ")

        if number.isdigit():
            print("YAAP!! Let's play!")
            number=int(number)
            flag=False

        else :
            print("You have typed an invalid input! Plz try again!")

    secrect=random.randint(1,number)

    guess=None
    count = 1

    while guess!=secrect:
        guess =input("Guess a number between 1 and " +str(number)+": ")

        if guess.isdigit():
            guess=int(guess)

        if guess==secrect:
            print("Yaah! You got it!")
        else:
            print("Try again")
            count+=1
    if count==1:
        st1=str("guess")
    else:
        st1=str("guesses")

    print("it took you "+str(count)+" "+st1)
