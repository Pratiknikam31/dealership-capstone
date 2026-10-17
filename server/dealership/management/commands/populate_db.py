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

        # Create Dealers - 50 dealers across multiple states
        dealers_data = [
            # New York
            {'full_name': 'Cars Dealership New York', 'city': 'New York City', 'address': '123 Broadway, Manhattan', 'zip': '10001', 'state': 'New York', 'lat': 40.7580, 'long': -73.9855, 'short_name': 'NYC Dealer', 'st': 'NY'},
            {'full_name': 'Cars Dealership Brooklyn', 'city': 'Brooklyn', 'address': '456 Atlantic Ave', 'zip': '11217', 'state': 'New York', 'lat': 40.6782, 'long': -73.9442, 'short_name': 'Brooklyn Dealer', 'st': 'NY'},
            {'full_name': 'Cars Dealership Queens', 'city': 'Queens', 'address': '789 Queens Blvd', 'zip': '11374', 'state': 'New York', 'lat': 40.7282, 'long': -73.7949, 'short_name': 'Queens Dealer', 'st': 'NY'},
            # California
            {'full_name': 'Cars Dealership Los Angeles', 'city': 'Los Angeles', 'address': '456 Sunset Blvd', 'zip': '90028', 'state': 'California', 'lat': 34.0928, 'long': -118.3287, 'short_name': 'LA Dealer', 'st': 'CA'},
            {'full_name': 'Cars Dealership San Francisco', 'city': 'San Francisco', 'address': '123 Market Street', 'zip': '94105', 'state': 'California', 'lat': 37.7749, 'long': -122.4194, 'short_name': 'SF Dealer', 'st': 'CA'},
            {'full_name': 'Cars Dealership San Diego', 'city': 'San Diego', 'address': '789 Fifth Ave', 'zip': '92101', 'state': 'California', 'lat': 32.7157, 'long': -117.1611, 'short_name': 'San Diego Dealer', 'st': 'CA'},
            {'full_name': 'Cars Dealership Sacramento', 'city': 'Sacramento', 'address': '321 Capitol Mall', 'zip': '95814', 'state': 'California', 'lat': 38.5816, 'long': -121.4944, 'short_name': 'Sacramento Dealer', 'st': 'CA'},
            # Texas
            {'full_name': 'Cars Dealership Houston', 'city': 'Houston', 'address': '321 Main Street', 'zip': '77002', 'state': 'Texas', 'lat': 29.7604, 'long': -95.3698, 'short_name': 'Houston Dealer', 'st': 'TX'},
            {'full_name': 'Cars Dealership Dallas', 'city': 'Dallas', 'address': '456 Commerce Street', 'zip': '75202', 'state': 'Texas', 'lat': 32.7767, 'long': -96.7970, 'short_name': 'Dallas Dealer', 'st': 'TX'},
            {'full_name': 'Cars Dealership Austin', 'city': 'Austin', 'address': '789 Congress Ave', 'zip': '78701', 'state': 'Texas', 'lat': 30.2672, 'long': -97.7431, 'short_name': 'Austin Dealer', 'st': 'TX'},
            {'full_name': 'Cars Dealership San Antonio', 'city': 'San Antonio', 'address': '123 Alamo Plaza', 'zip': '78205', 'state': 'Texas', 'lat': 29.4241, 'long': -98.4936, 'short_name': 'San Antonio Dealer', 'st': 'TX'},
            # Florida
            {'full_name': 'Cars Dealership Miami', 'city': 'Miami', 'address': '888 Ocean Drive', 'zip': '33139', 'state': 'Florida', 'lat': 25.7617, 'long': -80.1918, 'short_name': 'Miami Dealer', 'st': 'FL'},
            {'full_name': 'Cars Dealership Orlando', 'city': 'Orlando', 'address': '456 International Drive', 'zip': '32819', 'state': 'Florida', 'lat': 28.5383, 'long': -81.3792, 'short_name': 'Orlando Dealer', 'st': 'FL'},
            {'full_name': 'Cars Dealership Tampa', 'city': 'Tampa', 'address': '789 Kennedy Blvd', 'zip': '33606', 'state': 'Florida', 'lat': 27.9506, 'long': -82.4572, 'short_name': 'Tampa Dealer', 'st': 'FL'},
            {'full_name': 'Cars Dealership Jacksonville', 'city': 'Jacksonville', 'address': '321 Riverside Ave', 'zip': '32204', 'state': 'Florida', 'lat': 30.3322, 'long': -81.6557, 'short_name': 'Jacksonville Dealer', 'st': 'FL'},
            # Illinois
            {'full_name': 'Cars Dealership Chicago', 'city': 'Chicago', 'address': '789 Michigan Ave', 'zip': '60611', 'state': 'Illinois', 'lat': 41.8916, 'long': -87.6238, 'short_name': 'Chicago Dealer', 'st': 'IL'},
            # Kansas
            {'full_name': 'Cars Dealership Kansas City', 'city': 'Kansas City', 'address': '555 Main Street', 'zip': '64111', 'state': 'Kansas', 'lat': 39.0997, 'long': -94.5786, 'short_name': 'KC Dealer', 'st': 'KS'},
            {'full_name': 'Cars Dealership Wichita', 'city': 'Wichita', 'address': '123 Douglas Ave', 'zip': '67202', 'state': 'Kansas', 'lat': 37.6872, 'long': -97.3301, 'short_name': 'Wichita Dealer', 'st': 'KS'},
            # Arizona
            {'full_name': 'Cars Dealership Phoenix', 'city': 'Phoenix', 'address': '456 Central Ave', 'zip': '85004', 'state': 'Arizona', 'lat': 33.4484, 'long': -112.0740, 'short_name': 'Phoenix Dealer', 'st': 'AZ'},
            {'full_name': 'Cars Dealership Tucson', 'city': 'Tucson', 'address': '789 Broadway Blvd', 'zip': '85701', 'state': 'Arizona', 'lat': 32.2226, 'long': -110.9747, 'short_name': 'Tucson Dealer', 'st': 'AZ'},
            # Georgia
            {'full_name': 'Cars Dealership Atlanta', 'city': 'Atlanta', 'address': '321 Peachtree Street', 'zip': '30303', 'state': 'Georgia', 'lat': 33.7490, 'long': -84.3880, 'short_name': 'Atlanta Dealer', 'st': 'GA'},
            {'full_name': 'Cars Dealership Savannah', 'city': 'Savannah', 'address': '123 Broughton Street', 'zip': '31401', 'state': 'Georgia', 'lat': 32.0809, 'long': -81.0976, 'short_name': 'Savannah Dealer', 'st': 'GA'},
            # Colorado
            {'full_name': 'Cars Dealership Denver', 'city': 'Denver', 'address': '456 16th Street Mall', 'zip': '80202', 'state': 'Colorado', 'lat': 39.7392, 'long': -104.9903, 'short_name': 'Denver Dealer', 'st': 'CO'},
            {'full_name': 'Cars Dealership Colorado Springs', 'city': 'Colorado Springs', 'address': '789 Nevada Ave', 'zip': '80903', 'state': 'Colorado', 'lat': 38.8339, 'long': -104.8214, 'short_name': 'Colorado Springs Dealer', 'st': 'CO'},
            # Michigan
            {'full_name': 'Cars Dealership Detroit', 'city': 'Detroit', 'address': '321 Woodward Ave', 'zip': '48226', 'state': 'Michigan', 'lat': 42.3314, 'long': -83.0458, 'short_name': 'Detroit Dealer', 'st': 'MI'},
            {'full_name': 'Cars Dealership Grand Rapids', 'city': 'Grand Rapids', 'address': '123 Monroe Ave', 'zip': '49503', 'state': 'Michigan', 'lat': 42.9634, 'long': -85.6681, 'short_name': 'Grand Rapids Dealer', 'st': 'MI'},
            # Washington
            {'full_name': 'Cars Dealership Seattle', 'city': 'Seattle', 'address': '456 Pike Street', 'zip': '98101', 'state': 'Washington', 'lat': 47.6062, 'long': -122.3321, 'short_name': 'Seattle Dealer', 'st': 'WA'},
            {'full_name': 'Cars Dealership Spokane', 'city': 'Spokane', 'address': '789 Main Ave', 'zip': '99201', 'state': 'Washington', 'lat': 47.6588, 'long': -117.4260, 'short_name': 'Spokane Dealer', 'st': 'WA'},
            # Oregon
            {'full_name': 'Cars Dealership Portland', 'city': 'Portland', 'address': '321 SW Morrison St', 'zip': '97204', 'state': 'Oregon', 'lat': 45.5152, 'long': -122.6784, 'short_name': 'Portland Dealer', 'st': 'OR'},
            {'full_name': 'Cars Dealership Eugene', 'city': 'Eugene', 'address': '123 Willamette Street', 'zip': '97401', 'state': 'Oregon', 'lat': 44.0521, 'long': -123.0868, 'short_name': 'Eugene Dealer', 'st': 'OR'},
            # Nevada
            {'full_name': 'Cars Dealership Las Vegas', 'city': 'Las Vegas', 'address': '456 Las Vegas Blvd', 'zip': '89101', 'state': 'Nevada', 'lat': 36.1699, 'long': -115.1398, 'short_name': 'Las Vegas Dealer', 'st': 'NV'},
            {'full_name': 'Cars Dealership Reno', 'city': 'Reno', 'address': '789 Virginia Street', 'zip': '89501', 'state': 'Nevada', 'lat': 39.5296, 'long': -119.8138, 'short_name': 'Reno Dealer', 'st': 'NV'},
            # North Carolina
            {'full_name': 'Cars Dealership Charlotte', 'city': 'Charlotte', 'address': '321 Tryon Street', 'zip': '28202', 'state': 'North Carolina', 'lat': 35.2271, 'long': -80.8431, 'short_name': 'Charlotte Dealer', 'st': 'NC'},
            {'full_name': 'Cars Dealership Raleigh', 'city': 'Raleigh', 'address': '123 Fayetteville Street', 'zip': '27601', 'state': 'North Carolina', 'lat': 35.7796, 'long': -78.6382, 'short_name': 'Raleigh Dealer', 'st': 'NC'},
            # Ohio
            {'full_name': 'Cars Dealership Columbus', 'city': 'Columbus', 'address': '456 High Street', 'zip': '43215', 'state': 'Ohio', 'lat': 39.9612, 'long': -82.9988, 'short_name': 'Columbus Dealer', 'st': 'OH'},
            {'full_name': 'Cars Dealership Cleveland', 'city': 'Cleveland', 'address': '789 Euclid Ave', 'zip': '44115', 'state': 'Ohio', 'lat': 41.4993, 'long': -81.6944, 'short_name': 'Cleveland Dealer', 'st': 'OH'},
            # Pennsylvania
            {'full_name': 'Cars Dealership Philadelphia', 'city': 'Philadelphia', 'address': '321 Market Street', 'zip': '19102', 'state': 'Pennsylvania', 'lat': 39.9526, 'long': -75.1652, 'short_name': 'Philadelphia Dealer', 'st': 'PA'},
            {'full_name': 'Cars Dealership Pittsburgh', 'city': 'Pittsburgh', 'address': '123 Liberty Ave', 'zip': '15222', 'state': 'Pennsylvania', 'lat': 40.4406, 'long': -79.9959, 'short_name': 'Pittsburgh Dealer', 'st': 'PA'},
            # Massachusetts
            {'full_name': 'Cars Dealership Boston', 'city': 'Boston', 'address': '456 Washington Street', 'zip': '02108', 'state': 'Massachusetts', 'lat': 42.3601, 'long': -71.0589, 'short_name': 'Boston Dealer', 'st': 'MA'},
            {'full_name': 'Cars Dealership Worcester', 'city': 'Worcester', 'address': '789 Main Street', 'zip': '01608', 'state': 'Massachusetts', 'lat': 42.2626, 'long': -71.8023, 'short_name': 'Worcester Dealer', 'st': 'MA'},
            # Tennessee
            {'full_name': 'Cars Dealership Nashville', 'city': 'Nashville', 'address': '321 Broadway', 'zip': '37201', 'state': 'Tennessee', 'lat': 36.1627, 'long': -86.7816, 'short_name': 'Nashville Dealer', 'st': 'TN'},
            {'full_name': 'Cars Dealership Memphis', 'city': 'Memphis', 'address': '123 Beale Street', 'zip': '38103', 'state': 'Tennessee', 'lat': 35.1495, 'long': -90.0490, 'short_name': 'Memphis Dealer', 'st': 'TN'},
            # Indiana
            {'full_name': 'Cars Dealership Indianapolis', 'city': 'Indianapolis', 'address': '456 Monument Circle', 'zip': '46204', 'state': 'Indiana', 'lat': 39.7684, 'long': -86.1581, 'short_name': 'Indianapolis Dealer', 'st': 'IN'},
            {'full_name': 'Cars Dealership Fort Wayne', 'city': 'Fort Wayne', 'address': '789 Clinton Street', 'zip': '46802', 'state': 'Indiana', 'lat': 41.0793, 'long': -85.1394, 'short_name': 'Fort Wayne Dealer', 'st': 'IN'},
            # Missouri
            {'full_name': 'Cars Dealership St. Louis', 'city': 'St. Louis', 'address': '321 Olive Street', 'zip': '63101', 'state': 'Missouri', 'lat': 38.6270, 'long': -90.1994, 'short_name': 'St. Louis Dealer', 'st': 'MO'},
            {'full_name': 'Cars Dealership Kansas City MO', 'city': 'Kansas City', 'address': '123 Main Street', 'zip': '64105', 'state': 'Missouri', 'lat': 39.0997, 'long': -94.5786, 'short_name': 'KC MO Dealer', 'st': 'MO'},
            # Minnesota
            {'full_name': 'Cars Dealership Minneapolis', 'city': 'Minneapolis', 'address': '456 Nicollet Mall', 'zip': '55402', 'state': 'Minnesota', 'lat': 44.9778, 'long': -93.2650, 'short_name': 'Minneapolis Dealer', 'st': 'MN'},
            {'full_name': 'Cars Dealership St. Paul', 'city': 'St. Paul', 'address': '789 Wabasha Street', 'zip': '55102', 'state': 'Minnesota', 'lat': 44.9537, 'long': -93.0900, 'short_name': 'St. Paul Dealer', 'st': 'MN'},
            # Wisconsin
            {'full_name': 'Cars Dealership Milwaukee', 'city': 'Milwaukee', 'address': '321 Wisconsin Ave', 'zip': '53202', 'state': 'Wisconsin', 'lat': 43.0389, 'long': -87.9065, 'short_name': 'Milwaukee Dealer', 'st': 'WI'},
            {'full_name': 'Cars Dealership Madison', 'city': 'Madison', 'address': '123 State Street', 'zip': '53703', 'state': 'Wisconsin', 'lat': 43.0731, 'long': -89.4012, 'short_name': 'Madison Dealer', 'st': 'WI'},
            # New Jersey
            {'full_name': 'Cars Dealership Newark', 'city': 'Newark', 'address': '456 Broad Street', 'zip': '07102', 'state': 'New Jersey', 'lat': 40.7357, 'long': -74.1724, 'short_name': 'Newark Dealer', 'st': 'NJ'},
            {'full_name': 'Cars Dealership Jersey City', 'city': 'Jersey City', 'address': '789 Montgomery Street', 'zip': '07302', 'state': 'New Jersey', 'lat': 40.7178, 'long': -74.0431, 'short_name': 'Jersey City Dealer', 'st': 'NJ'},
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
