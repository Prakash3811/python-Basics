class Box:
    def __init__(self, name, rollNo, dbmsMarks, pythonMarks, cMarks, osMarks, cnMarks):
        self.name = name
        self.rollNo = rollNo
        self.dbmsMarks = dbmsMarks
        self.pythonMarks = pythonMarks
        self.cMarks = cMarks
        self.osMarks = osMarks
        self.cnMarks = cnMarks


student1 = Box("Harika", "5A1", 78, 67, 77, 89, 46)
student2 = Box("Swapna", "5A2", 38, 65, 97, 59, 41)
student3 = Box("Sushma", "5A3", 88, 95, 47, 89, 31)


print(f"{student1.name} {student1.rollNo} {student1.dbmsMarks} {student1.pythonMarks} {student1.cMarks} {student1.osMarks} {student1.cnMarks}")
print(f"{student2.name} {student2.rollNo} {student2.dbmsMarks} {student2.pythonMarks} {student2.cMarks} {student2.osMarks} {student2.cnMarks}")
print(f"{student3.name} {student3.rollNo} {student3.dbmsMarks} {student3.pythonMarks} {student3.cMarks} {student3.osMarks} {student3.cnMarks}")
