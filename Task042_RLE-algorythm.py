# 42. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#     a) входные и выходные данные хранятся в отдельных файлах

############  Блок восстановления данных  #############

def Unpack_block(letter, mult):
    return letter * mult


def RLE_decoder(input_data: str):
    res = ''
    while input_data != ' ':
        letter = input_data[0]
        input_data = input_data[1:]
        next_pos = 0
        for i in range(len(input_data)):
            if input_data[i].isalpha() or input_data[i].isspace():
                next_pos = i
                break
        mult = int(input_data[:next_pos])
        res += Unpack_block(letter, mult)
        input_data = input_data[next_pos:]
    return res


with open('Task042_DecoderInput.txt', 'r') as data:
    line = data.readline() + ' '

print(line)
out_data = RLE_decoder(line)
print(out_data)

with open('Task042_DecoderOutput.txt', 'w') as data:
    data.write(out_data)

############  Блок сжатия данных  #############
# MMMMMMMMMMBBBBBBBBBBBPPPPPPPPPPPPPPzzzzzjjjrrrrrrrvvvvvvvvvvvvvvvvvvvvoooooooooooooooooCCCCCCCCCCCCCCCCCCCmmmmmmmmmmmmmmmmmmmmYYYYYYYpppppppppppppppppppTTTTTTTTTTTTTTTTRRRRAAAAAAAAAZZZZZZZZZZZZZZZZmmmmmmmmmMMMMMMMMIIfffffffffffnnnnnnnnnnnnnnOOOOOOOsssssssssOOOOTTTTTTTTTTTTTTTTTTPPPPPPjkkkkkk
def RLE_encoder(input_data: str):
    res = ''
    while input_data != ' ':
        letter = input_data[0]
        next_pos = 0
        for i in range(len(input_data)):
            if input_data[i] != letter or input_data[i].isspace():
                next_pos = i
                break
        mult = next_pos
        res += f'{letter}{mult}'
        input_data = input_data[next_pos:]
    return res


with open('Task042_EncoderInput.txt', 'r') as data:
    line = data.readline() + ' '

print(line)
out_data = RLE_encoder(line)
print(out_data)

with open('Task042_EncoderOutput.txt', 'w') as data:
    data.write(out_data)
