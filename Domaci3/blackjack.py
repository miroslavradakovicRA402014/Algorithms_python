import random

def cmp(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else: 
        return -1        


def blackJack(deck,i):
    moves = [0]
    n = len(deck)
    if n-1 < 4: 
        print ("Don't enough cards in deck!")
        return 0
    print ("\n")    
    for p in range(2,n-i-2):
        print ("Player draws :",deck[i+4 : i+p+2])
        player = cardNumValue(deck[i]) + cardNumValue(deck[i+2])
        for ci in range(i+4,i+p+2):
            player += cardNumValue(deck[ci])        
        if player > 21:
            print ("Player busted!")
            print ("Player = ",player)
            moves.append(-1 + blackJack(deck,i+p+2))   
            break    
        for d in range(2,n-i-p):
            print ("Dealer draws :",deck[i+p+2 : i+p+d])
            dealer = cardNumValue(deck[i+1]) + cardNumValue(deck[i+3])
            for ci in range(i+p+2,i+p+d):
                dealer += cardNumValue(deck[ci])
            if dealer >= 17:
                print ("Dealer stop drawing")
                break
        if dealer > 21:
            print ("Dealer busted!")
            dealer = 0
        print ("Player = ",player,"Dealer = ",dealer)
        moves.append(cmp(player,dealer) + blackJack(deck,i+p+d))                          
    return max(moves)    

def cardValue(val):    
    if val == 2:
        return '2'
    elif val == 3:
        return '3'
    elif val == 4:
        return '4'
    elif val == 5:
        return '5'
    elif val == 6:
        return '6'
    elif val == 7:
        return '7'
    elif val == 8:
        return '8'
    elif val == 9:
        return '9'
    elif val == 10:
        return '10'
    elif val == 11:
        return 'A'
    elif val == 12:
        return 'J'
    elif val == 13:
        return 'Q'
    elif val == 14:
        return 'K'
        
def cardNumValue(val):
    if val == '2':
        return 2
    elif val == '3':
        return 3
    elif val == '4':
        return 4
    elif val == '5':
        return 5
    elif val == '6':
        return 6
    elif val == '7':
        return 7
    elif val == '8':
        return 8
    elif val == '9':
        return 9
    elif val == '10':
        return 10
    elif val == 'A':
        return 11        
    elif val == 'J':
        return 12
    elif val == 'Q':
        return 13
    elif val == 'K':
        return 14
        
        
           
def prepareDeck(deck):
    for i in range(0,52):
        deck.append(0)
    
def insertToDeck(deck,pos,val):
    for p in pos:
        deck[p] = val   
        
def shuffleDeck(deck,posSet):
    cardPos = []
    for i in range(2,14):
        cardPos = random.sample(posSet,4)
        insertToDeck(deck,cardPos,cardValue(i))     
        posSetDel = set(cardPos)                   
        posSet = posSet - posSetDel
    insertToDeck(deck,posSet,cardValue(14))
    
####################################################################################
pos = range(0,52)
posSet = set(pos)
deck = []

prepareDeck(deck)
shuffleDeck(deck,posSet)
print (deck)


won = blackJack(deck,0)
print ("Player will be won ",won,"$")
