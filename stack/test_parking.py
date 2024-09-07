import pytest
from parking import Parking


@pytest.fixture
def parking_lot():
    return Parking()


def test_add_car(parking_lot):
    parking_lot.add_car("ABC-1234")
    assert not parking_lot.parking.is_empty()
    assert parking_lot.parking.peek() == "ABC-1234"


def test_get_car(parking_lot):
    parking_lot.add_car("ABC-1234")
    parking_lot.add_car("XYZ-5678")
    parking_lot.get_car("ABC-1234")
    assert parking_lot.parking.peek().value.value == "XYZ-5678"
    assert parking_lot.street.is_empty()


def test_get_car_not_found(parking_lot):
    parking_lot.add_car("ABC-1234")
    parking_lot.get_car("XYZ-5678")
    assert parking_lot.parking.peek().value.value == "ABC-1234"
    assert parking_lot.street.is_empty()


if __name__ == "__main__":
    pytest.main()
