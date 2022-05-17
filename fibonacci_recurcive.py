def input_str():
    return int(input())

def fibonacci_recurcive(limit_number, cur_list, cur_value):
    if cur_value <= limit_number:
        if cur_value <= 1:
            cur_list.append(1)
        else:    
            cur_list.append(cur_list[cur_value - 1] + cur_list[cur_value - 2])
        cur_value += 1
        fibonacci_recurcive(limit_number,cur_list, cur_value)
    else:
        print(cur_list[cur_value-1])
        return

if __name__ == '__main__':
    limit_number = input_str()
    cur_list = []
    cur_value = 0
    fibonacci_recurcive(limit_number, cur_list, cur_value)
