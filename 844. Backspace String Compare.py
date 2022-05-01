# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

s = "ab#c"
t = "ad#c"
l=[]
l1=[]
for i in range(0,len(s)):
    if(s[i]=="#"):
        if(l):
            l.pop()
    else:
        l.append(s[i])
print(l)
for i in range(0,len(t)):
    if(t[i]=='#'):
        if(l1):
            l1.pop()
    else:
        l1.append(t[i])
print(l1)
if(l1==l):
    print("YES")
else:
    print("NO")
