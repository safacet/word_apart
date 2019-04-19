a= input("Type a text:")
print("Text:", a)
b=a[::2]
c=a[1::2]
print("First part:", b)
print("Second part:", c)
print("Text is being to re-combining")
d=0
e=0
word = str()
for i in range(len(a)):
    if i%2==0:
        word += b[d]
        d+=1
    else:
        word += c[e]
        e+=1
print(word)