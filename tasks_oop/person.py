from datetime import datetime, date


class Person:
    """
    Class for persons
    """

    count = 0

    def __init__(self, first_name, last_name, dob, country, city, phone, job_title, experience, salary,
                 gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.strptime(dob, "%d.%m.%Y")
        self.gender = gender
        self.country = country
        self.city = city
        self.phone = phone
        self.job_title = job_title
        self.experience = float(experience)
        self.salary = float(salary)
        self.__class__.count += 1

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_age(self):
        not_full_year = (self.dob.month, self.dob.day) > (date.today().month, date.today().day)
        age = (date.today().year - self.dob.year) - not_full_year
        return age

    def show_personal_info(self):
        return f'Full name: {self.get_full_name()}, Age: {self.get_age()}, Gender: {self.gender}'

    def show_contacts(self):
        return f'Country: {self.country}, City: {self.city}, Phone: {self.phone}'

    def show_job_profile(self):
        return f"Job title: {self.job_title}, Experience: {self.experience}, Salary: {self.salary} USD"

    def calculate_bonus(self) -> float:
        if self.experience < 1:
            return 1
        return 1 + 0.1 * (self.experience - 1)

    def calculate_income(self, period) -> float:
        return self.salary * self.calculate_bonus() * int(period)

    def show_income(self, period):
        return f'Income for {period} months: {self.calculate_income(period)}'


if __name__ == "__main__":
    person1 = Person('Karen', 'Holms', '10.10.2000', 'USA', 'New York',
                     '011-222-3333', 'Python developer', '1.5', '2500.0',
                     'Female')

    person2 = Person('David', 'Brown', '10.10.1991', 'USA', 'Chicago',
                     '011-444-3333', 'Project Manager', '4.25', '2000.0',
                     'Male')

    print(person2.show_personal_info())
    print(person2.show_job_profile())
    print(person2.show_contacts())
    print(person2.show_income(12))
    print(person2.__class__.count)
