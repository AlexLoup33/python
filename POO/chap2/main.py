#usr/bin/env python

class MyFirstClass:
    
    def __init__(self):
        test = 0
    
    def test(self):
        print("YO")

class Point():
    
    def move(self, x : int, y : int) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.x = 0
        self.y = 0
    
    def calculate_distance(self, other):
        return math.hypot(self.x - other.x, self.y - other)

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)

p1.reset()
p2.reset()

print(p1.x, p1.y)
print(p2.x, p2.y)

def main():
    a = MyFirstClass()
    print(a)
    a.test()

if __name__ == '__main__':
    main()