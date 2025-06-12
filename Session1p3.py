def tiggerfy(word):
    word2 = list(word)
    i = 0
    while i < len(word2):
        if(word2[i] == "t" or word2[i] == "T"):
            word2.pop(i)
        elif(word2[i] == "i"):
            word2.pop(i)
        elif(word2[i] == "g"  and word2[i+1] == "g"):
            word2.pop(i)
            word2.pop(i)
        elif(word2[i] == "e" and word2[i+1] == "r"):
            word2.pop(i)
            word2.pop(i)
        else:
            i+=1
    return word2

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))