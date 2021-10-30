import sys
sys.stdin = open('input.txt','r')
num = {
    0 : 'A',
    1 : 'B',
    2 : 'C',
    3 : 'D',
    4 : 'E',
    5 : 'F',
    6 : 'G',
    7 : 'H',
    8 : 'I',
    9 : 'J',
    10 : 'K',
    11 : 'L',
    12 : 'M',
    13 : 'N',
    14 : 'O',
    15 : 'P',
    16 : 'Q',
    17 : 'R',
    18 : 'S',
    19 : 'T',
    20 : 'U',
    21 : 'V',
    22 : 'W',
    23 : 'X',
    24 : 'Y',
    25 : 'Z',
}
res = [0]*26
lst = input()
for i in range(len(lst)):
    if lst[i] == 'a' or lst[i] == 'A':
        res[0] += 1
    elif lst[i] == 'b' or lst[i] == 'B':
        res[1] += 1
    elif lst[i] == 'c' or lst[i] == 'C':
        res[2] += 1
    elif lst[i] == 'd' or lst[i] == 'D':
        res[3] += 1
    elif lst[i] == 'e' or lst[i] == 'E':
        res[4] += 1
    elif lst[i] == 'f' or lst[i] == 'F':
        res[5] += 1
    elif lst[i] == 'g' or lst[i] == 'G':
        res[6] += 1
    elif lst[i] == 'h' or lst[i] == 'H':
        res[7] += 1
    elif lst[i] == 'i' or lst[i] == 'I':
        res[8] += 1
    elif lst[i] == 'j' or lst[i] == 'J':
        res[9] += 1
    elif lst[i] == 'k' or lst[i] == 'K':
        res[10] += 1
    elif lst[i] == 'l' or lst[i] == 'L':
        res[11] += 1
    elif lst[i] == 'm' or lst[i] == 'M':
        res[12] += 1
    elif lst[i] == 'n' or lst[i] == 'N':
        res[13] += 1
    elif lst[i] == 'o' or lst[i] == 'O':
        res[14] += 1
    elif lst[i] == 'p' or lst[i] == 'P':
        res[15] += 1
    elif lst[i] == 'q' or lst[i] == 'Q':
        res[16] += 1
    elif lst[i] == 'r' or lst[i] == 'R':
        res[17] += 1
    elif lst[i] == 's' or lst[i] == 'S':
        res[18] += 1
    elif lst[i] == 't' or lst[i] == 'T':
        res[19] += 1
    elif lst[i] == 'u' or lst[i] == 'U':
        res[20] += 1
    elif lst[i] == 'v' or lst[i] == 'V':
        res[21] += 1
    elif lst[i] == 'w' or lst[i] == 'W':
        res[22] += 1
    elif lst[i] == 'x' or lst[i] == 'X':
        res[23] += 1
    elif lst[i] == 'y' or lst[i] == 'Y':
        res[24] += 1
    elif lst[i] == 'z' or lst[i] == 'Z':
        res[25] += 1
if res.count(max(res)) == 1:
    print(num[res.index(max(res))])
else:
    print('?')