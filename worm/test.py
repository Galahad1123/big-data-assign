# coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import arange, meshgrid, sqrt, sin

# ax = plt.axes(projection='3d')
#
# x = arange(-5, 5, 0.1)
# y = arange(-5, 5, 0.1)
# x, y = meshgrid(x, y)
# R = sqrt(x ** 2 + y ** 2)
# z = sin(R)
#
# # ax.plot_surface(x, y, z)
# # ax.set_xlabel('X Axes')
# # ax.set_ylabel('Y Axes')
# # ax.set_zlabel('Z Axes')
# #
# # plt.show()
#
# print('x:')
# print(type(x))
# print('y:')
# print(type(y))
# print('z:')
# print(type(z))

# from openpyxl import load_workbook
#
# wb = load_workbook('Movie-Data2.xlsx')
# sheets = wb.worksheets  # 获取当前所有的sheet
# # print(sheets)
#
# # 获取第一张sheet
# sheet1 = sheets[0]
# # sheet1 = wb['Sheet']  # 也可以通过已知表名获取sheet
# print(sheet1)
#
# # 通过Cell对象读取
# cell_11 = sheet1.cell(1, 1).value
# print(cell_11)
# cell_11 = sheet1.cell(2, 2).value
# print(cell_11)
import csv

src_file = open('1000-Data2.csv', encoding='utf-8-sig')
reader = csv.reader(src_file)
print(next(reader))
