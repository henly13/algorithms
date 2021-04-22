##Salary Threshold
def salary_threshold(salary:list,target:int)->int:
    size=len(salary)-1
    remaining=target
    for i in range(len(salary)):
        if((remaining-salary[i])/(size)>=salary[i]):
            size-=1
            remaining-=salary[i]
            print("A")
        else:
            print(remaining)
            print(size)
    
