def firstNotRepeatingCharacter(s):
    alphabet = [-2]*26
    firsts = list()
    for i in s:
        index = ord(i)-97
        if alphabet[index] == -2 :
            alphabet[index] = 1
            firsts.append(i)
        elif alphabet[index] == 1:
            alphabet[index]+=1
            firsts.remove(i)
        else:
            alphabet[index]+=1
            continue
    if len(firsts) == 0:
        return '_'
    else:
        return firsts[0]

print (firstNotRepeatingCharacter("abacabaabacaba"))