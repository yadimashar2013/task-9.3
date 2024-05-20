class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.start, self.end = 8, 26
        return self

    def __next__(self):
        self.start += 2
        if self.start == self.end:
            raise StopIteration()
        return self.start


en = EvenNumbers(10, 25)
for i in en:
    print(i)
