import random

def gen(output="output/data.txt"):
    """
    Tạo bộ dữ liệu gồm 10 dãy
    mỗi dãy khoảng 1 triệu số thực (ngẫu nhiên)
    dãy thứ nhất đã có thứ tự tăng dần, dãy thứ sáu có thứ tự giảm dần, 
    5 dãy đầu số thực, 5 dãy sau số nguyên

    args:
        output là đường dẫn tới file data.txt
    """

    n = 10          # num of array
    length = 1e6   # number of element in each array
    MIN = -(2**31)
    MAX = 2**31 - 1

    with open(output, "w") as f:
        for i in range(n):
            if not i:                
                cur = random.uniform(MIN, MAX)
                for j in range(int(length)):
                    f.write(str(cur) + " ")
                    cur += random.random() * (MAX - MIN) / int(length)
                f.write("\n")

            elif i == 5:
                cur = random.randint(MIN, MAX)
                for j in range(int(length)):
                    f.write(str(cur) + " ")
                    cur -= random.randint(MIN, MAX)
                f.write("\n")

            elif i < 5:
                for j in range(int(length)):
                    f.write(str(random.random() * (MAX - MIN)) + " ")
                f.write("\n")

            else:
                for j in range(int(length)):
                    f.write(str(random.randint(MIN, MAX)) + " ")
                f.write("\n")

if __name__ == "__main__":
    gen()