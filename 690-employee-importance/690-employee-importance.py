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
            
        total_importance = graph[id][0]
        
        def dfs(id):
            nonlocal total_importance
            
            if not graph[id][1]:
                return
            
            for subordinate_id in graph[id][1]:
                total_importance += graph[subordinate_id][0]
                dfs(subordinate_id)
                
        dfs(id)
        return total_importance
    
    

        