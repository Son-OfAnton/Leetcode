class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = 0
        curr_gas = 0
        starting_index = 0

        for i in range(len(gas)):
            net += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                curr_gas = 0
                starting_index = i + 1

        return starting_index if net >= 0 else -1