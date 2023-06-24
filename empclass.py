class Employee:
    def __init__(self):
        self.emp_id=input("emp_id")
        self.emp_name=input("emp_name")
        self.emp_salary=int(input("emp_salary"))
        self.emp_dept=input("emp_dept")
        self.wrkdhrs=int(input("wrkdhrs"))
    def wrkdhrs_cal(self,wrkdhrs):
        if (self.wrkdhrs)>50:
            overtime=self.wrkdhrs-50
            overtimeamount=(overtime*(self.emp_salary/50))
            print(self.emp_salary+overtimeamount)
        else:
            print(self.emp_salary)
    def print_emp_details(self):
        print("emp id",self.emp_id)
        print("emp_name",self.emp_name)
        print("emp salary",self.emp_salary)
        print("emp dept",self.emp_dept)
obj1=Employee()
obj1.wrkdhrs_cal(55)
obj1.print_emp_details()