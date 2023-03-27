class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # a list to be used as a map building to
        # the number of people in it currently
        building_people = [0] * n
        max_requests = 0
        
        def backtrack(index, curr_total_req):
            nonlocal max_requests
            
            if index == len(requests):
                # check if all buildings are balanced
                # i.e the net flow of people is 0 for all buildings
                if any(building_people):
                    return
                
                max_requests = max(max_requests, curr_total_req)
                return
            
            source, destination = requests[index]
            
            # pick index'th req
            building_people[source] -= 1
            building_people[destination] += 1
            
            backtrack(index + 1, curr_total_req + 1)
            
            # don't pick index'th req
            building_people[source] += 1
            building_people[destination] -= 1
            
            backtrack(index + 1, curr_total_req)
            
        backtrack(0, 0)
        
        return max_requests
            
            
        