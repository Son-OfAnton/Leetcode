class ListNode:
    def __init__(self, key: int = 0, val: int = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_capacity = 0
        self.DH = ListNode()    # Dummy head
        self.DT = ListNode()    # Dummy tail
        self.DH.next = self.DT
        self.DT.prev = self.DH
        self.table = dict()


    def insert_at_front(self, curr: ListNode) -> None:
        curr.prev = self.DH
        curr.next = self.DH.next
        self.DH.next.prev = curr
        self.DH.next = curr

    
    def remove(self, curr: ListNode) -> None:
        curr.prev.next = curr.next
        curr.next.prev = curr.prev


    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        
        curr = self.table[key]
        self.remove(curr)
        self.insert_at_front(curr)   

        return curr.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.table:
            new_node = ListNode(key, value)
            self.table[key] = new_node
            self.insert_at_front(new_node)
            self.curr_capacity += 1

            if self.curr_capacity > self.capacity:
                last = self.DT.prev

                # Evicting the Least Recently Used        
                self.table.pop(last.key)
                self.remove(last)
        else:
            curr = self.table[key]
            self.remove(curr)
            self.insert_at_front(curr)
            curr.val = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)