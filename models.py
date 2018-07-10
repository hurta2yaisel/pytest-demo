try:
    from functools import reduce
except ImportError:
    pass

__author__ = 'Yaisel Hurtado <hurta2yaisel@gmail.com>'
__date__ = '8/07/18'


class Rental(object):
    def __init__(self, duration=0, charging=0):
        self.duration = duration
        self.charging = charging

    @property
    def price(self):
        return self.charging * self.duration


class RentalByHour(Rental):
    def __init__(self, hours=0):
        super(RentalByHour, self).__init__(duration=hours, charging=5)


class RentalByDay(Rental):
    def __init__(self, days=0):
        super(RentalByDay, self).__init__(duration=days, charging=20)


class RentalByWeek(Rental):
    def __init__(self, weeks=0):
        super(RentalByWeek, self).__init__(duration=weeks, charging=60)


class BasePromotion(object):
    __discount = 0
    __rentals = []

    def __init__(self, discount=0):
        self.discount = discount

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount=0):
        if type(discount) not in (int, float):
            raise TypeError('discount argument must be int or float')

        self.__discount = float(abs(discount)) / 100


class FamilyRental(BasePromotion):
    min_rentals = 3
    max_rentals = 5

    def __init__(self, rentals=None):
        self.rentals = rentals
        super(FamilyRental, self).__init__(discount=30)

    @property
    def rentals(self):
        return self.__rentals

    @rentals.setter
    def rentals(self, rentals):
        if type(rentals) not in (list, tuple, set):
            raise TypeError('rentals argument must be an iterable')

        rentals_count = len(rentals) if rentals else 0
        if rentals_count:
            valid_rentals = []
            for rental in rentals:
                if isinstance(rental, Rental):
                    valid_rentals.append(
                        rental
                    )
                else:
                    raise TypeError('{invalid_type} object is not an instance of {rental_type}'.format(
                        invalid_type=rental.__class__.__name__,
                        rental_type=Rental.__name__
                    ))
            rentals_count = len(valid_rentals)
            if self.min_rentals <= rentals_count <= self.max_rentals:
                self.__rentals = valid_rentals
            elif rentals_count < self.min_rentals:
                raise ValueError(
                    'Rentals count ({rentals_count}) must be greater or equal to {edge}'.format(
                        rentals_count=rentals_count,
                        edge=self.min_rentals
                    ))
            else:
                raise ValueError(
                    'Rentals count ({rentals_count}) must be less or equal to {edge}'.format(
                        rentals_count=rentals_count,
                        edge=self.max_rentals
                    ))

    @property
    def total_price(self):
        price = reduce(lambda x, y: x + y, [rental.price for rental in self.rentals], 0)
        discount = price * self.discount if self.discount else 0
        return price - discount
