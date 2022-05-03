import random
import string

print("It might take a few seconds to produce a key")
chars = string.ascii_letters.lower() # lower case values gave a quick result


while (1):
    key1=''.join(random.choice(chars) for x in range(12))
    #lets find a key that will pass the first phase of the key checking algorithm
    #we will test only the characters used in the first phase namely characters at index :6,7,9,10,11
    val = (ord(key1[11])+ord(key1[6]))*ord(key1[9])+ord(key1[10])*ord(key1[7])
    if val == 0x9af2:
        while(1):
            key=''.join(random.choice(chars) for x in range(12))
           
            #here we passed the first phase and we will need to find the combination of
            #characters that will pass the second phase we will process only characters 
            #used in second phase namely characters at index : 0,1,2,3,4,5
            if  (( (((ord(key[5]) * ord(key[1])) - ((ord(key[4]) >> 1) * (ord(key[4]) >> 1))) * ord(key[0]) ) - ((( ord(key[5]) * (ord(key[2]) * 0.5 ) ) - ( (ord(key[4]) >> 1) * (ord(key[3]) >> 1) )) * (ord(key[2]) * 0.5 )) ) + (( ( (ord(key[4]) >> 1) * (ord(key[2]) * 0.5 ) ) - ( ord(key[1]) * (ord(key[3]) >> 1) ) ) * (ord(key[3]) >> 1) )) == 733898.75 :
                
                #after the second condition is met we combine both characters of first and second phase 
                print(key[0:6]+key1[6:12])
                
                quit()
            
