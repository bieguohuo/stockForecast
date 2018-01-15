# -*- coding: UTF-8 -*-
import json


def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))


def load():
    global v
    with open('600000.json') as json_file:
        data = json.load(json_file)
        for (k, v) in data.items():
            # for i in v.items():
            # print(i)
            if k == 'mashData':
                # print v
                for i in v:
                    # print("序号：%s   值：%s" % (v.index(i) + 1, i))
                    for x, y in i.items():
                        if type(y) == list:
                            print('list:', x, ':', y)
                            for u in y:
                                for v, o in u.items():
                                    print(x, '-', v, ':', o)
                        elif type(y) == dict:
                            print('dict:', x, ':', y)
                            for z, w in y.items():
                                print(x, '-', z, ':', w)
                        else:
                            print(x, ':', y)
                            # print x,':',y
                            # print("data[%s]=" % k,v)
        return data


if __name__ == "__main__":
    data = {}
    data = load()
    # print(data)
