def file_fixing(filename):
    lis=[]
    with open('HW2.txt','r') as file:
        li=file.read().split("\n")
    for line in li:
        word=line.split()
        lis.append(word)
        lis[0].reverse()

    print(lis)

file_fixing('HW2.txt')
