import random 

def play_game():
    lucky_num=random.randint(1,50)


    while True:
        user_num=int(input('Guess the lucky number'))
        
        if user_num==lucky_num:
            print('your guess is exact you are the winner')
            break

        elif user_num<lucky_num:
            print('You guess is too low')
        elif user_num>lucky_num:
            print('You guess is too high')

    print('Thank you for playing')
play_game()


