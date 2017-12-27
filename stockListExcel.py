# -*- coding: UTF-8 -*-
import json

import xlwt


def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))


def writeExcelHeader(name):
    name.write(0, 0, 'date')
    name.write(0, 1, 'kline - open')
    name.write(0, 2, 'kline - close')
    name.write(0, 3, 'kline - low')
    name.write(0, 4, 'kline - amount')
    name.write(0, 5, 'kline - ccl')
    name.write(0, 6, 'kline - high')
    name.write(0, 7, 'kline - preClose')
    name.write(0, 8, 'kline - volume')
    name.write(0, 9, 'kline - netChangeRatio')
    name.write(0, 10, 'ma5 - volume')
    name.write(0, 11, 'ma5 - ccl')
    name.write(0, 12, 'ma5 - avgPrice')
    name.write(0, 13, 'ma10 - volume')
    name.write(0, 14, 'ma10 - ccl')
    name.write(0, 15, 'ma10 - avgPrice')
    name.write(0, 16, 'ma20 - volume')
    name.write(0, 17, 'ma20 - ccl')
    name.write(0, 18, 'ma20 - avgPrice')
    name.write(0, 19, 'macd - diff')
    name.write(0, 20, 'macd - macd')
    name.write(0, 21, 'macd - dea')
    name.write(0, 22, 'kdj - k')
    name.write(0, 23, 'kdj - j')
    name.write(0, 24, 'kdj - d')
    name.write(0, 25, 'rsi - rsi2')
    name.write(0, 26, 'rsi - rsi3')
    name.write(0, 27, 'rsi - rsi1')
    name.write(0, 28, 'event - type')
    name.write(0, 29, 'event - desc')


def load():
    global v
    for e in list:
        with open(e + '.json') as json_file:
            data = json.load(json_file)
            writeExcelHeader(sheet[list.index(e) + 1])
            for (k, v) in data.items():
                # for i in v.items():
                # print(i)
                if k == 'mashData':
                    # print v
                    for i in v:
                        # print("序号：%s   值：%s" % (v.index(i) + 1, i))
                        for x, y in i.items():
                            if x == 'event':
                                print 'list:', x, ':', y
                                for u in y:
                                    for a, o in u.items():
                                        print x, '-', v, ':', o
                                        if a == 'type':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 28, o)
                                        if a == 'desc':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 29, o)
                            elif type(y) == dict:
                                print 'dict:', x, ':', y
                                for z, w in y.items():
                                    print x, '-', z, ':', w
                                    if x == 'kline':
                                        if z == 'open':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 1, w)
                                        if z == 'close':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 2, w)
                                        if z == 'low':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 3, w)
                                        if z == 'amount':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 4, w)
                                        if z == 'ccl':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 5, w)
                                        if z == 'high':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 6, w)
                                        if z == 'preClose':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 7, w)
                                        if z == 'volume':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 8, w)
                                        if z == 'netChangeRatio':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 9, w)
                                    if x == 'ma5':
                                        if z == 'volume':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 10, w)
                                        if z == 'ccl':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 11, w)
                                        if z == 'avgPrice':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 12, w)
                                    if x == 'ma10':
                                        if z == 'volume':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 13, w)
                                        if z == 'ccl':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 14, w)
                                        if z == 'avgPrice':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 15, w)
                                    if x == 'ma20':
                                        if z == 'volume':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 16, w)
                                        if z == 'ccl':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 17, w)
                                        if z == 'avgPrice':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 18, w)
                                    if x == 'macd':
                                        if z == 'diff':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 19, w)
                                        if z == 'macd':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 20, w)
                                        if z == 'dea':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 21, w)
                                    if x == 'kdj':
                                        if z == 'k':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 22, w)
                                        if z == 'j':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 23, w)
                                        if z == 'd':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 24, w)
                                    if x == 'rsi':
                                        if z == 'rsi2':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 25, w)
                                        if z == 'rsi3':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 26, w)
                                        if z == 'rsi1':
                                            sheet[list.index(e) + 1].write(v.index(i) + 1, 27, w)
                            else:
                                print x, ':', y
                                sheet[list.index(e) + 1].write(v.index(i) + 1, 0, y)
                                # print x,':',y
                                # print("data[%s]=" % k,v)
                                # return data


if __name__ == "__main__":
    data = {}
    sheet = [50]
    list = ['600000', '600029', '600048', '600104',
            '600485',
            '600547',
            '600887',
            '600999',
            '601166',
            '601198',
            '601288',
            '601336',
            '601601',
            '601688',
            '601800',
            '601881',
            '601988',
            '600016',
            '600030',
            '600050',
            '600111',
            '600518',
            '600606',
            '600919',
            '601006',
            '601169',
            '601211',
            '601318',
            '601390',
            '601628',
            '601766',
            '601818',
            '601901',
            '601989',
            '600028',
            '600036',
            '600100',
            '600340',
            '600519',
            '600837',
            '600958',
            '601088',
            '601186',
            '601229',
            '601328',
            '601398',
            '601668',
            '601788',
            '601857',
            '601985']
    workbook = xlwt.Workbook()  # 注意Workbook的开头W要大写
    # sheet1= workbook.add_sheet('6000000', cell_overwrite_ok=True)
    for i in list:
        j = list.index(i)
        sheet.append(workbook.add_sheet(i, cell_overwrite_ok=True))
    data = load()
    workbook.save('E:\\stockList.xls')
    # print(data)
