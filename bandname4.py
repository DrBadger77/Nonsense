##Band Name creator

import random
import requests
nounarray =[]
adjarray = []
nounarray2 = []
adjarray2 = []

while True:
    try:
        namecount = int(input("How many band names would you like generating (0 to exit)?"))
        if namecount == 0:
            print("Ok, bye bye!")
            break
        else:
            nounfile = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-nouns.txt")
            nounfile2 = requests.get("http://www.desiquintans.com/downloads/nounlist/nounlist.txt")

            noundata = nounfile.text
            noundata2 = nounfile2.text

            nounarray = noundata.splitlines()
            nounarray2 = noundata2.splitlines()

            

            finalnounarray = nounarray + nounarray2

            


            adjfile = requests.get("https://raw.githubusercontent.com/hugsy/stuff/main/random-word/english-adjectives.txt")
            adjfile2 = requests.get("https://raw.githubusercontent.com/taikuukaits/SimpleWordlists/master/Wordlist-Adjectives-All.txt")

            adjdata = adjfile.text
            adjdata2 = adjfile2.text

            adjarray = adjdata.splitlines()
            adjarray2 = adjdata2.splitlines()

            

            finaladjarray = adjarray + adjarray2
            
            
            repeats = 1
            
            while repeats < namecount + 1:
                adjnumber = random.randint(0, len(finaladjarray))
                nounnumber = random.randint(0, len(finalnounarray))
                noun = finalnounarray[nounnumber]
                adj = finaladjarray[adjnumber]
                print("Band name " + str(repeats) + ": " + adj, noun)
                repeats += 1
                if repeats == namecount+1:
                    print("Done!")
                    break
    except ValueError:
        print("Just integer values, please")
















