from mantis.openbrowser import Test
from mantis.wkdemo import buglist_group
from mantis.exceldemo import run_excel
import openpyxl

def openbrowser(projectlist):
    open_bugs_list = []
    for project in projectlist:
        t.open_browser()
        t.login()
        t.search_buglist(project)
        t.open_bugs()
        open_bugs_list.append(t.global_wkdic)
    return open_bugs_list

if __name__ == '__main__':
    # 浏览器处理
    # projectlist = ['E1 AL-LX110ST/AL-LW110ST','中器S1','A62S/C/D/、A66H','微投']
    # projectlist = ['微投','A62S/C/D/、A66H','A63D/C']
    # projectlist = ['E1 AL-LX110ST/AL-LW110ST','中器S1','A63D/C']
    # projectlist = ['E1 AL-LX110ST/AL-LW110ST','中器S1','S1商教机TI5.0平台','S1商教机TI8.0平台','E2 希沃','E2升级版TI5.0平台','E2升级版TI8.0平台']
    projectlist = ['E1 AL-LX110ST/AL-LW110ST','中器S1','S1商教机TI5.0平台','S1商教机TI8.0平台','E2升级版TI5.0平台','E2升级版TI8.0平台']



    # list_wkdict = openbrowser(project)

    # print(list_wkdict)
    # list_wkdict = [{'wk1': [[0, 0, 0], [[], [], []]], 'wk2': [[0, 0, 0], [[], [], []]], 'wk3': [[0, 0, 0], [[], [], []]], 'wk4': [[0, 4, 0], [[], ['0017060', '0018789', '0017069', '0017060'], []]], 'wk5': [[0, 0, 0], [[], [], []]], 'wk6': [[2, 0, 0], [['0005551', '0005551'], [], ['0005551', '0005551']]], 'wk7': [[0, 0, 0], [[], [], []]], 'wk8': [[0, 0, 0], [[], [], []]], 'wk9': [[0, 0, 0], [[], [], []]], 'wk10': [[9, 1, 2], [['0006005', '0005980', '0005979', '0005975', '0005971', '0005971', '0005975', '0005979', '0005980'], ['0017008', '0005980', '0005980'], ['0005971', '0005971']]], 'wk11': [[0, 0, 0], [[], [], []]], 'wk12': [[0, 0, 0], [[], [], []]], 'wk13': [[0, 0, 0], [[], [], []]], 'wk14': [[0, 0, 0], [[], [], []]], 'wk15': [[0, 0, 0], [[], [], []]], 'wk16': [[0, 0, 0], [[], [], []]], 'wk17': [[1, 0, 0], [['0015586'], [], []]], 'wk18': [[0, 0, 0], [[], [], []]], 'wk19': [[0, 0, 0], [[], [], []]], 'wk20': [[0, 0, 0], [[], [], []]], 'wk21': [[0, 0, 0], [[], [], []]], 'wk22': [[0, 0, 0], [[], [], []]], 'wk23': [[0, 0, 0], [[], [], []]], 'wk24': [[0, 0, 0], [[], [], []]], 'wk25': [[0, 0, 0], [[], [], []]], 'wk26': [[0, 0, 0], [[], [], []]], 'wk27': [[0, 0, 0], [[], [], []]], 'wk28': [[0, 0, 0], [[], [], []]], 'wk29': [[0, 0, 0], [[], [], []]], 'wk30': [[0, 0, 0], [[], [], []]], 'wk31': [[0, 0, 0], [[], [], []]], 'wk32': [[2, 0, 0], [['0017008', '0017002'], [], []]], 'wk33': [[0, 0, 0], [[], [], []]], 'wk34': [[24, 0, 0], [['0017059', '0017060', '0017061', '0017062', '0017063', '0017090', '0017087', '0017085', '0017082', '0017081', '0017078', '0017077', '0017076', '0017075', '0017074', '0017071', '0017069', '0017065', '0017064', '0017063', '0017062', '0017061', '0017060', '0017059'], [], ['0017076', '0017075']]], 'wk35': [[0, 4, 2], [[], ['0015586', '0006005', '0005979', '0005975', '0005975', '0005979'], []]], 'wk36': [[2, 0, 11], [['0017194', '0017192'], ['0017061', '0017062', '0017063', '0017002', '0017082', '0017077', '0017074', '0017064', '0017063', '0017062', '0017061'], []]], 'wk37': [[0, 0, 0], [[], [], []]], 'wk38': [[0, 4, 0], [[], ['0017194', '0017192', '0017078', '0017065'], []]], 'wk39': [[0, 2, 0], [[], ['0017087', '0017071'], []]], 'wk40': [[0, 0, 0], [[], [], []]], 'wk41': [[0, 1, 0], [[], ['0017081'], []]], 'wk42': [[0, 0, 0], [[], [], []]], 'wk43': [[2, 2, 1], [['0018789', '0018788'], ['0017059', '0017085', '0017059'], ['0018788']]], 'wk44': [[0, 0, 0], [[], [], []]], 'wk45': [[0, 0, 0], [[], [], []]], 'wk46': [[0, 0, 0], [[], [], []]], 'wk47': [[0, 0, 0], [[], [], []]], 'wk48': [[0, 0, 0], [[], [], []]], 'wk49': [[0, 0, 0], [[], [], []]], 'wk50': [[0, 0, 0], [[], [], []]], 'wk51': [[0, 0, 0], [[], [], []]], 'wk52': [[0, 1, 0], [[], ['0017090'], []]]}, {'wk1': [[0, 0, 0], [[], [], []]], 'wk2': [[0, 0, 0], [[], [], []]], 'wk3': [[0, 0, 0], [[], [], []]], 'wk4': [[0, 4, 0], [[], ['0017060', '0018789', '0017069', '0017060'], []]], 'wk5': [[0, 0, 0], [[], [], []]], 'wk6': [[2, 0, 0], [['0005551', '0005551'], [], ['0005551', '0005551']]], 'wk7': [[0, 0, 0], [[], [], []]], 'wk8': [[0, 0, 0], [[], [], []]], 'wk9': [[0, 0, 0], [[], [], []]], 'wk10': [[9, 1, 2], [['0006005', '0005980', '0005979', '0005975', '0005971', '0005971', '0005975', '0005979', '0005980'], ['0017008', '0005980', '0005980'], ['0005971', '0005971']]], 'wk11': [[0, 0, 0], [[], [], []]], 'wk12': [[0, 0, 0], [[], [], []]], 'wk13': [[0, 0, 0], [[], [], []]], 'wk14': [[0, 0, 0], [[], [], []]], 'wk15': [[0, 0, 0], [[], [], []]], 'wk16': [[0, 0, 0], [[], [], []]], 'wk17': [[1, 0, 0], [['0015586'], [], []]], 'wk18': [[0, 0, 0], [[], [], []]], 'wk19': [[0, 0, 0], [[], [], []]], 'wk20': [[0, 0, 0], [[], [], []]], 'wk21': [[0, 0, 0], [[], [], []]], 'wk22': [[0, 0, 0], [[], [], []]], 'wk23': [[0, 0, 0], [[], [], []]], 'wk24': [[0, 0, 0], [[], [], []]], 'wk25': [[0, 0, 0], [[], [], []]], 'wk26': [[0, 0, 0], [[], [], []]], 'wk27': [[0, 0, 0], [[], [], []]], 'wk28': [[0, 0, 0], [[], [], []]], 'wk29': [[0, 0, 0], [[], [], []]], 'wk30': [[0, 0, 0], [[], [], []]], 'wk31': [[0, 0, 0], [[], [], []]], 'wk32': [[2, 0, 0], [['0017008', '0017002'], [], []]], 'wk33': [[0, 0, 0], [[], [], []]], 'wk34': [[24, 0, 0], [['0017059', '0017060', '0017061', '0017062', '0017063', '0017090', '0017087', '0017085', '0017082', '0017081', '0017078', '0017077', '0017076', '0017075', '0017074', '0017071', '0017069', '0017065', '0017064', '0017063', '0017062', '0017061', '0017060', '0017059'], [], ['0017076', '0017075']]], 'wk35': [[0, 4, 2], [[], ['0015586', '0006005', '0005979', '0005975', '0005975', '0005979'], []]], 'wk36': [[2, 0, 11], [['0017194', '0017192'], ['0017061', '0017062', '0017063', '0017002', '0017082', '0017077', '0017074', '0017064', '0017063', '0017062', '0017061'], []]], 'wk37': [[0, 0, 0], [[], [], []]], 'wk38': [[0, 4, 0], [[], ['0017194', '0017192', '0017078', '0017065'], []]], 'wk39': [[0, 2, 0], [[], ['0017087', '0017071'], []]], 'wk40': [[0, 0, 0], [[], [], []]], 'wk41': [[0, 1, 0], [[], ['0017081'], []]], 'wk42': [[0, 0, 0], [[], [], []]], 'wk43': [[2, 2, 1], [['0018789', '0018788'], ['0017059', '0017085', '0017059'], ['0018788']]], 'wk44': [[0, 0, 0], [[], [], []]], 'wk45': [[0, 0, 0], [[], [], []]], 'wk46': [[0, 0, 0], [[], [], []]], 'wk47': [[0, 0, 0], [[], [], []]], 'wk48': [[0, 0, 0], [[], [], []]], 'wk49': [[0, 0, 0], [[], [], []]], 'wk50': [[0, 0, 0], [[], [], []]], 'wk51': [[0, 0, 0], [[], [], []]], 'wk52': [[0, 1, 0], [[], ['0017090'], []]]}]
    # print(list_wkdict)

    wb = openpyxl.Workbook()
    for project in projectlist:
        # 浏览器处理
        t = Test()
        # t.wkdic = {}
        t.open_browser()
        t.login()
        t.init_wkdic()
        t.search_buglist(project)
        t.open_bugs()
        print('wkdic:%s'%t.global_wkdic)
        wkdic = buglist_group(t.global_wkdic)
        # t.driver.close()
        #excel处理
        index = projectlist.index(project)
        projectname = projectlist[index]
        if '/' in projectname:
            projectname = projectname.replace('/','|')
        run_excel(wb,wkdic,projectname,index)
    # print(wkdic)
