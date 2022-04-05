from collections import Counter


def hands_dex(k, matrix):
    # Вот тут мы сделали "список частот"
    cnt = Counter(matrix)
    cnt = list(cnt.values())
    counter = 0
    [counter := counter + 1 for i in range(
        len(cnt)) if (cnt[i] > 0 and cnt[i] <= k * 2)]
    return counter


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
    # Ни одной ошибки линтеров flake8, pycodestyle, mypy нет
    print(hands_dex(k, matrix))
