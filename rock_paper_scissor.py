import random

my_score = []
comp_score = []

dict = {
    "rock" : "🪨",
    "paper" : "📃",
    "scissor" : "🔪"
        }

while True:
    choice = input("rock/paper/scissor (q to quit) :  ").lower()
    possible_choice = ["rock" , "paper" , "scissor"]

    if choice == "q":
        print(" ")
        print("*" * 50)
        print(f"your score : {sum(my_score)}")
        print(f"computer's score : {sum(comp_score)}")

        if sum(my_score) > sum(comp_score):
            print("you won !!!!!!!")
        elif sum(comp_score) > sum(my_score):
            print("the computer won!!!!!!")
        else:
            print("its a draw !!!!")
        break

    elif choice == "rock" or choice == "r":
        print(f"you chose rock")
        computer_choice = random.choice(possible_choice)
        print(f"the computer chose {computer_choice}{dict[computer_choice]}")

        if computer_choice == "paper":
            comp_score.append(1)

        elif computer_choice == "scissor":
            my_score.append(1)

    elif choice == "paper" or choice == "p":
        print(f"you chose paper")
        computer_choice = random.choice(possible_choice)
        print(f"the computer chose {computer_choice}{dict[computer_choice]}")

        if computer_choice == "scissor":
            comp_score.append(1)
        elif computer_choice == "rock":
            my_score.append(1)

    elif choice == "scissor" or choice == "s":
        print(f"you chose scissor")
        computer_choice = random.choice(possible_choice)
        print(f"the computer chose {computer_choice}{dict[computer_choice]}")

        if computer_choice == "rock":
            comp_score.append(1)
        elif computer_choice == "paper":
            my_score.append(1)

    else:
        print("invalid input !!!")
        continue





