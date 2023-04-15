class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.family_tree = defaultdict(list)
        self.family_tree[kingName]
        self.cemetery = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.family_tree[parentName].append(childName)                

    def death(self, name: str) -> None:
        self.cemetery.add(name)

    def getInheritanceOrder(self) -> List[str]:
        curr_order = []
        
        def dfs(person):
            if person not in self.cemetery:
                curr_order.append(person)
            
            for child in self.family_tree[person]:
                dfs(child)
                    
        dfs(self.kingName)
                    
        return curr_order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()