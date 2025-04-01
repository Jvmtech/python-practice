# 3. Given a dictionary of employees and salaries, increase all salaries by 10%.

employees = {
    "emp1": 10000,
    "emp2": 20000,
    "emp3": 30000,
    "emp4": 40000,
    "emp5": 50000
}
print("Initial Dictionary: ",employees)

for key, value in employees.items():
    employees[key] = value * 1.1    

print("After 10% increased in salaries: ",employees)    
