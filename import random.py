import random
random.randint(1,3)

choices=['Rock','Scissor','Paper']
print('''welcome to our game these are the rules \n - Rock vs paper-> paper wins\n
- Rock vs scissor-> Rock wins\n
- paper vs scissor-> scissor wins.''')

while True:
    print('choose\n 1- Rock \n 2- Scissor \n 3- Paper')
    user_choice=int(input('ur choice: '))
    if user_choice >3 or user_choice<1:
        user_choice=int(input('enter valid choice(1,2,3): '))

    user_choice_name=choices[user_choice-1]

    comp_choice=random.randint(1,3)
    while comp_choice==user_choice:
        comp_choice=random.randint(1,3)
    comp_choice_name=choices[comp_choice-1]

    print('user choice: ',user_choice_name)
    print('computer choice: ',comp_choice_name)

    print(user_choice_name,'V/s',comp_choice_name)

    if (user_choice==1 and comp_choice==2) or(user_choice==2 and comp_choice==1):
        result='Rock'
    elif (user_choice==1 and comp_choice==3) or(user_choice==3 and comp_choice==1):
        result='Paper'
    else:
        result='Scissor'

    if result==user_choice_name:
        print('u win')
    else:
        print('u lost')
    ans=input('play again(y/n)?: ')
    if ans.lower()=='n':
        break