import random
game = '''Let's Play
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vapourises Rock
(and as it always has)Rock crushes Scissors
'''
print(game)
while(1):
 play = input("Want to play game(Y/N)")
 if ((play=='Y') | (play=='y')):
    choice = '''Enter Your choice.
    1.Rock
    2.Paper
    3.Scissors
    4.Lizard
    5.Spock
    '''
    a= int(input(choice))
    c = random.randint(1,6)
    comp_choice ={1:'Rock',2:'Paper',3:'Scissors',4:'Lizard',5:'Spock'}
    b = comp_choice.get(c)
    d = comp_choice.get(a)
    print("Computer picked",b)
    print("You picked",d)

    if ((a==1 & c==1) | (a==2&c==2) | (a==3&c==3) | (a==4&c==4) | (a==5&c==5)):
        print("Tie")
    elif ((a==3&c==1)  | (a==4&c==1) | (a==1&c==2) | (a==5&c==2) | (a==2&c==3) |(a==4&c==3) | (a==5&c==4) | (a==2&c==4) | (a==1&c==5) | (a==3&c==5) | (a>5)  ):
        print("Computer Won")
    else:
        print("You Won")
 else:
    print("Thank You")
    break
