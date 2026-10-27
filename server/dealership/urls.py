from django.urls import path
from . import views

urlpatterns = [
    # Dealer endpoints
    path('dealers/', views.get_dealers, name='get_dealers'),
    path('dealer/<int:dealer_id>/', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('dealers/<str:state>/', views.get_dealers_by_state, name='get_dealers_by_state'),

    # New endpoints for assignment requirements
    path('fetchDealer/<int:dealer_id>/', views.fetch_dealer, name='fetch_dealer'),
    path('fetchDealers/<str:state>', views.fetch_dealers_by_state, name='fetch_dealers_by_state'),
    path('fetchDealers/<str:state>/', views.fetch_dealers_by_state, name='fetch_dealers_by_state_slash'),

    # Review endpoints
    path('dealer/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('fetchReviews/dealer/<int:dealer_id>', views.fetch_dealer_reviews, name='fetch_dealer_reviews'),
    path('fetchReviews/dealer/<int:dealer_id>/', views.fetch_dealer_reviews, name='fetch_dealer_reviews_slash'),
    path('review/', views.add_review, name='add_review'),
    path('analyze/', views.analyze_review, name='analyze_review'),
    path('analyze/<str:text>', views.analyze_review_text, name='analyze_review_text'),

    # Car endpoints
    path('car_makes/', views.get_car_makes, name='get_car_makes'),

    # Authentication endpoints
    path('csrf/', views.get_csrf_token, name='get_csrf_token'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register_user'),

    # Django app specific endpoints for assignment
    path('djangoapp/login', views.djangoapp_login, name='djangoapp_login'),
    path('djangoapp/logout', views.djangoapp_logout, name='djangoapp_logout'),
    path('djangoapp/get_cars', views.get_cars, name='get_cars'),

    # Static pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
]

