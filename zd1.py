tb1 = {'7': ' ' , '8': ' ' , '9': ' ' ,
      '4': ' ' , '5': ' ' , '6': ' ' ,
      '1': ' ' , '2': ' ' , '3': ' ' }
print('вот макрировка полей таблицы:')
print('7' + '|' + '8' + '|' + '9')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('1' + '|' + '2' + '|' + '3')

print('начинаем игру :')

ke1 = []


for key in tb1:
    ke1.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def gm1():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(tb1)
        print("Ходите знаком," + turn + ".Выберите куда поставить знак?")

        move = input()        

        if tb1[move] == ' ':
            tb1[move] = turn
            count += 1
        else:
            print("Выберите другую позицию.\nКуда поставить знак?")
            continue

        
        if count >= 5:
            if tb1['7'] == tb1['8'] == tb1['9'] != ' ': # across the top
                printBoard(tb1)
                print("\nКонец.\n")                
                print(" **** " +turn + " Вы поведили!. ****")                
                break
            elif tb1['4'] == tb1['5'] == tb1['6'] != ' ': # across the middle
                printBoard(tb1)
                print("\nКонец .\n")                
                print(" **** " +turn + " Вы поведили!. ****")
                break
            elif tb1['1'] == tb1['2'] == tb1['3'] != ' ': # across the bottom
                printBoard(tb1)
                print("\nКонец .\n")                
                print(" **** " +turn + " Вы поведили!. ****")
                break
            elif tb1['1'] == tb1['4'] == tb1['7'] != ' ': # down the left side
                printBoard(tb1)
                print("\nКонец .\n")                
                print(" **** " +turn + " Вы поведили!. ****")
                break
            elif tb1['2'] == tb1['5'] == tb1['8'] != ' ': # down the middle
                printBoard(tb1)
                print("\nКонец .\n")                
                print(" **** " +turn + " Вы поведили!. ****")
                break
            elif tb1['3'] == tb1['6'] == tb1['9'] != ' ': # down the right side
                printBoard(tb1)
                print("\nКонец .\n")                
                print(" **** " +turn + " Вы поведили!. ****")
                break 
            elif tb1['7'] == tb1['5'] == tb1['3'] != ' ': # diagonal
                printBoard(tb1)
                print("\nКонец .\n")                
                print(" **** " +turn + " Вы поведили!. ****")
                break
            elif tb1['1'] == tb1['5'] == tb1['9'] != ' ': # diagonal
                printBoard(tb1)
                print("\nКонец .\n")                
                print(" **** " +turn + " Вы поведили!. ****")
                break 

        
        if count == 9:
            print("\nКонец .\n")                
            print("Ничья!!")

        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    
    restart = input("Хотите сыграть ещё раз?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in ke1:
            tb1[key] = " "

        gm1()

if __name__ == "__main__":
    gm1()