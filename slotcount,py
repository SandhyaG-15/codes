string=input().strip()
strval=int(input())
strnames=[]
for i in range(strval):
    strnames.append(input().strip())
underscore,cnt=[],0
for i in range(0,len(string)):
    if(string[i]=="_"):
        cnt+=1
    elif(string[i-1]=="_" and string[i]!="_"):
        underscore.append(cnt)
        cnt=0
if(cnt>0):
    underscore.append(cnt)
slotcnt=0
for i in strnames:
    if len(i) in underscore:
        underscore.remove(len(i))
        slotcnt+=1
print(slotcnt)
