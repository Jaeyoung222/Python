class Calculator:
    def __init__(self):
        #write your code below
        nums = 0
        boolean = 0
        save = 0
        self.nums = nums
        self.boolean = boolean
        self.save = save
        
    def digit(self,num):
        #write your code below
        self.nums = self.nums*10 + num
        
    def plus(self):
        #write your code below
        if self.boolean == False :
            self.save += self.nums
        else :
            self.save -= self.nums
        self.nums = 0
        self.boolean = False

    def minus(self):
        #write your code below
        if self.boolean == False :
            self.save += self.nums
        else :
            self.save -= self.nums
        self.nums = 0
        self.boolean = True


    def clear(self):
        #write your code below
        self.nums = 0
        self.save = 0
        self.boolean = 0

    def equal(self):
        #write your code below
        ans = 0
        if self.boolean == False :
            ans = self.save + self.nums
        else :
            ans = self.save - self.nums
        return print(ans)
            