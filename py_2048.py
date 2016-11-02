# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: py_2048.py
@time: 2016/11/2 14:29
"""
import random
import sys


def init():
    """初始化"""
    matrix = [0 for i in range(16)]
    # 随机生成2的倍数的数
    random_list = random.sample(range(16), 2)
    # 第一个和第二个初始化2
    matrix[random_list[0]] = matrix[random_list[1]] = 2
    return matrix


def move(matrix, direction):
    """移动方框"""
    mergedlist = []
    if direction == 'u':
        for i in range(16):
            j = i
            while j - 4 >= 0:
                if matrix[j - 4] == 0:
                    matrix[j - 4] = matrix[j]
                    matrix[j] = 0
                elif matrix[j - 4] == matrix[j] and j - 4 not in mergedlist and j not in mergedlist:
                    matrix[j - 4] *= 2
                    matrix[j] = 0
                    mergedlist.append(j - 4)
                    mergedlist.append(j)
                j -= 4
    elif direction == 'd':
        for i in range(15, -1, -1):
            j = i
            while j + 4 < 16:
                if matrix[j + 4] == 0:
                    matrix[j + 4] = matrix[j]
                    matrix[j] = 0
                elif matrix[j + 4] == matrix[j] and j + 4 not in mergedlist and j not in mergedlist:
                    matrix[j + 4] *= 2
                    matrix[j] = 0
                    mergedlist.append(i)
                    mergedlist.append(j + 4)
    elif direction == 'l':
        for i in range(16):
            j = i
            while j % 4 != 0:
                if matrix[j - 1] == 0:
                    matrix[j - 1] = matrix[j]
                    matrix[j] = 0
                elif matrix[j - 1] == matrix[j] and j - 1 not in mergedlist and j not in mergedlist:
                    matrix[j - 1] *= 2
                    matrix[j] = 0
                    mergedlist.append(j - 1)
                    mergedlist.append(j)
                j -= 1
    else:
        for i in range(15, -1, -1):
            j = i
            while j % 4 != 3:
                if matrix[j + 1] == 0:
                    matrix[j + 1] = matrix[j]
                    matrix[j] = 0
                elif matrix[j + 1] == matrix[j] and j + 1 not in mergedlist and j not in mergedlist:
                    matrix[j + 1] *= 2
                    matrix[j] = 0
                    mergedlist.append(j)
                    mergedlist.append(j + 1)
                j += 1
    print mergedlist
    return matrix


def insert(matrix):
    """插入2/4"""
    getZeroIndex = []
    for i in range(16):
        if matrix[i] == 0:
            getZeroIndex.append(i)
    randowZeroIndex = random.choice(getZeroIndex)
    matrix[randowZeroIndex] = 2
    return matrix


def output(matrix):
    """输出matrix"""
    max_num_width = len(str(max(matrix)))
    demarcation = ('+' + '-' * (max_num_width + 2)) * 4 + '+'
    print demarcation
    for i in range(len(matrix)):
        if matrix[i] == 0:
            printchar = ''
        else:
            printchar = str(matrix[i])
        print '|'
        print '{0:>{1}}'.format(printchar, max_num_width)
        if (i + 1) % 4 == 0:
            print '|'
            print demarcation


def isOver(matrix):
    """是否game over"""
    if 0 in matrix:
        return False
    else:
        for i in range(16):
            if i % 4 != 3:
                if matrix[i] == matrix[i + 1]:
                    return False
            if i < 12:
                if matrix[i] == matrix[i + 4]:
                    return False
    return True


def play():
    matrix = init()
    matrix_old = list(matrix)
    vim_mode = False
    vim_map = {'h':'l', 'j':'d', 'k':'u', 'l':'r'}
    step = 0
    while True:
        output(matrix)
        if not isOver(matrix):
            if max(matrix) == 2048:
                input = raw_input('输入q退出')
                if input == 'q':
                    exit()
            while True:
                prompt = "up/down/left/right"
                if vim_mode:
                    prompt = "h:left, jup/down/left/right"

                if vim_mode:
                    input = vim_map.get(input, input)

if __name__ == '__main__':
    play()

