
num1 = list(map(int, input('Enter list 1').split()))
num2 = list(map(int, input('Enter list 2').split()))

# ******************************
# Make your Code
# ******************************

# print ('True') or print ('False')
sums = 0
for i in range(len(num2)):
    count = num1.count(num2[i])

    if count > 0:
        sums = sums + 1
        continue
    else:
        print('False')   
        break
if sums >= len(num2):
    print('True') 