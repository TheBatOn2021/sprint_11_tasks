from msilib.schema import Error


class Deque:
    def __init__(self, max_size: int):
        self._max_size = max_size
        self._size = 0
        self._head = 0
        self._tail = max_size - 1
        self.head_block = []
        self.tail_block = []
        self.main = [None] * max_size

    def is_empty(self):
        return self._size == 0

    def idx(self, add=False):
        print(self.head_block, self.main, self.tail_block)
        # idx = idx + 1 if add else idx - 1
        # print(self._elements)p/';;
        try:
            self.main = self.head_block + self.main + self.tail_block
            # return idx % self._size
        except ZeroDivisionError:
            return idx

    def push_back(self, value: int):
        if self._size != self._max_size:
            self.tail_block.append(value)
            self._tail -= 1
            self.idx(False)
        else:
            print("error!")

    def push_front(self, value: int):
        if self._size != self._max_size:
            self.head_block.insert(0,value)
            self._head += 1
            self.idx(True)
        else:
            print("error!")

    def pop_back(self):
        # if self.is_empty():
        #     print("error!")
        # x = self._elements[self._tail - 1]
        # self._elements[self._tail - 1] = None
        # self.idx(self._tail)
        # self._size -= 1
        return x

    def pop_front(self):
        # if self.is_empty():
        #     print("error!")
        # x = self._elements[self._head]
        # self._elements[self._head] = None
        # self.idx(self._head, True)
        # self._size -= 1
        return x


def main():
    count_command = int(input())
    queue_size = int(input())

    queue = Deque(queue_size)
    commands = {
        'push_front': queue.push_front,
        'push_back': queue.push_back,
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back,
    }
    for i in range(count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                result = commands[operation](int(*value))
                if result is not None:
                    print(result)
            except Error:
                print('error')
        else:
            try:
                result = commands[operation]()
                print(result)
            except Error:
                print('error')


if __name__ == '__main__':
    main()
