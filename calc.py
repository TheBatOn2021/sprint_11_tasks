# Success Contest ID 67699928
def read_input():
    return input().split()


def calc(input_string):
    stek = []
    for i in input_string:
        if i not in '*-+/':
            stek.append(i)
        else:
            b = stek.pop(-1)
            a = stek.pop(-1)
            if i == '+':
                stek.append(int(a) + int(b))
            elif i == '-':
                stek.append(int(a) - int(b))
            elif i == '*':
                stek.append(int(a) * int(b))
            elif i == '/':
                stek.append(int(a) // int(b))
    return stek[-1]


if __name__ == "__main__":
    input_string = read_input()
    print(calc(input_string))
