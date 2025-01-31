class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {'I':1,'V':5, 
                'X':10,'L':50, 
                'C':100,'D':500, 'M':1000}
        exps = {'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 
                'CD' : 400, 'CM' : 900}     # IV, IX, XL, XC, CD, CM

        i = 0 ; answer = 0 
        while i < len(s): 
            cur = s[i:i+2]
            if cur in exps.keys() :      # exception 
                answer += exps[cur]
                i += 2
            else : 
                answer += sym[s[i]]
                i += 1
        return answer 
