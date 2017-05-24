# -*- coding: utf-8 -*-

from os import path
import numpy
import csv
import glob
#                  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
categoryList17 = [ 0, 1, 4, 5, 7, 6, 2, 4, 2, 6, 2, 7, 1, 5, 2, 6, 2, 4, 1, 3, 4, 7, 7, 3, 7, 2, 1, 3, 5, 2, 1, 5, 4, 7, 4, 2, 5, 4, 3, 7, 3]
colorList17 =    [ 0, 1, 4, 5, 1, 9, 5, 2, 9, 4, 2, 4, 3, 4, 3, 1, 7, 6, 4, 6, 8, 4, 8, 8, 9, 2, 1, 4, 3, 3, 1, 1, 4, 1, 1, 3, 1, 1, 5, 7, 2]

#                  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39
categoryList16 = [ 0, 1, 7, 7, 7, 3, 7, 4, 3, 2, 4, 5, 7, 1, 3, 2, 7, 7, 4, 4, 7, 5, 1, 1, 2, 2, 5, 3, 2, 7, 5, 5, 7, 7, 6, 7, 6, 3, 6, 6]
colorList16 =    [ 0, 1, 1, 2, 1, 8, 3, 7, 4, 5, 1, 1, 9, 2, 4, 9, 5, 1, 6, 1, 1, 1, 4, 7, 7, 1, 1, 6, 3, 5, 1, 9, 4, 5, 5, 3, 3, 1, 4, 4]

#                  0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25
categoryList15 = [ 0, 5, 2, 2, 2, 5, 2, 6, 5, 6, 5, 2, 2, 4, 7, 5, 3, 5, 5, 1, 7, 7, 7, 7, 7, 1]
colorList15 =    [ 0, 2, 4, 2, 4, 5, 5, 1, 9, 5, 8, 4, 2, 5, 1, 4, 6, 9, 1, 1, 9, 3, 4, 1, 5, 4]

"""
categoryList
1: Book
2: Box
3: Cylinder
4: Deformable
5: Wrapped
6: Clamshell
7: Other

colorList
1: White
2: Blue
3: Green
4: Red
5: Yellow
6: Black
7: Sky Blue
8: Clear
9: Any Colors
"""

#テキストファイルを読んでコンマでセパレート
def readTxt(filePath):
    coordinate = []
    f = open(filePath, 'r')

    if f != None:
        for row in f:
            data = row.split()
            coordinate.append(data)
        f.close()
        return coordinate
    else:
        print("テキストファイルが読めません")
        return 1

#テキストファイル保存
def saveTxt(filePath, data):
    f = open(filePath, 'w')
    for i in range(len(data)):
        f.write(str(data[i][0]) + " " + str(data[i][1]) + " " + str(data[i][2]) + " " + str(data[i][3]) + " " + str(data[i][4]) +  " " + str(data[i][5]) +  " " + str(data[i][6]) + "\n")
    f.close()
    print(filePath + "に保存しました")
    return 0

if __name__ == "__main__":
    #変換前ラベル
    inDir = "/Users/ryorsk/Documents/ARC2017/MELFA_Data/label/multiitem/"
    #変換後ラベル
    outDir = "/Users/ryorsk/Documents/ARC2017/MELFA_Data/label_cat/2016-multiitem/"



    labelList = glob.glob(inDir + "*.txt")
    labelList.sort()

    for labelPath in labelList:
        print("Processing:" + labelPath)
        writeData = []
        coordinate = readTxt(labelPath)
        for i in range(len(coordinate)):
            if(len(coordinate[i][0])>=4):
                year = int(coordinate[i][0][0:2])
            else:
                year = 17

            ub = coordinate[i][0].rfind('_') # アンダーバーの位置
            if year == 17:
                category = categoryList17[int(coordinate[i][0])]
                color = colorList17[int(coordinate[i][0])]
            elif year == 16:
                category = categoryList16[int(coordinate[i][0][ub+1:])]
                color = colorList16[int(coordinate[i][0][ub+1:])]
            elif year == 15:
                category = categoryList15[int(coordinate[i][0][ub+1:])]
                color = colorList15[int(coordinate[i][0][ub+1:])]
            else:
                print("[Error] Unexpected ID")
                exit()

            writeData.append([coordinate[i][0], category, color, coordinate[i][1], coordinate[i][2], coordinate[i][3], coordinate[i][4]])
        saveTxt(outDir + labelPath[labelPath.rfind('/'):], writeData)
