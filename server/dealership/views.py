from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CarMake, CarModel, Dealer, Review
from .serializers import CarMakeSerializer, CarModelSerializer, DealerSerializer, ReviewSerializer, UserSerializer
import json

# Mock sentiment analysis function
def analyze_sentiment(text):
    positive_words = ['fantastic', 'great', 'excellent', 'amazing', 'wonderful', 'awesome', 'good', 'love', 'best']
    negative_words = ['terrible', 'bad', 'awful', 'horrible', 'worst', 'hate', 'poor', 'disappointing']

    text_lower = text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)

    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    else:
        return 'neutral'

# Dealer endpoints
@api_view(['GET'])
def get_dealers(request):
    dealers = Dealer.objects.all()
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_dealer_by_id(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
        serializer = DealerSerializer(dealer)
        return Response(serializer.data)
    except Dealer.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=404)

@api_view(['GET'])
def get_dealers_by_state(request, state):
    dealers = Dealer.objects.filter(state=state)
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)

# Review endpoints
@api_view(['GET'])
def get_dealer_reviews(request, dealer_id):
    reviews = Review.objects.filter(dealership=dealer_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@csrf_exempt
def add_review(request):
    data = json.loads(request.body)
    sentiment = analyze_sentiment(data.get('review', ''))
    data['sentiment'] = sentiment
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def analyze_review(request):
    data = json.loads(request.body)
    text = data.get('review', '')
    sentiment = analyze_sentiment(text)
    return Response({'sentiment': sentiment})

# Car endpoints
@api_view(['GET'])
def get_car_makes(request):
    car_makes = CarMake.objects.all()
    serializer = CarMakeSerializer(car_makes, many=True)
    return Response(serializer.data)

# Authentication endpoints
@api_view(['POST'])
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response({'status': 'Logged in', 'user': serializer.data})
    return Response({'error': 'Invalid credentials'}, status=401)

@api_view(['POST'])
@csrf_exempt
def logout_user(request):
    logout(request)
    return Response({'status': 'Logged out'})

@api_view(['POST'])
@csrf_exempt
def register_user(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    serializer = UserSerializer(user)
    return Response({'status': 'Registered', 'user': serializer.data}, status=201)

# Static page views
def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def index(request):
    return render(request, 'index.html')
