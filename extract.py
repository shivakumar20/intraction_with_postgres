x = "E-BLUESTAR S/AC 1.5T FS318EBTU 3S"
y = len(x)

print(y)

y = y * -1

print(y)

for i in range(y,0):
    if x[i] == 'S':
        j = i-1
        check_num = x[j]
        print(x[j])
        try:
            int(check_num)
        except:
            print('Can not convert', check_num ,"to int")
        print(type(check_num))