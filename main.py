from fileinput import filename
import os.path
from tkinter.font import NORMAL
import requests
from os import getcwd
import json
import random
import tkinter as tk

if not os.path.exists("words.json"):
    url = "https://raw.githubusercontent.com/HyperHarsho/Crosswords/master/words.json"
    directory = getcwd()
    filename = directory+"/words.json"
    r = requests.get(url)

    f = open(filename, "x")
    f.write(r.content.decode())

file = open("words.json", "r", encoding="utf8")
jsonObj = file.read()
word = json.loads(jsonObj)
file.close()

CROSSWORD = []

words = []

for w in word:
    CROSSWORD.append(w)

TABLE = [[0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
         [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
         [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
         [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
         [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
         [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
         [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
         [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
         [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
         [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]

LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

DIRECTIONS = [1, 2, 3, 4, 5, 6, 7, 8]

marked = []

r = random.SystemRandom()


def tablePrint():
    for i in range(len(TABLE)):
        for j in range(len(TABLE[i])):
            print(TABLE[i][j], "\t", end="")
        print()


def checkSpace(i, j):
    n = i*10+j
    if(marked.count(n) > 0):
        return False
    else:
        return True


def addWord(word, wlen, i, j):
    match DIRECTIONS[r.randint(0, len(DIRECTIONS)-1)]:
        case 1:
            if checkN(wlen, i, j):
                for w in word:
                    TABLE[i][j] = w
                    i = i - 1
                return True
            else:
                return False
        case 2:
            if checkNE(wlen, i, j):
                for w in word:
                    TABLE[i][j] = w
                    i = i - 1
                    j = j + 1
                return True
            else:
                return False
        case 3:
            if checkE(wlen, i, j):
                for w in word:
                    TABLE[i][j] = w
                    j = j + 1
                return True
            else:
                return False
        case 4:
            if checkSE(wlen, i, j):
                for w in word:
                    TABLE[i][j] = w
                    i = i + 1
                    j = j + 1
                return True
            else:
                return False
        case 5:
            if checkS(wlen, i, j):
                for w in word:
                    TABLE[i][j] = w
                    i = i + 1
                return True
            else:
                return False
        case 6:
            if checkSW(wlen, i, j):
                for w in word:
                    TABLE[i][j] = w
                    i = i + 1
                    j = j - 1
                return True
            else:
                return False
        case 7:
            if checkW(wlen, i, j):
                for w in word:
                    TABLE[i][j] = w
                    j = j - 1
                return True
            else:
                return False
        case 8:
            if checkNW(wlen, i, j):
                for w in word:
                    TABLE[i][j] = w
                    i = i - 1
                    j = j - 1
                return True
            else:
                return False
        case _:
            return False


def checkN(wlen, i, j):
    if(i-wlen >= 0):
        for x in range(wlen):
            ava = checkSpace(abs(i-x), j)
            if(ava == False):
                return False
        for x in range(wlen):
            marked.append((abs(i-x)*10)+j)
        return True
    else:
        return False


def checkNE(wlen, i, j):
    if(i-wlen >= 0 and j+wlen < 10):
        for x in range(wlen):
            ava = checkSpace(abs(i-x), j+x)
            if(ava == False):
                return False
        for x in range(wlen):
            marked.append((abs(i-x)*10)+(j+x))
        return True
    else:
        return False


def checkE(wlen, i, j):
    if(j+wlen < 10):
        for x in range(wlen):
            ava = checkSpace(i, j+x)
            if(ava == False):
                return False
        for x in range(wlen):
            marked.append((i*10)+(j+x))
        return True
    else:
        return False


def checkSE(wlen, i, j):
    if(i+wlen < 10 and j+wlen < 10):
        for x in range(wlen):
            ava = checkSpace(i+x, j+x)
            if(ava == False):
                return False
        for x in range(wlen):
            marked.append(((i+x)*10)+(j+x))
        return True
    else:
        return False


def checkS(wlen, i, j):
    if(i+wlen < 10):
        for x in range(wlen):
            ava = checkSpace(i+x, j)
            if(ava == False):
                return False
        for x in range(wlen):
            marked.append(((i+x)*10)+j)
        return True
    else:
        return False


def checkSW(wlen, i, j):
    if(i+wlen < 10 and j-wlen >= 0):
        for x in range(wlen):
            ava = checkSpace(i+x, j-x)
            if(ava == False):
                return False
        for x in range(wlen):
            marked.append(((i+x)*10)+(abs(j-x)))
        return True
    else:
        return False


def checkW(wlen, i, j):
    if(j-wlen >= 0):
        for x in range(wlen):
            ava = checkSpace(i, abs(j-x))
            if(ava == False):
                return False
        for x in range(wlen):
            marked.append((i*10)+(abs(j-x)))
        return True
    else:
        return False


def checkNW(wlen, i, j):
    if(i-wlen >= 0 and j-wlen >= 0):
        for x in range(wlen):
            ava = checkSpace(abs(i-x), abs(j-x))
            if(ava == False):
                return False
        for x in range(wlen):
            marked.append((abs(i-x)*10)+(abs(j-x)))
        return True
    else:
        return False


def main():
    for i in range(len(TABLE)):
        for j in range(len(TABLE[i])):
            TABLE[i][j] = str.upper(LETTERS[r.randint(0, len(LETTERS)-1)])
    i = 1
    while i <= 10:
        rword = str.upper(CROSSWORD[r.randint(0, len(CROSSWORD)-1)])
        length = len(rword)
        ri = r.randint(0, 9)
        rj = r.randint(0, 9)
        if(addWord(rword, length, ri, rj) == False):
            continue
        words.append(rword)
        i = i + 1
    tablePrint()
    with open("table.txt", "w") as f:
        pass
    file = open("table.txt", "a")
    file.write("Words-\n")
    for x in words:
        file.write(x+"\n")
    file.write("Table-\n")
    for i in range(len(TABLE)):
        for j in range(len(TABLE[i])):
            file.write(TABLE[i][j]+"\t")
        file.write("\n")
    file.write("Array-\n{")
    for i in range(len(TABLE)):
        for j in range(len(TABLE[i])):
            file.write("\""+TABLE[i][j]+"\",")
    file.write("}")


main()

m = tk.Tk()
m.title("CrossWord")
m.wm_resizable(False,False)
for i in range(len(TABLE)):
    for j in range(len(TABLE[i])):
        frame = tk.Frame(
            master=m,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(
            master=frame, text=TABLE[i][j], width=7, height=3)
        label.pack()

for i in range(len(words)):
    frame = tk.Frame(master=m, relief=tk.RAISED, borderwidth=1)
    frame.grid(row=i, column=11)
    label = tk.Label(master=frame, text=words[i], width=10, height=3)
    label.pack()

m.mainloop()
