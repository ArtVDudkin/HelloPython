# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

# x | y | ¬(X ⋁ Y)   | ¬X ⋀ ¬Y
# 0 | 0 | -(0+0) =1  | (1 * 1) =1
# 0 | 1 | -(0+1) =0  | (1 * 0) =0
# 1 | 0 | -(1+0) =0  | (0 * 1) =0
# 1 | 1 | -(1+1) =0  | (0 * 0) =0

def CheckTrue(x, y):
    flag_X = x == 1
    flag_Y = y == 1
    left = not (flag_X or flag_Y)
    right = (not flag_X) and (not flag_Y)
    if left == right:
        result = f'{x} | {y} | ¬({x} ⋁ {y}) = {left} ' + '\t' + \
            f' | ¬{x} ⋀ ¬{y} = {right} ' + '\t  ' + '| Истинно'
    else:
        result = f'{x} | {y} | ¬({x} ⋁ {y}) = {left} ' + '\t' + \
            f' | ¬{x} ⋀ ¬{y} = {right} ' + '\t  ' + '| Ложно'
    return result


for x in range(0, 2):
    for y in range(0, 2):
        print(CheckTrue(x, y))
