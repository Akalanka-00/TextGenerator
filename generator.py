import time
#Chahractor list

items =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
        'x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','%','^','&','*',
        '(',')','-','=','_','+','{','}','[',']',';',':',"'",'"','\\','|',',','<','.','>','/','?','`',
        ' ','\t']

genorator = ''
count = 0

myText = input("Enter a text")
while True:
    reminder = count
    reCounter = count
    genorator = ''
    while reCounter > 0:
        reminder = reCounter % 94
        reCounter = reCounter // 94
        genorator = items[reminder] + genorator

    print(count, genorator)
    if myText==genorator:
        break
    count=count+1

time.sleep(1)
print("Your text is " +genorator)
