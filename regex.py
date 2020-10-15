import re

pattern = re.compile('text')  # search text to be compared

string = 'Search text in this text string'

a = pattern.search(string)
print(a.start())  # if match found, it returns the start position 
print(a.end())

b = pattern.findall(string)
print(b)

c = pattern.match(string)

pattern1 = re.compile(r"([a-zA-Z]).([a])")  
# any alphabet followed by any char and followed by lett a
d = pattern1.search(string)
print(d.group())  # returns sea

password = input ('Enter the password : ')
pattern2 = re.compile(r"([a-zA-Z0-9@#$%]{8,})")

e = pattern2.search(password)
print(e.group())