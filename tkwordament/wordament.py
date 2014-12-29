
from english import wordlist

NUM_LINS = 4
NUM_COLS = 4

def calc_neigbours((lin, col)):
        ret = []
        ret.append((lin-1, col-1))
        ret.append((lin-1, col  ))
        ret.append((lin-1, col+1))
        ret.append((lin  , col-1))
        #         ((lin  , col  ))
        ret.append((lin  , col+1))
        ret.append((lin+1, col-1))
        ret.append((lin+1, col  ))
        ret.append((lin+1, col+1))
        return filter((lambda(pr): pr[0]>=0 and pr[1] >=0 and pr[0]<NUM_LINS and pr[1]<NUM_COLS )  , ret)

def findwordsat(wrds, idx, mat, (lin, col)):
        #print ("findwordsat(..., " + str(idx) + ", ..., (" + str(lin) + ", " + str(col) + ")" + ")")
        #printgame((mat, wrds))
        #print
        
        if (mat[lin][col] == None) or (wrds == []): return []
        from copy import copy
        matrix2pass = copy(mat)
        matrix2pass[lin] = copy(mat[lin])
        matrix2pass[lin][col] = None
        
        rets = filter((lambda(wrd): len(wrd)==idx), wrds)
        words2pass = filter((lambda(wrd): (len(wrd) != idx) and (wrd[idx] == mat[lin][col])), wrds)
        if words2pass == []: return rets

        neigs = calc_neigbours((lin,col))
        for neig in neigs:
                rets.extend(findwordsat(words2pass, idx+1, matrix2pass, neig))
        return rets

# Old version of function
'''def choose_letter(words):
        from random import random
        letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return letters[int(random()*len(letters))]
'''
# This version is better than previous one because this one is more probablistic...
def choose_letter(words):
        from random import random
        statletters = []
        for i in words: statletters.extend(i)
        statletters.sort()
        return statletters[int(random()*len(statletters))]

def gentab(words):
        matrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
        
        for lin in range(NUM_LINS):
                for col in range(NUM_COLS):
                        matrix[lin][col] = choose_letter(words)
                        
        return matrix

def gensols(words, matrix):
        sols = []
        for lin in range(NUM_LINS):
                for col in range(NUM_COLS):
                        sols.extend(findwordsat(words, 0, matrix, (lin,col)))
        sols = list(set(sols))
        sols.sort()
        return sols

def gengame(words, matrix = None):
        if matrix == None:
                matrix = gentab(words)
        sols   = gensols(words, matrix)
        return (matrix, sols)


def printmat(matrix):
        for lin in range(NUM_LINS):
                for col in range(NUM_COLS):
                        print(matrix[lin][col]),
                print

def printgame(game):
        matrix = game[0]
        sols = game[1]
        
        for lin in range(NUM_LINS):
                for col in range(NUM_COLS):
                        print(matrix[lin][col]),
                print
        
        print (sols)


def genandprint():
        gened=gengame(wordlist)
        printgame(gened)
        return gened

''' Run instructions: ...
mygame = genandprint()
'''
