from models import FamilyRental

__author__ = 'Yaisel Hurtado <hurta2yaisel@gmail.com>'
__date__ = '8/07/18'


class TestFamilyRental(object):
    def test_null_rentals(self):
        try:
            FamilyRental()
            assert False
        except TypeError:
            assert True

    def test_family_rental(self, valid_rentals):
        family_rental = FamilyRental(valid_rentals)
        assert family_rental
        assert family_rental.total_price > 0

    def test_with_invalid_discount_type(self, valid_rentals):
        family_rental = FamilyRental(valid_rentals)
        try:
            family_rental.discount = '30'
            assert False
        except TypeError:
            assert True

    def test_with_violated_valid_min_rentals(self, violated_valid_min_rentals):
        try:
            FamilyRental(violated_valid_min_rentals)
            assert False
        except ValueError:
            assert True

    def test_with_violated_max_rentals(self, violated_valid_max_rentals):
        try:
            FamilyRental(violated_valid_max_rentals)
            assert False
        except ValueError:
            assert True

    def test_with_valid_and_invalid_rentals(self, two_valid_rentals_with_one_invalid):
        try:
            FamilyRental(two_valid_rentals_with_one_invalid)
            assert False
        except TypeError:
            assert True
