import datetime

#给定日期，返回对应当年第几周
def week_date(year,month,day):
    year = int(year)
    month = int(month)
    day = int(day)
    date = datetime.date(year,month,day).isocalendar()
    return date

def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates

def weekRang(beginDate, endDate):
    week = set()
    for date in dateRange(beginDate, endDate):
        week.add(datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10])).isocalendar()[0:2])

    wk_l = []
    for wl in sorted(list(week)):
        wk_l.append(str(wl[0]) + '#' + str(wl[1]))
    return wk_l

def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates

if __name__ == '__main__':
    # .strftime('%Y，%m,%d')
    # print(datetime.datetime.now())
    # t = datetime.datetime.now().isocalendar()
    # print(t)
    #

    #
    # print(time.strftime('%W')) #返回当前时间对应的周序号
    # print(datetime.date(2018,8,30).strftime('%W'))
    #
    # week_date(2017,2,7)
    # for week in weekRang('2017-01-08', '2018-01-01'):
    #     print(week)

    t1 = datetime.date(2016,1,4).isocalendar()
    print(t1)

    # for date in dateRange('2017-01-01', '2017-12-31'):
    #     print(date)