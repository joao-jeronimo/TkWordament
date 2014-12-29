#!/usr/bin/env python

import Tkinter as tk
import wordament

NUM_LINS = 4
NUM_COLS = 4

class Letter(object):
        #lin
        #col
        #butt
        #letter
        
        def __init__(self, parent, lin, col):
                self.lin    = lin
                self.col    = col
                self.letter = parent.puzzle[0][lin][col]
                self.butt   = tk.Button(parent, text=self.letter)
                self.butt.bind('<Double-1>', self.doubleclicked)
                self.butt.bind('<Button-1>', self.clicked)
                self.butt.grid(row=lin, column=col, pady=5, padx=5, ipadx=0, sticky=tk.N+tk.E+tk.S+tk.W)
                self.parent = parent
        
        
        def addMeToMarklist(self):
                if self in self.parent.marked:       # Clicking twice on the same square!.....
                        return
                print "hello " + str(self.letter) + "! from lin=" + str(self.lin) + "and col=" + str(self.col)
                if self.parent.curcolor >= 0:
                        lastsquare = self.parent.marked[-1]
                        lastcoords = (lastsquare.lin, lastsquare.col)
                        if lastcoords not in wordament.calc_neigbours((self.lin,self.col)):
                                return          # Invalid move, you aldraboon!!!
                        
                        lastsquare.butt.configure(bg=Application.COLORS[self.parent.curcolor])
                self.parent.curcolor += 1
                
                self.parent.marked.append(self)
                self.butt.configure(bg=Application.HEADCOLOR)
        
        def clicked(self, event):
                self.addMeToMarklist()
        
        def doubleclicked(self, event):
                import time
                time.sleep(0.5)
                self.parent.commitword()
                

class Application(tk.Frame):
        wordtab = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
        COLORS = (      "#555000000", "#666000000", "#777000000", "#888000000", \
                        "#999000000", "#AAA000000", "#BBB000000", "#CCC000000", \
                        "#DDD000000", "#EEE000000", "#FFF000000", "#FFF111000", \
                        "#FFF222000", "#FFF333000", "#FFF444000", "#FFF555000", \
                        "#FFF666000", "#FFF777000", "#FFF888000", "#FFF999000", )
        HEADCOLOR   = ("#000ffffff")
        curcolor = -1         # -1 means that we are not selecting anything.....
        marked = []
        
    
        def __init__(self, puzzle, master=None):
                self.puzzle = puzzle
                
                tk.Frame.__init__(self, master)
                self.grid()
                self.createWidgets()
        
        def commitword(self):
                word = "".join(map(lambda(sqr):sqr.letter, self.marked))
                print ("Entered word: " + word)
                if word in self.puzzle[1]:
                        # User hit a word
                        self.okwords.insert(0, word)
                else:
                        # Word is not in the puzzle
                        pass
                
                self.resetbuttons()

        def resetbuttons(self):
                for lin in range(NUM_LINS):
                        for col in range(NUM_COLS):
                                self.wordtab[lin][col].butt.configure(bg="lightgray")
                self.marked   = []
                self.curcolor = -1

        def createWidgets(self):
                for lin in range(NUM_LINS):
                        for col in range(NUM_COLS):
                                self.wordtab[lin][col] = Letter(self, lin, col)
                
                self.foundwords = tk.StringVar()
                self.okwords = tk.Listbox(self, listvariable=self.foundwords)
                self.okwords.grid(row=0, column=NUM_COLS, rowspan=NUM_LINS+2, sticky=tk.N+tk.S+tk.E+tk.W)
                
                self.quitButton = tk.Button(self, text="Quit", command=self.quit)
                self.quitButton.grid(row=NUM_LINS+1, column=0, columnspan=NUM_COLS, pady=10, ipadx=0, sticky=tk.S+tk.E+tk.W)
        


app = Application(puzzle = wordament.gengame(wordament.wordlist))
app.master.title('Wordament')
app.mainloop()
