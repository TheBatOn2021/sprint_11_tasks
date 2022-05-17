DICT = ["{}", "[]", "()"]

def read_input():
    return input()

def is_correct_bracket_seq(input_string, len_size):
    req = 0
    for i in DICT:
        if input_string.find(i) != -1:
            input_string = input_string.replace(i,'', 1)
            len_size -= 2
            req = 1
            print("@", i, "@", input_string, len_size, req)
    if len_size == 0:
        print('True')
        return
    else:
        if req == 1:
            is_correct_bracket_seq(input_string, len_size)
        else:
            print('False')
            return

if __name__ == "__main__":
    input_string = read_input()
    if len(input_string) % 2 != 0:
        print("False")
    else:
        len_size = len(input_string)
        is_correct_bracket_seq(input_string, len_size)
