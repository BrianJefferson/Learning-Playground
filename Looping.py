# ACloudGuru Lab/Practice | "Looping"

count = 0

while count <= 4:
    print("looping")
    count += 1 

while count <= 25:
        if count % 4 == 0:
            print(count)
        count += 1

while count < 10:
     if count % 2 == 0:
          count += 1
          continue
     print (f"We're counting odd numbers: {count}")
     count += 1

colors = ['blue', 'green', 'red', 'purple']

for color in colors:
    print(color)

ages = {'kevin': 59, 'bob': 40, 'brian': 29}

for key in ages:
    print(key)

for key, value, in ages.items():
    print(key, value)

# Below is examples using 'else' with 'loops'

counter = 1

while counter <= 4:
     print(counter)
     counter += 1
else:
     print("While loop completed")

for i in [1, 2, 3, 4, 5]:
     print(i)
else:
     print('For loop completed')


for color in colors:
     if color == 'red':
          print('Red is in the list')
          break
else:
     print('Red is not in the list')


# Below is examples of using "range"

my_range = range(10)

print(my_range)

print(list(my_range))

print(list(range(1, 14, 2)))

for _ in range(4):
     print("looping")

