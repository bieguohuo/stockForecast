# -*- coding: UTF-8 -*-
import json

import xlwt


def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))


def writeExcelHeader():
    sheet1.write(0, 0, 'date')
    sheet1.write(0, 1, 'kline - open')
    sheet1.write(0, 2, 'kline - close')
    sheet1.write(0, 3, 'kline - low')
    sheet1.write(0, 4, 'kline - amount')
    sheet1.write(0, 5, 'kline - ccl')
    sheet1.write(0, 6, 'kline - high')
    sheet1.write(0, 7, 'kline - preClose')
    sheet1.write(0, 8, 'kline - volume')
    sheet1.write(0, 9, 'kline - netChangeRatio')
    sheet1.write(0, 10, 'ma5 - volume')
    sheet1.write(0, 11, 'ma5 - ccl')
    sheet1.write(0, 12, 'ma5 - avgPrice')
    sheet1.write(0, 13, 'ma10 - volume')
    sheet1.write(0, 14, 'ma10 - ccl')
    sheet1.write(0, 15, 'ma10 - avgPrice')
    sheet1.write(0, 16, 'ma20 - volume')
    sheet1.write(0, 17, 'ma20 - ccl')
    sheet1.write(0, 18, 'ma20 - avgPrice')
    sheet1.write(0, 19, 'macd - diff')
    sheet1.write(0, 20, 'macd - macd')
    sheet1.write(0, 21, 'macd - dea')
    sheet1.write(0, 22, 'kdj - k')
    sheet1.write(0, 23, 'kdj - j')
    sheet1.write(0, 24, 'kdj - d')
    sheet1.write(0, 25, 'rsi - rsi2')
    sheet1.write(0, 26, 'rsi - rsi3')
    sheet1.write(0, 27, 'rsi - rsi1')
    sheet1.write(0, 28, 'event - type')
    sheet1.write(0, 29, 'event - desc')


def load():
    global v
    with open('600000.json') as json_file:
        data = json.load(json_file)
        writeExcelHeader()
        for (k, v) in data.items():
            # for i in v.items():
            # print(i)
            if k == 'mashData':
                # print v
                for i in v:
                    # print("序号：%s   值：%s" % (v.index(i) + 1, i))
                    for x, y in i.items():
                        if type(y) == list:
                            print 'list:', x, ':', y
                            for u in y:
                                for a, o in u.items():
                                    print x, '-', v, ':', o
                                    if a == 'type':
                                        sheet1.write(v.index(i) + 1, 28, o)
                                    if a == 'desc':
                                        sheet1.write(v.index(i) + 1, 29, o)
                        elif type(y) == dict:
                            print 'dict:', x, ':', y
                            for z, w in y.items():
                                print x, '-', z, ':', w
                                if x == 'kline':
                                    if z == 'open':
                                        sheet1.write(v.index(i) + 1, 1, w)
                                    if z == 'close':
                                        sheet1.write(v.index(i) + 1, 2, w)
                                    if z == 'low':
                                        sheet1.write(v.index(i) + 1, 3, w)
                                    if z == 'amount':
                                        sheet1.write(v.index(i) + 1, 4, w)
                                    if z == 'ccl':
                                        sheet1.write(v.index(i) + 1, 5, w)
                                    if z == 'high':
                                        sheet1.write(v.index(i) + 1, 6, w)
                                    if z == 'preClose':
                                        sheet1.write(v.index(i) + 1, 7, w)
                                    if z == 'volume':
                                        sheet1.write(v.index(i) + 1, 8, w)
                                    if z == 'netChangeRatio':
                                        sheet1.write(v.index(i) + 1, 9, w)
                                if x == 'ma5':
                                    if z == 'volume':
                                        sheet1.write(v.index(i) + 1, 10, w)
                                    if z == 'ccl':
                                        sheet1.write(v.index(i) + 1, 11, w)
                                    if z == 'avgPrice':
                                        sheet1.write(v.index(i) + 1, 12, w)
                                if x == 'ma10':
                                    if z == 'volume':
                                        sheet1.write(v.index(i) + 1, 13, w)
                                    if z == 'ccl':
                                        sheet1.write(v.index(i) + 1, 14, w)
                                    if z == 'avgPrice':
                                        sheet1.write(v.index(i) + 1, 15, w)
                                if x == 'ma20':
                                    if z == 'volume':
                                        sheet1.write(v.index(i) + 1, 16, w)
                                    if z == 'ccl':
                                        sheet1.write(v.index(i) + 1, 17, w)
                                    if z == 'avgPrice':
                                        sheet1.write(v.index(i) + 1, 18, w)
                                if x == 'macd':
                                    if z == 'diff':
                                        sheet1.write(v.index(i) + 1, 19, w)
                                    if z == 'macd':
                                        sheet1.write(v.index(i) + 1, 20, w)
                                    if z == 'dea':
                                        sheet1.write(v.index(i) + 1, 21, w)
                                if x == 'kdj':
                                    if z == 'k':
                                        sheet1.write(v.index(i) + 1, 22, w)
                                    if z == 'j':
                                        sheet1.write(v.index(i) + 1, 23, w)
                                    if z == 'd':
                                        sheet1.write(v.index(i) + 1, 24, w)
                                if x == 'rsi':
                                    if z == 'rsi2':
                                        sheet1.write(v.index(i) + 1, 25, w)
                                    if z == 'rsi3':
                                        sheet1.write(v.index(i) + 1, 26, w)
                                    if z == 'rsi1':
                                        sheet1.write(v.index(i) + 1, 27, w)
                        else:
                            print x, ':', y
                            sheet1.write(v.index(i) + 1, 0, y)
                            # print x,':',y
                            # print("data[%s]=" % k,v)
        return data


if __name__ == "__main__":
    data = {}
    workbook = xlwt.Workbook()  # 注意Workbook的开头W要大写
    sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    data = load()
    workbook.save('E:\\600000.xls')
    # print(data)
