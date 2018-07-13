# pytest-demo
Just a pytest demo.
## Setup
Just execute ``pip install -r requirements.txt``.
## Design
The model describes a company that rents bikes under some options.
### Models
![Class diagram](https://raw.githubusercontent.com/hurta2yaisel/pytest-demo/master/diagram.png)
#### Rental
Base class for rentals. This class has the following attributes:
- duration: Duration of the rent.
- charging: The charge for each unit of time(duration).
- price: This is a property that calculates the price by multiplying (duration * charging).
#### RentalByHour
Rental by hour, charging $5 per hour.
#### RentalByDay
Rental by day, charging $20 a day.
#### RentalByWeek
Rental by week, changing $60 a week.
#### Promotion
Base class for discount promotions.
- __discount: Discount percent for applying to the total price.
- __rentals: Rentals list.
#### FamilyRental
Promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price.
- min_rentals: Minimal amount of rentals set to 3.
- max_rentals: Maximum limit of rentals set to 3.
- rentals: Property that applies some validations to the rentals list for this promotion.
- total_price: Property that calculates the total price by multiplying the sum of rentals prices by the discount.

## Testing
Enter to the directory and execute the command ``pytest``.
