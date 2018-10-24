from mantis.bugs2017.openbrowser import Test
from mantis.bugs2017.wkdemo import buglist_group
from mantis.bugs2017.exceldemo import run_excel
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
    # projectlist = ['S1商教机TI5.0平台','S1商教机TI8.0平台','E2升级版TI5.0平台','E2升级版TI8.0平台']
    projectlist = ['E2升级版TI5.0平台']

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
