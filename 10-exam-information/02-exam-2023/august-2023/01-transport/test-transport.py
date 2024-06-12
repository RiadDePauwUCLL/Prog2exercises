import pytest
from transport import Taxi, Bus, Passenger

@pytest.mark.parametrize("vehicle_class, seats, expected_maximum_occupants", [
    (Taxi, 4, 4),  # Taxi should only allow as many passengers as seats
    (Bus, 50, 100),  # Bus should allow double the amount of seats as passengers
])
def test_maximum_occupants(vehicle_class, seats, expected_maximum_occupants):
    vehicle = vehicle_class('AB1234', seats)
    assert vehicle.maximum_occupants == expected_maximum_occupants

def test_passenger_name_validation():
    with pytest.raises(ValueError):
        Passenger(1, "InvalidName", 10)

    p = Passenger(1, "Valid Name", 10)
    assert p.name == "Valid Name"

def test_vehicle_maximum_occupants():
    taxi = Taxi('TX1234', 4)
    assert taxi.maximum_occupants == 4

    bus = Bus('BS5678', 50)
    assert bus.maximum_occupants == 100

def test_taxi_pickup():
    taxi = Taxi('TX1234', 4)
    passengers = [Passenger(i, f"Passenger {i}", 10) for i in range(5)]

    with pytest.raises(ValueError):
        taxi.pickup(passengers, 5)

    passengers.pop()
    taxi.pickup(passengers, 5)
    assert taxi.number_of_occupants == 4
    assert not taxi.is_available