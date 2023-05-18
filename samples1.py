# 在不使用系统自带深拷贝函数的前提下，请使用最高效、最通用的方式来编写算法实现对[1, 2, {'a': 3, 'b': [4, 5]}]的深拷贝

# def deep_copy(obj):
#     if isinstance(obj, list):
#         return [deep_copy(i) for i in obj]
#     elif isinstance(obj, dict):
#         return {k: v for k, v in obj.items()}
#     elif isinstance(obj, tuple):
#         return tuple(deep_copy(i) for i in obj)
#     else:
#         return obj


# 给一个字符串和一个二维码字符数组，如果该字符串存在于该数组中。则按字符串的字符顺序输出字符串每个字符所在单元格的位置下标字符串，
# 如果找不到返回字符串“N”
# 1.需要按照字符串的字符组成顺序搜索，且搜索到的位置必须是相邻单元格，其中“相邻单元格”是指那些水平相邻或垂直相邻的单元格。
# 2.同一个单元格内的字母不允许被重复使用。
# 3.假定在数组中最多只存在一个可能得匹配。
# 输入描述
# 1.第一行为一个数字（N）指示二维数组在后续输入所占的行数。
# 2.第2行到第N+1行输入为一个二维大写字符数组，每行字符用半角,分割。
# 3.第N+2行为待查找的字符串，由大写字符组成。
# 4.二维数组的大小为N*N，0＜N＜＝100。
# 5.单词长度k，0＜k＜1000。
# 输出描述：输出一个位置下标字符串，拼接格式为：
# 第1个字符行下标+“,”+第1个字符列下标+“,”+第2个字符行下标+“,”+第2个字符列下标......+“,”+第N个字符行下标+“,”+第N个字符列下标示例1：
# 输入4A,C,C,FC,D,E,DB,E,S,SF,E,C,AACCESS输出0,0,0,1,0,2,1,2,2,2,2,3

all_cases = [([['A', 'C', 'C', 'F'],
               ['C', 'D', 'E', 'D'],
               ['B', 'E', 'S', 'S'],
               ['F', 'E', 'C', 'A']],
              'ACCESS'),
             ([['C', 'C', 'C', 'F'], ['C', 'D', 'E', 'D'], ['B', 'E', 'S', 'S'], ['F', 'E', 'C', 'A']], 'ACCESS'),
             ([['A', 'S', 'C', 'F'], ['C', 'S', 'C', 'D'], ['B', 'E', 'C', 'S'], ['F', 'E', 'C', 'A']], 'ACCESS'), (
             [['C', 'C', 'C', 'F', 'k'], ['C', 'D', 'E', 'C', 'K'], ['B', 'M', 'F', 'O', 'D'],
              ['F', 'E', 'E', 'A', 'E'], ['F', 'F', 'B', 'B', 'E']], 'DECODE'), (
             [['C', 'C', 'C', 'F', 'k'], ['C', 'D', 'E', 'C', 'K'], ['B', 'M', 'D', 'O', 'D'],
              ['F', 'E', 'S', 'A', 'E'], ['F', 'F', 'B', 'B', 'E']], 'DECODE'), ]
def tmp(matrix,ss):
    # matrix = [['C', 'C', 'C', 'F'], ['C', 'D', 'E', 'D'], ['B', 'E', 'S', 'S'], ['F', 'E', 'C', 'A']]
    # ss = "ACCESS"
    n = len(matrix)


    def dfs(matrix, word, i, j, k, visited):  # 深度优先搜索的递归
        if k == len(word):  # 找到的长度等于字符的长度,且全为可行的
            return True, visited

        if 0 <= i < n and 0 <= j < n and not visited[i][j] and matrix[i][j] == word[k]:
            visited[i][j] = True
            direction_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 找相邻单元格
            for direction in direction_list:
                i_tmp, j_tmp = i + direction[0], j + direction[1]  # 相邻单元格
                found, path = dfs(matrix, word, i_tmp, j_tmp, k + 1, visited)
                if found:
                    return True, path
            else:
                visited[i][j] = False  # 标记此方向不可行
        return False, visited


    for i in range(n):
        for j in range(n):
            if matrix[i][j] == ss[0]:  # 找第一个字符位置的所有可能位置
                visited = [[False] * n for _ in range(n)]  # 路线二维表
                found, path = dfs(matrix, ss, i, j, 0, visited)
                if found:
                    res = []
                    for m in range(n):
                        for b in range(n):
                            if visited[m][b]:  # 标定可行位置
                                res.extend([m, b])
                    print(''.join(map(str, res)))

for s in all_cases:
    tmp(s[0],s[1])