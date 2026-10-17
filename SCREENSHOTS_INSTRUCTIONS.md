# Screenshots Required for Assignment Submission

This document lists all screenshots required for the capstone project submission. You will need to take these screenshots manually after running the application.

## Required Screenshots

### 1. Admin Login (admin_login.png or admin_login.jpeg)
- Navigate to http://localhost:8000/admin/
- Login with username: `root` and password: `root123`
- Take a screenshot showing the admin dashboard after successful login

### 2. Admin Logout (admin_logout.png or admin_logout.jpeg)
- From the admin panel, click logout
- Take a screenshot showing the logged-out state

### 3. Dealers Before Login (get_dealers.png or get_dealers.jpeg)
- Navigate to http://localhost:8000/
- Take a screenshot showing the dealers on the home page
- Ensure the URL is visible in the browser address bar
- Should show dealers without login/registration options active

### 4. Dealers After Login (get_dealers_loggedin.png or get_dealers_loggedin.jpeg)
- First, register a user or login using the login modal
- Navigate to http://localhost:8000/
- Take a screenshot showing:
  - Dealers displayed on the home page
  - The "Review Dealer" button visible on dealer cards
  - The logged-in username displayed in the navigation
  - The endpoint visible in the browser address bar

### 5. Dealers by State (dealersbystate.png or dealersbystate.jpeg)
- On the home page, use the state filter dropdown
- Select any state (e.g., "Kansas")
- Take a screenshot showing:
  - Filtered dealers for the selected state
  - The endpoint visible in the browser address bar (should show /api/dealers/Kansas/ or similar)

### 6. Dealer Details with Reviews (dealer_id_reviews.png or dealer_id_reviews.jpeg)
- Click on "View Details" for any dealer
- Take a screenshot showing:
  - Selected dealer details
  - Reviews displayed for that dealer
  - The endpoint visible in the browser address bar

### 7. Review Submission Page (dealership_review_submission.png or dealership_review_submission.jpeg)
- Login to the application
- Click "Review Dealer" on any dealer card
- Fill in the review form with sample data
- Take a screenshot BEFORE clicking submit
- Should show the review form with entered details

### 8. Posted Review (added_review.png or added_review.jpeg)
- After submitting the review
- Take a screenshot showing:
  - The newly posted review displayed
  - The review details visible

### 9. Deployed Landing Page (deployed_landingpage.png or deployed_landingpage.jpeg)
- After deploying to IBM Cloud Code Engine or your chosen platform
- Navigate to the deployed URL
- Take a screenshot showing the landing page

### 10. Deployed Logged In Page (deployed_loggedin.png or deployed_loggedin.jpeg)
- Login to the deployed application
- Take a screenshot showing:
  - The home page with dealers
  - The logged-in username clearly visible

### 11. Deployed Dealer Detail (deployed_dealer_detail.png or deployed_dealer_detail.jpeg)
- On the deployed application
- Navigate to a dealer's detail page
- Take a screenshot showing the dealer details

### 12. Deployed Review Display (deployed_add_review.png or deployed_add_review.jpeg)
- On the deployed application
- Navigate to a dealer's reviews
- Take a screenshot showing the reviews displayed

## How to Take Screenshots

### Windows:
- Press `Windows + Shift + S` to open the Snipping Tool
- Select the area you want to capture
- Save the image as PNG or JPEG

### Mac:
- Press `Command + Shift + 4` to capture a selected area
- The screenshot will be saved to your desktop

### Linux:
- Use `gnome-screenshot` or similar tools
- Or press `Print Screen` key

## File Naming
Ensure all screenshots are saved with the exact names specified in the assignment:
- admin_login.png or admin_login.jpeg
- admin_logout.png or admin_logout.jpeg
- get_dealers.png or get_dealers.jpeg
- get_dealers_loggedin.png or get_dealers_loggedin.jpeg
- dealersbystate.png or dealersbystate.jpeg
- dealer_id_reviews.png or dealer_id_reviews.jpeg
- dealership_review_submission.png or dealership_review_submission.jpeg
- added_review.png or added_review.jpeg
- deployed_landingpage.png or deployed_landingpage.jpeg
- deployed_loggedin.png or deployed_loggedin.jpeg
- deployed_dealer_detail.png or deployed_dealer_detail.jpeg
- deployed_add_review.png or deployed_add_review.jpeg
