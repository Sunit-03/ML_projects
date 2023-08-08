ctr=65
while ctr<91:
    if ctr in range(65,67) or ctr == 68 or ctr == 69 or ctr in range(71,75) or ctr in range(76,85) or ctr in range(86,91):
        continue
    print(chr(ctr))
    ctr+=1
