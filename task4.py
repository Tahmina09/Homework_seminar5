# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = input()

def rle_encode(string):
    buff = ''
    data_list = []

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            buff += data[i - 1]
        else:
            buff += data[i - 1]
            data_list.append(buff)
            buff = ''
    else:
        data_list.append(buff)
    print(data_list)

    res = ''
    
    for i in range(len(data_list)):
        count = 0
        for j in data_list[i]:
            count += 1
        res = res + str(count) + j
    return res
        
print(rle_encode(data))



d = input()

def rle_decode(strn):
    s = ''
    d_list = []
    for i in range(len(d)):
        if d[i].isdigit():
            s += d[i]
        else:
            d_list.append((s))
            d_list.append(d[i])
            s = ''

    r = ''
    
    for i in range(len(d_list)):
        count = 0
        if d_list[i].isdecimal():
            count = int(d_list[i])
            for j in range(count):
                print(d_list[i + 1], end='')            

rle_decode(d)