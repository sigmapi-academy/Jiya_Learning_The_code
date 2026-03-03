print("Enter 16 values to make a 4*4 magic square: ")
user_values=[]
for l in range(0,16,1):
    Value=int(input())
    user_values.append(Value)
n=0
Values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
values=user_values
for Value in user_values:
    if Value in Values:
        Values.remove(Value)
        n+=1
        continue
    else:
        print("Numbers from 1,2,...,16 do not occur in user input")
        exit()
y=0
for value in values:
    print(value,end=" ")
    if y%4==3:
        print('\n')
    y+=1
inx=0
sum_0=values[inx]+values[inx+1]+values[inx+2]+values[inx+3]
sum2=0
magic_sqr=True
while inx<8:
    inx+=4
    sum=values[inx]+values[inx+1]+values[inx+2]+values[inx+3]
    if sum==sum_0:
        magic_sqr=True
        continue
    else:
        magic_sqr=False
        print("Not a magic square")
        exit()
ind=0
inl=1
colsum=0
colsum2=0
t=0
while ind<16:
    while t<4:
        colsum+=values[ind]
        ind+=4
        colsum2+=values[inl]
        inl+=4
        t+=1
if colsum==colsum2:
    magic_sqr=True
elif colsum!=colsum2:
    magic_sqr=False
    print("Not a magic square")
    exit()
f=0
k=3
diagnol1=0
diagnol2=0
while f<16 and k<13:
    diagnol1+=values[f]
    diagnol2+=values[k]
    f+=5
    k+=3
if diagnol1==diagnol2:
    magic_sqr=True
elif diagnol1!=diagnol2:
    magic_sqr=False
    print("Not a magic square")
    exit()

print("Magic square")
