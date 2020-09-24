class Board:

    def __init__(self):
        self.boxes = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '7': ' ', '8': ' ', '9': ' '}

    def show_board(self):
        print(self.boxes['1'] + '|' + self.boxes['2'] + '|' + self.boxes['3'])
        print('-+-+-')
        print(self.boxes['4'] + '|' + self.boxes['5'] + '|' + self.boxes['6'])
        print('-+-+-')
        print(self.boxes['7'] + '|' + self.boxes['8'] + '|' + self.boxes['9'])