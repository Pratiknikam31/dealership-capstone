# dealership-capstone

## Repository Name
dealership-capstone

## Project Name
Cars Dealership Capstone Project

## Project Overview
Cars Dealership is a national car retailer in the United States. This full-stack web application allows users to view dealership branches, filter dealers by state, read and submit reviews, and access information about car makes and models.

## Technologies Used
- **Backend**: Django 6.1.2, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 4.5.2
- **Database**: SQLite (with MongoDB configuration option)
- **Authentication**: Django's built-in authentication system
- **Sentiment Analysis**: Custom mock sentiment analysis service
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Deployment**: IBM Cloud Code Engine (ready for deployment)

## Features
1. **Dealership Management**
   - View all dealerships across the United States
   - Filter dealers by state
   - View detailed dealer information including location coordinates

2. **User Authentication**
   - User registration with username, name, email, and password
   - Login and logout functionality
   - Session management

3. **Review System**
   - Submit reviews for dealerships
   - View existing reviews
   - Sentiment analysis on review text (positive/negative/neutral)
   - Track purchase information and car details

4. **Car Information**
   - Browse car makes and models
   - View detailed car specifications

5. **Static Pages**
   - About Us page with team information
   - Contact Us page with contact form and information

6. **Admin Panel**
   - Django admin interface for managing dealers, reviews, and car data
   - Root user access for administrative tasks

## Project Structure
```
dealership-capstone/
├── server/
│   ├── dealership/              # Main Django app
│   │   ├── models.py           # Database models
│   │   ├── views.py            # API views and endpoints
│   │   ├── serializers.py      # DRF serializers
│   │   ├── urls.py             # URL routing
│   │   ├── admin.py            # Admin configuration
│   │   ├── templates/          # HTML templates
│   │   │   └── index.html      # Main homepage
│   │   └── management/         # Custom management commands
│   │       └── commands/
│   │           └── populate_db.py
│   ├── frontend/               # Frontend assets
│   │   ├── static/            # Static files (CSS, HTML)
│   │   │   ├── About.html
│   │   │   ├── Contact.html
│   │   │   └── styles.css
│   │   └── src/               # React components
│   │       └── components/
│   │           └── Register/
│   │               ├── Register.jsx
│   │               └── Register.css
│   ├── server/                # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD workflow
└── README.md
```

## API Endpoints

### Dealer Endpoints
- `GET /api/dealers/` - Get all dealers
- `GET /api/fetchDealers/<state>` - Get dealers by state (with `_id`, `id`, `city`, `state`, `address`, `zip`, `lat`, `long`, `short_name`, `full_name`)
- `GET /api/dealer/<id>/` - Get dealer by ID
- `GET /api/fetchDealer/<id>/` - Get dealer by ID (MongoDB style with `_id`)

### Review Endpoints
- `GET /api/fetchReviews/dealer/<id>` - Get reviews for a dealer
- `POST /api/review/` - Submit a new review
- `GET /api/analyze/` - Analyze sentiment of review text (query param)
- `GET /api/analyze/<text>` - Analyze sentiment of review text (path param)

### Car Endpoints
- `GET /api/djangoapp/get_cars` - Get all car makes and models (returns `CarModels` array with `CarMake`/`CarModel`)
- `GET /api/car_makes/` - Get all car makes and models

### Authentication Endpoints
- `POST /api/djangoapp/login` - User login (accepts `userName` and `password`)
- `GET /api/djangoapp/logout` - User logout (returns `userName` and `status`)
- `POST /api/login/` - User login
- `POST /api/logout/` - User logout
- `POST /api/register/` - User registration

### Static Pages
- `GET /api/about/` - About Us page
- `GET /api/contact/` - Contact Us page
- `GET /` - Homepage

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- pip
- Django 6.1.2

### Installation
1. Clone the repository
2. Navigate to the server directory:
   ```bash
   cd server
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Populate the database with sample data:
   ```bash
   python manage.py populate_db
   ```
6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Accessing the Application
- Homepage: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/
- API Base: http://localhost:8000/api/

## Database Models

### CarMake
- name: CharField
- description: TextField

### CarModel
- car_make: ForeignKey to CarMake
- name: CharField
- year: IntegerField

### Dealer
- full_name: CharField
- city: CharField
- address: TextField
- zip: CharField
- state: CharField
- lat: FloatField
- long: FloatField
- short_name: CharField
- st: CharField

### Review
- dealership: IntegerField
- name: CharField
- purchase: BooleanField
- review: TextField
- purchase_date: DateField
- car_make: CharField
- car_model: CharField
- car_year: IntegerField
- sentiment: CharField

## Testing
Run tests using:
```bash
python manage.py test
```

## Docker Deployment
Build and run with Docker:
```bash
docker build -t dealership-app .
docker run -p 8000:8000 dealership-app
```

## CI/CD
The project uses GitHub Actions for continuous integration and deployment. The workflow includes:
- Code checkout
- Python environment setup
- Dependency installation
- Database migrations
- Test execution
- Build verification
- Deployment steps

## Admin Access
- Username: root
- Password: root123
- Access the admin panel at: http://localhost:8000/admin/

## License
This project is part of the Full-stack Development Capstone Project for educational purposes.
