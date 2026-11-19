'''string=(input("enter the string: "))
i=0
while i<len(string):
    ch=string[i]
    if ch.isupper():
        print(f"{ch} is uppercase")
    elif ch.islower():
        print(f"{ch} is lowercase")
    elif ch.isdigit():
        print(f"{ch} is digit")
    else:
        print(f"{ch} is special character")
    i=i+1   '''

'''l=eval(input("enter the list: "))
integer=''
i=0
while i<len(l):
    if type(l[i])==int:
        integer=integer+str(l[i])+' '
    i=i+1
print("the integers in the list are:",integer)'''

'''l=eval(input("enter the list: "))
integer=[]
i=0
while i<len(l):
    if type(l[i])==int:
        integer.append(l[i])
    i=i+1
print("the integers in the list are:",integer)'''


'''l=eval(input("enter the list: "))
out=[]
i=0
while i<len(l):
    if type(l[i])==int and 100<=l[i]<=999 and l[i]%5==0:
        out.append(l[i])
    i=i+1
print("the three digit numbers in the list are:",out)'''

'''n= input("enter the num: ")
result=""
for i in n:
    if i==" ":
        result=result+"_"
    else:
        result=result+i
print(result)'''

'''s= input("enter the string: ")
vow=""
for i in s:
    if i in "aeiouAEIOU":
        vow+=i
print(vow)'''


'''lis= eval(input("enter the list: "))
out={}
for i in lis:
    x= i.split('.')
    key=x[-1]
    value=x[0]
    out[key]=value
print(out)'''

'''s= input("enter the string: ").split()
out=""
for i in s:
    a= i[::-1]
    out+=a+" "
print(out)
s = 'hai hello bye'
print(len(s))
print(len(out))'''

'''a= input("enter the string: ")
out=""
for i in range('a', 'z'):
    if i in a:
        out+=i
print(out) '''

'''s= input("enter the string: ")
out={}
for i in s:
    if  i not in out:
        count=s.count(i)
        out[i]=count
print(out)'''


'''s= int(input("enter the integer: "))
for i in str(s):
    last= int(i)
if last % 2==0:
    print( "the last digit is even" )
else:
    print("it is odd")'''

'''d=eval(input("enter the dictionary : "))
out={}
for i in d:
    if i==d[i]:
            out[i]=d[i]
print (out)'''

'''a=input("enter the string: ")
out=0
for i in a:
    if i in ("aeiouAEIOU"):

        out=out+1
print(out)'''

'''for i in range (1,51,1):
    if i%3==0 and i%5==0:
        print (i)'''

'''fruits=["apple","banana","cheery"]
for i in fruits:
    b=i.upper()
    print(b,end=" ")'''
"largest number in the list"
'''ln =[12,45,7,89,23]
for i in ln:
    if i==max(ln):
        print(i)'''

'''ln =[12,45,7,89,23]
for i in ln:
    if i==min(ln):
        print(i)
'''




'''lv=[10,55,30,72,49,90]

for i in lv:
    if i>50:
        print(i,end=" ")'''


'''n=[5,-2,8,-7,0,3]
s=[]
for i in n:
    if i>0:
        s.append(i)
print(len(s))'''


'''marks=[80,90,70,60,100]
out=0
for i in marks:
    out+=i
print(out/len(marks))'''

'''e="banana"
b=""
for i in e:
    if i=="a":
        b=b+i
print(len(b))'''

'''a="python"
c=""
for i in a:
    c=i+c
print(c)'''

'''for i in range (1,6,1):
    if i%2==0:
        print(f"{i} even")
    else:
        print(f"{i}odd")
'''
'''a=0
for i in range(1,7,1):
    b=i**2
    a=a+b
print(a)'''

"""first 8 powers of 2, starting from 2 to the power of 1"""
'''for i in range(1,9,1):
    print(f"{2**i}")'''
'''
for i in range (1,21):
    if i%5==0:
        continue
    else:

        print(i)'''
'''c=0
for i in range (1,6,1):
    a=int(input("enther the value"))
    c=c+a

print(a)'''

'''s="chromepet"
out={}
for i,j in enumerate(s):
    out[i]=j
print(out)'''

'''from itertools import zip_longest
names=["adithiya","bavani","chandramugi","dinesh","elanmusk"]
marks=[75,56,36]
out={}
for i,j in zip_longest(names,marks,fillvalue="ap"):
    out[i]=j

print (out)'''


'''s="power star".split()
out={}
for i in s:
    out[i]=i[::-1]
print(out)'''

'''l=[0,23,3,4,5,'',False,None,[1],0,0.0]
out=[]
for i in l:
    if bool(i)!=False:
        out.append(i)
print(out)'''

'''a="hai every one i am varma"
result=''
for i in a:
    if i==" ":
        result=result+'*'
    else:
        result=result+i
print(result)'''

'''s='always keep smiling'.split()
out=[]
for i in s:
    r=i[::-1]
    out.append(r)
print(" ".join(out))'''

'''s='always keep smiling'.split()
out=" ". join(i[::-1] for i in s)
print(out)
b=len('always keep smiling')
c=len(out)
print(b,c)'''


'''s=['spark','power','thunder','magic','monster']
out={}
for i in s:
    rev=""
    for j in i:
        if j in "aeiouAEIOU":
             rev=rev+j    
    out[i]=rev

print(out)'''

'''s='super star rajini'.split()
out={}
for i in s:
    
    c=""
    v=""
    
    for j in i:
        if j in "aeiouAEIOU":
             v=v+j
             
        else:
            c=c+j 
   
    
    out[i]= [c,v]
print(out)'''

'''s='super star rajini'.split()
d={}
for a,i in enumerate(s):
        v=''
        c=''
        for j in i:
            if j in "aeiouAEIOU":
                v=v+j
            else:
                c=c+j
        k=(len(i),len(v),len(c))
        d[a]=k
print(d)'''



'''s='super star rajini'.split()
d={}
for a,i in enumerate(s):
        v=''
        c=''
        count=0
        for j in i:
            count=count+1
            if j in "aeiouAEIOU":
                v=v+j
            else:
                c=c+j
        vc=0
        cc=0
        for j in v:
            vc=vc+1
        for j in c:
            cc=cc+1
        k=(count,vc,cc)
        d[a]=k
print(d)'''

'''s='super star rajini'.split()
d={}
def rec (s,i=0):
    if s=='':
        return 0
    return 1 + rec (s[1:])
for a,i in enumerate(s):
        v=''
        c=''
        for j in i:
            if j in "aeiouAEIOU":
                v=v+j
            else:
                c=c+j
        d[a] = (rec(i), rec(v), rec(c))
print(d)'''


'''s='super star rajini'.split()
d={}
for a,i in enumerate(s):
        v=''
        c=''
        for j in i:
            if j in "aeiouAEIOU":
                v=v+j
            else:
                c=c+j
        k=(len(i),len(v),len(c))
        d[a]=k
print(d)'''

'''s = 'super star rajini'
out = []
w = ''

for i in s:
    if i != ' ':
        w = w + i
    else:
        out.append(w)
        w = ''

out.append(w)
d={}
for i in out:
    for a,i in enumerate(out):
        v=''
        c=''
        for j in i:
            if j in "aeiouAEIOU":
                v=v+j
            else:
                c=c+j
        k=(len(i),len(v),len(c))
        d[a]=k

print(d)'''



'''a = [2, 3, 5, 1, 9, 4]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)'''


'''In="push maadi kushi padi".split()
out={}
for i in In:
    if len(i)%2==0:
        out[i]=i[0]+i[-1]
    else:
        if len(i)%2!=0:
            a=len(i)//2
            out[i]=i[a]
print (out)'''

'''n=5
for i in range (1,n+1):
    for j in range (1,n+1):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=5
for i in range (1,n+1):
    for j in range (1,n+1):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=5
for i in range (1,n+1):
    for j in range (1,n+1):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n = 10

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == (n//2)+1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("* * * * * * * * * *")'''


'''n = 11

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i+j>=n+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("1 2 3 4 5 6 7 8 9 10 11")'''


'''n=11
for i in range (1,n+1):
    for j in range (1,n+1):
        if j%2!=0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("1 2 3 4 5 6 7 8 9 10 11")'''

'''n=5
for i in range (1,n+1):
    for j in range (1,n+1):
        if i==j:
            print("*",end=" ")
        elif i>=j:
            print("@",end=" ")
        else:
            print(" ",end=" ")
        
    print()'''

'''n=5
for i in range (1,n+1):
    for j in range (1,n+1):
        if j==1:
            print("*",end=" ")
        elif i==1:
            print("*",end=" ")
        elif j==n:
            print("*",end=" ")
        elif i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''n =int(input("enther the value"))

for i in range(1, n ):
    for j in range(1, n ):
        if j == (n//2) :
            print("*", end=" ")
        elif i == (n//2) :
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=5
for i in range (1,n+1):
    for j in range (1,n+1):
        if i==j or i+j==n+1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''
n=5
#
for i in range (1,n+1):
    for j in range (1,n+1):
            print(j,end=" ")
    print()'''


'''n=5
#
for i in range (1,n+1):
    for j in range (1,n+1):
            if i>=j:
                print(j,end=" ")
    print()'''

'''#----------13--------
 n=5

 for i in range (1,n+1):
    for j in range (1,n+1):
             if i>=j:
                print(i,end=" ")
    print()'''

'''n=5

for i in range (1,n+1):
    k=i
    for j in range (1,n+1):
            if i>=j:
                print(k,end=" ")
                
                k=k+1
    print()'''

'''n=5
k=1
for i in range (1,n+1):
    
    
    for j in range (1,n+1):
            if i>=j:
                print(k,end=" ")
                
                k=k+1
    print()'''

#16
'''n=5

for i in range (1,n+1):
    k=ord("A")
    
    for j in range (1,n+1):
            if i<=j:
                print(chr(k),end=" ")
                k=k+1
            else:
                 print(" ",end=" ")
    print()
'''


'''n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("X", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("X", end=" ")
    print()'''

'''n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()'''



'''n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print("_", end="")
    for k in range(1, i + 1):
        print("*", end="_")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print("_", end="")
    for k in range(i):
        print("*", end="_")
    print()'''

'''n = 7
i = 3

for j in range(n - i):
    print("@", end=" ")

for k in range(1, i + 1):
    print("*", end=" ")'''

'''n = 4

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
'''
'''n = 6
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()'''



'''n = 6

for i in range(1, n + 1):
    for j in range(n - i):
        print("_", end="")

    if i == 1:
        print("*")
    else:
        print("*", end="")
        for k in range(2 * i - 3):
            print("_", end="")
        print("*")


for i in range(n-1, 0, -1):
    for j in range(n - i):
        print("_", end="")

    if i == 1:
        print("*")
    else:
        print("*", end="")
        for k in range(2 * i - 3):
            print("_", end="")
        print("*")'''


# n= eval(input("enter the number: "))
# if type(n)==float:
#     print ("float")
# else:
#     print ("not")


'''print ("hello varma")
print("how are you")'''

'''n="united states of america".split()
k=""
j=""
for i in n:
    if i== 'a':
        k=k+i.join()
    else :
        j=j+i

print (k)
print (" ".join(j))'''


'''age =int (input("enter the age : "))
if age >= 18:
    id=input(" enter the id : ")
    if id == "1234":
        print ("you are eligible to vote")
    else:
        print("you dont have voter id")
else:
    print("you are not eligible to vote")'''
'''
n=int(input("enter the number: "))
if n>=0
    if n>0 :

        if n%2==0:
            print("positive even")
        else:
            print ("positive odd")
    else:
        print ("zero")
else:
    print("it is negative")   
    '''


'''a= int(input("entre the A value"))
b=int(input("enter the B value"))
c=int(input("enter the C value"))
if a>b :
    if a>c:
        print("a is greater")
    else:
        print ("c is greater")
else:

    if b>c:
        print("b is greater" )
    else:
        print("c is greater")'''


'''mark = int(input("enter the mark : "))
if mark > 35 and mark <=100:
    
    if mark >=75:
        print("pass with the student secured distiction")
    else:
        print("pass")

else :
    print("the student is failed")'''


'''
a = int(input("Enter the A value: "))
b = int(input("Enter the B value: "))
c = int(input("Enter the C value: "))'''

'''if a > b:
    if a > c:
        if b > c:
            print("b is second greatest")
        else:
            print("c is second greatest")
    else:
        print("a is second greatest")

else:
    if b > c:
        if a > c:
            print("a is second greatest")
        else:
            print("c is second greatest")
    else:
        print("b is second greatest")
'''

# wap to print the even number
'''i=2
while i<=20:
    print(i)
    i=i+2'''

# wap to print the numbers from n to 1
'''n= int(input( "enter the  number : "))

while n>=1:
    print (n)
    n=n-1'''

# wap to print the n table
'''n=int(input(" enter the number: "))
i=1
while i<=10:
    k=i*n
    print(f"{n} X {i} = {k}")
    i=i+1    ''' 

#find the factorial of the given number
'''n= int(input(" enter the number: "))
fact=1
i=1
while i<=n:
    fact=fact*i
    
    i=i+1
print(fact)'''


# wap to find the sum of n natural numbers 
'''n=int(input(" enter the number : "))
i=1
k=0
while i <=n:
    k=k+i
    i=i+1
print(k)'''

# wap to print the divisors of the given number
'''n = int(input("Enter the number: "))

i = 1

while i <= n:
    if n % i == 0:
        print(i)

    i = i + 1'''


#wap to reverse the given number without using slicing
'''
n= int(input("enter the number: "))
r=0
while n!=0:
    ld=n%10
    r=r*10+ld
    n=n//10
print(r)'''


#wap to find the sum of individual numbers from the given number
'''
n= int(input("enter the number: "))
r=0
while n!=0:
    ld=n%10
    r=r+ld
    n=n//10
print(r)
 '''

'''n= int(input("enter the number: "))
r=0
while n!=0:
    ld=n%10
    r=r+ld**2
    n=n//10
print(r)'''



#password retry counter

p='XXX'
i=1
while i<4 :
    
    p_w=input("enter the password: ")
    if p_w == p:
        print("Access Granted") 
        break          
    else:
        if i==3:
            print("access locked too many incorrect attempts")
    i=i+1


#sum untill the user input is zero
'''total=0
i=1
while True:
    n=int(input("enter the number: "))
    if n==0:
        break
    total=total+n
    i=i+1
print(total)'''


# above or below are correct
'''
total=0
i=1
run=True
while run:
    n=int(input("enter the number: "))
    if n==0:
        run=False
    total=total+n
    i=i+1
print(total)'''

