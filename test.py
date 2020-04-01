import math

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

    }

]
import numpy as np


def key_in_dict(key, dic):
    if key in dic:
        return dic[key]
    else:
        return 0


def cal_entropy(data_lst):
    result = {}  # ip_addr:count
    d = []
    for each_dic in data_lst:
        for ip in each_dic:
            t = each_dic[ip]
            for _ in range(t):
                d.append(ip)
    s = set(d)
    entropy_values = {}
    for i in s:
        entropy_values[i] = []

    N = len(data_lst) - 1
    for ip in s:
        lower = d.count(ip)
        for win_num in range(N):
            val = 0
            lamb = 0
            a = key_in_dict(ip, data_lst[win_num])
            b = key_in_dict(ip, data_lst[win_num + 1])
            if a == 0 or b == 0:
                lamb = 0
                pass
            elif a >= b:
                lamb = abs(np.log(b / a))
            else:
                lamb = abs(np.log(a / b))
            if a == 0:
                val = 0
            else:
                val = -np.log(a / lower) + lamb
            entropy_values[ip].append(val)

    return entropy_values


{'access9.accsyst.com': [1.791759469228055, 1.791759469228055, 1.791759469228055, 1.791759469228055,
                         1.791759469228055],
 'ppp19.glas.apc.org': [3.3473946756691793, 3.3473946756691793, 3.3473946756691793, 5.85000090255658,
                        0.844788448781778],
 'd24-1.cpe.Brisbane.aone.net.au': [1.4170660197866443, 1.4170660197866443, 1.4170660197866443, 4.189654742026425,
                                    4.189654742026425],
 'er6.rutgers.edu': [1.8870696490323797, 2.012232791986386, 1.7619065060783738, 1.7619065060783738,
                     1.7619065060783738],
 '204.249.225.59': [1.791759469228055, 1.791759469228055, 1.791759469228055, 1.791759469228055, 1.791759469228055],
 'world.std.com': [2.673092497242454, 2.9779276489204842, 1.5916332878005937, 1.5916332878005937,
                   1.5916332878005937],
 'cssu24.cs.ust.hk': [2.1567332159814825, 2.4080476442623886, 1.9054187877005764, 1.9054187877005764,
                      1.9054187877005764],
 'cyclom1-1-6.intersource.com': [3.388893197856861, 4.463705623101906, 1.4835233134988377, 1.4835233134988377,
                                 1.4835233134988377]}


def cal_average_entropy(dic, N):
    lst = []
    for i in range(N):
        temp = 0
        for k in dic:
            temp += dic[k][i]
        temp = temp / N
        lst.append(temp)
    return lst


def cal_std_deviation(dic, average_list):
    lst = []
    N = len(average_list)
    for i in range(N):
        temp = 0
        for k in dic:
            temp += (dic[k][i] - average_list[i]) ** 2
        temp = math.sqrt(temp / N)
        lst.append(temp)
    return lst


def algorithm(data_dic, avg_lst, std_lst):
    ddos_lst = set()
    N = len(avg_lst)

    for i in range(N):
        beta = 1
        for k in data_dic:
            H_it = data_dic[k][i]
            u_t = avg_lst[i]
            D_it = abs(u_t - H_it)
            if H_it > 1.5 * u_t:
                beta += 1
            elif 0.5 * u_t <= H_it < 1.5 * u_t:
                beta = beta
            elif H_it < 0.5 * u_t:
                beta -= 1

            if D_it > beta * std_lst[i]:
                print("D: " + str(D_it) + ", B: " + str(beta) + " ip: " + k)
                ddos_lst.add(k)
                beta = 1
    return ddos_lst


def algorithm1(data_dic, avg_lst, std_lst):
    ddos_lst = set()
    N = len(avg_lst)

    for k in data_dic:
        beta = 1
        for win in range(N):
            H_it = data_dic[k][win]
            u_t = avg_lst[win]
            D_it = abs(u_t - H_it)
            if H_it > 1.5 * u_t:
                beta += 1
            elif 0.5 * u_t <= H_it < 1.5 * u_t:
                beta = beta
            elif H_it < 0.5 * u_t:
                beta -= 1
            if D_it > beta * std_lst[win]:
                print("D: " + str(D_it) + ", B: " + str(beta) + " ip: " + k)
                ddos_lst.add(k)

    return ddos_lst


if __name__ == "__main__":
    print(cal_entropy(data))
    # a = cal_entropy(data)
    # avg_lst = cal_average_entropy(a, 5)
    # std_dev = cal_std_deviation(a, avg_lst)
    # print("Avg: ", avg_lst)
    # print("Std dev: ", std_dev)
    # print(len(algorithm1(a, avg_lst, std_dev)))
