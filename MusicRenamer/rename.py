import os
path=os.getcwd()
p=os.listdir(path)

for c in p:
    print(c)
    z = ''
    ind = 0
    for b in range(len(c)):
        if c[b].isalpha():
            ind = b
            break
    z = c[ind::]
    os.rename(c,z)
