from Board import Board

class Game:

    def __init__(self):
        self.board = Board()
        self.board_keys = []
        self.turn = 'X'
        self.count = 0
        for key in self.board.boxes:
            self.board_keys.append(key)

    def game(self):
        for i in range(10):
            self.board.show_board()
            print("Posicion de: " + self.turn)

            move = input()
            try:
                if 0 < int(move) >= 10:
                    print("Posicion invalida, ingrese : ")
                    continue
            except:
                pos = (ord(move))
                if 48 < pos > 57:
                    print("Posicion invalida, ingrese : ")
                    continue

            if self.board.boxes[move] == ' ':
                self.board.boxes[move] = self.turn
                self.count += 1
            else:
                print("Posicion llena, ingrese otra: ")
                continue

            if self.count >= 5:
                if self.board.boxes['1'] == self.board.boxes['2'] == self.board.boxes['3'] != ' ':
                    self.board.show_board()
                    print("\nGame Over.\n")
                    print(" Gano: " + self.turn)
                    break
                elif self.board.boxes['4'] == self.board.boxes['5'] == self.board.boxes['6'] != ' ':
                    self.board.show_board()
                    print("\nGame Over.\n")
                    print(" Gano: " + self.turn)
                    break
                elif self.board.boxes['7'] == self.board.boxes['8'] == self.board.boxes['9'] != ' ':
                    self.board.show_board()
                    print("\nGame Over.\n")
                    print(" Gano: " + self.turn)
                    break
                elif self.board.boxes['1'] == self.board.boxes['4'] == self.board.boxes['7'] != ' ':
                    self.board.show_board()
                    print("\nGame Over.\n")
                    print(" Gano: " + self.turn)
                    break
                elif self.board.boxes['2'] == self.board.boxes['5'] == self.board.boxes['8'] != ' ':
                    self.board.show_board()
                    print("\nGame Over.\n")
                    print(" Gano: " + self.turn)
                    break
                elif self.board.boxes['3'] == self.board.boxes['6'] == self.board.boxes['9'] != ' ':
                    self.board.show_board()
                    print("\nGame Over.\n")
                    print(" Gano: " + self.turn)
                    break
                elif self.board.boxes['3'] == self.board.boxes['5'] == self.board.boxes['7'] != ' ':
                    self.board.show_board()
                    print("\nGame Over.\n")
                    print(" Gano: " + self.turn)
                    break
                elif self.board.boxes['1'] == self.board.boxes['5'] == self.board.boxes['9'] != ' ':
                    self.board.show_board()
                    print("\nGame Over.\n")
                    print(" Gano: " + self.turn)
                    break


            if self.count == 9:
                print("\nGame Over.\n")
                print("Empato!!")

            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'

        restart = input("Jugar de nuevo?(s/n)")
        if restart == "s" or restart == "S":
            for key in self.board_keys:
                self.board.boxes[key] = " "
            self.game()
