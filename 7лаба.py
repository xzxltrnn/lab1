class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id},"

emp1 = Employee("Алиса", "001")
print('Информация о сотруднике: ', "\n", emp1.get_info(), '\n')


class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def manage_project(self, project_name):
        return f"{self.name} занимается проектом: {project_name}"

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}, Отдел: {man1.department}"

man1 = Manager('Антон', '002', 'Oтдел продаж')
print("Информация о менеджере: " "\n",  man1.get_info())
print(man1.manage_project("Продажи"), '\n')





class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}, Специализация: {tech1.specialization}"


    def perform_maintenance(self, task):
        return f"{self.name} проводит: {task}"

tech1 = Technician('Андрей', '003', 'Системный администратор')
print("Информация о технике: \n", tech1.get_info())
print(tech1.perform_maintenance("Работу с техникой"), '\n')



class TechManager(Manager, Technician):
    def __init__(self, name, id, specialization, department):
        self.name = name
        self.id = id
        self.team = []
        self.specialization = specialization
        self.department = department


    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}, Специализация: {tm1.specialization}, Отдел: {tm1.department}"

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = "Участники команды:\n"
        for member in self.team:
            team_info += f"- {member.get_info()}\n"
        return team_info

tm1 = TechManager("Александр","004", 'Тим.лид', 'Глава отдела')
print("Информация о тех.менеджере: \n", tm1.get_info())
print(tm1.manage_project(f"Набор сотрудников в команду"))
print(tm1.perform_maintenance(f"Собрание команды"), "\n")

tm1.add_employee(emp1)
tm1.add_employee(man1)
tm1.add_employee(tech1)
tm1.add_employee(tm1)

print(tm1.get_team_info())









