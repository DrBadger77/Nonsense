##Band Name creator

import random
import requests
nounarray =[]
adjarray = []

while True:
    try:
        namecount = int(input("How many band names would you like generating (0 to exit)?"))
        if namecount == 0:
            print("Ok, bye bye!")
            break
        else:
            #nounfile = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt")
            nounfile = requests.get("http://www.desiquintans.com/downloads/nounlist/nounlist.txt")
            noundata = nounfile.text
            nounarray = noundata.splitlines()
            #adjfile = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-adjectives.txt")
            adjfile = requests.get("https://raw.githubusercontent.com/taikuukaits/SimpleWordlists/master/Wordlist-Adjectives-All.txt")
            adjdata = adjfile.text
            adjarray = adjdata.splitlines()
            
            repeats = 1
            
            while repeats < namecount + 1:
                adjnumber = random.randint(0, len(adjarray))
                nounnumber = random.randint(0, len(nounarray))
                noun = nounarray[nounnumber]
                adj = adjarray[adjnumber]
                print("Band name " + str(repeats) + ": " + adj, noun)
                repeats += 1
                if repeats == namecount+1:
                    print("Done!")
                    break
    except ValueError:
        print("Just integer values, please")
















