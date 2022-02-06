# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

# x | y | z | ¬(X ⋁ Y ⋁ Z)    | ¬X ⋀ ¬Y ⋀ ¬Z
# 0 | 0 | 0 | -(0 + 0 + 0) =1  | (1 * 1 * 1) =1
# 0 | 0 | 1 | -(0 + 0 + 1) =0  | (1 * 1 * 0) =0
# 0 | 1 | 0 | -(0 + 1 + 0) =0  | (1 * 0 * 1) =0
# 0 | 1 | 1 | -(0 + 1 + 1) =0  | (1 * 0 * 0) =0
# 1 | 0 | 0 | -(1 + 0 + 0) =0  | (0 * 1 * 1) =0
# 1 | 0 | 1 | -(1 + 0 + 1) =0  | (0 * 1 * 0) =0
# 1 | 1 | 0 | -(1 + 1 + 0) =0  | (0 * 0 * 1) =0
# 1 | 1 | 1 | -(1 + 1 + 1) =0  | (0 * 0 * 0) =0

def CheckTrue(x, y, z):
    flag_X = x == 1
    flag_Y = y == 1
    flag_Z = z == 1
    left = not (flag_X or flag_Y or flag_Z)
    right = (not flag_X) and (not flag_Y) and (not flag_Z)
    if left == right:
        result = f'{x} | {y} | {z} |¬({x} ⋁ {y} ⋁ {z}) = {left}  ' + '\t' + \
            f' | ¬{x} ⋀ ¬{y} ⋀ ¬{z}= {right} ' + '\t  ' + '| Истинно'
    else:
        result = f'{x} | {y} | {z} |¬({x} ⋁ {y} ⋁ {z}) = {left} ' + '\t' + \
            f' | ¬{x} ⋀ ¬{y} ⋀ ¬{z}= {right} ' + '\t  ' + '| Ложно'
    return result


for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(CheckTrue(x, y, z))
