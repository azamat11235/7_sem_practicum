import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot()
ax.set_xscale('log')
ax.set_yscale('log')

diam = [0.152021, 0.0760106, 0.0380053, 0.0190027, 0.00950133]
errL2 = [0.00934286, 0.0023597, 0.000592076, 0.000148143, 0.000037019]
ord1 = diam
ord2 = [i ** 2 for i in diam]

ax.plot(diam, errL2, '-bo', label='$||u-u_N||_{L_2}$')
ax.plot(diam, ord1, '-r', label = '1-й порядок')
ax.plot(diam, ord2, '-g', label = '2-й порядок')
ax.legend()
plt.xlabel("Диаметр сетки")
plt.title("Для $u(x,y) = sin(\pi x)\cdot sin(\pi y)$")
plt.show()
plt.savefig('fig.pdf')
