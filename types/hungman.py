# HANGMAN = (
# """
# """,

# """1-STEP
# _______
# """,
# """2-STEP
#        |
#        |
#        |
#        |
#        |     
#        |     
#        | 
# _______| 
# """,
# """3-STEP
# ________
#    |   |
#        |
#        |
#        |
#        |          
#        |
#        | 
# _______| 
# """,
# """4-STEP
#  _______
#    |   |
#    0   |
#   /X\  |
#   / \  |
#        |     
#        |     
#        |
# _______|  
# """,
# """ЖАЛЬ
#  _______
#        |
#    0   |
#   |X|  |
#   / \  |
#        |     
#        |     
#        | 
# _______|
# """
# )
# while True:
#     max_wrong = len(HANGMAN) - 1
#     words = {"KUTMAN":"\n✮✮✮✮✮✮The Best student in the group Питоновая долина...",
#              "DANIYAL":"\n☄☄☄☄☄☄Fireman of the second week..." ,
#              "MAKERS" :"\n①①①①①First bootcamp in Bishkek...",
#              "SANZHAR":"\n👨‍💻👨‍💻👨‍💻👨‍💻The best curator on Makers ",
#              "KASYM":"\n♔♔♔♔President of Kazahstan",
#              "БИШКЕК":"\nStolitsa Kyrgyzstana"
#             }
#     import random
#     key = random.choice(list(words.keys()))
#     length = "*"*len(key)
#     wrong = 0
#     used = []
#     while wrong<max_wrong and length!=key:
#         print(">>>Вот тебе небольшая подсказка:\n",words[key])
#         print(HANGMAN[wrong])
#         print('''>>>Вы уже предлагали следующие буквы: ''',used)
#         print(">>>Отгаданное вами в слове сейчас выглядит так: ",length,"\n")
#         guess1 = input("Введите букву: ")
#         guess = guess1.upper()
#         while guess in used:
#             guess = input("Введите другую букву: ")
#             guess = guess.upper()
#         used.append(guess)
#         if guess in key:
#             print("Молодец! Буква ",guess," есть в слове!")
#             new = ""
#             for i in range(len(key)):
#                 if guess == key[i]:
#                     new += guess
#                 else:
#                     new += length[i]
#             length = new
#         else:
#             print("К сожалению буквы ",guess," нет в слове.")
#             wrong += 1
#     if wrong == max_wrong:
#         print("Вас повесили ༒ ")
#         print(HANGMAN[wrong])
#     else:
#         print("\n\n\nУра! У тебя получилось!")
#     print("Вы предлагали следующие буквы: ",used)
#     print("Отгаданное вами в слове выглядит так: ",length,"\n")
    
#     play_again = input("Сыграем еще? (y/n): ") 
#     if play_again.lower() != "y": 
#         break 


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# new_dict = {k: [v2 for v2 in v.values()] for k, v in my_dict.items()}
# print(new_dict)

# def count_symbols(str_):
#     vowels = 0
#     consonants = 0
#     symbols = 0
    
#     for l in str_.lower():
#         if l in "йуеыаоэяиюё":
#             vowels += 1 
#         elif l in "цкнгбшщзмчвфжрлдтсп":
#             consonants += 1
#         else:
#             symbols += 1
#     return f'Количество гласных: {vowels}, согласных: {consonants}, остальных символов: {symbols}'

# print(count_symbols('Кутман медербеков'))


"""
def func(name,last_name,age,*args,**kwargs):
    print('Имя:' ,name)
    print('Фамилия:',last_name)
    print('Возраст:',age)
    if args:
        print('Статус:',args[0])
        print('Супруг:',kwargs)
    else:
        print('Статус : Холост(-а)')
    
func('Jhon','Snow',26)
func('Trion','Lanister',21,'Женат',wife_name = 'Sansa',wife_last_name='Stark')
"""
