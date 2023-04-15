import matplotlib.pyplot as plt
import numpy as np
a =float( input("a="))
b = float(input("b="))
n = int(input("n="))
dx = ((b - a) / n)
integral = 0
i = 0
x = a
while i < n:
    function= x**3 * dx
    x = x + dx
    integral = integral + function
    i = i + 1
integral=round(integral,2)
def F(x):
  return x**4/4
intb=F(b)
inta=F(a)
def f(x):
    return x**3
nl=intb-inta
print("Интеграл равен " + str(integral))
def intgr(integral):
    return integral
if nl==integral:
    print("Интегральная сумма высчитана правильно")
else:
    print("Ошибка!Интергральная сумма не совпадает с интегралом по формуле Ньютона-Лебница")
plt.xlabel("Ось х")
plt.ylabel("Ось у")
plt.title("График интеграла")
x = np.linspace(a, b, n)
plt.plot(x, f(x))
plt.fill_between(x, f(x), where=[(x > a) and (x < b) for x in x])
plt.show()


