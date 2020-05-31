import math

import numpy as np


def cal_entropy_per_window(data_lst):
    entropy_list = []
    N = len(data_lst)
    for i in range(1, N):
        m = len(data_lst[i].keys())
        n = 0
        for k in data_lst[i]:
            n += data_lst[i][k]

        ent = 0
        if n == 0:
            ent = math.inf
        else:
            ent = - np.log(m / n)
        n_minus_1 = 0
        for k in data_lst[i - 1]:
            n_minus_1 += data_lst[i - 1][k]

        if n == 0 or n_minus_1 == 0:
            ent = math.inf
        elif n >= n_minus_1:
            ent += abs(np.log(n_minus_1 / n))
        else:
            ent += abs(np.log(n / n_minus_1))
        entropy_list.append(ent)
    return entropy_list


def average(data_list):
    avg = 0
    if len(data_list) == 0:
        return 0
    for i in data_list:
        avg += i
    avg = avg / len(data_list)
    return avg


def cal_std_deviation(data_list, avg):
    result = 0
    for i in data_list:
        result += (i - avg) ** 2
    result = math.sqrt(result / len(data_list))
    return result


beta = 3
omega = 0


def algorithm(data_list, avg_val):
    global beta
    global omega
    std_dev = cal_std_deviation(data_list, avg_val)
    omega = beta * std_dev
    for H in data_list:
        D_i = abs(H - avg_val)
        if H > 1.5 * avg_val:
            beta += 1
        elif 0.5 * avg_val <= H <= 1.5 * avg_val:
            pass
        else:
            beta -= 1

        if D_i >= omega:
            print("Detected")
        omega = beta * std_dev
    print("Beta:", beta)
    print("Omega:", omega)


def sliding_window(data):
    entropy = cal_entropy_per_window(data)
    print("Entropy: ", entropy)
    avr = average(entropy)
    print("Avg:", avr)
    st_dev = cal_std_deviation(entropy, avr)
    print("Std dev", st_dev)
    algorithm(entropy, avr)


if __name__ == "__main__":
    data = [
        {
            "abc.com": 1,
            "204.249.225.59": 35,
            "access9.accsyst.com": 31,
            "cssu24.cs.ust.hk": 35,
            "er6.rutgers.edu": 16,
            "world.std.com": 14,
            "cyclom1-1-6.intersource.com": 13,
            "d24-1.cpe.Brisbane.aone.net.au": 16,
            "ppp19.glas.apc.org": 28,
            "pqr.com": 2,

        },
        {
            "cssu24.cs.ust.hk": 14,
            "cyclom1-1-6.intersource.com": 16,
            "er6.rutgers.edu": 15,
            "world.std.com": 17,
            "access9.accsyst.com": 31,
            "204.249.225.59": 35,
            "d24-1.cpe.Brisbane.aone.net.au": 16,
            "ppp19.glas.apc.org": 28,
            "pqr.com": 3,
        },
        {
            "cssu24.cs.ust.hk": 18,
            "d24-1.cpe.Brisbane.aone.net.au": 16,
            "world.std.com": 34,
            "er6.rutgers.edu": 17,
            "cyclom1-1-6.intersource.com": 71,
            "access9.accsyst.com": 31,
            "204.249.225.59": 35,
            "ppp19.glas.apc.org": 28,
            "pqr.com": 1,
        },
        {
            "cssu24.cs.ust.hk": 18,
            "d24-1.cpe.Brisbane.aone.net.au": 16,
            "world.std.com": 34,
            "er6.rutgers.edu": 17,
            "cyclom1-1-6.intersource.com": 71,
            "access9.accsyst.com": 31,
            "204.249.225.59": 35,
            "ppp19.glas.apc.org": 28,
            "abc.com": 1,
            "pqr.com": 1,

        },
        {
            "ppp19.glas.apc.org": 342,
            "d24-1.cpe.Brisbane.aone.net.au": 1,
            "cssu24.cs.ust.hk": 18,
            "world.std.com": 34,
            "er6.rutgers.edu": 17,
            "cyclom1-1-6.intersource.com": 71,
            "access9.accsyst.com": 31,
            "204.249.225.59": 35,
            "abc.com": 1,
            "pqr.com": 2,

        },
        {
            "ppp19.glas.apc.org": 342,
            "d24-1.cpe.Brisbane.aone.net.au": 1,
            "cssu24.cs.ust.hk": 18,
            "world.std.com": 34,
            "er6.rutgers.edu": 17,
            "cyclom1-1-6.intersource.com": 71,
            "access9.accsyst.com": 31,
            "204.249.225.59": 35,
            "pqr.com": 3,

        }

    ]
    a = [3.0550488507104108, 3.6888953270038343, 3.230820142897017, 4.7950819120487225, 4.116323468940876]
    sliding_window(data)
