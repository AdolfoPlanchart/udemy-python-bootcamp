def is_even(n):
    return n % 2 == 0

def get_even_list(nums):
    '''
    Returns a list of all the even numbers in a list
    '''
    even_nums = []
    
    for n in nums:
        if(is_even(n)):
            even_nums.append(n)
            
    return even_nums
        
print(get_even_list([1,2,5,7]))