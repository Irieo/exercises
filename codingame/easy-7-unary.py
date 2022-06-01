import sys
import math

answer = ''
binary = ''.join(f'{ord(c):07b}' for c in input())

def splitter(text):
    return (''.join(x + ('' if x == x2 else ' ') 
            for x, x2 in zip(text, text[1:] + text[-1])))

series = splitter(binary)
chunks = series.split()

for chunk in chunks:
    code = ''
    code += '0' if '1' in chunk else '00'
    answer += code + ' '
    answer += '0'*len(chunk) + ' '     

print(f'binary: {binary}',  file=sys.stderr)
print(f'series: {series}',  file=sys.stderr)
print(f'chunks: {chunks}',  file=sys.stderr)

print(answer[:-1])
