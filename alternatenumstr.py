string=input().strip();i=0
while(i<len(string)):
    num=0
    if(string[i].isalpha()==1):
        j=i+1
        while(string[j].isalpha()==0):
            num=(num*10)+int(string[j])
            j+=1
            if(j>=len(string)):
                break
    if(num%2==0):
        for cnt in range(1,num+1):
            print(string[i],end="")
    else:
        print(string[i],end="")
        print(num,end="")
    i=j
