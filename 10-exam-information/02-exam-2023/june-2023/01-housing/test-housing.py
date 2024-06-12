# Write your own tests for the housing.py file here.
# You must include the tests asked for in the assignment for full credit.
# You may add additional tests if you would like to test your code more thoroughly.
# Additional tests will not result in a higher grade.
# This file must be able to be run without error in order to receive credit for the required testing.
####
import pytest
from housing import Residence

class Residence(Residence):
    def calculate_value(self):
        return 0  # Implement this method as needed for your tests

@pytest.mark.parametrize("area, rooms, expected", [
    (7200, 323, min(7200 // 20, 323 * 2)),
    (7343, 434, min(7343 // 20, 434 * 2)),
    (2321321, 5000, min(2321321 // 20, 5000 * 2)),
    (21, 1, min(21 // 20, 1 * 2)),
    (45, 2, min(45 // 20, 2 * 2)),
    (655, 36, min(655 // 20, 36 * 2)),
    (1234, 240, min(1234 // 20, 240 * 2)),
])

def test_maximum_occupants(area, rooms, expected):
    residence = Residence("your momma fat", area, rooms)
    assert residence.maximum_occupants == expected