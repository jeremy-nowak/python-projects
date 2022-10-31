nombre = int(input ("Entrez un nomnbre de lettres : "))

with open("/home/vitaly/Projet python/data.txt", "r") as f:
    text = f.read()
    text = text.replace(",", "").replace(";", "").replace(".", "").replace("?", "").replace("!", "").replace(":", "")
    words = text.split()
    count = 0

    for i in words:
        if len(i) == nombre:
            count = count +1

print(count)