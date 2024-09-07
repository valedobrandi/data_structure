from class_queue import Stack


class Parking():
    def __init__(self) -> None:
        self.parking = Stack()
        self.street = Stack()

    def add_car(self, plate):
        self.parking.push(plate)
        print("Car parked")

    def get_car(self, plate):
        is_removed = True
        while not self.parking.is_empty():
            parked_plate = self.parking.pop()
            if plate == parked_plate:
                print("removed")
                is_removed = False
            else:
                self.street.push(parked_plate)
        while not self.street.is_empty():
            street_car = self.street.pop()
            self.parking.push(street_car)
        if not is_removed:
            print("Plate not found")




parking_lot = Parking()

parking_lot.add_car("ABC-1234")
parking_lot.add_car("XYZ-5678")
parking_lot.get_car("ABC-1234")
print(parking_lot.parking.peek().value.value)
parking_lot.street.is_empty()