#!/usr/bin/env python

import Tkinter as tk
import wordament

NUM_LINS = 4
NUM_COLS = 4

class Letter(object):
        # Additional attributes:
        #  lin
        #  col
        #  butt
        #  letter
        
        def __init__(self, game, lin, col):
                self.game   = game
                self.lin    = lin
                self.col    = col
                self.letter = game.puzzle[0][lin][col]
                self.butt   = tk.Button(game.gameFrame, text=self.letter)
                self.butt.bind('<Double-1>', self.doubleclicked)
                self.butt.bind('<Button-1>', self.clicked)
                self.butt.grid(row=lin, column=col, pady=5, padx=5, ipadx=0, sticky=tk.N+tk.E+tk.S+tk.W)
        
        
        def addMeToMarklist(self):
                if self in self.game.marked:       # Clicking twice on the same square!.....
                        return
                print "hello " + str(self.letter) + "! from lin=" + str(self.lin) + "and col=" + str(self.col)
                if self.game.curcolor >= 0:
                        lastsquare = self.game.marked[-1]
                        lastcoords = (lastsquare.lin, lastsquare.col)
                        if lastcoords not in wordament.calc_neigbours((self.lin,self.col)):
                                return          # Invalid move, you aldraboon!!!
                        
                        lastsquare.butt.configure(bg=Application.game.COLORS[self.game.curcolor])
                self.game.curcolor += 1
                
                self.game.marked.append(self)
                self.butt.configure(bg=Application.game.HEADCOLOR)
        
        def clicked(self, event):
                self.addMeToMarklist()
        
        def doubleclicked(self, event):
                import time
                time.sleep(0.5)
                self.game.commitword()
                

class Application(tk.Frame):
        # Stuff that describes the game...
        class __game__CLASS:
                # Additional attributes:
                #  mainwindow
                #  puzzle
                #  gameFrame
                
                wordtab = [ [None,None,None,None], [None,None,None,None],
                            [None,None,None,None], [None,None,None,None] ]

                COLORS       = ("#555000000", "#666000000", "#777000000", "#888000000", \
                                "#999000000", "#AAA000000", "#BBB000000", "#CCC000000", \
                                "#DDD000000", "#EEE000000", "#FFF000000", "#FFF111000", \
                                "#FFF222000", "#FFF333000", "#FFF444000", "#FFF555000", \
                                "#FFF666000", "#FFF777000", "#FFF888000", "#FFF999000", )
                HEADCOLOR    = ("#000ffffff")
                DEFAULTCOLOR = ("lightgray")
                curcolor = -1         # -1 means that we are not selecting anything.....
                marked = []
                
                foundwords = set()
                
                # When the user doubleclicks, this gets called to find out the selected word...
                def commitword(self):
                        word = "".join(map(lambda(sqr):sqr.letter, self.marked))
                        print ("Entered word: " + word)
                        if word in self.puzzle[1]:
                                # User hit a word
                                if word not in self.foundwords:
                                        self.foundwords.add(word)
                                        self.mainwindow.okwords.insert(0, word)
                        else:
                                # Word is not in the puzzle
                                pass
                        
                        self.resetbuttons()
                
                def resetbuttons(self):
                        for lin in self.wordtab:
                                for elm in lin:
                                        elm.butt.configure(bg = self.DEFAULTCOLOR)
                        self.marked   = []
                        self.curcolor = -1
        game = __game__CLASS()
        
        class __gamestats__CLASS:
                # Additional attributes:
                #  mainwindow
                #  frame
                #  totalWordsLabel
                #  totalWords
                
                def createWidgets(self, mainwindow):
                        self.mainwindow = mainwindow
                        self.frame = tk.Frame(mainwindow)
                        
                        self.totalWordsLabel = tk.Label(self.frame, text="Total Words: ")
                        self.totalWordsLabel.grid(row=0, column=0)
                        
                        self.totalWords = tk.Label(self.frame, text=str(self.totalwords))
                        self.totalWords.grid(row=0, column=1)
        gamestats = __gamestats__CLASS()
        
        # okwords
        
    
        def __init__(self, puzzle, master=None):
                self.game.mainwindow = self
                self.game.puzzle = puzzle
                self.gamestats.totalwords = len(puzzle[1])
                
                tk.Frame.__init__(self, master)
                self.grid()
                self.createWidgets()

        def createWidgets(self):
                # A Frame for the game - better organization!...
                self.game.gameFrame = tk.Frame(self)
                self.game.gameFrame.grid(row=1, column=0)
                # The buttons to play...
                for lin in range(NUM_LINS):
                        for col in range(NUM_COLS):
                                self.game.wordtab[lin][col] = Letter(self.game, lin, col)
                
                # Some top-window info controls...
                self.gamestats.createWidgets(self)
                self.gamestats.frame.grid(row=0, column=0)
                
                # Side panel with list of words you found...
                self.game.foundwordsTk = tk.StringVar()
                self.okwords = tk.Listbox(self, listvariable=self.game.foundwordsTk)
                self.okwords.grid(row=0, column=1, rowspan=3, sticky=tk.N+tk.S+tk.E+tk.W)
                
                # The "Quit" button...
                self.quitButton = tk.Button(self, text="Quit", command=self.quit)
                self.quitButton.grid(row=2, column=0, pady=10, ipadx=0, sticky=tk.S+tk.E+tk.W)
        


app = Application(puzzle = wordament.gengame(wordament.wordlist))
app.master.resizable(width="FALSE", height="FALSE")
app.master.title('Wordament')
app.mainloop()
