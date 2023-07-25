class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [None] * (n+1)
        dp[n] = True
            
        def word_checker(start):
            if dp[start] == None:
                for end in range(start+1, n+1):  
                    word = s[start:end] 
                    
                    if word in word_set and word_checker(end):
                        dp[start] = True
                        
                        return True
                    
                dp[start] = False
                
                return False
            
            return dp[start]

        return word_checker(0)
    
    
    
