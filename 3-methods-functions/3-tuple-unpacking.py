work_hours = [
    ('Abby',100),
    ('Billy',400),
    ('Cassie',800)
]

def employee_check(work_hours):
    '''
    Returns the employee with the most hours worked in a month
    '''
    curr_max = 0
    curr_emp = ''
    
    for emp,hrs in work_hours: # Tuple unpacking
        if(hrs > curr_max):
            curr_emp = emp
            curr_max = hrs
            
    return (curr_emp,curr_max)

name,hours = employee_check(work_hours)

print(f'Worker {name} is the employee of the month with {hours} hrs worked.')