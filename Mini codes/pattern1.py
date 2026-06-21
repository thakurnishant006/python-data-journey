number = [5,2,5,2,2]
for i in number:
    if i == 5:
        print('x'*5)
    else:
        print('x'*2)

# Using range
num = [5,2,5,2,2]
for i in num:
    out = ''
    for x in range(i):
        out += 'x'
    print(out)