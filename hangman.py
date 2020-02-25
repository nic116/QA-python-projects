#!/usr/bin/env python3.8
import random

def split(word):
    return [char for char in word]

word =str(input("Enter your word: "))

count= len(word)

Alphabet= ["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s",
            "t","u","v","w","x","y","z"]

usedletters=[]

while count>0 :
    phi= random.choice(Alphabet) 
    Alphabet.remove(phi)

    if (phi in word):
        
       print("correct letter ["+ phi +"]")
       usedletters= [usedletters.append(phi)]
       
          
    elif (phi not in word or phi in usedletters ):
        
        print("wrong letter [" + phi +"]")
        usedletters= [usedletters.append(phi)] 
        count -=1
        
    if count ==0 or split(word) in usedletters:
        print("The answer was " +word)
        

