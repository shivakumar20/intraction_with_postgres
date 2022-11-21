s ="S 1 2 3 4 5S 5 6 20 hello Super Song 7S 8 9 0 19S"
x = ''
for i in range(0,len(s)):
    if s[i] == "S":
        if s[i-1]>="1" and s[i-1]<="9" and s[i-1] != " ":
            try:
                x = int(print(s[i-1]))
            except TypeError:
                print(f"Not a Nonetype : {s[i-1]}")
            print(f"{x}")
            
