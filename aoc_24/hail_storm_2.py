# Answer: 999782576459892
from sympy import Symbol, solve_poly_system

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        inp = f.read().splitlines()

    data = []
    for line in inp:
        d = line.replace(' @', ',')
        d = tuple(int(p) for p in d.split(','))
        data.append(d)

    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    vx = Symbol('vx')
    vy = Symbol('vy')
    vz = Symbol('vz')

    equ = []
    t_c = []

    for i, hail in enumerate(data[:3]):
        x0, y0, z0, vx_h, vy_h, vz_h = hail
        t = Symbol('t'+str(i))

        equ += [
            x - x0 + (vx - vx_h) * t,
            y - y0 + (vy - vy_h) * t,
            z - z0 + (vz - vz_h) * t
        ]

        t_c.append(t)
    print(equ)

    result = solve_poly_system(equ, *([x, y, z, vx, vy, vz]+t_c))
    print([f"{n} = {r}" for r, n in zip(result[0], ['x0', 'y0', 'z0', 'vx', 'vy', 'vz', 't0', 't1', 't2'])])
    print(result[0][0]+result[0][1]+result[0][2])  # part 2 answer
