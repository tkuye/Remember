from time import sleep 
import os 
import random


header ='------------------------------------------\nRemember The Word\n------------------------------------------'
print(header)
print('There will be a sequence of words displayed,\nchoose the word with the correct beginning letter.')

to_play = input('Do you wish to play? (Y/N): ')

def WordGame(words=[]):
    try: 
        wordcountstr = input('How many words would you like to play with?\n(Up to 26.): ')
        wordcount = int(wordcountstr)
        if wordcount > 26 or wordcount < 1:
            raise ValueError
    except ValueError:
        print('Sorry that is not a valid number.')
        return WordGame()

    with open('words.txt') as f:
        lines = [line.rstrip() for line in f]
        newdict = dict()
        random.shuffle(lines)
        for line in lines:
            newdict[line[0]] = line
        shufflewords = newdict.values()
        words = random.sample(list(shufflewords), k=wordcount)

    first_word = dict()
    for word in words:
        os.system('cls')
        print(header)
        first_word[word[0]] = word
        print(word)
        sleep(1)

    os.system('cls')
    first, word = random.choice(list(first_word.items()))
    print(header)
    input_word = input(f'What was the word that started with the letter {first}?: ')

    if input_word == word:
        print('Yes that is correct!')
        play_again = input('Do you wish to play again? (Y/N) ')
        if play_again.strip() == 'Y':
            choicefunc()
        f.close()
    else:
        print('Sorry, that is not the correct answer.')
        print(f'The correct answer is {word}.')
        play_again = input('Do you wish to play again? (Y/N) ')
        if play_again.strip() == 'Y':
            choicefunc()
        f.close()




def WordGameIncrement(i):
    os.system('cls')
    print(f'---------------------------------------------------\nLEVEL {i}\n---------------------------------------------------')
    sleep(1.5)
    with open('words.txt') as f:
        lines = [line.rstrip() for line in f]
        newdict = dict()
        random.shuffle(lines)
        for line in lines:
            newdict[line[0]] = line
        shufflewords = newdict.values()
        words = random.sample(list(shufflewords), k=i)

    first_word = dict()
    for word in words:
        os.system('cls')
        print(header)
        first_word[word[0]] = word
        print(word)
        sleep(1)

    os.system('cls')
    first, word = random.choice(list(first_word.items()))
    print(header)
    input_word = input(f'What was the word that started with the letter {first}?: ')

    if input_word == word:
        print('Yes that is correct!')
        continuer = input('Press enter key to continue... ')
        if continuer == '':
            pass
        if i == 26:
            sleep(1.2)
            print('Congratulations, you beat all the levels!')
            
            return 
        WordGameIncrement(i + 1)

    else:
        print('Sorry, that is not the correct answer.')
        print(f'The correct answer is {word}.')
        play_again = input('Want to play again? (Y/N): ')
        if play_again.strip() == 'Y' or play_again.strip() == 'y':
            choicefunc()
        f.close()



def choicefunc():
    os.system('cls')
    print(header)
    num = 1
    choices = input('Do you wish to play with levels or free-play mode?\n(Enter 1 for levels or 2 for free-play): ')
    if choices.strip() == '1':
        WordGameIncrement(num)
    elif choices.strip() == '2':
        WordGame()
    else:
        print('Please pick a valid choice. (1 or 2)')
        sleep(1.1)
        return choicefunc()


if to_play.strip() == 'Y' or to_play.strip() =='y':
    choicefunc()
    



