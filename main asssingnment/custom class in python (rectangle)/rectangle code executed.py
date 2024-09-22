class Rectangle:
    def __init__(self):
        self.length=int(input('enter length :'))
        self.width=int(input('enter width :'))
        #self.length=length
        #self.width=width
    def __iter__(self):
        if self.length and self.width>0:
            yield {'length':self.length,'width':self.width,'area':self.length*self.width}
        else:
            yield "enter valid input"
rect=Rectangle()
for attr in rect:
    print(attr)
