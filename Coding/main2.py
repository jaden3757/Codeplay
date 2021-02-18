# -*- coding: utf-8 -*-

# import loadingw
import pygame
import sys
from module1 import *
import openpyxl # pip install openpyxl 필수

wb = openpyxl.load_workbook('itemo.xlsx')
wb.save('item.xlsx')

from excel import *

item_t = [] #현재 내가 소지중인 아이템 목록 : main시트의 1번째 가로줄( 리스트 형태 )
item_t = getxllist('main', 1)
# item_s = {'손전등' : '길을 밝혀줍니다.', '보안키' : '보안실에서 사용 가능', '연구일지':'연구실에서 얻은 일지이다', '똥' : '푸짐하다'} # 아이템 관련 설명 (딕셔너리 형태)
# item_y = {'지도' : 10, '손전등' : 10, '창고열쇠' : 10, '보안키' : 10, '연구일지' : 20, '오징어 맛살' : 10, '똥' : 10, '500원' : 10, '마음' : 0, '밥' : 10, '갑오징어' : 50} # 아이템의 고유 값(무게)
item_s = {} # 아이템 관련 설명 (딕셔너리 형태) # items시트의 3번째 세로줄
item_y = {} # 아이템의 고유 값(무게) # items시트의 2번째 세로줄

i = 1
while getxl('items', 1, i) != None:
    item_s[getxl('items', 1, i)] = getxl('items', 3, i)
    item_y[getxl('items', 1, i)] = getxl('items', 2, i)
    i += 1

# 주의할 점 : 아이템을 추가할 때는 반드시 item_y 에 고유 값을 지정해줘야함

# ::::::::::::::

def getitem():
    # i = 0
    # itemlist = []
    # for key in item.keys():
    #     if item[key] == True:
    #         itemlist.append(key)
    #     i += 1
    # return itemlist
    return item_t

o = [0,0,0,0]

def changemap(a):
    if a == 0:
        import loadingw
    if a == 1:
        import sp2
    if a == 2:
        import sp3
    if a == 3:
        import story2

changemap(0)