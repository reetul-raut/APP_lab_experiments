def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


class Report:
    def __init__(self, title):
        self.title = title

    @classmethod
    def create(cls, title):
        return cls(title)

    def __str__(self):
        return "Report: " + self.title

    @uppercase
    def generate(self):
        return "This is " + self.title



title = input("Enter report title: ")

report = Report.create(title)

print(report)
print(report.generate())