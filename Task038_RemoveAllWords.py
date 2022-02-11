# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".


text = 'Напишите програбвмму, удаляющую из текстабв все слова содержащие "абв". Или признайте, что она не работает)'
remove_word = 'абв'
print(text)


def Textprepare(input_text: str):
    res = ''
    for i in range(len(input_text)):
        if input_text[i] in ',.!?:;':
            res += '|' + input_text[i]
        elif input_text[i] == ' ':
            res += '| |'
        else:
            res += input_text[i]
    return res

def Remove_words(input_text: str, remove_word):
    if remove_word == '':
        return input_text
    else:
        line = input_text.split('|')
        for e in line:
            if remove_word in e:
                line[line.index(e)] = ''
        return "".join(line)

res_text = Textprepare(text)
res_text = Remove_words(res_text, remove_word)
print(res_text)
