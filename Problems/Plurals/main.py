number = int(input())
word = input()

# write a condition for plurals

if number != 1:
    print(number, word + 's')
else:
    print(number, word)


number = 0
while number < 5:
    print(number)
    number += 1
print('Now, the number is equal to 5')
