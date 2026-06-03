# 리스트 클래스 구현 및 테스트
class Arraylist:
    def __init__(self, max_size = 10):
        '''self.items =[]
        self.max_size = 10
        self.size = 0 '''
        self.max_size =max_size
        self.items = [None] * self.max_size
        self.size = 0


    def insert(self, pos, e):
        if self.isFull():
            print('포화상태')
            return
        for i in range(self.size, pos, -1):
            self.items[i] = self.items[i-1]
        self.items[pos] = e
        self.size += 1

    def delete(self,pos):
        '''return self.items.pop(pos)'''
        value =self.items[pos]
        for i in range(pos, self.size -1):
            self.items[i] = self.items[i+1]
        self.size -= 1
        return value

    def isEmpty(self):
        '''return len (self.items) == 0 '''
        return self.size == 0

    def isFull(self):
        '''return len(self.items) == self.max_size'''
        return self.size == self.max_size


    def getEntry(self, pos):
        return self.items[pos]

    def Size(self): 
        return self.size
        '''return len(self.items)'''
    
    def Clear(self):
        '''self.items = []'''
        self.items = [None] * self.max_size
        self.size = 0

    def Find(self, item):
        '''return self.items.index(item)'''
        for i in range(self.size):
            if self.items[i] == item:
                return i
        return -1

    def Replace(self,pos,item):
        self.items[pos] = item

    def Sort(self):
        '''self.items.sort()'''
        for i in range(self.size-1):
            for j in range(i+1, self.size):

                if self.items[i] > self.items[j]:
                    temp = self.items[i]
                    self.items[i] = self.items[j]
                    self.items[j] = temp

    def Merge(self,list):
        self.items.extend(list)


    def Display(self, msg = 'Arraylist: '):
        print(msg, '개수= ',self.size)
        for i in range(self.size):
            print(self.items[i], end = ' ' )
        print()

    def Append(self,e):
        '''self.items.append(e)'''
        if self.isFull():
            print('포화상태')
            return

        self.items[self.size] = e
        self.size += 1

        

s = Arraylist(10)
s.Display('리스트로 구현한 Arraylist 테스트')

s.insert(0, 70)
s.insert(1, 20)
s.insert(1, 15)
s.insert(s.Size(), 25)
s.insert(2, 50)
s.Display('새로운 요소 삽입 후 리스트 내용: ')

s.insert(3, 10)
s.Display('추가 삽입 후 리스트 내용: ')

s.Sort()
s.Display('정렬한 리스트 내용: ')


s.delete(2) 
s.Display('삭제(인덱스 2) 후 리스트 내용: ')


s.Replace(2, 30)
s.Display('교체(인덱스 2를 30으로) 후 리스트 내용: ')

s.Display('최종 리스트 내용: ')








