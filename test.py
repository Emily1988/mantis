def dict_list(dic: dict):
    keys = dic.keys()
    vals = dic.values()
    #字典转化成列表
    L = [(key,val) for key,val in zip(keys, vals)]
    wk = []
    #列表分组，用于计算本周wk,wk+1,wk+2,wk+3
    for i in range(0,len(L),1):
        print(L[i:i+4])
        print(L[i:i+4][0][0])    #wk?
        print(L[i:i+4][0][1][0]) #newbug
        print(L[i:i+4][0][1][1]) #wk周解决和关闭的bug
        print(L[i:i+4][1][1][1])  # wk+1周解决和关闭的bug
        print(L[i:i+4][2][1][1])  # wk+2周解决和关闭的bug
        print(L[i:i+4][3][1][1])  # wk+3周解决和关闭的bug

    return L

if __name__ == '__main__':
    dict = {'wk1': [0, 0, 0], 'wk2': [0, 0, 0], 'wk3': [0, 0, 0], 'wk4': [0, 0, 0], 'wk5': [0, 0, 0], 'wk6': [1, 0, 0], 'wk7': [0, 0, 0], 'wk8': [0, 0, 0], 'wk9': [0, 0, 0], 'wk10': [5, 1, 1], 'wk11': [0, 0, 0], 'wk12': [0, 0, 0], 'wk13': [0, 0, 0], 'wk14': [0, 0, 0], 'wk15': [0, 0, 0], 'wk16': [0, 0, 0], 'wk17': [1, 0, 0], 'wk18': [0, 0, 0], 'wk19': [0, 0, 0], 'wk20': [0, 0, 0], 'wk21': [0, 0, 0], 'wk22': [0, 0, 0], 'wk23': [0, 0, 0], 'wk24': [0, 0, 0], 'wk25': [0, 0, 0], 'wk26': [0, 0, 0], 'wk27': [0, 0, 0], 'wk28': [0, 0, 0], 'wk29': [0, 0, 0], 'wk30': [0, 0, 0], 'wk31': [0, 0, 0], 'wk32': [2, 0, 0], 'wk33': [0, 0, 0], 'wk34': [0, 0, 0], 'wk35': [0, 3, 1], 'wk36': [0, 0, 1], 'wk37': [0, 0, 0], 'wk38': [0, 0, 0], 'wk39': [0, 0, 0], 'wk40': [0, 0, 0], 'wk41': [0, 0, 0], 'wk42': [0, 0, 0], 'wk43': [0, 0, 0], 'wk44': [0, 0, 0], 'wk45': [0, 0, 0], 'wk46': [0, 0, 0], 'wk47': [0, 0, 0], 'wk48': [0, 0, 0], 'wk49': [0, 0, 0], 'wk50': [0, 0, 0], 'wk51': [0, 0, 0], 'wk52': [0, 0, 0], 'wk53': [0, 0, 0]}
    # print(dict)
    for key,value in dict.items():
        # print(key,value)
        bz = value[1]+value[2]
        value[1] = bz
        del(value[2])
        # wk1 = dict[i+1]+value[i+1]
        # value[2] = wk1
        # wk2 = dict[i+2]+value[i+2]
        # value.append(wk2)
        # wk3 = dict[i+3]+value[i+3]
        # value.append(wk3)

    # print(dict)


    # dict_list(dict)

    L = [('wk1', [20, 10]), ('wk2', [5, 1]), ('wk3', [7, 9]), ('wk4', [56, 345])]
    # print(L[0][0])  # wk?
    # print(L[0][1][0])  # newbug
    # print(L[0][1][1])  # wk周解决和关闭的bug
    # print(L[1][1][1])  # wk+1周解决和关闭的bug
    # print(L[2][1][1])  # wk+2周解决和关闭的bug
    # print(L[3][1][1])  # wk+3周解决和关闭的bug

    A = ['a', 'b', 'c']
    B = ['c', 'd', 'e','f','g','a']
    # 两个集合中的相同元素
    res = list(set(A).intersection(set(B)))
    print(len(res))
    # 判断b里面的元素有一个在A里
    boo = len(res) > 0
