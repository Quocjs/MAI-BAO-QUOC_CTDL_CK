#Cách 1: Sử dụng 2 Stack
class Queue:
    def __init__(self):
        self.enqueue_stack = [] #sử dụng stack cho enqueue
        self.dequeue_stack = [] #sử dụng stack cho dequeue
    
    def enqueue(self, data): #thêm một phần tử vào queue với độ phức tạp của thuật toán là O(1)
        self.enqueue_stack.append(data)
    
    def dequeue(self):

        #Lập điều kiện cho trường hợp trong stack rỗng
        if len(self.enqueue_stack)==0 and len(self.dequeue_stack) == 0:
            raise Exception("Stack is empty")
        
        #Điều kiện khi bên trong dequeue_stack là rỗng, thì ta cần thêm 1 phần tử với độ phức tạp là O(N)
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        #ngoài điều kiện trên thì ta chỉ cần dùng hàm pop để để đẩy đi 1 phần tử với độ phức tạp chỉ là O(1)
        return self.dequeue_stack.pop()

queue = Queue()

queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(20)
print(queue.dequeue())
queue.enqueue(100)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())


