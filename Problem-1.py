class Calculator:
    def __init__(self,a,b,operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b != 0:
                return self.a / self.b
            return "Zero division error"
        else:
            return "invalid operation"
        

a = float(input("enter a: "))
b = float(input("enter b: "))
operation = input("select operation in (addition, subtraction, multiplication, division): ")
c1 = Calculator(a, b, operation)
print("the result:",c1.calculate())