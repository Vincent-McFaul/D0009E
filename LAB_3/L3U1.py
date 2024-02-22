#Metod 1: För att lägga in ett ord och beskrivning i respektive lista.
def insertLists(wordList, descList):
    while True:
        userWordInsert = input("\nWord to insert: ")
        
        #Kollar om karaktärer finns, tillåter inte noll karaktärer.
        if len(userWordInsert) > 0:
            
            #Lägger till ordet till "wordList", men kollar om det redan finns.
            wordList.append(userWordInsert.lower())
            if len(set(wordList)) != len(wordList): #Jämför längden av listan med "set"-versionen (har bara unika element).
                print("Duplicate word not allowed")
                del wordList[-1] #Tar bort senaste ordet då det redan finns ett.
            else:
                break
            
        else:
            print("\nEmpty space not allowed")
    
    while True:
        userDescInsert = input("\nDescription to insert: ")
        #Kollar om karaktärer finns, tillåter inte noll karaktärer.
        if len(userDescInsert) > 0:
            descList.append(userDescInsert) #Lägger till beskrivningen i "deskList".
            break
           
        else:
            print("\nEmpty space not allowed")

#Metod 2: För att lägga in ett ord och beskrivning i listan med tupletter.
def insertTuplets(tupletList):
    while True:
        userWordInsert = input("\nWord to insert: ")
        
        #Kollar om karaktärer finns, tillåter inte noll karaktärer.
        if len(userWordInsert) > 0:
            
            #Genererar en temporär lista med det nyangivna ordet plus bara orden från "tupletList".
            tempList = [userWordInsert.lower()]
            for tup in tupletList:
                tempList.append(tup[0])
            
            #Jämför längden av listan med "set"-versionen (har bara unika element).
            if len(tempList) != len(set(tempList)):
                print("Duplicate word not allowed")
                tempList.clear() #Rensar listan.
                
            else:
                while True:
                    userDescInsert = input("\nDescription to insert: ")
                    
                    #Kollar om karaktärer finns, tillåter inte noll karaktärer.
                    if len(userDescInsert) > 0:
                        
                        #Slår ihop ordet och beskrivningen till en tuplet för att lägga in i listan "tupletList".
                        wordAndDesc = (userWordInsert.lower(), userDescInsert)
                        tupletList.append(wordAndDesc)
                        return

                    else:
                        print("\nEmpty space not allowed")
        else:
            print("\nEmpty space not allowed")
            
#Metod 3: För att lägga in ett ord och beskrivning i katalogen.            
def insertDict(wordDict):
    while True:
        userWordInsert = input("\nWord to insert: ")
        
        #Kollar om karaktärer finns, tillåter inte noll karaktärer.
        if len(userWordInsert) > 0:
            
            #Genererar en temporär lista med det nyangivna ordet plus bara orden/nycklar från "wordDict".
            tempList = [userWordInsert.lower()]
            for key in wordDict.items():
                tempList.append(key[0])
            
            #Jämför längden av listan med "set"-versionen (har bara unika element).
            if len(tempList) != len(set(tempList)):
                print("Duplicate word not allowed")
                tempList.clear() #Rensar listan.
                
            else:
                while True:
                    userDescInsert = input("\nDescription to insert: ")
                    
                    #Kollar om karaktärer finns, tillåter inte noll karaktärer.
                    if len(userDescInsert) > 0:
                        
                        #Lägger in ordet som nyckel och beskrivning i "wordDict".
                        wordDict[userWordInsert.lower()] = userDescInsert.lower()
                        return

                    else:
                        print("\nEmpty space not allowed")
        else:
            print("\nEmpty space not allowed")

#Metod 1: För att slå upp ett ord och få dess beskrivning.
def lookupLists(wordList, descList):
    while True:
        userLookUp = input("\nWord to lookup: ")
        
        #Kollar om karaktärer finns, tillåter inte noll karaktärer.
        if len(userLookUp) > 0:
            
            #Letar efter ordets existens i "wordList".
            if userLookUp.lower() in wordList:
                print("\nWord: ", userLookUp.lower())
                
                #Tar index av ordet i "wordList" och skriver ut med samma index i "descList".
                print("Description: ", descList[wordList.index(userLookUp.lower())])
                break
            else:
                print("\nWord does not exist")
            
        else:
            print("\nEmpty space not allowed")

#Metod 2: För att slå upp ett ord och få dess beskrivning.         
def lookupTuplets(tupletList):
    while True:
        userLookUp = input("\nWord to lookup: ")
        
        #Kollar om karaktärer finns, tillåter inte noll karaktärer.
        if len(userLookUp) > 0:
            
            #Letar efter ordets existens genom iterering av varje tuple i "tupletList".
            indexCounter = 0 #En räknare för att hålla koll på indexet av ordet som söks.
            for tup in tupletList:
                if userLookUp.lower() in tup[0]:
                    print("\nWord: ", userLookUp.lower())
                    
                    #Letar upp och skriver ut beskrivningen i med samma index som ordet i "tupletList".
                    print("Description: ", tupletList[indexCounter][1])
                    return
                else:
                    indexCounter += 1
                    
            print("\nWord does not exist")
            
        else:
            print("\nEmpty space not allowed")

#Metod 3: För att slå upp ett ord och få dess beskrivning.    
def lookupDict(wordDict):
    while True:
        userLookUp = input("\nWord to lookup: ")
        
        #Kollar om karaktärer finns, tillåter inte noll karaktärer.
        if len(userLookUp) > 0:
            
            #Letar efter ordets existens i "wordDict".
            if userLookUp.lower() in wordDict:
                print("\nWord: ", userLookUp.lower())
                
                #Letar upp och skriver ut beskrivningen i "wordDict".
                print("Description: ", wordDict[userLookUp.lower()])
                break
            else:
                print("\nWord does not exist")
            
        else:
            print("\nEmpty space not allowed")

#Huvudfunktionen genererar menyerna, och är oändlig om man inte väljer att stänga av.
def main():
    
    #Metod 1: Två listor.
    wordList = [
        
    ]
    descList = [
        
    ]

    #Metod 2: En lista med ord/beskrivning i tupletter.
    tupletList = [
        
    ]

    #Metod 3: En katalog.
    wordDict = {
        
    }
    
    while True:
        #Skriver ut start-menyn
        print("\nMenu for dictionary")
        print("1: Insert")
        print("2: Lookup")
        print("3: Exit program\n")
        userMenuChoose = input("Choose alternative: ")
        
        #Alternativen kallar olika funktioner programmet kan göra.
        
        if userMenuChoose == "1": #För att lägga till ord och beskrivning.
            #insertLists(wordList, descList)
            #insertTuplets(tupletList)
            insertDict(wordDict)
        elif userMenuChoose == "2": #För att slå upp ord.
            #lookupLists(wordList, descList)
            #lookupTuplets(tupletList)
            lookupDict(wordDict)
        elif userMenuChoose == "3": #Dödar/"Hoppar ur" programmet.
            return
        else:
            print("Input not valid")

#Startar programmet.
main()