class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1 : 
            return [0]
        else : 
            # n == even 
            ## --> if 4 : [0,1,0,-1]
            if n % 2 == 0 : 
                can_nums = list(range(1, (n//2)+1))
                neg_nums = [-abs(x) for x in can_nums]
                final = can_nums + neg_nums 

            # n == odd
            else : 
                can_nums = list(range(1, ((n-1)//2)+1 ))
                neg_nums = [-abs(x) for x in can_nums]
                final = can_nums + neg_nums + [0]
            return final 
