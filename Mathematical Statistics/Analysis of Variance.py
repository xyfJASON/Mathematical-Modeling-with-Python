from scipy.stats import f_oneway


def Ex1():
    x = [[256, 242, 280, 298],
         [254, 330, 290, 295],
         [250, 277, 230, 302],
         [248, 280, 305, 289],
         [236, 252, 220, 252]]
    res = f_oneway(*x)
    print(res)


def Ex2():
    x = [[1620, 1670, 1700, 1750, 1800],
         [1580, 1600, 1640, 1720],
         [1460, 1540, 1620],
         [1500, 1550, 1610, 1680]]
    res = f_oneway(*x)
    print(res)


Ex1()