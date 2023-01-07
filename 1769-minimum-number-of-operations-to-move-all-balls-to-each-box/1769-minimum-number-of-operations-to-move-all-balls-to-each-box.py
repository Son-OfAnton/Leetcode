class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        box_num = len(boxes)
        answer = [0] * box_num

        for added in range(box_num):
            for taken in range(box_num):
                if boxes[taken] == '1':
                    answer[added] += abs(added - taken)

        return answer
    
    