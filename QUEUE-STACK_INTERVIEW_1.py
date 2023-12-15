class Stack:
    def __init__(self):
        self.list = [] #khởi tạo list
        self.MaxEle = None #khởi tạo giá trị lớn nhất
        
    def Push(self, value):  #hàm push có chức năng thêm phần tử vào trong list
        return self.list.append(value) #phương thức append cho phép thêm phần tử vào trong list theo LIFO
    
    def Pop(self): #hàm đẩy element được thêm vào gần nhất ra khỏi stack
        if len(self.list) > 0: #kiểm tra mảng có đủ điều kiện hay không
            return self.list.pop() #sử dụng phương thức pop để lấy phần tử gần nhất ra
        else:
            return -1        #nếu ban đầu mảng rỗng thì trả về -1
    
    def GetMax(self): #hàm lấy giá trị lớn nhất trong stack
        if len(self.list) > 0: #kiểm tra mảng có rỗng hay không, nếu không thì thực hiện bên dưới
            self.MaxEle = max(self.list) #gán giá trị lớn nhất bằng chính với giá trị max trong list
        else:
            return -1 #nếu điều kiện sai thì trả về -1
        return self.MaxEle #trả về giá trị lớn nhất của list
        
    

stack1 = Stack()
stack1.Push(5)
stack1.Push(6)
print(stack1.list)
print(stack1.GetMax())
stack1.Pop()
print(stack1.list)
print(stack1.GetMax())
stack1.Pop()
print(stack1.GetMax())












