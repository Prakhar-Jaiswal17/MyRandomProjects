import random

def enter():
    inp=input('Enter your choice - Rock, Paper or Scissor : ')
    print('\n')
    return inp


def Random_Select():
    l={1:'Rock', 2:'Scissor', 3:'Paper'}
    r=random.randint(1,3)
    t=l[r]
    return t

# def Tie():
#     print(f"I chose {ra}\nIt's a tie!!")
#     print('\n')
#     print(f"Current Score :\nComputer's Points\tUser Points\n   {CP}\t\t\t{UP}")
#     print('\n')
#     print("\tCHOOSE AGAIN!!")
#     print('\n')
#     choice=enter()
#     ra=Random_Select()

def main():
    Points=int(input('Of how many points do you want the game to be : '))
    print('\n')
    ra=Random_Select()
    choice=enter()
    CP=0
    UP=0
    while(CP!=Points or UP!=Points):
            # tie
        if(choice=='Rock' and ra=='Rock'):
            print(f"I chose {ra}\nIt's a tie!!")
            print('\n')
            print(f"Current Score :\nComputer's Points\tUser Points\n   {CP}\t\t\t{UP}")
            print('\n')
            print("\tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()
            continue

            #tie
        elif(choice=='Scissor' and ra=='Scissor'):
            print(f"I chose {ra}\nIt's a tie!!")
            print('\n')
            print(f"Current Score :\nComputer's Points\tUser Points\n   {CP}\t\t\t{UP}")
            print('\n')
            print("/tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()
            continue

            #tie
        elif(choice=='Paper' and ra=='Paper'):
            print(f"I chose {ra}\nIt's a tie!!")
            print('\n')
            print(f"Current Score :\nComputer's Points\tUser Points\n{CP}\t\t\t{UP}")
            print('\n')
            print("/tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()
            continue

            # loose
            # User choose rock and system chooses paper. System wins
        elif(choice=='Rock' and ra=='Paper'):
            print(f'I chose {ra}\n\nYou Loose!!')
            print('\n')
            CP+=1
            print(f"Current Score :\nComputer's Points\tUser Points\n{CP}\t\t\t{UP}")
            print('\n')
            # if(CP==Points or UP==Points):
            #     break
            print("/tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()

            # loose
            # User chose paper but system chose scissor. System wins
        elif(choice=='Paper' and ra=='Scissor'):
            print(f'I chose {ra}\n\nYou Loose!!')
            print('\n')
            CP+=1
            print(f"Current Score :\nComputer's Points\tUser Points\n{CP}\t\t\t{UP}")
            print('\n')
            # if(CP==Points or UP==Points):
            #     break
            print("/tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()

            # loose
            # User chose scissor but system chose rock. System wins
        elif(choice=='Scissor' and ra=='Rock'):
            print(f'I chose {ra}\n\nYou Loose!!')
            print('\n')
            CP+=1
            print(f"Current Score :\nComputer's Points\tUser Points\n{CP}\t\t\t{UP}")
            print('\n')
            # if(CP==Points or UP==Points):
            #     break
            print("/tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()

            # Win 
            # User chose rock but system chose scissor. User wins
        elif(choice=='Rock' and ra=='Scissor'):
            print(f'I chose {ra}\n\nYou Win!')
            print('\n')
            UP+=1
            print(f"Current Score :\nComputer's Points\tUser Points\n{CP}\t\t\t{UP}")
            print('\n')
            # if(CP==Points or UP==Points):
            #     break
            print("/tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()

            # Win 
            # User chose paper but system chose rock. User wins
        elif(choice=='Paper' and ra=='Rock'):
            print(f'I chose {ra}\n\nYou Win!!')
            print('\n')
            UP+=1
            print(f"Current Score :\nComputer's Points\tUser Points\n{CP}\t\t\t{UP}")
            print('\n')
            # if(CP==Points or UP==Points):
            #     break
            print("/tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()

            # Win 
            # User chose scissor but system chose paper. User wins
        elif(choice=='Scissor' and ra=='Paper'):
            print(f'I chose {ra}\n\nYou Win!!')
            print('\n')
            UP+=1
            print(f"Current Score :\nComputer's Points\tUser Points\n{CP}\t\t\t{UP}")
            print('\n')
            # if(CP==Points or UP==Points):
            #     break
            print("/tCHOOSE AGAIN!!")
            print('\n')
            choice=enter()
            ra=Random_Select()
        else:
            print('You chose a wrong input. Try Again')
            choice=enter()
            continue
    print('\n')
    if(UP>CP):
        print('Congratulations!!!!\nYou won against Computer.')
    else:
        print('You lost against Computer.\nBetter Luck Next Time!!!')
main()