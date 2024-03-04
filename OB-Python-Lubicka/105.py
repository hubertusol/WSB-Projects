file = open('d:/WSB-Projects/OB-Python-Lubicka/Numbers.txt', 'w')
for i in range(0,5):
    if i!=4:
        file.write(f"{str(i)},")
    if i==4: file.write(str(i))
file.close()