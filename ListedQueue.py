class MyQueueSized:
    def __init__(self):
        self.items = []
        self.current_queue_size = 0
        self.head = 0
        self.tale = 0

    def put(self, item):
        if self.current_queue_size >= 0:
            self.items.append(item)
            self.current_queue_size += 1
            self.tale +=1
        else:
            print('error')

    def get(self):
        if self.current_queue_size > 0:
            print(self.items[self.head])
            self.head += 1
            self.current_queue_size -= 1
            #self.items.pop()
        else:
            print('error')

    def size(self):
        print(self.current_queue_size)

def main():
    MyQueueSized.count_command = int(input())
    queue = MyQueueSized()
    commands = {
        'put': queue.put,
        'get': queue.get,
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
