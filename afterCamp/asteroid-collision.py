class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                # Curr asteroid is big and heading to the left
                # and continues smashing smaller right heading ones
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                # They are equal, hence destroys eachother
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                # This break kind of destroys the curr astroid
                break
            # If the loop is not finished by 'break', 
            # the curr asteroid is not destroyed yet
            else:
                stack.append(asteroid)

        return stack
                