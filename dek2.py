class Dek:
    def __init__(self):
        self.items = [None]*self.max_size
        self.current_queue_size = 0
        self.max_index = self.max_size - 1
        self.head_write_index = 0
        self.head_read_index = 0
        self.tale_write_index = 0
        self.tale_read_index = 0

    def check_max_size(self):
        if (self.current_queue_size + 1 <= self.max_size):
            return True
        print('error')
        return False

    def check_min_size(self):
        if (self.current_queue_size > 0):
            return True
        print('error')
        return False

    def make_inc(self, index_item, value):
        if index_item + value > self.max_index:
            return (value + index_item - self.max_index) - 1
        return index_item + value

    def make_dec(self, index_item, value):
        if index_item - value < 0:
            return (self.max_index - value + index_item) + 1
        return index_item - value

    def push_back(self, item):
        self.items[self.tale_write_index] = item
        self.tale_read_index = self.tale_write_index
        self.tale_write_index = self.make_inc(self.tale_write_index, 1)
        self.current_queue_size += 1
        self.head_write_index = self.make_dec(self.tale_read_index, self.current_queue_size)

    def push_front(self, item):
        self.items[self.head_write_index] = item
        self.head_read_index = self.head_write_index
        self.head_write_index = self.make_dec(self.head_write_index, 1)
        self.current_queue_size += 1
        self.tale_write_index = self.make_inc(self.head_read_index, self.current_queue_size)

    def pop_back(self):
        print(self.items[self.tale_read_index])
        self.items[self.tale_read_index] = None
        self.tale_write_index = self.tale_read_index
        self.tale_read_index = self.make_dec(self.tale_read_index, 1)
        self.current_queue_size -= 1

    def pop_front(self):
        print(self.items[self.head_read_index])
        self.items[self.head_read_index] = None
        self.head_write_index = self.head_read_index
        self.head_read_index = self.make_inc(self.head_read_index, 1)
        self.current_queue_size -= 1


def main():
    Dek.count_command = int(input())
    Dek.max_size = int(input())
    queue = Dek()
    commands = {
        'push_front': queue.push_front,
        'push_back': queue.push_back,
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back
    }
    for i in range(Dek.count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                if queue.check_max_size():
                    commands[operation](int(*value))
            except:
                print('bad error')
        else:
            try:
                if queue.check_min_size():
                    commands[operation]()
            except:
                print('bad error')


if __name__ == '__main__':
    main()
