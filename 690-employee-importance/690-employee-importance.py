"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict()
        
        for employee in employees:
            graph[employee.id] = [employee.importance, employee.subordinates]
            
            
        def dfs(id):
            total_importance = graph[id][0]
            
            if not graph[id][1]:
                return total_importance
            
            for subordinate_id in graph[id][1]:                
                total_importance += dfs(subordinate_id)
                
            return total_importance
                
        return dfs(id)
    
    

        