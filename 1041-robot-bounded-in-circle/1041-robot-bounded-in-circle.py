class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        moves = {
            'N': {'G': (0, 1), 'L': 'W', 'R': 'E'},
            'E': {'G': (1, 0), 'L': 'N', 'R': 'S'},
            'S': {'G': (0, -1), 'L': 'E', 'R': 'W'},
            'W': {'G': (-1, 0), 'L': 'S', 'R': 'N'}
        }
        
        position = [0, 0]
        direction = 'N'
        for instruction in instructions:
            if instruction == 'G':
                dx, dy = moves[direction][instruction]
                position[0] += dx
                position[1] += dy
            else:
                direction = moves[direction][instruction]

        in_circle = position == [0, 0] or direction != 'N'

        return in_circle
