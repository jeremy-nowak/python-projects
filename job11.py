#get file object reference to the file
file = open("/home/vitaly/Projet python/domains.xml", "r")

#read content of file to string
data = file.read()

#get number of occurrences of the substring in the string
occurrences = data.count("domain")
print('Line Number:')

print('Number of occurrences of the word :', occurrences)