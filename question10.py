def change_case(sample_str): 
    snake = [sample_str[0].lower()] 
    for c in sample_str[1:]: 
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            snake.append('_') 
            snake.append(c.lower()) 
        else: 
            snake.append(c)
    snake = ''.join(snake) 

    kebab = [sample_str[0].lower()] 
    for c in sample_str[1:]: 
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
            kebab.append('-') 
            kebab.append(c.lower()) 
        else: 
            kebab.append(c)
        
    kebab = ''.join(kebab)  

    final_list = [snake,kebab]

    return final_list
      
sample_str = input("Enter your string :")
final_list = change_case(sample_str) 
print(final_list)