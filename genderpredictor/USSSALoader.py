#!/usr/bin/env python
# encoding: utf-8
import os
import re
import urllib2
import csv
import pickle
from zipfile import ZipFile


def getNameList():
    if not os.path.exists('names.pickle'):
        print 'names.pickle does not exist, generating'
        if not os.path.exists('names.zip'):
            print 'names.zip does not exist, downloading from www.ssa.gov'
            downloadNames()
        else:
            print 'names.zip exists, not downloading'

        print 'Extracting names from names.zip'
        namesDict = extractNamesDict()

        maleNames = list()
        femaleNames = list()

        print 'Sorting Names'
        for name in namesDict:
            counts = namesDict[name]
            tuple = (name, counts[0], counts[1])
            if counts[0] > counts[1]:
                maleNames.append(tuple)
            elif counts[1] > counts[0]:
                femaleNames.append(tuple)

        names = (maleNames, femaleNames)

        print 'Saving names.pickle'
        fw = open('names.pickle', 'wb')
        pickle.dump(names, fw, -1)
        fw.close()
        print 'Saved names.pickle'
    else:
        print 'names.pickle exists, loading data'
        f = open('names.pickle', 'rb')
        names = pickle.load(f)
        print 'names.pickle loaded'

    print '%d male names loaded, %d female names loaded' % \
        (
            len(names[0]),
            len(names[1])
        )

    return names


def downloadNames():
    u = urllib2.urlopen('http://www.ssa.gov/oact/babynames/names.zip')
    localFile = open('names.zip', 'w')
    localFile.write(u.read())
    localFile.close()


def extractNamesDict():
    zf = ZipFile('names.zip', 'r')
    filenames = zf.namelist()

    names = dict()
    genderMap = {'M': 0, 'F': 1}

    for filename in filenames:
        if not '.txt' in filename:
            continue
        _file = zf.open(filename, 'rU', 'utf-16')
        rows = csv.reader(_file.read().splitlines(), delimiter=',')

        for row in rows:
            if len(row) < 3:
                continue
            name = row[0].upper()
            gender = genderMap[row[1]]
            count = int(row[2])

            if name not in names:
                names[name] = [0, 0]
            names[name][gender] = names[name][gender] + count

        _file.close()
        print '\tImported %s' % filename
    return names


if __name__ == '__main__':
    getNameList()
