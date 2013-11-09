a={1:1,2:2,3:3}
b=''
for i in a.keys():
    b+=str(i)+','
print b[0:-1]
