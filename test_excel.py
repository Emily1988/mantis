import openpyxl

class Test:
    a = 0
    def aa(self):
        self.a = 1
        self.a = 5

    wkdic = {}

    def init_wkdic(self):
        for i in range(1, 53):
            key = 'wk{}'.format(i)
            # [0, 0, 0] = [新建bug总数，解决bug总数，关闭bug总数]
            # self.wkdic = {key: [[0, 0, 0], [[], [], []]]}
            # self.wkdic.update(self.wkdic)
            self.wkdic.setdefault(key, [[0, 0, 0], [[], [], []]])  # [[新建],[解决和关闭],[截止到目前还未关闭的bug]]
    # wkdic.clear()

        print(self.wkdic)

if __name__ == '__main__':
    # for i in range(3):

    t = Test()

    t.init_wkdic()
        # print(t.aa)