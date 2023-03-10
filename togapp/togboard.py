import random

class TogBoard:
    TUZD = -1

    def __init__(self, pos):
        self.fields = [int(x) for x in pos.split(',')]
        self.finished = False
        self.gameResult = -2
        self.moves = []

    def getPosition(self):
        return ",".join(str(x) for x in self.fields)
    
    def printPosition(self):
        position = "<table border='1' cellspacing='3' height='300'>"
        position += "<tr class='numbering'>"
        position += "<td class='kazan' rowspan='4'>" + str(self.fields[21]) + "</td>"
        for i in range(9,0,-1):
            position += "<td>" + str(i) + "</td>"
        position += "<td class='kazan' rowspan='4'>" + str(self.fields[20]) + "</td>"
        position += "</tr>"

        position += "<tr class='otau'>"
        for i in range(17,8,-1):
            if (self.fields[i] == TogBoard.TUZD):
                position += "<td>X</td>"
            else:
                position += "<td>" + str(self.fields[i]) + "</td>"

        position += "</tr>"

        position += "<tr class='otau'>"
        for i in range(0,9):
            if (self.fields[i] == TogBoard.TUZD):
                position += "<td>X</td>"
            else:
                position += "<td>" + str(self.fields[i]) + "</td>"
        position += "</tr>"

        position += "<tr class='numbering'>"
        for i in range(1,10):
            position += "<td>" + str(i) + "</td>"
        position += "</tr>"
        position += "</table>"
 
        return position

    def printNotation(self):
        num = 0
        notation = ""

        for move in self.moves:
            num += 1
            if num % 2 == 1:
                notation += str(num // 2 + 1) + ". " + move
            else:
                notation += " " + move + "\n"

        return notation

    def checkPosition(self):
        color = self.fields[22]

        numWhite = 0
        for i in range(9):
            if self.fields[i] > 0:
                numWhite += self.fields[i]

        numBlack = 162 - numWhite - self.fields[20] - self.fields[21]

        if color == 0 and numWhite == 0:
            self.fields[21] += numBlack
        elif color == 1 and numBlack == 0:
            self.fields[20] += numWhite

        if self.fields[20] > 81:
            self.finished = True
            self.gameResult = 1

        elif self.fields[21] > 81:
            self.finished = True
            self.gameResult = -1

        if self.fields[20] == 81 and self.fields[21] == 81:
            self.finished = True
            self.gameResult = 0

    def makeMove(self, move):
        madeMove = str(move)
        color = self.fields[22]
        move = move + (color * 9) - 1
        num = self.fields[move]
        tuzdCaptured = False

        if num == 0 or num == TogBoard.TUZD:
            print("Incorrect move!")
            return

        if num == 1:
            self.fields[move] = 0
            sow = 1
        else:
            self.fields[move] = 1
            sow = num - 1

        num = move

        for i in range(sow):
            num += 1
            if num > 17:
                num = 0

            if self.fields[num] == TogBoard.TUZD:
                if num < 9:
                    self.fields[21] += 1
                else:
                    self.fields[20] += 1
            else:
                self.fields[num] += 1

        if self.fields[num] % 2 == 0:
            if color == 0 and num > 8:
                self.fields[20] += self.fields[num]
                self.fields[num] = 0
            elif color == 1 and num < 9:
                self.fields[21] += self.fields[num]
                self.fields[num] = 0

        elif self.fields[num] == 3:
            if color == 0 and self.fields[18] == 0 and num > 8 and num < 17 and self.fields[19] != num - 8:
                self.fields[18] = num - 8
                self.fields[num] = TogBoard.TUZD
                self.fields[20] += 3
                tuzdCaptured = True
            elif color == 1 and self.fields[19] == 0 and num < 8 and self.fields[18] != num + 1:
                self.fields[19] = num + 1
                self.fields[num] = TogBoard.TUZD
                self.fields[21] += 3
                tuzdCaptured = True

        if color == 0:
            self.fields[22] = 1
        else:
            self.fields[22] = 0

        if num < 9:
             num = num + 1
        else:
             num = num - 8

        madeMove += str(num)
        if tuzdCaptured:
            madeMove += 'x';
        self.moves.append(madeMove)

        self.checkPosition()
        return madeMove

    def makeRandomMove(self):
        possible = []
        color = self.fields[22]
                             
        for i in range(1, 10):
            move = i + (color * 9) - 1
            num = self.fields[move]
            if num > 0:
                possible.append(i)
        
        if len(possible) == 0:
            print("No possible moves!")
            return
        
        randMove = random.choice(possible)
        return self.makeMove(randMove)