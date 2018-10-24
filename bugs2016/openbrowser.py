from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import requests
from bs4 import BeautifulSoup
from mantis.bugs2016 import date


class Test:
    global_wkdic = {}
    driver = None

    # 字典中的值列表[0]存放键对应周的新增bug数目，[1]存放键对应周的解决的bug数目，[2]存放键对应周关闭的bug数目，解决bug，优先关闭bug
    wkdic = {}
    def init_wkdic(self):
        self.wkdic = {'wk1': [[0, 0, 0], [[], [], []]], 'wk2': [[0, 0, 0], [[], [], []]], 'wk3': [[0, 0, 0], [[], [], []]],
         'wk4': [[0, 0, 0], [[], [], []]], 'wk5': [[0, 0, 0], [[], [], []]], 'wk6': [[0, 0, 0], [[], [], []]],
         'wk7': [[0, 0, 0], [[], [], []]], 'wk8': [[0, 0, 0], [[], [], []]], 'wk9': [[0, 0, 0], [[], [], []]],
         'wk10': [[0, 0, 0], [[], [], []]], 'wk11': [[0, 0, 0], [[], [], []]], 'wk12': [[0, 0, 0], [[], [], []]],
         'wk13': [[0, 0, 0], [[], [], []]], 'wk14': [[0, 0, 0], [[], [], []]], 'wk15': [[0, 0, 0], [[], [], []]],
         'wk16': [[0, 0, 0], [[], [], []]], 'wk17': [[0, 0, 0], [[], [], []]], 'wk18': [[0, 0, 0], [[], [], []]],
         'wk19': [[0, 0, 0], [[], [], []]], 'wk20': [[0, 0, 0], [[], [], []]], 'wk21': [[0, 0, 0], [[], [], []]],
         'wk22': [[0, 0, 0], [[], [], []]], 'wk23': [[0, 0, 0], [[], [], []]], 'wk24': [[0, 0, 0], [[], [], []]],
         'wk25': [[0, 0, 0], [[], [], []]], 'wk26': [[0, 0, 0], [[], [], []]], 'wk27': [[0, 0, 0], [[], [], []]],
         'wk28': [[0, 0, 0], [[], [], []]], 'wk29': [[0, 0, 0], [[], [], []]], 'wk30': [[0, 0, 0], [[], [], []]],
         'wk31': [[0, 0, 0], [[], [], []]], 'wk32': [[0, 0, 0], [[], [], []]], 'wk33': [[0, 0, 0], [[], [], []]],
         'wk34': [[0, 0, 0], [[], [], []]], 'wk35': [[0, 0, 0], [[], [], []]], 'wk36': [[0, 0, 0], [[], [], []]],
         'wk37': [[0, 0, 0], [[], [], []]], 'wk38': [[0, 0, 0], [[], [], []]], 'wk39': [[0, 0, 0], [[], [], []]],
         'wk40': [[0, 0, 0], [[], [], []]], 'wk41': [[0, 0, 0], [[], [], []]], 'wk42': [[0, 0, 0], [[], [], []]],
         'wk43': [[0, 0, 0], [[], [], []]], 'wk44': [[0, 0, 0], [[], [], []]], 'wk45': [[0, 0, 0], [[], [], []]],
         'wk46': [[0, 0, 0], [[], [], []]], 'wk47': [[0, 0, 0], [[], [], []]], 'wk48': [[0, 0, 0], [[], [], []]],
         'wk49': [[0, 0, 0], [[], [], []]], 'wk50': [[0, 0, 0], [[], [], []]], 'wk51': [[0, 0, 0], [[], [], []]],
         'wk52': [[0, 0, 0], [[], [], []]]}

        # for i in range(1, 53):
        #     key = 'wk{}'.format(i)
        #     # [0, 0, 0] = [新建bug总数，解决bug总数，关闭bug总数]
        #     self.wkdic = {key:[[0, 0, 0], [[], [], []]]}
        #     self.wkdic.update(self.wkdic)
        #     # self.wkdic.setdefault(key, [[0, 0, 0], [[], [], []]])  # [[新建],[解决和关闭],[截止到目前还未关闭的bug]]
    # wkdic.clear()

    def open_browser(self):
        url = 'http://172.32.252.27/mantisbt/'
        # url = 'http://www.baidu.com'
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        assert "缺陷跟踪管理系统" in self.driver.title
        return self.driver

    def login(self):
        uname = self.driver.find_element_by_name('username')
        pwd = self.driver.find_element_by_name("password")
        login = self.driver.find_element_by_class_name('button')
        uname.clear()
        pwd.clear()
        uname.send_keys("dywu")
        pwd.send_keys('dywu')
        login.click()
        # locator = self.driver.find_element_by_xpath("//a[contains(@href,'dywu')]")
        try:
            # WebDriverWait.until(ec.presence_of_element_located(locator))  #显示等待
            time.sleep(5)
            assert "dywu" in self.driver.page_source
        except Exception as e:
            print('登录失败')

    # 根据条件搜索数据
    def search_buglist(self, project):
        self.driver.find_element_by_link_text('查看问题').click()
        # 选择项目
        self.driver.find_element_by_link_text(project).click()
        # 高级过滤器
        self.driver.find_element_by_xpath("//a[@href='view_all_set.php?type=6&view_type=advanced']").click()  # 模糊定位
        # 选择严重性
        self.driver.find_element_by_xpath("//a[contains(@href,'show_severity')]").click()  # 模糊定位
        # self.driver.find_element_by_name('show_severity[]').find_element_by_xpath("//option[@value='30']").click()
        # self.driver.find_element_by_xpath(".//*[@name='show_severity[]']/option[4]").click()  #Xpath, index从1开始
        s = self.driver.find_element_by_name('show_severity[]')
        Select(s).deselect_by_index(0)
        Select(s).select_by_index(3)  # Select模块的index index从0开始
        Select(s).select_by_index(4)
        # Select(s).select_by_value('Maj')
        # 选择分类
        self.driver.find_element_by_xpath("//a[contains(@href,'show_category[]')]").click()
        # s = self.driver.find_element_by_name('show_category[]')
        s = self.driver.find_element_by_name("show_category[]")
        classlist = s.text.split('\n')
        Select(s).deselect_by_index(0)
        for list in classlist:
            if "软件测试" in list:
                # print(list)
                Select(s).select_by_value(list)
        # 显示全部bug clear
        self.driver.find_element_by_xpath(
            "//a[@href='view_filters_page.php?for_screen=1&view_type=advanced&target_field=per_page']").click()
        self.driver.find_element_by_name('per_page').clear()
        # 选择变更时间 clear
        self.driver.find_element_by_xpath(
            "//a[@href='view_filters_page.php?for_screen=1&view_type=advanced&target_field=highlight_changed']").click()
        self.driver.find_element_by_name('highlight_changed').clear()
        # 使用时间过滤
        self.driver.find_element_by_xpath(
            "//a[@href='view_filters_page.php?for_screen=1&view_type=advanced&target_field=do_filter_by_date']").click()
        self.driver.find_element_by_name('do_filter_by_date').click()
        start_year = self.driver.find_element_by_name('start_year')
        Select(start_year).select_by_value('2016')
        start_month = self.driver.find_element_by_name('start_month')
        Select(start_month).select_by_value('1')
        start_day = self.driver.find_element_by_name('start_day')
        Select(start_day).select_by_value('4')
        end_year = self.driver.find_element_by_name('end_year')
        Select(end_year).select_by_value('2017')
        end_month = self.driver.find_element_by_name('end_month')
        Select(end_month).select_by_value('1')
        end_day = self.driver.find_element_by_name('end_day')
        Select(end_day).select_by_value('1')
        # 点击筛选按钮进行过滤
        self.driver.find_element_by_name('filter').click()
        # 点击报告日期进行排序
        self.driver.find_element_by_xpath("//a[@href='view_all_set.php?sort=date_submitted&dir=DESC&type=2']").click()

    def get_bug_url(self):
        self.driver.find_elements_by_partial_link_text("")
        driver_urllist = self.driver.find_elements_by_xpath("//td/a[contains(@href,'/mantisbt/view.php?id=')]")
        return driver_urllist

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate"
    }

    def getsession_request_login(self):
        url = 'http://172.32.252.27/mantisbt/login_page.php'
        param = {
            "username": "dywu",
            "password": "dywu",
            "secure_session": "on"
        }
        response = requests.post(url, param, headers=self.headers, allow_redirects=False)
        if response.status_code == 200:
            print('登录成功')
            return response.cookies.get_dict()['PHPSESSID']
        else:
            print('登录失败')

    def request_bug(self, url, session, bugid):
        cookie = {
            "PHPSESSID": session,
            "MANTIS_secure_session": "1",
            "MANTIS_STRING_COOKIE": "9c126f1b6a03696250bc3ee5952da7c2d85e4e300565e74ba39cc7dce807128a"
        }
        response = requests.get(url, allow_redirects=False,
                                headers=self.headers, cookies=cookie)
        if response.status_code == 200:
            content = response.text
            # fp = open('bug.html', "w+", encoding='utf-8')
            # fp.write(content)
            # fp.close()

            # with open('bug.html', mode='r', encoding='UTF-8') as f:
            #     try:
            #         self.html_parser(f, bugid)
            #     finally:
            #         f.close()

            self.html_parser(response.text, bugid)


    def open_bugs(self):
        driver_urls = self.get_bug_url()
        sessionid = self.getsession_request_login()

        bugid = []
        for bug_url in driver_urls:  # 去除重复的bugid
            if bug_url.text not in bugid:
                if bug_url.text.find(':') != -1: #去除id=0000692:0000045类型的
                    continue
                bugid.append(bug_url.text)

        for id in bugid:
            url = "http://172.32.252.27/mantisbt/view.php?id={}".format(id)
            print(url)
            self.request_bug(url, sessionid, id)

    def year2016_baogao_time(self):
        datestring = baogao_time.split(' ')[0]
        datelist = datestring.split('-')
        wk = date.week_date(datelist[0], datelist[1], datelist[2])
        return wk[0]

    #bug状态是关闭的，但是关闭日期不详（优先按照结案日期算，如果没有结案日期，按照解决对策，最后更新日期）
    def closetime_isNot_detailed(self,bugstate,bugid):
        global slove_isFind  #解决日期
        global close_isFind  #关闭日期
        global revise_closedata_isFind  # 改善结案日期
        global close_common   #解决对策/最后更新时间
        slove_isFind = False
        close_isFind = False
        revise_closedata_isFind = False
        close_common = False
        for i in range(0, len(bugstate), 4):
            b = bugstate[i:i + 4]
            if b[3].find('已解决') is not -1:
                datestring = b[0].split(' ')[0]
                datelist = datestring.split('-')
                wk = date.week_date(datelist[0], datelist[1], datelist[2])
                if self.year2016_baogao_time() == '2016':
                    key = 'wk{}'.format(wk[1])
                    print('已解决%s' % key)
                    value = self.wkdic[key]
                    value[0][1] = value[0][1] + 1
                    value[1][1].append(bugid)
                else:
                    print('bugid = %s,【报告日期】 = %s,【解决日期】 = %s'%(bugid,baogao_time,datestring))
                slove_isFind = True
                break
            if b[3].find('已关闭') is not -1:
                datestring = b[0].split(' ')[0]
                datelist = datestring.split('-')
                wk = date.week_date(datelist[0], datelist[1], datelist[2])
                if self.year2016_baogao_time() == '2016':
                    key = 'wk{}'.format(wk[1])
                    print('已关闭%s' % key)
                    value = self.wkdic[key]
                    value[0][2] = value[0][2] + 1
                    value[1][1].append(bugid)
                else:
                    print('bugid = %s,【报告日期】 = %s,【关闭日期】 = %s' % (bugid, baogao_time, datestring))
                close_isFind = True
                break
            if b[2].find('改善结案日期') is not -1:
                if b[3].find('/') is not -1:
                    datestring = b[3].split(' ')[1]
                    datelist = datestring.split('/')
                    wk = date.week_date(datelist[0], datelist[1], datelist[2])
                    if self.year2016_baogao_time() == '2016':
                        key = 'wk{}'.format(wk[1])
                        print('改善结案日期%s' % key)
                        value = self.wkdic[key]
                        value[0][1] = value[0][1] + 1
                        value[1][1].append(bugid)
                    else:
                        print('bugid = %s,【报告日期】 = %s,【改善结案日期】 = %s' % (bugid, baogao_time, datestring))
                    revise_closedata_isFind = True
                    break
                else:
                    print('【结案日期格式不标准】%s的结案日期是%s' % (bugid, b[3]))
            if b[2].find('解决对策') is not -1:
                datestring = b[0].split(' ')[0]
                datelist = datestring.split('-')
                wk = date.week_date(datelist[0], datelist[1], datelist[2])
                if self.year2016_baogao_time() == '2016':
                    key = 'wk{}'.format(wk[1])
                    print('给出解决对策%s' % key)
                    value = self.wkdic[key]
                    value[0][1] = value[0][1] + 1
                    value[1][1].append(bugid)
                else:
                    print('bugid = %s,【报告日期】 = %s,【给出解决对策日期】 = %s' % (bugid, baogao_time, datestring))
                close_common = True
                break
        if slove_isFind == False and close_isFind == False and revise_closedata_isFind == False and close_common == False:
            print('没有找到关闭的标识，可bug状态已经是关闭的了，因此按照最后更新日记即为关闭日期')
            self.updata_bug_time(bugid)

    # 把新建bug时间放入已定义好的空字典
    def new_bug_time(self,bugid):
        global newkey
        datestring = baogao_time.split(' ')[0]
        datelist = datestring.split('-')
        newwk = date.week_date(datelist[0], datelist[1], datelist[2])
        newkey = 'wk{}'.format(newwk[1])
        print('新建%s' % newkey)
        value = self.wkdic[newkey]
        value[0][0] = value[0][0] + 1
        # 统计新建的buglist，以便后续跟踪本周新建bug，统计wk+1解决bug时排除其他周新建的bug
        # 例如wk5提交了5个bug,wk+1周解决了7个bug，这7个bug中有一部分是其他周（wk6,wk7....）提出的
        value[1][0].append(bugid)

    def updata_bug_time(self,bugid):
        datestring = update_time.split(' ')[0]
        datelist = datestring.split('-')
        wk = date.week_date(datelist[0], datelist[1], datelist[2])
        if self.year2016_baogao_time() == '2016':
            updatekey = 'wk{}'.format(wk[1])
            print('最后更新%s' % updatekey)
            value = self.wkdic[updatekey]
            value[0][1] = value[0][1] + 1
            value[1][1].append(bugid)
        else:
            print('bugid = %s,【报告日期】 = %s,【最后更新日期】 = %s' % (bugid, baogao_time, datestring))
        close_common = True

    def html_parser(self, html, bugid = None):
        global baogao_time
        global update_time
        soup = BeautifulSoup(html, "html.parser")
        # soup = BeautifulSoup(open('bug.html', mode='r', encoding='UTF-8'),"html.parser").body

        #找到报告日期和更新日期
        for elem in soup(text='报告日期'):
            next_table = elem.parent.next_sibling
            for index, children in enumerate(next_table.parent.next_sibling.children):
                print(index,children)
                if index == 4:
                    baogao_time = children.text
                if index == 5:
                    update_time = children.text
            # print(baogao_time)

        # 找到bug状态：关闭
        for elem in soup(text='状态'):
            table = elem.parent
            next_table = table.next_sibling

            tds = soup.find_all("td", "small-caption")
            rows = int(len(tds) / 4)
            # bugstate = [[0 for col in range(4)] for row in range(rows)]  #rows行4列的空列表
            bugstate = [num.text.lstrip().rstrip('\t') for num in tds]  # 列表生成器
            # print(bugstate)
            bugs = [bugstate[i:i + 4] for i in range(0, len(bugstate), 4)]  #
            print(bugs)

            if next_table.string == '已关闭':
                self.new_bug_time(bugid)  # 新建bug日期
                self.closetime_isNot_detailed(bugstate,bugid)
            elif next_table.string == '持续跟踪':
                self.new_bug_time(bugid)
                if slove_isFind == False and close_isFind == False and revise_closedata_isFind == False :
                    value = self.wkdic[newkey]
                    value[1][2].append(bugid)
            else:
                print('【bug状态是】%s'%next_table.string)
                if slove_isFind == False and close_isFind == False and revise_closedata_isFind == False and close_common == False:
                    print('截止到目前还未处理的bug')
                    value = self.wkdic[newkey]
                    value[1][2].append(bugid)

        self.global_wkdic = self.wkdic
    # 为了循环下一个项目，清空数据表
    # for i in range(1, 53):
    #     key = 'wk{}'.format(i)
    #     # [0, 0, 0] = [新建bug总数，解决bug总数，关闭bug总数]
    #     wkdic.setdefault(key, [[0, 0, 0], [[], [], []]])  # [[新建],[解决和关闭],[截止到目前还未关闭的bug]]



if __name__ == '__main__':
    projectlist = ['E1 AL-LX110ST/AL-LW110ST','中器S1']

    t = Test()
    # t.open_browser()
    # t.login()
    # t.search_buglist(projectlist[0])
    # t.open_bugs()
    # print(t.global_wkdic)
    # t.driver.close()
    t.init_wkdic()
    with open('bug.html', mode='r', encoding='UTF-8') as f:
        try:
            t.html_parser(f, bugid = None)
        finally:
            f.close()