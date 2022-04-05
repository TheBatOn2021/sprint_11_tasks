from collections import Counter


def hands_dex(k, matrix):
    cnt = Counter(matrix)
    cnt = list(cnt.values())
    new_cnt = [0 if value > k * 2 else 1 for value in cnt]
    return sum(new_cnt)


def read_input():
    k = int(input())
    matrix = []
    for i in range(4):
        matrix.append(input())
    matrix = "".join(map(str, matrix))
    matrix = "".join(c for c in matrix if c.isdecimal())
    return (k, matrix)


if __name__ == "__main__":
    k, matrix = read_input()
    print(hands_dex(k, matrix))
