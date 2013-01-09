#import external booklist

file = open('booklist.txt','r')

#create new lists

basicdata=[]
booklist=[]

#organise data

for row in file:
    
    basicdata.append(row)

    cleanrow=row.rstrip('\n')

    booklist.append(cleanrow)

file.close

#sort booklist

booklist.sort()

#set new variable for amount of booktitles inside booklist

amount=len(booklist)

#set length according first booktitle

lengthtitle1=len(booklist[0])

#run loop 

#loop to see booktitles sortet horizontal

for i in range(0,amount):
    print(booklist[i])
    print()

#loop to get all the first letters, all the second...of all booktitles

for x in range(0,lengthtitle1):

        
    for i in range(0,amount):
        booktitle=booklist[i]

#print all the first letters, the second, the third... of all the booktitles

        print(booktitle[x],' ',end='')
    print()

         
