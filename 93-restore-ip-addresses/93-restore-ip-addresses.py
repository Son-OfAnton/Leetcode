class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        
        if n < 4 or n > 12:
            return []
        
        valid_IPs = []
        
        def backtrack(dot_pos, candidate_IP):
            if len(candidate_IP) == 4 and dot_pos == n:
                valid_IPs.append(".".join(candidate_IP))
                return

            for i in range(dot_pos, n):
                octate = s[dot_pos:i + 1]

                if i <= n and int(octate) <= 255 \
                and (octate == '0' or octate[0] != '0'):    # checking validity then place,call,remove
                    candidate_IP.append(octate)
                    backtrack(i + 1, candidate_IP)
                    candidate_IP.pop()
                            
        backtrack(0, [])
        
        return valid_IPs
            
                