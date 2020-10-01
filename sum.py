count = 0

lst = []

print("Enter number to compute their sum: ")
while True:
    num = input()
    if num.lower() == "stop":
        break

    lst.append(int(num))

print('before:',count)
for i in lst:
    count = count + i

print('After:',count)
