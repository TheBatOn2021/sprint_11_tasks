class MyQueueSized:
    def __init__(self):
        self.items = []
        self.current_queue_size = 0
        self.head = 0
        self.tale = 0

    def push(self, item):
        if self.current_queue_size < self.max_queue_size:
            self.items.append(item)
            self.current_queue_size += 1
            self.tale +=1
        else:
            print('error')

    def pop(self):
        if self.current_queue_size > 0:
            print(self.items[self.head])
            self.head += 1
            self.current_queue_size -= 1
            #self.items.pop()
        else:
            print('None')

    def peek(self):
        if self.current_queue_size > 0:
            print(self.items[self.head])
        else:
            print('None')

    def size(self):
        print(self.current_queue_size)

def main():
    MyQueueSized.count_command = int(input())
    MyQueueSized.max_queue_size = int(input())
    queue = MyQueueSized()
    commands = {
        'push': queue.push,
        'pop': queue.pop,
        'peek': queue.peek,
        'size': queue.size
    }
    for i in range(MyQueueSized.count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                commands[operation](int(*value))
            except:
                print('bad error')
        else:
            try:
                commands[operation]()
            except:
                print('bad error')


if __name__ == '__main__':
    main()
