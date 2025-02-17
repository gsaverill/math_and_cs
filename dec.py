import decimal
from mpmath import mp
from matplotlib.ticker import EngFormatter

D = decimal.Decimal

a = D(1)
b = D(3)
c = D(10)
d = D(81)


with decimal.localcontext() as ctx:
    # print(ctx)
    ctx.prec = 64   # Perform a high precision calculation
    # print(ctx)
    s = a/b
    w = c/d
    w = decimal.Decimal.sqrt(D(2))

s = s * 1000000000000000000
print(s.normalize().to_eng_string())
print(w)

mp.dps = 10000
mp.pretty = True
print(mp.pi)

engFormat = EngFormatter(unit='Hz', places=2, sep=' ')
print(engFormat(1000))
engFormat = EngFormatter(places=2, sep=' ')
print(type(engFormat(1/3)))
print(engFormat(1/3))
# 1.00kHz

print(' ')
print(' ')
print(' ')
print(' ')
myfloat = 0.00000001
print(f'{myfloat:.3E}')
print('time = {:.3E}'.format(myfloat))
print('time = {:.3e}'.format(myfloat))
print('time = {:.3F}'.format(myfloat))
print('time = {:.3f}'.format(myfloat))
print('time = {:.3G}'.format(myfloat))
print('time = {:.3g}'.format(myfloat))
print('time = {:.3f}'.format(myfloat))
print('time = {:.3f}'.format(myfloat))

print('time = {:.3E}'.format(myfloat))
print('time = {:.3E}'.format(myfloat))
print('time = {:.3E}'.format(myfloat))
print('time = {:.3E}'.format(myfloat))
print('time = {:.3E}'.format(myfloat))

# quantiphy

# x = EngFormatter.format_eng(2)
# print(x)

catch = f'{myfloat:.3E}'
print(type(catch))
print(catch)

