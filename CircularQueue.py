

CircularQueue(n){
	elements = [n]
  head_index = 0
  tail_index = 0
  size_left = len(elements)
}

def InsertMultipleElements(elements_to_add):
	amount_left_to_write = len(elements_to_add)
	length_to_add = len(elements_to_add)
  
  # write 1 - write to end
  first_write_size = min(length_to_add, (length_to_add - (len(elements) - head_index)), size_left)
  elements[head_index:len(elements)] = elements_to_add[0:first_write_size]
  amount_left_to_write = amount_left_to_write - first_write_size
  size_left = size_left - first_write_size

  # write 2 - start from head and write remaining
  if amount_left_to_write > 0:
      # write 2nd half from head
      head_index = 0;
      length_to_end = min((length_to_add - first_write_size), size_left) 
      elements[head_index:length_to_end] = elements_to_add[first_write_size:length_to_end]
      head_index = length_to_end
      amount_left = amount_left - first_write_size
  		size_left = size_left - first_write_size
    

  return amount_left
    
def RemoveMultipleElements(index):
	 
	


