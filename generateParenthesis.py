class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output_arr = []
        self.backtrack(output_arr, "", 0, 0, n)
        return output_arr
    
    def backtrack(self, output_arr, current_string, open_par, close_par, max_n):
        
        if len(current_string) == max_n * 2: 
            output_arr.append(current_string)
            return
        
        # decisions
        if (open_par < max_n):
            self.backtrack(output_arr, current_string + "(", open_par+1, close_par, max_n)
        
        if (close_par < open_par):
            self.backtrack(output_arr, current_string + ")", open_par, close_par+1, max_n)
