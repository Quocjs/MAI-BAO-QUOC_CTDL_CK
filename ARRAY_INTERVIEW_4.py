def Check_Anagram(string1, string2):
    count = 0 #đặt biến đếm
    if len(string1) != len(string2): #xem xét chiều dài của 2 word: vì nếu khác nhau thì không cần kiểm tra
        return False #trả về False nếu sai
    else:
        for i in range(len(string1)): #đặt biến chạy cho string1
            for j in range(len(string2)): #đặt biến chạy cho string2
                if string2[j] == string1[i]: #nếu biến chạy của string2 giống với biến chạy string1
                    count = count+1 #thì tăng đếm lên 1
        if count != len(string1): #vì các chữ chỉ được xuất hiện 1 lần nên count phải = với chiều dài string
            return False #nếu điều kiện đúng thì trả về False
        return True #nếu điều kiện không đúng thì trả về True
    
a = "restful" #chuỗi cần kiểm tra
b = "flusret" #chuỗi cần kiểm tra 
print(Check_Anagram(a, b)) #In ra kết quả kiểm tra của 2 chuỗi đã cho 





