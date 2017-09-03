class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        res = self.current
        self.current += 1
        return res

class FileReader:
    def __init__(self, filename):
        self.f = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        s = self.f.readline()
        if s:
            return s
        else:
            raise StopIteration

if __name__ == "__main__":
    c = Counter(4, 10)

    for cnt in c:
        print(cnt)

    fr = FileReader('test.txt')
    print(next(fr), end = '')
    print(next(fr), end = '')
    print(next(fr), end = '')
    print(next(fr), end = '')

    
