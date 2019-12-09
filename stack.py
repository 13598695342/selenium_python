class Dqueue():
    '''双端队列'''
    def __init__(self):
        self.__list = []
    def add_front(self,item):
        '''头部添加'''
        self.__list.insert(0,item)
    def add_rear(self,item):
        '''尾部添加'''
        self.__list.append(item)
    def pop_rear(self):
        '''尾部取'''
        return self.__list.pop(0)
    def is_empty(self):
        '''判断一个队列是否为空'''
        return self.__list == []
    def size(self):
        '''返回队列大小'''
        return len(self.__list)
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())