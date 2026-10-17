from django.test import TestCase
from .models import CarMake, CarModel, Dealer, Review

class CarMakeModelTest(TestCase):
    def setUp(self):
        CarMake.objects.create(name="Toyota", description="Test description")

    def test_car_make_creation(self):
        car_make = CarMake.objects.get(name="Toyota")
        self.assertEqual(car_make.name, "Toyota")
        self.assertEqual(car_make.description, "Test description")

class DealerModelTest(TestCase):
    def setUp(self):
        Dealer.objects.create(
            full_name="Test Dealer",
            city="Test City",
            address="123 Test St",
            zip="12345",
            state="Test State",
            lat=40.0,
            long=-74.0,
            short_name="Test",
            st="TS"
        )

    def test_dealer_creation(self):
        dealer = Dealer.objects.get(full_name="Test Dealer")
        self.assertEqual(dealer.city, "Test City")
        self.assertEqual(dealer.state, "Test State")

class ReviewModelTest(TestCase):
    def setUp(self):
        Review.objects.create(
            dealership=1,
            name="Test User",
            purchase=True,
            review="Great experience!",
            sentiment="positive"
        )

    def test_review_creation(self):
        review = Review.objects.get(name="Test User")
        self.assertEqual(review.review, "Great experience!")
        self.assertEqual(review.sentiment, "positive")
