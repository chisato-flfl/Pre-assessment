class MultiplicationTable:
    @classmethod
    def generate(cls, n=12):
        for i in range(1, n+1):
            row = [i * j for j in range(1, n+1)]
            print(" ".join(map(str, row)))

# 使用例
MultiplicationTable.generate()