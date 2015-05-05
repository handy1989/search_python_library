#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def PrintResult(results):
    print '''<?xml version="1.0"?>'''
    print "<items>"
    for item in results:
        title = item[0]
        link = "https://docs.python.org/2/library/" + item[1]
        print "    <item arg=\"" + link + "\">"
        print "        <title>" + title + "</title>"
        print "        <icon>python.jpg</icon>"
        print "    </item>"
    print "</items>"

def ReadDict(dict_name):
    dict_func2class = {}
    for line in open(dict_name):
        line = line.strip('\n')
        f = line.split('\t')
        if len(f) != 2:
            continue
        dict_func2class[f[1]] = f[0]

    return dict_func2class

def Search(query):
    dict_func2class = ReadDict("./class_and_functions.txt")
    results = []

    query = query.lower()

    # 先检查class，前缀匹配
    for value in dict_func2class.values():
        if value.lower() == query:
            results.append((value, value + '.html', 0))
        elif value.lower()[:len(query)] == query:
            results.append((value, value + '.html', 1))

    # 再检查function，前缀匹配
    for key in dict_func2class.keys():
        value = dict_func2class[key]
        if key.lower() == query:
            results.append((key, value + '.html#' + key, 2))
        elif key.lower()[:len(query)] == query:
            results.append((key, value + '.html#' + key, 3))
        elif key.lower().find(query) > 0:
            results.append((key, value + '.html#' + key, 4))

    # 去重
    results = list(set(results))
    results.sort(key=lambda x:(x[2], x[0]))
    PrintResult(results)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage:%s query' % sys.argv[0] 
        sys.exit(1)
    Search(sys.argv[1])

