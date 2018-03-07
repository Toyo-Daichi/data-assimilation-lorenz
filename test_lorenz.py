"""
Lorenzモデルのテスト用コードです。
"""
from pdb import set_trace
import numpy as np
from Lorenz96 import Lorenz96RungeKutta4
from Lorenz96_ctypes import Lorenz96RungeKutta4UsingCtypes

init_x = np.array([
    -0.679799334156,
    2.24549196973,
    6.50848241008,
    2.98786771677,
    3.7757894922,
    6.41612168904,
    -0.849883653656,
    0.490267418744,
    5.02796275658,
    9.02871869451,
    -1.99319219775,
    4.10875572742,
    1.89050878143,
    0.804617730459,
    2.44920045547,
    8.00829747282,
    -2.03755155898,
    2.77604491608,
    0.388885527726,
    10.7903106441,
    -0.637886680605,
    -3.25531886671,
    0.630896470624,
    6.49200853834,
    7.53147888734,
    0.441372256095,
    0.325108869831,
    4.70690665387,
    0.87113419718,
    -2.29239138825,
    0.952222699216,
    7.57957272967,
    1.95841646062,
    -2.73327771154,
    -1.33666413136,
    0.489786549422,
    5.597269164,
    3.65203522304,
    -5.99049279084,
    1.46340200753
])

if __name__ == '__main__':
    N = 40
    dt = 0.05
    F = 8.0

    model1 = Lorenz96RungeKutta4(F=F, dt=dt, N=N)
    model2 = Lorenz96RungeKutta4UsingCtypes(F=F, dt=dt, N=N)


    for days in [0.25, 0.5, 1, 2]:
        res1 = model1.run(init_x, days)
        res2 = model2.run(init_x, days)
        set_trace()
