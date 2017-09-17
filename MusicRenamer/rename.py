import os
path=os.getcwd()
p=os.listdir(path)

ty='.'+input('Enter the type of file you want to rename : ')
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
    if (z!='rename.py'):
        print(z,'\n')
        n=input('If you want to skip the song just press enter or else type the new name ').rstrip()
        print()
        if (len(n)==0):
            pass
        else:
            os.rename(z,n+ty)
            
