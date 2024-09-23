class Group:
    def __init__(self) -> None:
        self.set = [False for i in range(1000)]
        self.last_element = 0

    def __str__(self) -> str:
        string = "{"
        for index, is_in_set in enumerate(self.set):
            if is_in_set:
                string += str(index)
                if index < self.last_element:
                    string += ", "
        string += "}"
        return string

    def add(self, item: int):
        if not self.set[item]:
            self.set[item] = True
        if item > self.last_element:
            self.last_element = item

    def __contains__(self, item):
        return self.set[item]

    def union(self, next_group):
        new_group = Group()
        for index in range(len(self.set)):
            if self.set[index] or next_group.set[index]:
                new_group.add(index)
        return new_group

    def intersection(self, next_group):
        new_group = Group()
        for index in range(len(self.set)):
            if self.set[index] and next_group.set[index]:
                new_group.add(index)
        return new_group

    def difference(self, next_group):
        new_group = Group()
        for index in range(len(self.set)):
            if self.set[index] and not next_group.set[index]:
                new_group.add(index)
        return new_group
    
    def issubset(self, next_group):
        if len(self.set) != len(next_group.set):
            return False
        for index in range(len(self.set)):
            if self.set[index] and not next_group.set[index]:
                return False
        return True
    
    def issuperset(self, next_group):
        for index in range(len(self.set)):
            if self.set[index] and not next_group.set[index]:
                return False
        return True


# other = set()
# set.isdisjoint(other)
# set.issubset(other)
# set.issuperset(other)
# set == other
# set.union(others)
# set.intersection(others)
# set.difference(others)
# set.symmetric_difference(others)

if __name__ == "__main__":

    instance = Group()
    instance_b = Group()

    for i in range(11):
        instance.add(i)

    for i in range(9, 21):
        instance_b.add(i)

"""     print(instance)

    print(10 in instance)
    print(20 in instance)

    print(instance.union(instance_b))
    print(instance.intersection(instance_b))
    print(instance.difference(instance_b))
    print(instance.issubset(instance_b))
    print(instance.issuperset(instance_b)) """

estudantes = [1, 2, 3, 4, 5, 6, 7]
lista1_entregues = [1, 4, 7, 3]
lista2_entregues = [3, 1, 6]

studets = Group()
deliver_one = Group()
deliver_two = Group()

for i in estudantes:
    studets.add(i)

for i in lista1_entregues:
    deliver_one.add(i)

for i in lista2_entregues:
    deliver_two.add(i)


print(studets.difference(deliver_one))
print(deliver_one.intersection(deliver_two))
print(deliver_one.union(deliver_two))
print(studets.difference(deliver_one.union(deliver_two)))