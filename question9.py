def binary_search(sample_list, low, high, input_num): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        if sample_list[mid] == input_num: 
            return mid 
  
        elif sample_list[mid] > input_num: 
            return binary_search(sample_list, low, mid - 1, input_num) 
  
        else: 
            return binary_search(sample_list, mid + 1, high, input_num) 
  
    else: 
        return -1
  
sample_list = [0,1,2,3,4,5,6,7,8,9,10] 
input_num = int(input("Enter your number to search :"))
  


result = binary_search(sample_list, 0, len(sample_list)-1, input_num) 
if result != -1: 
    print("Element is present at index", str(result)) 
else:
    print(str(result))