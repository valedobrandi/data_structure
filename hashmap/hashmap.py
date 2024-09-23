class Employee:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name


class HashMap:
    def __init__(self):
        self._buckets = [[] for i in range(10)]

    def get_address(self, id_num):
        return id_num % 10

    def insert(self, employee):
        index = self.get_address(employee[0])
        self._buckets[index].append(employee)

    def get_value(self, id_num):
        index = self.get_address(id_num)
        for id in self._buckets[index]:
            if id[0] == id_num:
                return id[1]
        return None

    def has(self, id_num):
        index = self.get_address(id_num)
        return self._buckets[index][1] is not None
    
    def update_value(self, id_num, new_name):
        entry = self.get_address(id_num)
        for index, i in enumerate(self._buckets[entry]):
            if i[0] == id_num:
                self._buckets[entry][index] = (id_num, new_name)
                return self._buckets[entry][index]
        return None
       

employees = [(14, "name1"), (23, "name2"), (10, "name3"), (9, "name4")]

hashmap = HashMap()

for employee in employees:
    hashmap.insert(employee)

print(hashmap.get_value(employees[2][0]))
print("------------")
print(hashmap.update_value(10, 'Updated'))