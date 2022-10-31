left = "/"
right = "\\"
base = "__"

h = int(input("Hauteur:"))
for i in range(h):
    print((h-i)* " " + left +((i*2)* " ") + right)
    if i == h -1:
        print (left + base*h +right)
