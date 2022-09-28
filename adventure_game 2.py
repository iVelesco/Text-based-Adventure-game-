import random
import time


def print_pause(message):
    print(message)
    time.sleep(2)


def solution_1():
    print_pause("Hearing about the invasion, the peasants and farmers "
                "decided to join you in the fight.")
    print_pause("Theyy want to defend the homeland.")
    print_pause("They need prior training, knowing that they have"
                " never held a gun in their hand.")
    print_pause("But it seems that the motivation to defend the"
                " country can defeat any enemy.")


def solution_2():
    print_pause("Messages with requests for help arrived in "
                "neighboring countries.")
    print_pause("You have managed to convince them that a possible oss"
                " of yours will allow the aggressor to continue his "
                "campaign further in Europe.")
    print_pause("That it's questioning freedom and peace in their"
                " country.")
    print_pause("Requests for help were heard and each sent you help "
                "in money and soldiers to oppose a common enemy "
                "together.")
    print_pause("What solidarity!!!!!!!")


def solution_3():
    print_pause("Your engineers have invented a new method of casting "
                "cannons.")
    print_pause("This allows them to be poured faster.")
    print_pause("Also, cannons are lighter and can shoot at a greater "
                "distance.")
    print_pause("It seems that the new discovery will radically change"
                " rules of the game.")


def solution_4():
    print_pause("The advisers from the Contry Council decided to carry"
                " out a strategic fight against the enemy...")
    print_pause("having the advantage of knowing the birthplaces.")
    print_pause("Harassment and exhaustion of the enemy army due to "
                "small attacks, allows you to slow down he invader.")
    print_pause("Now he is forced to fight in the winter in "
                "unfavirable conditions.")
    print_pause("It seems the ideal time to give the final fight.")


def introduction():
    print_pause("You are in the 15th century after Christ. You are the"
                " leader of a small country in the east of the "
                "European continent")
    print_pause("You are in the situation of a potential aggression "
                "from an empire that, from what we heard, conquers "
                "everything on which it turns its eyes")
    print_pause("Even if you do not have unlimited wealth, this "
                "territory is still an important strategic point for "
                "the developement of the campaign inside Europe.")
    print_pause("The time has come to convene the country's assembly "
                "to find a solution.")
    print_pause("The final decision is up to you.")


list_of_solutions = [solution_1, solution_2, solution_3, solution_4]


def first_choice(items):
    print_pause("It seems like a good idea that is supported by the "
                "vast majority of boyars.")
    if "Solution founded" in items:
        print_pause("But you have already made a decision and this was"
                    " accepted in the country's assembly.")
        print_pause("Now it's time to take action.")
    else:
        random.choice(list_of_solutions)()
        items.append("Solution founded")


def second_choice(items):
    print_pause("You decided to attack.")
    print_pause("Legends will be written about your courage.")
    if "Solution founded" in items:
        print_pause("Now it's the best moment to go for final attack.")
        decision_2 = input("1. Yes. We will surely win!\n2. Non. Maybe"
                           " it's better to postpone this fight.\n")
        if decision_2 == '1':
            print_pause("Do not hesitate! You won!")
            play_again(items)

        elif decision_2 == '2':
            print_pause("Looks like you have some doubts about the "
                        "upcoming battle. You return to the meeting.")
    else:
        print_pause("From what we managed to find out, a army of 120,"
                    "000 soldiers is heading towards your country")
        print_pause("It seems too naive to rely only on luck in this "
                    "battle")
        print_pause("Are you sure you want to continue the attack?")
        decision_2 = input("1. Yes. We will surely win!\n"
                           "2. Non. Maybe it's better to postpone this"
                           " fight.\n")
        if decision_2 == '1':
            print_pause("The soldiers followed you until the last"
                        " moment,")
            print_pause("but it turned out that the enemy was better "
                        "prepared than you.")
            print_pause("Legends will be written about your courage"
                        "...")
            print_pause("if anyone stays alive to tell them.")
            play_again(items)
        elif decision_2 == '2':
            print_pause("Even if the battle preparations aare in full "
                        "swing, it seems that the decision to postpone"
                        " the battle is welcome.")
            print_pause("Better to review your strategy before "
                        "attacking.")
            print_pause("You have returned to the country's assembly "
                        "to make another decision.")


def play_game(items):
    items = []
    introduction()
    while True:
        print_pause("What will you decide now?")
        print_pause("1. Postpone the fight and retreat to a safer "
                    "place.")
        print_pause("2. You decide to face the enemy here and now.")
        decision_1 = input("Make you choice: 1 or 2\n")
        if decision_1 == '1':
            first_choice(items)
        elif decision_1 == '2':
            second_choice(items)
        else:
            print_pause("Looks like no one agrees with this decision.")
            print_pause("I suggest you review your order.")


def play_again(items):
    input_again = input("Do you want to play again?\n"
                        "Please Enter \"yes\" or \"no\".\n")
    if input_again == "yes" or input_again == "y":
        play_game(items)
    if input_again == "no" or input_again == "n":
        print_pause("Game Over\n")
        exit()
    else:
        print_pause("Please only Enter \"yes\" or \"no\".")
        play_again(items)


def start_to_play():

    items = []
    play_game(items)
    play_again(items)


start_to_play()
