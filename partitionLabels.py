class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        seen_letters = []
        
        running_index = 0;
        
        current_break_point = 0
        ret_list = []
        
        for j in range(0, len(s)): 
            seen_letters.append(s[j])
            for i in range(j, len(s)): 
                if s[i] in seen_letters:
                    running_index = i + 1 # account for 0 indexed
            if running_index > current_break_point:
                current_break_point = running_index
                ret_list.append(current_break_point)

            seen_letters = []
           # current_break_point = 0
        
        print("RET LIST BEFORE: ", ret_list)
        # process ret list
        for i in range(len(ret_list) - 1, 0, -1): 
            ret_list[i] = ret_list[i] - ret_list[i-1]
        
        return ret_list
                    
