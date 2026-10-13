import statistics
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
    def person_data(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

    def add_skill(self, skill):
        self.skills.append(skill)
p = Person('Michal', 'Gnacinski', 25, 'Polska', 'Poznan')
print(p.person_data())
p.add_skill('CSS')
p.add_skill('HTML')
print(p.skills)
p2 = Person()
print(p2.person_data())

class Student(Person):
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki', gender = 'Male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_data(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_data())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_data())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


#Ex 1
class Statistics:
    def __init__(self, data = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]):
        self.data = data
    def count(self):
        return len(self.data)
    def sum(self):
        suma = 0
        for i in self.data:
            suma += i
        return suma
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def range(self):
        return max(self.data) - min(self.data)
    def mean(self):
        return round(sum(self.data) / self.count())
    def median(self):
        return statistics.median(self.data)
    def mode(self):
        return statistics.mode(self.data)
    def std(self):
        return statistics.stdev(self.data)
    def var(self):
        return statistics.variance(self.data)
datas = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
d1 = Statistics(datas)
print('Count:', d1.count()) # 25
print('Sum: ', d1.sum()) # 744
print('Min: ', d1.min()) # 24
print('Max: ', d1.max()) # 38
print('Range: ', d1.range()) # 14
print('Mean: ', d1.mean()) # 30
print('Median: ', d1.median()) # 29
print('Mode: ', d1.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', d1.std()) # 4.2
print('Variance: ', d1.var()) # 17.5


    