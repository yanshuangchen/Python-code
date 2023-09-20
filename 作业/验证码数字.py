import random
# 用randint()
code = ''
for i in range(4):
    n = random.randint(0, 9)
    b = chr(random.randint(65, 90))
    s = chr(random.randint(97, 122))
    code += str(random.choice([n, b, s]))
print(code)

