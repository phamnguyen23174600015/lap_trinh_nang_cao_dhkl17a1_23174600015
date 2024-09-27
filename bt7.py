class Date():
    def __init__(self):
        self.day = int(input("Ngày: "))
        self.month = int(input("Tháng: "))
        self.year = int(input("Năm: "))

    def is_leap_year(self):
        return (self.year % 400 == 0) or (self.year % 100 != 0 and self.year % 4 == 0)

    def days_in_month(self):
        if self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        else:
            return 31

    def next(self):
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1
        self.display()

    def display(self):
        print("Ngày", self.day, "tháng", self.month, "năm", self.year)

vd = Date()   
vd.display()  
vd.next()     
  