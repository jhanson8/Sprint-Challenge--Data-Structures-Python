

class RingBuffer:
 
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity 
        self.head = 0
        
    

    def append(self, item):
        #if queue is full
        if len(self.queue) >= self.capacity:
            if self.head == self.capacity:
                #resets to zero
                self.head -= self.capacity
                #place new item at 0 index
                self.queue[self.head] = item 
                #increment by 1 so the new will replace oldest 
                self.head +=1
            else:
                self.queue[self.head] = item 
                self.head += 1
        else:    
           self.queue.append(item)
           self.head += 1
           
    

    def get(self):
        return self.queue