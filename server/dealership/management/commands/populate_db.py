from django.core.management.base import BaseCommand
from dealership.models import CarMake, CarModel, Dealer, Review

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Create Car Makes
        makes_data = [
            {'name': 'Toyota', 'description': 'Japanese automaker known for reliability'},
            {'name': 'Honda', 'description': 'Japanese automaker known for fuel efficiency'},
            {'name': 'Ford', 'description': 'American automaker with a rich history'},
            {'name': 'BMW', 'description': 'German luxury automaker'},
            {'name': 'Mercedes', 'description': 'German luxury automaker'},
        ]

        for make_data in makes_data:
            make, created = CarMake.objects.get_or_create(
                name=make_data['name'],
                defaults={'description': make_data['description']}
            )
            if created:
                self.stdout.write(f'Created CarMake: {make.name}')

        # Create Car Models
        models_data = [
            {'make': 'Toyota', 'name': 'Camry', 'year': 2024},
            {'make': 'Toyota', 'name': 'Corolla', 'year': 2024},
            {'make': 'Honda', 'name': 'Civic', 'year': 2024},
            {'make': 'Honda', 'name': 'Accord', 'year': 2024},
            {'make': 'Ford', 'name': 'Mustang', 'year': 2024},
            {'make': 'Ford', 'name': 'F-150', 'year': 2024},
            {'make': 'BMW', 'name': 'X5', 'year': 2024},
            {'make': 'BMW', 'name': '3 Series', 'year': 2024},
            {'make': 'Mercedes', 'name': 'C-Class', 'year': 2024},
            {'make': 'Mercedes', 'name': 'E-Class', 'year': 2024},
        ]

        for model_data in models_data:
            car_make = CarMake.objects.get(name=model_data['make'])
            model, created = CarModel.objects.get_or_create(
                car_make=car_make,
                name=model_data['name'],
                year=model_data['year']
            )
            if created:
                self.stdout.write(f'Created CarModel: {model_data["year"]} {model_data["make"]} {model_data["name"]}')

        # Create Dealers
        dealers_data = [
            {
                'full_name': 'Cars Dealership New York',
                'city': 'New York City',
                'address': '123 Broadway, Manhattan',
                'zip': '10001',
                'state': 'New York',
                'lat': 40.7580,
                'long': -73.9855,
                'short_name': 'NYC Dealer',
                'st': 'NY'
            },
            {
                'full_name': 'Cars Dealership Los Angeles',
                'city': 'Los Angeles',
                'address': '456 Sunset Blvd',
                'zip': '90028',
                'state': 'California',
                'lat': 34.0928,
                'long': -118.3287,
                'short_name': 'LA Dealer',
                'st': 'CA'
            },
            {
                'full_name': 'Cars Dealership Chicago',
                'city': 'Chicago',
                'address': '789 Michigan Ave',
                'zip': '60611',
                'state': 'Illinois',
                'lat': 41.8916,
                'long': -87.6238,
                'short_name': 'Chicago Dealer',
                'st': 'IL'
            },
            {
                'full_name': 'Cars Dealership Houston',
                'city': 'Houston',
                'address': '321 Main Street',
                'zip': '77002',
                'state': 'Texas',
                'lat': 29.7604,
                'long': -95.3698,
                'short_name': 'Houston Dealer',
                'st': 'TX'
            },
            {
                'full_name': 'Cars Dealership Kansas City',
                'city': 'Kansas City',
                'address': '555 Main Street',
                'zip': '64111',
                'state': 'Kansas',
                'lat': 39.0997,
                'long': -94.5786,
                'short_name': 'KC Dealer',
                'st': 'KS'
            },
            {
                'full_name': 'Cars Dealership Miami',
                'city': 'Miami',
                'address': '888 Ocean Drive',
                'zip': '33139',
                'state': 'Florida',
                'lat': 25.7617,
                'long': -80.1918,
                'short_name': 'Miami Dealer',
                'st': 'FL'
            },
        ]

        for dealer_data in dealers_data:
            dealer, created = Dealer.objects.get_or_create(
                full_name=dealer_data['full_name'],
                defaults=dealer_data
            )
            if created:
                self.stdout.write(f'Created Dealer: {dealer.full_name}')

        # Create Sample Reviews
        reviews_data = [
            {
                'dealership': 1,
                'name': 'John Doe',
                'purchase': True,
                'review': 'Fantastic services! Great experience buying my new car.',
                'purchase_date': '2024-01-15',
                'car_make': 'Toyota',
                'car_model': 'Camry',
                'car_year': 2024,
                'sentiment': 'positive'
            },
            {
                'dealership': 1,
                'name': 'Jane Smith',
                'purchase': False,
                'review': 'Good customer service, staff was very helpful.',
                'purchase_date': None,
                'car_make': '',
                'car_model': '',
                'car_year': None,
                'sentiment': 'positive'
            },
            {
                'dealership': 2,
                'name': 'Mike Johnson',
                'purchase': True,
                'review': 'Excellent dealership, highly recommend!',
                'purchase_date': '2024-02-20',
                'car_make': 'Honda',
                'car_model': 'Civic',
                'car_year': 2024,
                'sentiment': 'positive'
            },
        ]

        for review_data in reviews_data:
            review, created = Review.objects.get_or_create(
                dealership=review_data['dealership'],
                name=review_data['name'],
                defaults=review_data
            )
            if created:
                self.stdout.write(f'Created Review by {review.name}')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
