#!-*- coding: utf-8 -*-

from random import choice, randint

import pytest

from models import FamilyRental, RentalByDay, RentalByHour, RentalByWeek


def get_random_rental_class():
    return choice([RentalByHour, RentalByDay, RentalByWeek])


def generate_valid_rentals(count):
    rentals = []
    while count:
        rental_class = get_random_rental_class()
        rentals.append(rental_class(randint(1, 99)))
        count -= 1
    return rentals


@pytest.fixture(scope='function')
def valid_rentals():
    count = randint(3, 5)
    return generate_valid_rentals(count)


@pytest.fixture(scope='function')
def violated_valid_min_rentals():
    return generate_valid_rentals(FamilyRental.min_rentals - 1)


@pytest.fixture(scope='function')
def violated_valid_max_rentals():
    return generate_valid_rentals(FamilyRental.max_rentals + 1)


@pytest.fixture(scope='function')
def two_valid_rentals_with_one_invalid():
    rentals = generate_valid_rentals(2)
    rentals.append(1)
    return rentals
