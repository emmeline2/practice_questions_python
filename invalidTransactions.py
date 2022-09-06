class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        return_list = []
        added_list = []
        seen_list = []
        
        for transaction in transactions: 
            items = transaction.split(",")
            
            if int(items[2]) > 1000:
                return_list.append(transaction)
                
                # add to seen list
                # seen_list[name] = [name, time, amount, city]
                seen_list.append( [items[0], items[1], items[2], items[3]] )
                added_list.append(True)
            else:
                was_added = False
                
                for i in range(0, len(seen_list)): 
                    # if name matches
                    if items[0] == seen_list[i][0]:

                        # if city does not match
                        if seen_list[i][2] != items[3]:
                            # if time matches window
                            if int(seen_list[i][1]) <= (int(items[1]) + 60):
                                if (int(seen_list[i][1]) >= (int(items[1]) - 60)):
                                    # add current transaction
                                    return_list.append(transaction)
                                    
                                    # add to seen list
                                    # seen_list[name] = [name, time, amount, city]
                                    seen_list.append( [items[0], items[1], items[2], items[3]] )
                                    added_list.append(True)
                                    was_added = True

                                    # add colliding transaction
                                    temp = ','.join(seen_list[i])
                                    if added_list[i] == False:
                                        return_list.append(temp)
                                        added_list[i] = True
                
                if not was_added:
                    # add to seen list
                    # seen_list[name] = [name, time, amount, city]
                    seen_list.append( [items[0], items[1], items[2], items[3]] )
                    added_list.append(False)
                    

        return return_list
                
