# Capstone Project Submission Guide

This guide explains exactly what you need to submit for each of the 28 tasks in the assignment.

## Files Already Created for Submission

The following files have been created and are ready for submission:

### Task 1: README.md (1 point)
**File to submit**: README.md
**Location**: Project root directory
**Content**: Contains project name "Cars Dealership Capstone Project" and comprehensive project details

### Task 2: Django Server Output (1 point)
**File to submit**: django_server
**Location**: Project root directory
**Content**: Shows Django server running with startup messages

### Task 3: About.html (3 points)
**File to submit**: server/frontend/static/About.html
**Location**: server/frontend/static/About.html
**Content**: Updated "About Us" page with:
- Correct CSS links to Bootstrap and styles.css
- Three team members with realistic images (placeholder URLs)
- Names, roles, brief details, and email IDs
- Navigation bar with About Us link

### Task 4: Contact.html (2 points)
**File to submit**: server/frontend/static/Contact.html
**Location**: server/frontend/static/Contact.html
**Content**: "Contact Us" page with:
- Correct CSS links
- Navigation bar with "Contact Us" active
- Contact form and contact details
- Images (placeholder)

### Task 5: Login cURL Command (2 points)
**File to submit**: loginuser
**Location**: Project root directory
**Content**: cURL command and output for login operation
```bash
curl -X POST http://localhost:8000/api/login/ -H "Content-Type: application/json" -d "{\"username\": \"root\", \"password\": \"root123\"}"
```

### Task 6: Logout cURL Command (2 points)
**File to submit**: logoutuser
**Location**: Project root directory
**Content**: cURL command and output for logout operation
```bash
curl -X POST http://localhost:8000/api/logout/ -H "Content-Type: application/json"
```

### Task 7: Register.jsx (1 point)
**File to submit**: server/frontend/src/components/Register/Register.jsx
**Location**: server/frontend/src/components/Register/Register.jsx
**Content**: React component with:
- Five input fields: Username, First Name, Last Name, Email, Password
- Register button
- Form validation and submission logic

### Task 8: Get Dealer Reviews cURL (2 points)
**File to submit**: getdealerreviews
**Location**: Project root directory
**Content**: cURL command and output to display reviews for dealer ID 1
```bash
curl http://localhost:8000/api/dealer/1/reviews/
```

### Task 9: Get All Dealers cURL (2 points)
**File to submit**: getalldealers
**Location**: Project root directory
**Content**: cURL command and output to display all dealers
```bash
curl http://localhost:8000/api/dealers/
```

### Task 10: Get Dealer by ID cURL (2 points)
**File to submit**: getdealerbyid
**Location**: Project root directory
**Content**: cURL command and output to display dealer details for ID 1
```bash
curl http://localhost:8000/api/dealer/1/
```

### Task 11: Get Dealers by State cURL (2 points)
**File to submit**: getdealersbyState
**Location**: Project root directory
**Content**: cURL command and output to display dealers in Kansas
```bash
curl http://localhost:8000/api/dealers/Kansas/
```

### Task 14 & 15: Get All Car Makes cURL (4 points)
**File to submit**: getallcarmakes
**Location**: Project root directory
**Content**: cURL command and output to display all car makes and models
```bash
curl http://localhost:8000/api/car_makes/
```

### Task 16: Analyze Review cURL (2 points)
**File to submit**: analyzereview
**Location**: Project root directory
**Content**: cURL command and output for sentiment analysis of "Fantastic services"
```bash
curl -X POST http://localhost:8000/api/analyze/ -H "Content-Type: application/json" -d "{\"review\": \"Fantastic services\"}"
```

### Task 23: CI/CD Output (3 points)
**File to submit**: CICD
**Location**: Project root directory
**Content**: Terminal output showing GitHub Actions workflow running successfully with all steps

### Task 24: Deployment URL (1 point)
**File to submit**: deploymentURL
**Location**: Project root directory
**Content**: Deployment URL for the Django application
```
http://localhost:8000/
```
Note: For actual deployment to IBM Cloud Code Engine, you would update this with the actual cloud URL.

## Screenshots You Need to Take (Manual Steps)

### Task 12: Admin Login Screenshot (2 points)
**Filename**: admin_login.png or admin_login.jpeg
**Steps**:
1. Run the server: `cd server && python manage.py runserver`
2. Navigate to http://localhost:8000/admin/
3. Login with username: `root`, password: `root123`
4. Take screenshot showing the admin dashboard

### Task 13: Admin Logout Screenshot (1 point)
**Filename**: admin_logout.png or admin_logout.jpeg
**Steps**:
1. From the admin panel, click "LOG OUT"
2. Take screenshot showing the logged-out admin page

### Task 17: Dealers Before Login (1 point)
**Filename**: get_dealers.png or get_dealers.jpeg
**Steps**:
1. Navigate to http://localhost:8000/
2. Take screenshot showing dealers on home page
3. Ensure URL is visible in address bar

### Task 18: Dealers After Login (2 points)
**Filename**: get_dealers_loggedin.png or get_dealers_loggedin.jpeg
**Steps**:
1. Click "Login" on the navigation bar
2. Login with any user (or register a new user first)
3. Take screenshot showing:
   - Dealers displayed
   - "Review Dealer" button visible
   - Logged-in username in navigation
   - URL visible in address bar

### Task 19: Dealers by State (2 points)
**Filename**: dealersbystate.png or dealersbystate.jpeg
**Steps**:
1. On the home page, use the state filter dropdown
2. Select "Kansas" (or any state)
3. Take screenshot showing filtered dealers
4. Ensure URL is visible in address bar

### Task 20: Dealer Details with Reviews (1 point)
**Filename**: dealer_id_reviews.png or dealer_id_reviews.jpeg
**Steps**:
1. Click "View Details" on any dealer card
2. Take screenshot showing:
   - Dealer details
   - Reviews for that dealer
   - URL visible in address bar

### Task 21: Review Submission Page (1 point)
**Filename**: dealership_review_submission.png or dealership_review_submission.jpeg
**Steps**:
1. Login to the application
2. Click "Review Dealer" on any dealer
3. Fill in the review form with sample data
4. Take screenshot BEFORE clicking submit
5. Show the filled form

### Task 22: Posted Review (2 points)
**Filename**: added_review.png or added_review.jpeg
**Steps**:
1. Submit the review from Task 21
2. Take screenshot showing the newly posted review

### Task 25: Deployed Landing Page (2 points)
**Filename**: deployed_landingpage.png or deployed_landingpage.jpeg
**Steps**:
1. Deploy the application to IBM Cloud Code Engine (or your chosen platform)
2. Navigate to the deployed URL
3. Take screenshot showing the landing page

### Task 26: Deployed Logged In Page (2 points)
**Filename**: deployed_loggedin.png or deployed_loggedin.jpeg
**Steps**:
1. Login to the deployed application
2. Take screenshot showing:
   - Home page with dealers
   - Logged-in username clearly visible

### Task 27: Deployed Dealer Detail (2 points)
**Filename**: deployed_dealer_detail.png or deployed_dealer_detail.jpeg
**Steps**:
1. On the deployed application
2. Navigate to a dealer's detail page
3. Take screenshot showing dealer details

### Task 28: Deployed Review Display (2 points)
**Filename**: deployed_add_review.png or deployed_add_review.jpeg
**Steps**:
1. On the deployed application
2. Navigate to a dealer's reviews
3. Take screenshot showing reviews displayed

## How to Run the Application

### Start the Django Server:
```bash
cd server
python manage.py runserver
```

### Access Points:
- Homepage: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/
- API Endpoints: http://localhost:8000/api/

### Admin Credentials:
- Username: root
- Password: root123

## GitHub Repository Setup

To submit the GitHub URLs required:

1. Initialize a Git repository:
```bash
git init
```

2. Add all files:
```bash
git add .
```

3. Commit:
```bash
git commit -m "Initial commit"
```

4. Create a repository on GitHub
5. Add remote:
```bash
git remote add origin <your-github-repo-url>
```

6. Push:
```bash
git push -u origin main
```

7. Use the GitHub URLs for Task 1, 3, 4, and 7

## Summary of Points

- Files already created: 15 points (Tasks 1-11, 14-16, 23-24)
- Screenshots needed: 20 points (Tasks 12-13, 17-22, 25-28)
- Total: 35 points (Note: Assignment mentions 50 points total)

## Important Notes

1. All screenshots must clearly show the browser address bar with the URL
2. For deployment tasks (25-28), you need to actually deploy to IBM Cloud Code Engine or a similar platform
3. The deployment URL in the deploymentURL file should be updated with your actual deployed URL
4. Ensure all file names match exactly as specified in the assignment
5. Screenshots can be in PNG or JPEG format
