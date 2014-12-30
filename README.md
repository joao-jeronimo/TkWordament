TkWordament
===========

Simple Wordament clone in Python+Tkinter.
There is room for improvement.

How to run?
===========

Just run "gui.py" Python script.
   python guy.py

How to add a new language?
==========================

1 - You need a ugly lot of word in the language you want. The words
    must be in ALLCAPS, with no spaces or non-letters, and they must
    be put into a Python list.

2 - Go find a big list of word in the Internet and save it in a txt
    file with some name (it doesn't need to be a .txt, but that way
    it is the same way that I have done for Portuguese and English).
    For exemplo "esperanto.txt". You can use whatever non-letter
    character to separtate the word, ideally a newline, but that's
    not necessary!

3 - Tweak "data.py" module to suit your preprocesing needs. It alread
    has some code that will remove all ponctuation for you.
     - However, if your tongue uses accents, then you have to include
       some code to get rid of them. For portuguese I was lucky enough
       to find a list of words that already had their accents stripped
       out, so... The magic words are "unicode normalization".

4 - Load "data.py" module into Python with command "python -i data.py".
    Then, inside the interactive session, run:
       dumpfrom("esperanto.txt", "esperanto.py")
    Press Ctrl-D to quit Python's intereactive session.

5 - Edit "wordament.py" file and put the filename without extension of
    your .py file where it currently ways "portugues".

6 - Then run the game with:
       python guy.py

* - This may not work with Python 3. Let me know if you try.
