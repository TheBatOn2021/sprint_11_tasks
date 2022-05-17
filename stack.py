class StackMax:
    def __init__(self):
        self.items = []
        self.max = None

    def print_get_max(self):
        print(self.max)

    def get_max(self):
        if len(self.items) > 0:
            self.max = max(self.items)
        else:
            self.max = None
        # print(self.items, ':', self.max)
    
    def push(self, item):
        self.items.append(item)
        self.get_max()

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
            self.get_max()
        else:
            print('error')

def main():
    queue = StackMax()
    commands = {
        'push': queue.push,
        'pop': queue.pop,
        'get_max': queue.print_get_max
    }
    count_command = int(input())
    for i in range(count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                commands[operation](int(*value))
            except:
                print('error')
        else:
            try:
                commands[operation]()
            except:
                print('error')


if __name__ == '__main__':
    main()
