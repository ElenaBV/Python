# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Алгоритм RLE
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def code_file():
    text = "avvsssDdFFgggOOiiiaa"
    print(text)
    new_code_file = ''
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else :
            if count == 1:
                new_code_file += str(count) + text[i - 1]
            else:
                new_code_file += str(count) + text[i - 1]
                count = 1
    print (new_code_file)
    return new_code_file

def decode_file(new_code_file):
    new_decode_file = ''
    count = ''
    for i in new_code_file:
        if i.isdigit():
            count += i
        else :
            new_decode_file += int(count) * i
            count = ''
    print (new_decode_file)           
    return new_decode_file

decode_file(code_file())
