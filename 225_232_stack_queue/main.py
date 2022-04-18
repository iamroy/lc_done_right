#225. Implement Stack using Queues
#232. Implement Queue using Stacks

class MyStack:
    def __init__(self):
        self.inbox = []
        self.outbox = []
        self.top_value = []

    def push(self, data):
        self.inbox.append(data)
        self.top_value = data

    def pop(self):
        if len(self.inbox):
            for i in range(len(self.inbox)-1):
                self.top_value = self.inbox[i]
                self.outbox.append(self.inbox[i])

            output = self.inbox[-1]
            self.inbox = self.outbox

            if len(self.inbox) == 0:
                self.top_value = []

            self.outbox = []
            return output

    def top(self):
        return self.top_value

    def empty(self):
        return len(self.inbox) == 0

class myQueue:
    def __init__(self):
        self.inbox = []
        self.outbox = []
        self.head_value = []

    def enqueue(self, data):
        self.inbox.append(data)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

        return self.outbox.pop()

    def peek(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

        return self.outbox[-1]

    def empty(self):
        return (len(self.inbox)+len(self.outbox)) == 0



if __name__ == '__main__':
    stack = MyStack()
    #stack.push(1)
    #stack.push(2)
    #stack.push(3)
    #stack.push(4)
    #print(stack.inbox)
    #print(stack.pop())
    #print(stack.top())
    #print(stack.inbox)
    #print(stack.pop())
    #print(stack.top())
    #print(stack.empty())

    queue = myQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.peek())
    print(queue.inbox, queue.outbox)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(4)
    print(queue.inbox, queue.outbox)
    #print(queue.dequeue())
    print(queue.peek())
    #print(queue.empty())

    #print(stack.inbox)
    #print(stack.pop())
    #print(stack.top())
    #print(stack.empty())