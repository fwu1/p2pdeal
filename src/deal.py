'''
Created on Feb 6, 2014

@author: fwu
'''

import random

class Map(object):
    
    def __init__(self,size):
        self.size=size
        self.forward=[]
        self.backward=[]
        for i in range(size):
            self.backward.append(0);
        for i in range(size):
            while True:
                v=random.randint(0, size-1)
                found=False
                for v1 in self.forward:
                    if v1==v:
                        found=True
                        break;
                if not found:
                    self.forward.append(v)
                    self.backward[v]=i
                    break
                
    def __str__(self):
        str = ""
        for i in range(self.size):
            if i==0:
                delimiter=""
            else:
                delimiter=", "
            str+="%s%s"%(delimiter,self.forward[i])
        
        return str
    
    def __repr__(self):
        return self.__str__()


def getKey():
    return random.randint(0, 0xFFFFFFFF)

class Hand(object):
    
    def __init__(self):
        self.map1=Map(52)
        self.map2=Map(52)
        self.key=getKey()
        self.keys=[]
        for i in range(52):
            self.keys.append(getKey())
    
    def link(self,l,n):
        self.last=l
        self.next=n

def rotate():
    random.seed(100)
    h1=Hand()
    h2=Hand()
    h1.link(h2,h2)
    h2.link(h1,h1)
    print h1.map1
    print h1.map2
    
    cards=[]
    for i in range(52):
        cards.append(i)
        
    cards1=[]
    for i in range(52):
        mi=h1.map1.backward[i]
        cv=cards[mi]^h1.key
        cards1.append(cv)
    
    print "card1=",cards1
    
    cards2=[]
    for i in range(52):
        mi=h2.map1.backward[i]
        cv=cards1[mi]^h2.key
        cards2.append(cv)
    
    print "card2=",cards2
    

    cards3=[]
    for i in range(52):
        mi=h1.map2.backward[i]
        cv=cards2[mi]^h1.keys[i]
        cards3.append(cv)
    
    print "card3=",cards3


    cards4=[]
    for i in range(52):
        mi=h2.map2.backward[i]
        cv=cards3[mi]^h2.keys[i]
        cards4.append(cv)
    
    print "card4=",cards4
    
    # get the private card for p 1
    decards=[]
    for sel in range(52):
        cv4=cards4[sel]^h2.keys[sel]
        sel=h2.map2.backward[sel]
        
        # P1 keeps his key and pass the card value
        key3=h1.keys[sel]
        sel=h1.map2.backward[sel]
    
        cv2=cv4^h2.key
        sel=h2.map1.backward[sel]
        
        cv1=h1.key^cv2^key3
        
        decards.append(cv1)
    print "P1 cards:", decards
    
    # p1 anounce key1
    key1=h1.key

    # get the private card for p 2
    decards=[]
    for sel in range(52):
        # P2 keeps his key and pass the card value
        key4=h2.keys[sel]
        cv4=cards4[sel]
        sel=h2.map2.backward[sel]
        
        cv3=cv4^h1.keys[sel]
        sel=h1.map2.backward[sel]
    
        cv2=cv3^key4^h2.key^key1
        
        decards.append(cv2)
    print "P2 cards:", decards

    # p2 anounce key2
    key2=h2.key

    # get the public card
    decards=[]
    for sel in range(52):
        # P2 keeps his key and pass the card value
        cv4=cards4[sel]^h2.keys[sel]
        sel=h2.map2.backward[sel]
        
        cv3=cv4^h1.keys[sel]
        sel=h1.map2.backward[sel]
    
        cv2=cv3^key2^key1
        
        decards.append(cv2)
    print "public cards:", decards




def testXOR():
    a=0x3
    key=random.randint(0, 0xFFFFFFFF)
    c= a ^ key
    print "%X"%(c)
    
if __name__== "__main__":
    
    #testXOR()
    rotate()
    











