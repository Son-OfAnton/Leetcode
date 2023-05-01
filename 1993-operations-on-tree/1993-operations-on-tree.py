class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        self.lock_history = [None] * len(parent)

        for child, p in enumerate(parent):
            self.graph[p].append(child)

    def lock(self, num: int, user: int) -> bool:
        if self.lock_history[num] == None:
            self.lock_history[num] = user
            return True
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.lock_history[num] == user:
            self.lock_history[num] = None
            return True
        return False


    def locked_ancestor_exists(self, node: int) -> bool:
        if self.lock_history[node] != None:
            return True
        if self.parent[node] != -1:
            return self.locked_ancestor_exists(self.parent[node])

        return False

    def locked_descendant_exists(self, node: int) -> bool:
        if self.lock_history[node] != None:
            return True

        for child in self.graph[node]:
            if self.locked_descendant_exists(child):
                return True  

        return False

    def unlock_descendants(self, node: int) -> None:
        self.lock_history[node] = None
        for child in self.graph[node]:
            self.unlock_descendants(child)

    def upgrade(self, num: int, user: int) -> bool:
        if self.lock_history[num] != None:
            return False
        
        flag = False
        for child in self.graph[num]:
            if self.locked_descendant_exists(child):
                flag = True
                break
        
        if not flag:
            return False

        if self.parent[num] != -1 and self.locked_ancestor_exists(self.parent[num]):
            return False

        self.unlock_descendants(num)
        self.lock_history[num] = user

        return True


        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)