word="RAja SekhaR"
lo = 0
up = 0

for i in range(len(word)):

    if word[i].islower():
        lo=lo+1
    else:
        up=up+1
print(f'lower {lo} \n upper {up}')
