


def preprocess(in_wordlist):
        upper_wordlist = map(str.upper, in_wordlist)

        seps_wordlist = []
        while True:
                redo = False
                for word in upper_wordlist:
                        points = list(set(word)-set("ABCDEFGHIJKLMNOPQRSTUVWXYZ "))
                        if   len(points) == 0:  seps_wordlist.extend(word.split())
                        else:
                                seps_wordlist.extend(word.split(points[0]))
                                if len(points) > 1: redo = True
                        
                        
                seps_wordlist = filter((lambda(wrd): len(wrd)>=3), seps_wordlist)
                
                if not redo:    break
                upper_wordlist = seps_wordlist
                seps_wordlist = []
        
        return seps_wordlist



