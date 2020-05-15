

class RingBuffer:
 
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity 
        self.head = 0
        
    

    def append(self, item):
        #if queue is full
        if len(self.queue) >= self.capacity:
            if self.head == self.capacity:
                self.head -= self.capacity
                self.queue[self.head] = item 
                self.head +=1
            else:
                self.queue[self.head] = item 
                self.head += 1
        else :    
            self.queue.append(item)
           
    

    def get(self):
        return self.queue