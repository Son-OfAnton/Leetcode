class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = [(position[i], speed[i]) for i in range(len(speed))]
        pos_speed.sort(reverse=True)
                
        for pos, speed in pos_speed:
            time = (target - pos) / speed
            
            if not stack or time > stack[-1]:
                stack.append(time)
                            
        return len(stack)
    
# We count fleets when slowest cars catch up the fast ones or when one
# car goes by itself. To solve this we need to