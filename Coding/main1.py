# -*- coding: utf-8 -*-

# import loadingw
import pygame
import sys
from module1 import *

item = {'손전등' : False, '창고열쇠' : True, '보안키' : True, '연구일지' : True, '오징어 맛살' : True, '똥' : True, '500원' : True}
item['손전등'] = True

item_t = ['지도', '손전등', '창고열쇠', '보안키', '연구일지', '오징어 맛살', '똥', '500원'] #현재 내가 소지중인 아이템 목록 ( 리스트 형태 )
item_s = {'손전등' : '길을 밝혀줍니다.', '보안키' : '보안실에서 사용 가능', '연구일지':'연구실에서 얻은 일지이다', '똥' : '푸짐하다'} # 아이템 관련 설명 (딕셔너리 형태)
item_y = {'지도' : 10, '손전등' : 10, '창고열쇠' : 10, '보안키' : 10, '연구일지' : 20, '오징어 맛살' : 10, '똥' : 10, '500원' : 10, '마음' : 0, '밥' : 10, '갑오징어' : 50} # 아이템의 고유 값(무게)

# 주의할 점 : 아이템을 추가할 때는 반드시 item_y 에 고유 값을 지정해줘야함

def getitem():
    # i = 0
    # itemlist = []
    # for key in item.keys():
    #     if item[key] == True:
    #         itemlist.append(key)
    #     i += 1
    # return itemlist
    return item_t
         
def changemap(a):
    if a == 0:
        import loadingw
    if a == 1:
        import sp2
    if a == 2:
        import story
    
changemap(0)