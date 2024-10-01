import random
lst=['stone','paper','scissor']
score_user=0
score_computer=0
# stone---> scissor
# scissor---->paper
# paper----> stone
while True:
    user=input("Enter your choice('stone','paper','scissor')\nif you want to exit type 'exit': ")
    if user.lower()=='exit':
        print(f"Computer score:{score_computer}\nYour score:{score_user}")
        if score_user>score_computer:
            print('You wins')
        elif score_computer>score_user:
            print('Computer wins')
        else:
            print('Score are draw')
        break
    comp=random.choice(lst)
    if comp=='stone' and user.lower()=='scissor':
        print(f"your choice:{user}\ncomputer choice:{comp}")
        print('Computer wins')
        score_computer+=1
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    elif comp=='stone' and user.lower()=='paper':
        score_user+=1
        print(f"your choice:{user}\ncomputer choice:{comp}")
        print('You wins')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    elif comp=='scissor' and user.lower()=='paper':
        score_computer+=1
        print(f"your choice:{user}\ncomputer choice:{comp}")
        print('Computer wins')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    elif comp=='scissor' and user.lower()=='stone':
        score_user+=1
        print(f"your choice:{user}\ncomputer choice:{comp}")
        print('You wins')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    elif comp=='paper' and user.lower()=='stone':
        score_computer+=1
        print(f"your choice:{user}\ncomputer choice:{comp}")
        print('Computer wins')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    elif comp=='paper' and user.lower()=='scissor':
        score_user+=1
        print(f"your choice:{user}\ncomputer choice:{comp}")
        print('You wins')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    else:
        if user.lower() in lst:
            print('Draw')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
        else:
            print('Enter a valid choice')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
a=10
def hello():
    pass
hello()

print('dssdfdf')

