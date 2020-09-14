board = {'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print("Posicion de: " + turn)

        move = input()
        try:
            if 0 < int(move) >= 9:
                print("Posicion invalida, ingrese : ")
                continue
        except:
            pos = (ord(move))
            if 48 < pos > 57:
                print("Posicion invalida, ingrese : ")
                continue

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("Posicion llena, ingrese otra: ")
            continue

        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ':
                print(board['1'] + '|' + board['2'] + '|' + board['3'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print("\nGame Over.\n")                
                print(" Gano: " +turn)                
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                print(board['1'] + '|' + board['2'] + '|' + board['3'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print("\nGame Over.\n")                
                print(" Gano: " +turn)                
                break
            elif board['7'] == board['8'] == board['9'] != ' ':
                print(board['1'] + '|' + board['2'] + '|' + board['3'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print("\nGame Over.\n")                
                print(" Gano: " +turn)                
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                print(board['1'] + '|' + board['2'] + '|' + board['3'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print("\nGame Over.\n")                
                print(" Gano: " +turn)                
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                print(board['1'] + '|' + board['2'] + '|' + board['3'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print("\nGame Over.\n")                
                print(" Gano: " +turn)                
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                print(board['1'] + '|' + board['2'] + '|' + board['3'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print("\nGame Over.\n")                
                print(" Gano: " +turn)                
                break 
            elif board['3'] == board['5'] == board['7'] != ' ':
                print(board['1'] + '|' + board['2'] + '|' + board['3'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print("\nGame Over.\n")                
                print(" Gano: " +turn)                
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                print(board['1'] + '|' + board['2'] + '|' + board['3'])
                print('-+-+-')
                print(board['4'] + '|' + board['5'] + '|' + board['6'])
                print('-+-+-')
                print(board['7'] + '|' + board['8'] + '|' + board['9'])
                print("\nGame Over.\n")                
                print(" Gano: " +turn)                
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("Empato!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Jugar de nuevo?(s/n)")
    if restart == "s" or restart == "S":  
        for key in board_keys:
            board[key] = " "
        game()

if __name__ == "__main__":
    game()