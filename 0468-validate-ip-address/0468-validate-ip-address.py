class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def check_IPV4():
            splited = queryIP.split('.')
            if len(splited) != 4:
                return False
            for chunk in splited:
                if len(chunk) > 1 and chunk[0] == '0':
                    return False
                if not chunk.isdigit():
                    return False
                if not 0 <= int(chunk) <= 255:
                    return False
                
            return True
        
        def check_IPV6():
            splited = queryIP.split(':')
            if len(splited) != 8:
                return False
            for chunk in splited:
                if not 1 <= len(chunk) <= 4:
                    return False
                for char in chunk:
                    if not (char.isdigit() or 'a' <= char <= 'f' or \
                            'A' <= char <= 'F'):
                        return False
                    
            return True
            
        if check_IPV4(): return 'IPv4'
        if check_IPV6(): return 'IPv6'
        return 'Neither'
        
        
        
        
        
        
        
        
        
        
        
        
        