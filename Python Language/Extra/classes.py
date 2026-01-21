class Pattern:
    def __init__(self, name):
      self.name = name
    def score(self, marks):
      self.marks = marks

h = Pattern("Ashutosh")
c = Pattern("Yash")
c.score(10)
print(c.marks)