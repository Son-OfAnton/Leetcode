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
# car goes by itself. To solve this we need to calculate the time to 
# reach the target to a car and append to a stack if stack is 
# empty(since a one car is also a fleet) or if the time is larget than
# the fleet infront of the car, this helps to maintain the increasing
# monotonocity of the stack. The reason we append a car with larger time
# ever seen is that it is guarenteed that it does reach the fleets infront
# if it. Therefore it creates its own fleet and go by itself or maybe other 
# cars from behind might join it. When they join it their common speed will be 
# the new cars' this intern means the time at stack[-1] will be the largest.
# Finally the stack contains times for each fleet and its length will be the 
# the number of fleets.