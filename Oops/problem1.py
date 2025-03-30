class Programmer:
    company = 'Microsoft'
    name = None
    salary = None
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(self.name," working in ",self.company, "and has salary of ",self.salary)

    def updateCompany(self, newCompany):
        self.company = newCompany

    @staticmethod
    def programmerInfo():
        print(Programmer.name," working in ",Programmer.company, "and has salary of ",Programmer.salary)

    

mohan = Programmer('Mohan',10000)
mohan.updateCompany('Google')
sohan = Programmer('Sohan',20000)
Programmer.programmerInfo()
