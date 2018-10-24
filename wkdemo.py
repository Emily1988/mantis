#此模块，对buglist数据按照周分类名

def buglist_group(dic):
    keys = dic.keys()
    vals = dic.values()
    #字典转化成列表
    L = [(key,val) for key,val in zip(keys, vals)]
    # #列表分组，用于计算本周wk,wk+1,wk+2,wk+3
    data = {}
    for i in range(0,len(L),1):
        # print(L[i:i+4])
        try:
            # 本周提出的buglist
            keybug = L[i:i+4][0][0]
            # print(keybug)
            newbugs = L[i:i + 4][0][1][1][0]
            # print(newbugs)
            # print("wk周新建了%s个bug" % len(newbugs))
            # wk解决的buglist
            wkbugs = L[i:i + 4][0][1][1][1]
            wkpresent_bugs = L[i:i + 4][0][1][1][2]
            wkpresent = list(set(newbugs).intersection(set(wkpresent_bugs)))
            # print("遗留未解决问题数目%s" % len(wkpresent))
            # print(wkbugs)
            res = list(set(newbugs).intersection(set(wkbugs)))
            # print("wk周解决了%s个bug" % len(res))
            # wk1解决的buglist
            wk1bugs = L[i:i + 4][1][1][1][1]
            # print(wk1bugs)
            res1 = list(set(newbugs).intersection(set(wk1bugs)))
            # print("wk+1周解决了%s个bug" % len(res1))
            # wk2解决的buglist
            wk2bugs = L[i:i + 4][2][1][1][1]
            # print(wk2bugs)
            res2 = list(set(newbugs).intersection(set(wk2bugs)))
            # print("wk+2周解决了%s个bug" % len(res2))
            # wk3解决的buglist
            wk3bugs = L[i:i + 4][3][1][1][1]
            # print(wk3bugs)
            res3 = list(set(newbugs).intersection(set(wk3bugs)))
            # print("wk+3周解决了%s个bug" % len(res3))
            no3 = len(newbugs)-len(res)-len(res1)-len(res2)-len(res3)
            # print("3周内未提供对策剩余bug数目%s"%no3)
            data[keybug] = [len(newbugs),len(res),len(res1),len(res2),len(res3),no3,len(wkpresent)]

        except Exception as exc:
            print(exc)
            data[keybug] = [len(newbugs), len(res), len(res1), len(res2), len(res3), no3,len(wkpresent)]
    # print(data)
    return data

if __name__ == '__main__':
    dict = {'wk1': [[0, 0, 0], [[], [], []]], 'wk2': [[0, 0, 0], [[], [], []]], 'wk3': [[0, 0, 0], [[], [], []]], 'wk4': [[0, 0, 0], [[], [], []]], 'wk5': [[0, 0, 0], [[], [], []]], 'wk6': [[1, 0, 0], [['0005551'], [], ['0005551']]], 'wk7': [[0, 0, 0], [[], [], []]], 'wk8': [[0, 0, 0], [[], [], []]], 'wk9': [[0, 0, 0], [[], [], []]], 'wk10': [[5, 1, 1], [['0006005', '0005980', '0005979', '0005975', '0005971'], ['0017008', '0005980'], ['0005971']]], 'wk11': [[0, 0, 0], [[], [], []]], 'wk12': [[0, 0, 0], [[], [], []]], 'wk13': [[0, 0, 0], [[], [], []]], 'wk14': [[0, 0, 0], [[], [], []]], 'wk15': [[0, 0, 0], [[], [], []]], 'wk16': [[0, 0, 0], [[], [], []]], 'wk17': [[1, 0, 0], [['0015586'], [], []]], 'wk18': [[0, 0, 0], [[], [], []]], 'wk19': [[0, 0, 0], [[], [], []]], 'wk20': [[0, 0, 0], [[], [], []]], 'wk21': [[0, 0, 0], [[], [], []]], 'wk22': [[0, 0, 0], [[], [], []]], 'wk23': [[0, 0, 0], [[], [], []]], 'wk24': [[0, 0, 0], [[], [], []]], 'wk25': [[0, 0, 0], [[], [], []]], 'wk26': [[0, 0, 0], [[], [], []]], 'wk27': [[0, 0, 0], [[], [], []]], 'wk28': [[0, 0, 0], [[], [], []]], 'wk29': [[0, 0, 0], [[], [], []]], 'wk30': [[0, 0, 0], [[], [], []]], 'wk31': [[0, 0, 0], [[], [], []]], 'wk32': [[2, 0, 0], [['0017002', '0017008'], [], []]], 'wk33': [[0, 0, 0], [[], [], []]], 'wk34': [[0, 0, 0], [[], [], []]], 'wk35': [[0, 3, 1], [[], ['0006005', '0015586', '0005979', '0005975'], []]], 'wk36': [[0, 0, 1], [[], ['0017002'], []]], 'wk37': [[0, 0, 0], [[], [], []]], 'wk38': [[0, 0, 0], [[], [], []]], 'wk39': [[0, 0, 0], [[], [], []]], 'wk40': [[0, 0, 0], [[], [], []]], 'wk41': [[0, 0, 0], [[], [], []]], 'wk42': [[0, 0, 0], [[], [], []]], 'wk43': [[0, 0, 0], [[], [], []]], 'wk44': [[0, 0, 0], [[], [], []]], 'wk45': [[0, 0, 0], [[], [], []]], 'wk46': [[0, 0, 0], [[], [], []]], 'wk47': [[0, 0, 0], [[], [], []]], 'wk48': [[0, 0, 0], [[], [], []]], 'wk49': [[0, 0, 0], [[], [], []]], 'wk50': [[0, 0, 0], [[], [], []]], 'wk51': [[0, 0, 0], [[], [], []]], 'wk52': [[0, 0, 0], [[], [], []]]}
    group = buglist_group(dict)

    print(group)