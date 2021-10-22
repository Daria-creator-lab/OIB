import math
import re
import mpmath
import random

chain = str(''.join(random.choice('0' + '1') for i in range(128)))
print(chain)
print(len(chain))

#частотный побитовый тест
sum = 0
for i in chain:
    if i == '0':
        sum = sum - 1
    else:
        sum = sum + 1
Sn = 1/math.sqrt(len(chain))*sum
Pvalue = math.erfc(Sn/math.sqrt(2))
print(Pvalue)

#тест на одинаковые подряд идущие биты
sum_ei = 0
Vn = 0
Pvalue = -1
for i in chain:
    sum_ei += int(i)
e = sum_ei/len(chain)
print(e)
if abs(e - 0.5) >= 2/((len(chain))**0.5):
    Pvalue = 0
else:
    for i in range(len(chain) - 1):
        if chain[i] != chain[i+1]:
            Vn += 1
print(Vn)
Pvalue = math.erfc(abs(Vn - 2*len(chain)*e*(1-e))/(2*e*(1-e)*(2*len(chain))**0.5))
print(Pvalue)

# тест на самую длинную последовательность единиц в блоке
string_of_chain = ''.join(str(chain))
v1 = 0
v2 = 0
v3 = 0
v4 = 0

a = 0
b = 7
while b < len(chain):
    if re.findall(r'[1]{4,}', chain[a:b]):
       v4 += 1
    elif re.findall(r'[1]{3}', chain[a:b]):
       v3 += 1
    elif re.findall(r'[1]{2}', chain[a:b]):
       v2 += 1
    elif re.findall(r'[1]?', chain[a:b]):
       v1 += 1
    a = b + 1
    b = b + 8
print(v1,v2,v3,v4)

hi2 = ((v1 - 16*0.2148)**2)/(16*0.2148)+((v2 - 16*0.3672)**2)/(16*0.3672)+((v3 - 16*0.2305)**2)/(16*0.2305)+((v4 - 16*0.1875)**2)/(16*0.1875)
print(hi2)
Pvalue = mpmath.gammainc(3/2, hi2/2)
print(Pvalue)

