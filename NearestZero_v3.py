def read_input():
    num = int(input())
    plots = [int(c) for c in input().split()]
    return num, plots


def nearest_zero(num, plots):
    free_plot = (num * -1)-1
    left_plot = [0] * num
    min_dist = [0] * num
    for i in range(num):
        if plots[i] == 0:
            free_plot = i
        else:
            left_plot[i] = i - free_plot
    free_plot = num + float("inf")
    for i in range(num-1, -1, -1):
        if plots[i] == 0:
            free_plot = i
        else:
            min_dist[i] = min(free_plot - i, left_plot[i])
    return (min_dist)


if __name__ == "__main__":
    num, plots = read_input()
    print(*nearest_zero(num, plots))
