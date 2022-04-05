def read_input():
    num = int(input())
    plots = [c for c in input().split()]
    return num, plots


def nearest_zero(num: int, plots: list):
    free_plot = (num * -1)-1
    left_plot = [0] * num
    min_dist = [0] * num
    for count, value in enumerate(plots):
        if value == '0':
            free_plot = count
        else:
            left_plot[count] = count - free_plot
    free_plot = float("inf")
    for count, value in reversed(list(enumerate(plots))):
        if value == '0':
            free_plot = count
        else:
            min_dist[count] = min(free_plot - count, left_plot[count])
    return min_dist


if __name__ == "__main__":
    num, plots = read_input()
    print(*nearest_zero(num, plots))
