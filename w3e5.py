#w3e5.py

original = list(input())
cipher = []

for i in range(len(original)):
    if (original[i]>='a' and original[i]<='z'):
        if chr(ord(original[i])+3) > 'z':
            cipher.append(chr((ord(original[i]) + 3 - 26)))
        else:
            cipher.append(chr((ord(original[i]) + 3)))
    elif (original[i]>='A' and original[i]<='Z'):
        if chr(ord(original[i])+3) > 'Z':
            cipher.append(chr((ord(original[i]) + 3 - 26)))
        else:
            cipher.append(chr((ord(original[i]) + 3)))
    else:
        cipher.append(original[i])
            
cipher = ''.join(cipher)
#print(original[2])
print(cipher)
