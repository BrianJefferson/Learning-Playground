# ACloudGuru Lab/Practice | "String Encoding and Functions"

string = 'DevOps'

print(ord('b'))

print(ord('B'))

print(chr(8482))

print("this".upper())

print("ThIs".lower())

print("thiS".capitalize())

print("This is a multiword String".title())

print(string.isascii())

print(string.islower())

print(string.isupper())

print(string.title().istitle())

print(" ".isspace())

print("f".isspace())

print("fbest".isidentifier())

print("3fbest".isidentifier())

phrase = "This is a simple phrase"

words = phrase.split()

print(words)

url = "https://www.linkedin.com/in/brianjeffersonbj/"
user = url.split('/')

print(user)

lines = ['First line', 'Second line', 'Third line']
output = '\n'.join(lines)

print(output)

# Below is format methods

template = print("Hello, my name is {}, and I really enjoy {}, Have a nice day!")

print(template.format('Brian', 'Python'))







