#Cách 2: Sử dụng phương pháp đệ quy.
class Queue:  
    def __init__(self):
        self.stack = []
  
    def enqueue(self, data): #hàm này dùng để thêm phần tử vào queue với độ phức tạp O(1)
        self.stack.append(data)
    
    def dequeue(self):

        if len(self.stack) == 1: #điều kiện để quét tới phần tử đầu tiên được thêm vào của stack
            return self.stack.pop() #trả về phần tử này.
        
        #thực hiện lấy item bằng cách pop từng thành phần của stack từ phần tử được thêm vào gần nhất
        item = self.stack.pop() 
        dequeued_item = self.dequeue()#thực hiện đệ quy cho hàm dequeued_item
        self.stack.append(item)#gán lại phần tử vừa pop vào trong stack
        return dequeued_item #trả về phần tử trong dequeued_item

queue = Queue()

queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(20)
print(queue.dequeue())
queue.enqueue(100)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

