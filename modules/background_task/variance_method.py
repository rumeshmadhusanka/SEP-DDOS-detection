import math

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
            if a >= b:
                if a == 0:
                    lamb = math.inf
                else:
                    lamb = abs(np.log(b / a))
            else:
                if b == 0:
                    lamb = math.inf
                else:
                    lamb = abs(np.log(a / b))
            if lower == 0:
                val = math.inf
            else:
                val = -np.log(a / lower) + lamb
            entropy_values[ip].append(val)

    return entropy_values


def cal_average_entropy_for_each_conn(dic):
    new_dic = {}
    for k in dic:
        total = 0
        for val in dic[k]:
            total += val
        new_dic[k] = total / len(dic[k])
    return new_dic


def cal_variance(dic_entropy, average_dict):
    result = {}
    for k in dic_entropy:
        val = 0
        for ent in dic_entropy[k]:
            val += (ent - average_dict[k]) ** 2
        val = val / len(dic_entropy[k])
        result[k] = val
    return result


def find_possibles(var_dic, all_dic):
    results = {}
    for k in var_dic:
        if var_dic[k] < 0.1:
            total = 0
            for i in all_dic:
                for d in i:
                    total += key_in_dict(k, i)
            results[k] = {"total_requests": total, "variance": var_dic[k]}
    return results


def variance_method(data):
    entropy = cal_entropy(data)
    print(entropy)
    avg_lst = cal_average_entropy_for_each_conn(entropy)
    var = cal_variance(entropy, avg_lst)
    print("Avg: ", avg_lst)
    print("Var: ", var)
    print("Results: ", find_possibles(var, data))


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
    a = {'access9.accsyst.com': [1.791759469228055, 1.791759469228055, 1.791759469228055, 1.791759469228055,
                                 1.791759469228055],
         'ppp19.glas.apc.org': [3.3473946756691793, 3.3473946756691793, 3.3473946756691793, 5.85000090255658,
                                0.844788448781778],
         'd24-1.cpe.Brisbane.aone.net.au': [1.4170660197866443, 1.4170660197866443, 1.4170660197866443,
                                            4.189654742026425,
                                            4.189654742026425],
         'er6.rutgers.edu': [1.8870696490323797, 2.012232791986386, 1.7619065060783738, 1.7619065060783738,
                             1.7619065060783738],
         '204.249.225.59': [1.791759469228055, 1.791759469228055, 1.791759469228055, 1.791759469228055,
                            1.791759469228055],
         'world.std.com': [2.673092497242454, 2.9779276489204842, 1.5916332878005937, 1.5916332878005937,
                           1.5916332878005937],
         'cssu24.cs.ust.hk': [2.1567332159814825, 2.4080476442623886, 1.9054187877005764, 1.9054187877005764,
                              1.9054187877005764],
         'cyclom1-1-6.intersource.com': [3.388893197856861, 4.463705623101906, 1.4835233134988377, 1.4835233134988377,
                                         1.4835233134988377]}
    variance_method(data)
