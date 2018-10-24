from mantis.bugs2017_single.openbrowser import Test
from mantis.bugs2017_single.wkdemo import buglist_group
from mantis.bugs2017_single.exceldemo import run_excel

def openbrowser(project):
    t = Test()
    t.open_browser()
    t.login()
    t.search_buglist(project)
    t.open_bugs()
    return t.global_wkdic

if __name__ == '__main__':
    projectlist = ['E1 AL-LX110ST/AL-LW110ST', '中器S1','A62S/C/D/、A66H','微投']
    project = '微投'
    # project = 'E1 AL-LX110ST/AL-LW110ST'

    dic = openbrowser(project)
    # if '/' in project:
    #     project = project.replace('/', '|')
    wkdic = buglist_group(dic)

    run_excel(wkdic)
    # print(wkdic)