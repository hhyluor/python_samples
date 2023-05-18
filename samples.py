# -*- coding: utf-8 -*-
# @Time : 2023/4/24 21:37
# @Author : hehaiyang
# @File : samples.py
# @Project : python_samples
# @Function :

import pandas as pd


def HJ1():
    s = input()
    n = len(s.split("")[-1])
    print(n)


def HJ2():
    s1 = input()
    s1 = s1.upper()
    s2 = input()
    s2 = s2.upper()
    print(s1.count(s2))


def HJ3():
    n1 = int(input())
    a = []
    for i in range(n1):
        a.append(int(input()))
    b = list(set(a))
    b.sort()
    for i in b:
        print(i)


def HJ4():
    l = input()
    for i in range(0, len(l), 8):
        print("{0:0<8s}".format(l[i:i + 8]))


def HJ5():
    s1 = input()
    n = int(s1, 16)
    print(n)


def HJ6():
    n = int(input())
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    print(" ".join(str(factor) for factor in factors))


def HJ7():
    f = float(input())
    n = f - int(f)
    if n >= 0.5:
        print(int(f) + 1)
    else:
        print(int(f))


def HJ8():
    n = int(input())
    l1 = []
    for i in range(n):
        s_tmp = input()
        l1.append(s_tmp.split(" "))
    df = pd.DataFrame(l1)
    df_sum = df.groupby(0).sum()
    dict_tmp = df_sum.to_dict()
    for k, v in dict_tmp:
        print(k, v)
    print('dasd')


def HJ9():
    s = input()
    s = s[::-1]
    l1 = []
    for i in s:
        if i not in l1:
            l1.append(i)
    s2 = "".join(l1)
    print(s2)


def HJ10():
    s = input()
    unique_chars = set(s)
    count = 0
    for char in unique_chars:
        if ord(char) in range(128) and char != '\n':
            count += 1
    print(count)


def HJ11():
    s = input()
    print(s[::-1])


def HJ12():
    s = input()
    print(s[::-1])


def HJ13():
    s = input()
    s2 = s.split(" ")
    s3 = s2[::-1]
    s4 = " ".join(s3)
    print(s4)


def HJ14():
    n = int(input())
    l1 = []
    for i in range(n):
        l1.append(input())
    l1.sort()
    for i in l1:
        print(i)


def HJ15():
    n = int(input())
    count = bin(n).count("1")
    print(count)


def HJ17():
    s = input()
    l1 = s.split(";")
    l1 = [i for i in l1 if i != ""]
    l2 = []
    for i in l1:
        if i[0] in ["A", "S", "W", "D"] and i[1:].isdigit():
            l2.append(i)
    coordinate = [0, 0]
    for i in l2:
        s_tmp = i[0]
        if s_tmp == "A":
            coordinate[0] -= int(i[1:])
        elif s_tmp == "D":
            coordinate[0] += int(i[1:])
        elif s_tmp == "W":
            coordinate[1] += int(i[1:])
        elif s_tmp == "S":
            coordinate[1] -= int(i[1:])
    print("{0},{1}".format(coordinate[0], coordinate[1]))


def HJ20():
    s = input()
    if len(s) <= 8:
        return 0
    a, b, c, d = 0, 0, 0, 0
    for item in s:
        if ord('a') <= ord(item) <= ord('z'):
            a = 1
        elif ord('A') <= ord(item) <= ord('Z'):
            b = 1
        elif ord('0') <= ord(item) <= ord('9'):
            c = 1
        else:
            d = 1
    if a + b + c + d < 3:
        return 0
    for i in range(len(s) - 3):
        if len(s.split(s[i:i + 3])) >= 3:
            return 0
    return 1


def HJ21():
    s = input()
    l1 = []
    for i in s:
        if i in "abc":
            l1.append("2")
        elif i in "def":
            l1.append("3")
        elif i in "ghi":
            l1.append("4")
        elif i in "jkl":
            l1.append("5")
        elif i in "mno":
            l1.append("6")
        elif i in "pqrs":
            l1.append("7")
        elif i in "tuv":
            l1.append("8")
        elif i in "wxyz":
            l1.append("9")
        elif i.isupper():
            if ord(i) == 90:
                l1.append("a")
            else:
                l1.append(chr(ord(i) + 1).lower())
        else:
            l1.append(i)
    print(''.join(l1))


def HJ22():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            else:
                print(int(n / 2))
        except:
            break


def HJ23():
    s = input()
    dict_tmp = {}
    for i in s:
        dict_tmp[i] = dict_tmp.get(i, 0) + 1
    min = min(dict_tmp.values())
    l1 = []
    for i in s:
        if dict_tmp[i] != min:
            l1.append(i)
    s1 = "".join(l1)
    print(s1)


def HJ26():
    while True:
        try:
            s = input()
            a = ''
            for i in s:
                if i.isalpha():
                    a += i
            b = sorted(a, key=str.upper)
            index = 0
            d = ''
            for i in range(len(s)):
                if s[i].isalpha():
                    d += b[index]
                    index += 1
                else:
                    d += s[i]
            print(d)
        except:
            break


def HJ27():
    s = input()
    l1 = s.split(" ")
    x = l1[-2]
    k = int(l1[-1])
    l2 = l1[1:-2]
    l2 = [i for i in l2 if i != x]
    l3 = []
    for i in l2:
        if len(i) != len(x):
            continue
        if sorted(list(i)) == sorted(list(x)):
            l3.append(i)
    l3.sort()
    count = len(l3)
    print(count)
    if count >= k:
        print(l3[k - 1])


def HJ29():
    s1 = input()
    s2 = input()
    encrypted = []
    for char in s1:
        if char.isdigit():
            encrypted.append(str((int(char) + 1) % 10))
        elif char.isalpha():
            if char.islower():
                encrypted.append(chr(((ord(char) - ord('a') + 1) % 26) + ord('A')))
            else:
                encrypted.append(chr(((ord(char) - ord('A') + 1) % 26) + ord('a')))
        else:
            encrypted.append(char)

    decrypted = []
    for char in s2:
        if char.isdigit():
            decrypted.append(str((int(char) - 1) % 10))
        elif char.isalpha():
            if char.islower():
                decrypted.append(chr(((ord(char) - ord('a') - 1) % 26) + ord('A')))
            else:
                decrypted.append(chr(((ord(char) - ord('A') - 1) % 26) + ord('a')))
        else:
            decrypted.append(char)
    print(''.join(encrypted))
    print(''.join(decrypted))


# def HJ30():
#     ss = input()
#     s1 = ss.split(" ")[0]
#     s2 = ss.split(" ")[1]
#     s = s1 + s2
#     l1 = list(s[::2])
#     l2 = list(s[1::2])`
#     l1.sort()
#     l2.sort()
#     l3 = []
#     for i in range(len(l2)):
#         l3.append(l1[i])
#         l3.append(l2[i])
#     if len(l1) > len(l2):
#         l3.append(l1[-1])
#     s_tmp = ''.join(l3)
#     s_tmp = bin(int(s_tmp, 16))
#     s_tmp1 = s_tmp[2:][::-1]
#     s_tmp1 = s_tmp[:2] + s_tmp1
#     n = hex(int(s_tmp1, 2))
#     l_tmp = list(n[2:][::-1])
#     l_tmp = [i.upper() if i.isalpha() else i for i in l_tmp]
#     print(''.join(l_tmp))

def HJ31():
    ss = input()
    # 利用正则表达式将所有非字母字符替换为空格
    import re
    s = re.sub(r'[^a-zA-Z]+', ' ', ss)

    # 按空格将字符串拆分成单词列表，去掉空单词
    words = [w for w in s.split() if w]

    # 将单词列表反转，并按照要求用空格拼接成字符串
    print(' '.join(words[::-1]))


def HJ33():
    s1 = input()
    s2 = int(input())
    l1 = s1.split(".")
    l_ip = ["{0:0>8s}".format(bin(int(i))[2:]) for i in l1]
    ip = ''.join(l_ip)
    ip = int(ip, 2)
    print(ip)
    s2_b = bin(s2)[2:]
    n = len(s2_b)
    n1 = 8 - n % 8
    s2_b = "0" * n1 + s2_b
    n = n + n1
    s2_l = [s2_b[n - i - 8:n - i] for i in range(0, len(s2_b), 8)]
    s2_l = s2_l[::-1]
    s2_l = [str(int(i, 2)) for i in s2_l]
    ss = '.'.join(s2_l[-4:])
    print(ss)


def HJ34():
    s = input()
    # s = "Ihave1nose2hands10fingers"
    l1 = list(s)
    l1 = [ord(i) for i in l1]
    l1.sort()
    l1 = [chr(i) for i in l1]
    ss = ''.join(l1)
    print(ss)


def HJ35():
    n = int(input().strip())
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            # 输出的公式是转化后的，其实也可以写去括号前，int()的作用是将结果转化成整型，因为计算结果是有小数的，end = ' '作用是将内层循环的计算结果以空格隔开
            print(int(((j + j ** 2) / 2) - i + 1), end=' ')
        # 一次循环结束后打印空，用作换行
        print()


def HJ37():
    while True:
        try:
            month = int(input())
            n = month - 1

            def func(n):
                if n < 2:  # 基线条件
                    return 1
                else:  # 递归条件
                    return func(n - 1) + func(n - 2)

            print(func(n))
        except:
            break


def HJ38():
    while True:
        try:
            H1 = float(input())
            H2 = H1 / 2
            H3 = H2 / 2
            H4 = H3 / 2
            H5 = H4 / 2
            H6 = H5 / 2
            SUM_H = H1 + 2 * (H2 + H3 + H4 + H5)
            print(SUM_H)
            print(H6)
        except:
            break


def HJ40():
    while True:
        try:
            s = input()
            l = [0, 0, 0]
            for i in s:
                l[0] += int(i.isalpha())
                l[1] += int(i == ' ')
                l[2] += int(i.isnumeric())
            print(l[0])
            print(l[1])
            print(l[2])
            print(len(s) - l[0] - l[1] - l[2])
        except:
            break


def HJ41():
    while True:
        try:
            n = int(input())
            m = list(map(int, input().split()))
            x = list(map(int, input().split()))
        except:
            break
        else:
            amount = []
            weights = {0, }
            for i in range(n):
                for j in range(x[i]):
                    amount.append(m[i])

            for i in amount:
                for j in list(weights):
                    weights.add(i + j)
            print(len(weights))


def HJ45():
    while True:
        try:
            n = int(input())
            for i in range(n):
                each_name = input()
                beauty = 0

                # 字典放名字中每种字母对应出现到次数
                dict1 = {}
                for c in each_name:
                    dict1[c] = each_name.count(c)

                # 每种字母的出现次数从大到小排列
                times_list = sorted(dict1.values(), reverse=True)

                # 次数从大到小以此乘以26,25,24...
                for j in range(len(times_list)):
                    beauty += (26 - j) * times_list[j]
                print(beauty)

        except:
            break


def HJ46():
    while True:

        try:
            str_input = input()
            k = int(input())

            print(str_input[:k])

        except:
            break


def HJ50():
    s = input()
    s = s.replace("{", "(")
    s = s.replace("}", ")")
    s = s.replace("[", "(")
    s = s.replace("]", ")")
    print(int(eval(s)))


def HJ51():
    while True:
        try:
            count, num_list, k = int(input()), [int(x) for x in input().split()], int(input())
            print(num_list[-k] if k else 0)
        except EOFError:
            break


def HJ52():
    str1 = input()  # 等价于'oppa'
    str2 = input()  # 等价于'apple'

    # 构建bp表格,str1往str2编辑
    bp = [[x for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]
    # 现在bp表格中每一行的值为0、1、...len(str2)，其中第0行所有值是正确的
    # 现在要改变第0列的值为0、1、...len(str1)
    for w in range(1, len(str1)):
        bp[w][0] = bp[w - 1][0] + 1

    # 由于第0行和第0列均更新完成，现在要更新其他空格中的值
    for j in range(1, len(str1) + 1):  # 从第表格中的第1行第1列，即bp[1][1]处开始，遍历每一行str1:'oppa'
        for k in range(1, len(str2) + 1):  # 从第表格中的第1行第1列，即bp[1][1]处开始，遍历每一列
            if str1[j - 1] == str2[k - 1]:  # 当最后一个字符相同时，等价于没有改字符
                bp[j][k] = bp[j - 1][k - 1]
            elif str1[j - 1] != str2[k - 1]:  # 当最后一个字符不相同时，比较左、上、左上三个位置的值，+1后的找最小值，即最小编辑距离
                add = bp[j][k - 1] + 1
                delete = bp[j - 1][k] + 1
                replace = bp[j - 1][k - 1] + 1
                bp[j][k] = min(add, delete, replace)

    print(bp[len(str1)][len(str2)])


def HJ53():
    import sys
    alt = [2, 3, 2, 4]  # 发现规律，从第三行开始2324循环
    for line in sys.stdin:
        n = int(line.strip())
        if n < 3:
            print(-1)
        if n >= 3:
            print(alt[(n - 3) % 4])  # 所以对4求余，映射到上面alt列表中


def HJ54():
    while True:
        try:
            print(int(eval(input())))
        except:
            break


def HJ55():
    while True:
        try:
            n = int(input())
            c = 0
            for i in range(1, n + 1):
                if i % 7 == 0:
                    c += 1
                elif str(i).count('7') > 0:
                    c += 1
            print(c)
        except:
            break


def HJ56():
    while True:
        try:
            n = int(input())
            L = []
            for i in range(1, n):
                p = 0
                for y in range(1, i):
                    if i % y == 0:
                        p = p + y
                if i == p:
                    L.append(p)
            print(len(L))
        except:
            break


def HJ57():
    while True:
        try:
            n1 = int(input())
            n2 = int(input())
            print(n1 + n2)  # 直接输出整型数字相加之和的结果
        except:
            break


def HJ58():
    n, k = list(map(int, input().split()))
    num = list(map(int, input().split()))
    num = sorted(num)
    for i in num[:k]:
        print(i, end=' ')


def HJ59():
    while True:
        try:
            s = input()

            for i in s:
                if s.count(i) == 1:
                    print(i)
                    break
            else:
                print('-1')
        except:
            break


def HJ60():
    while True:
        try:
            n = int(input())
            prime = []
            for i in range(int(n / 2), 1, -1):
                for x in range(2, i):
                    if i % x == 0 or (n - i) % x == 0:
                        break
                else:
                    prime.append(i)
            print(prime[0])
            print(n - prime[0])
        except:
            break


def HJ61():
    '''
    放苹果分为两种情况，一种是有盘子为空，一种是每个盘子上都有苹果。
    令(m,n)表示将m个苹果放入n个盘子中的摆放方法总数。
    1.假设有一个盘子为空，则(m,n)问题转化为将m个苹果放在n-1个盘子上，即求得(m,n-1)即可
    2.假设所有盘子都装有苹果，则每个盘子上至少有一个苹果，即最多剩下m-n个苹果，问题转化为将m-n个苹果放到n个盘子上
    即求(m-n，n)
    '''

    def f(m, n):
        if m < 0 or n < 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        else:
            return f(m, n - 1) + f(m - n, n)

    while True:
        try:
            m, n = map(int, input().split())
            print(f(m, n))
        except:
            break


def HJ62():
    while True:
        try:
            n = int(input())
            count = 0
            while n:
                count += (n & 1)
                n >>= 1
            print(count)
        except:
            break


def HJ62():
    while True:
        try:
            n = int(input())
            count = 0
            while n:
                count += (n & 1)
                n >>= 1
            print(count)
        except:
            break


def HJ64():
    while True:
        try:
            n = int(input())  # 储存歌曲总数
            s = input().strip()  # 储存操作
            l = []
            for i in range(1, n + 1):  # 建立歌曲列表（非必要，我这里是为了统一输出，完全可以不用列表直接输出）
                l.append(i)
            # 关键变量
            f = 1  # f 用于指示当前页面第1首歌曲的索引位置，即应对问题 1
            p = 1  # p 用于指示当前页面光标所在位置，即应对问题 2 ，一页最多显示4首歌，所以 p 的取值范围在 1，2，3，4 之中

            if n < 5:  # 第一种情况，歌曲总数最多一页，没有翻页操作，比较简单，实现方法很多，这里不做介绍
                for i in s:
                    if i == 'U':
                        if p == 1:
                            p = n
                        else:
                            p -= 1
                    if i == 'D':
                        if p == n:
                            p = 1
                        else:
                            p += 1
            # 第二种情况，歌曲总数多于一页，有翻页操作，详见代码注释
            else:
                for i in s:  # 依次遍历操作
                    if i == 'U':  # 判断操作是否为 Up
                        if f == 1 and p == 1:  # 问题点3：特殊翻页处理；当且仅当，当前页面为歌曲1 2 3 4（f = 1）且光标位于位置 1（p = 1）时，从第一页翻到最后一页
                            f = n - 3  # 最后一页的4首歌为：n-3  n-2  n-1  n,因此 f = n-3
                            p = 4  # 特殊翻页过后，光标直接指向当前页面最后一首歌，即 p = 4
                        elif p == 1:  # 问题点3：一般翻页操作； 当光标位于当前页面第一首歌时，Up操作不会改变光标位置，即p=1不变，而向上翻页使得f = f-1
                            f -= 1
                        else:  # 问题点5：普通操作。当光标不在当前页面第一首歌时，Up操作只会改变光标位置（p = p-1），不会改变f
                            p -= 1
                    if i == 'D':  # Down 操作同理，理解特殊翻页，一般翻页 f 和 p的取值即变化，即可进行
                        if f == n - 3 and p == 4:
                            f = 1
                            p = 1
                        elif p == 4:
                            f += 1
                        else:
                            p += 1

            for i in l[f - 1:f + 4 - 1]:  # 输出当前页，列表索引从0开始，因此变量 f 需要减 1
                print(i, end=' ')
            print()
            print(f + p - 1)

        except:
            break


def HJ65():
    while True:  # 无限循环，直到遇到异常（没有输入）为止
        try:
            a, b = input(), input()  # 从输入中读取两个字符串，分别存储到变量 a 和 b 中

            # 交换 a 和 b，使得 a 总是比 b 短（或相等）
            if len(a) > len(b):
                a, b = b, a

            res = ''  # 用于存储最长公共子串的变量

            # 遍历短字符串 a 的所有子串
            for i in range(0, len(a)):
                for j in range(i + 1, len(a)):

                    # 检查子串 a[i:j+1] 是否在 b 中，并且子串长度大于当前的最长公共子串
                    if a[i:j + 1] in b and j + 1 - i > len(res):
                        res = a[i:j + 1]  # 更新最长公共子串

            print(res)  # 输出最长公共子串

        except:  # 如果遇到输入异常（没有输入），跳出循环
            break


def HJ67():
    def helper(arr, item):  # 先写一个利用递归+枚举解决算24的程序
        if item < 1:
            return False
        if len(arr) == 1:  # 递归终点，当数组arr只剩一个数的时候，判断是否等于item
            return arr[0] == item
        else:  # 如果arr不是只剩一个数，就调用函数本身（直到只剩一个为止返回真假）
            for i in range(len(arr)):
                m = arr[0:i] + arr[i + 1:]
                n = arr[i]
                if helper(m, item + n) or helper(m, item - n) or helper(m, item * n) or helper(m, item / n):
                    return True
            return False

    while True:
        try:
            if helper(list(map(int, input().split())), 24):
                print('true')
            else:
                print('false')
        except:
            break


def HJ68():
    while 1:
        try:
            n = int(input())
            if input() == "0":
                flag = True
            else:
                flag = False
            ls = []
            for i in range(n):
                name, score = input().split()
                ls.append((name, int(score)))
                ls.sort(key=lambda x: x[1], reverse=flag)
            for x in ls:
                print(*x)
        except:
            break


def HJ72():
    while True:
        try:
            a = input()
            for k in range(0, 4):
                x = 4 * k
                y = 25 - 7 * k
                z = 100 - x - y
                print('{} {} {}'.format(x, y, z))
        except:
            break


def HJ73():
    import datetime

    while True:
        try:
            y, m, d = map(int, input().split())
            d = datetime.date(y, m, d)  # 录入日期
            print(d.strftime("%j").lstrip("0"))  # 指定输出一年内的天数并且去掉左边的0
        except:
            break


def HJ74():
    while True:
        try:
            str1 = str(input())
            str1 = str1.replace(' ', '\n')
            e = ''
            flag = False
            for i in str1:
                if i == '"':  # 经过一次引号则拨动一次开关
                    flag = not flag
                elif flag == True and i == '\n':
                    e += ' '
                else:
                    e += i
            b = e.count('\n') + 1
            print(b)
            print(e)
        except:
            break


def HJ75():
    def solution(s1, s2):
        mxlen = 0
        if len(s1) > len(s2):
            s1, s2 = s2, s1  # s1为较短的字符串
        for i in range(len(s1)):
            for j in range(i, len(s1)):
                if s1[i:j + 1] in s2 and j + 1 - i > mxlen:  # 从s1中截取所有的子串在s2中进行匹配，并更新最大值
                    mxlen = j + 1 - i
        return mxlen

    while True:
        try:
            s1 = input()
            s2 = input()
            print(solution(s1, s2))
        except:
            break;


def HJ76():
    while True:
        try:
            m = int(input())
            l = [i for i in range(m * (m - 1) + 1, m * (m + 1)) if i % 2 != 0]
            print('+'.join(map(str, l)))
        except:
            break


def HJ80():
    while 1:
        try:
            s0, s1, s3, s2 = input(), input().split(), input(), input().split()
            s = map(str, sorted(map(int, set(s1 + s2))))
            print(''.join(s))
        except:
            break


def HJ81():
    while True:
        try:
            S, T = input(), input()
            if set(S) & set(T) == set(S):
                print('true')
            else:
                print('false')
        except:
            break


def HJ82():
    while True:
        try:
            a, b = map(int, input().split('/'))
            a = a * 10
            b = b * 10
            res = []
            while a:
                for i in range(a, 0, -1):
                    if (b % i == 0):
                        res.append('1' + '/' + str(int(b / i)))
                        a = a - i
                        break
            print('+'.join(res))
        except:
            break


def HJ84():
    while True:
        try:
            s = input()
            count = 0
            for i in s:
                if 'A' <= i <= 'Z':
                    count += 1
            print(count)
        except:
            break


def HJ85():
    while True:
        try:
            s = input()
            res = []

            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] == s[i:j][::-1]:
                        res.append(j - i)
            if res != '':
                print(max(res))
        except:
            break


def HJ86():
    while True:
        try:
            x = int(input())
            byte_x = bin(x)[2:]
            list1 = sorted(list(set(byte_x.split('0'))), key=lambda x: len(x), reverse=True)
            print(len(list1[0]))
        except:
            break


def HJ87():
    while True:
        try:
            s = input()
            sc = 0
            # 密码长度
            if len(s) <= 4:
                sc = sc + 5
            elif len(s) <= 7:
                sc = sc + 10
            else:
                sc = sc + 25

            # 字母
            isu = 0
            isl = 0
            for i in s:
                if i.isupper():
                    isu = 1
                    break
            for i in s:
                if i.islower():
                    isl = 1
                    break
            sc = sc + 10 * (isu + isl)

            # 数字
            shu = '0123456789'
            count1 = 0
            for i in s:
                if i in shu:
                    count1 = count1 + 1
            if count1 == 1:
                sc = sc + 10
            elif count1 > 1:
                sc = sc + 20
            else:
                sc = sc

            # 符号
            fh = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            count2 = 0
            for i in s:
                if i in fh:
                    count2 = count2 + 1
            if count2 == 1:
                sc = sc + 10
            elif count2 > 1:
                sc = sc + 25
            else:
                sc = sc

            # 奖励
            if isu + isl == 2 and count1 >= 1 and count2 >= 1:
                sc = sc + 5
            elif isu + isl > 1 and count1 >= 1 and count2 >= 1:
                sc = sc + 3
            elif isu + isl > 1 and count1 >= 1:
                sc = sc + 2
            if sc >= 90:
                print("VERY_SECURE")
            elif sc >= 80:
                print("SECURE")
            elif sc >= 70:
                print("VERY_STRONG")
            elif sc >= 60:
                print("STRONG")
            elif sc >= 50:
                print("AVERAGE")
            elif sc >= 25:
                print("WEAK")
            elif sc >= 0:
                print("VERY_WEAK")
        except:
            break

def HJ91():
    def func(x, y):
        if x < 0 or y < 0:
            return 0
        elif x == 0 or y == 0:
            return 1
        else:
            return func(x - 1, y) + func(x, y - 1)

    while True:
        try:
            a, b = map(int, input().split())
            c = func(a, b)
            print(c)
        except:
            break


if __name__ == '__main__':
    HJ50()
