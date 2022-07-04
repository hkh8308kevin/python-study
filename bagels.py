"""야구게임, by Kevin Lab kevin@kevinlab.com
A deducative logic game whrere you must guess a number based on clues.
This code is available at https://nostarch.com/big-book-small-python-programing
A version of this game is featured in the book, "Invent your Own
Computer Games with Pyhton" https://nostarch.com/inventwithpython
Tags: Short, game, puzzle"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('=============================================')
    print('''야구게임을 진행해 봅시다. Made by KEVINLAB
=============================================
                    
원하는 숫자를 생각해 보세요.
아래는 단서에 대한 의미입니다.

     Ball : 내가 생각하는 숫자가 포함되어 있습니다.
     Strike : 내가 생각하는 숫자와 위치가 정확합니다.
     Error : 내가 생각하는 숫자가 포함되어 있지 않습니다. 
     
     
단서는 Ball Strike Error.'''.format(NUM_DIGITS))
     
    while True:
        
        secretNum = getSecretNum()
        print('숫자를 생각해 보세요.{}자리'.format(NUM_DIGITS))
        print('당신은 {} 번째를 시도 하실 수 있습니다.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('추측 #{}: '.format(numGuesses))
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break   
            if numGuesses > MAX_GUESSES:
                print('당신의 정답은 아래와 같습니다.')
                print('정답은 {}.'.format(secretNum))
                   
    
        print('Do you waant to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thank you for playing!!!.')
        
        
def getSecretNum():
    """NUM_DIGITS개의 임의 숫자로 구성된 문자열을 반환한다."""
    numbers = list('0123456789')  
    random.shuffle(numbers)
    
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum



def getClues(guess, secretNum):
    
    
    if guess == secretNum: 
        return 'You got it'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            
            clues.append('strike')
        elif guess[i] in secretNum:
            
            clues.append('ball')
    if len(clues) == 0:
        return 'error'
    else:
        
        
        clues.sort()
        
        return ' '.join(clues)
    
        
if __name__ == '__main__':
    main()