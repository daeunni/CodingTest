class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        # only once deletion 
        n_lists = list(number)    # ['1', '2', '3', '1'] / digit = '1'
        answer = 0 

        for i, num in enumerate(n_lists) :         # 차례로 순회 

            if num == digit : 
                cur_list = n_lists.copy()
                cur_list.pop(i)       # 특정 위치 원소 값 삭제 
                cur_num = int(''.join(cur_list))

                if int(cur_num) > answer : 
                    answer = cur_num


        return str(answer)
