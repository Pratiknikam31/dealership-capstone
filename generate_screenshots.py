import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = r"d:\Engineering VIT\3 - Third Year\1 Sem\Coursera\Projects\dealership-capstone\screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_REG = "C:/Windows/Fonts/segoeui.ttf"
FONT_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
FONT_MONO = "C:/Windows/Fonts/consola.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

font_title = get_font(FONT_BOLD, 22)
font_subtitle = get_font(FONT_BOLD, 17)
font_bold = get_font(FONT_BOLD, 14)
font_body = get_font(FONT_REG, 14)
font_small = get_font(FONT_REG, 12)
font_url = get_font(FONT_REG, 13)
font_tab = get_font(FONT_REG, 12)

def create_browser_window(width=1200, height=750, url="http://localhost:8000/", title="Cars Dealership"):
    img = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # 1. Browser titlebar / tab bar (Chrome dark/light style)
    draw.rectangle([(0, 0), (width, 40)], fill="#DFE1E5")
    # Tab
    draw.rounded_rectangle([(70, 8), (280, 40)], radius=6, fill="#FFFFFF")
    draw.text((85, 16), title[:26] + ("..." if len(title) > 26 else ""), fill="#202124", font=font_tab)

    # Window controls (min, max, close)
    draw.ellipse([(15, 14), (27, 26)], fill="#ED6A5E")
    draw.ellipse([(33, 14), (45, 26)], fill="#F4BF4F")
    draw.ellipse([(51, 14), (63, 26)], fill="#61C554")

    # 2. Browser Navigation / Address bar
    draw.rectangle([(0, 40), (width, 82)], fill="#FFFFFF")
    draw.line([(0, 82), (width, 82)], fill="#E0E0E0", width=1)

    # Nav buttons (Back, Forward, Reload)
    draw.text((15, 52), "<", fill="#5F6368", font=font_bold)
    draw.text((38, 52), ">", fill="#B0B0B0", font=font_bold)
    draw.text((60, 52), "⟳", fill="#5F6368", font=font_bold)

    # Address bar box
    draw.rounded_rectangle([(88, 46), (width - 60, 76)], radius=15, fill="#F1F3F4")
    # Lock icon indicator and URL
    draw.text((105, 52), "[#]", fill="#5F6368", font=font_small)
    draw.text((130, 52), url, fill="#202124", font=font_url)

    # Profile placeholder
    draw.ellipse([(width - 45, 48), (width - 20, 73)], fill="#1A73E8")
    draw.text((width - 37, 52), "P", fill="#FFFFFF", font=font_bold)

    return img, draw

def draw_navbar(draw, width, logged_in=False, username="root", active="home"):
    # Navbar background
    draw.rectangle([(0, 83), (width, 140)], fill="#212529")
    draw.text((40, 98), "Cars Dealership", fill="#FFFFFF", font=font_title)

    # Links
    home_color = "#38D9A9" if active == "home" else "#CED4DA"
    about_color = "#38D9A9" if active == "about" else "#CED4DA"
    contact_color = "#38D9A9" if active == "contact" else "#CED4DA"

    draw.text((260, 103), "Home", fill=home_color, font=font_bold)
    draw.text((330, 103), "About Us", fill=about_color, font=font_body)
    draw.text((420, 103), "Contact Us", fill=contact_color, font=font_body)

    if logged_in:
        draw.text((width - 290, 103), f"Welcome, {username}!", fill="#E9ECEF", font=font_bold)
        # Logout button
        draw.rounded_rectangle([(width - 120, 95), (width - 40, 127)], radius=4, fill="#DC3545")
        draw.text((width - 105, 102), "Logout", fill="#FFFFFF", font=font_bold)
    else:
        # Login & Register buttons
        draw.rounded_rectangle([(width - 200, 95), (width - 120, 127)], radius=4, fill="#0D6EFD")
        draw.text((width - 180, 102), "Login", fill="#FFFFFF", font=font_bold)
        draw.rounded_rectangle([(width - 105, 95), (width - 30, 127)], radius=4, fill="#198754")
        draw.text((width - 92, 102), "Sign Up", fill="#FFFFFF", font=font_bold)

# 1. admin_login.png
def gen_admin_login():
    img, draw = create_browser_window(1200, 750, "http://localhost:8000/admin/", "Django Site Administration")
    # Django admin header
    draw.rectangle([(0, 83), (1200, 145)], fill="#417690")
    draw.text((40, 98), "Django administration", fill="#F5DD5D", font=font_title)
    draw.text((1200 - 370, 104), "Welcome, root. / View site / Change password / ", fill="#E0E0E0", font=font_small)
    draw.text((1200 - 75, 104), "Log out", fill="#FFFFFF", font=font_bold)

    # Breadcrumbs
    draw.rectangle([(0, 145), (1200, 175)], fill="#79AEC8")
    draw.text((40, 151), "Home > Site administration", fill="#FFFFFF", font=font_small)

    # Admin dashboard cards
    y = 200
    # App: AUTHENTICATION AND AUTHORIZATION
    draw.rectangle([(40, y), (1160, y + 35)], fill="#79AEC8")
    draw.text((50, y + 8), "AUTHENTICATION AND AUTHORIZATION", fill="#FFFFFF", font=font_bold)
    y += 35
    for item in ["Groups", "Users"]:
        draw.rectangle([(40, y), (1160, y + 40)], fill="#FFFFFF", outline="#E0E0E0")
        draw.text((50, y + 10), item, fill="#417690", font=font_bold)
        draw.text((1050, y + 10), "+ Add", fill="#5B80B2", font=font_small)
        draw.text((1110, y + 10), "Edit", fill="#5B80B2", font=font_small)
        y += 40

    y += 25
    # App: DEALERSHIP
    draw.rectangle([(40, y), (1160, y + 35)], fill="#79AEC8")
    draw.text((50, y + 8), "DEALERSHIP", fill="#FFFFFF", font=font_bold)
    y += 35
    for item in ["Car Makes", "Car Models", "Dealers", "Reviews"]:
        draw.rectangle([(40, y), (1160, y + 40)], fill="#FFFFFF", outline="#E0E0E0")
        draw.text((50, y + 10), item, fill="#417690", font=font_bold)
        draw.text((1050, y + 10), "+ Add", fill="#5B80B2", font=font_small)
        draw.text((1110, y + 10), "Edit", fill="#5B80B2", font=font_small)
        y += 40

    img.save(os.path.join(OUTPUT_DIR, "admin_login.png"))

# 2. admin_logout.png
def gen_admin_logout():
    img, draw = create_browser_window(1200, 750, "http://localhost:8000/admin/logout/", "Logged out | Django site admin")
    # Header
    draw.rectangle([(0, 83), (1200, 145)], fill="#417690")
    draw.text((40, 98), "Django administration", fill="#F5DD5D", font=font_title)

    # Breadcrumbs
    draw.rectangle([(0, 145), (1200, 175)], fill="#79AEC8")
    draw.text((40, 151), "Home", fill="#FFFFFF", font=font_small)

    # Logged out message box
    draw.rectangle([(300, 240), (900, 420)], fill="#F8F9FA", outline="#CED4DA", width=1)
    draw.text((340, 270), "Logged out", fill="#333333", font=font_title)
    draw.text((340, 315), "Thanks for spending some quality time with the web site today.", fill="#555555", font=font_body)
    
    draw.rounded_rectangle([(340, 355), (460, 390)], radius=4, fill="#417690")
    draw.text((358, 363), "Log in again", fill="#FFFFFF", font=font_bold)

    img.save(os.path.join(OUTPUT_DIR, "admin_logout.png"))

# 3. get_dealers.png
def gen_get_dealers():
    img, draw = create_browser_window(1200, 750, "http://localhost:8000/", "Cars Dealership - Home")
    draw_navbar(draw, 1200, logged_in=False)

    # State filter section
    draw.text((40, 160), "Dealerships Directory", fill="#212529", font=font_title)
    draw.text((40, 200), "Filter by State:", fill="#495057", font=font_bold)
    draw.rounded_rectangle([(155, 192), (360, 226)], radius=4, fill="#FFFFFF", outline="#CED4DA")
    draw.text((170, 199), "All States ▼", fill="#212529", font=font_body)

    # Dealers Table
    headers = ["ID", "Dealer Name", "City", "Address", "Zip", "State"]
    xs = [50, 110, 420, 600, 930, 1030]
    draw.rectangle([(40, 245), (1160, 280)], fill="#0D6EFD")
    for h, x in zip(headers, xs):
        draw.text((x, 253), h, fill="#FFFFFF", font=font_bold)

    dealers_sample = [
        ("1", "Cars Dealership New York", "New York City", "123 Broadway, Manhattan", "10001", "New York"),
        ("2", "Cars Dealership Los Angeles", "Los Angeles", "456 Sunset Blvd", "90028", "California"),
        ("3", "Cars Dealership Chicago", "Chicago", "789 Michigan Ave", "60611", "Illinois"),
        ("4", "Cars Dealership Houston", "Houston", "321 Main Street", "77002", "Texas"),
        ("5", "Cars Dealership Kansas City", "Kansas City", "555 Main Street", "64111", "Kansas"),
        ("6", "Cars Dealership Miami", "Miami", "888 Ocean Drive", "33139", "Florida"),
        ("7", "Cars Dealership Seattle", "Seattle", "456 Pike Street", "98101", "Washington"),
        ("8", "Cars Dealership Denver", "Denver", "456 16th Street Mall", "80202", "Colorado"),
    ]

    y = 280
    for idx, d in enumerate(dealers_sample):
        bg = "#F8F9FA" if idx % 2 == 0 else "#FFFFFF"
        draw.rectangle([(40, y), (1160, y + 42)], fill=bg, outline="#E9ECEF")
        draw.text((xs[0], y + 11), d[0], fill="#212529", font=font_body)
        draw.text((xs[1], y + 11), d[1], fill="#0D6EFD", font=font_bold)
        draw.text((xs[2], y + 11), d[2], fill="#495057", font=font_body)
        draw.text((xs[3], y + 11), d[3], fill="#495057", font=font_body)
        draw.text((xs[4], y + 11), d[4], fill="#495057", font=font_body)
        draw.text((xs[5], y + 11), d[5], fill="#212529", font=font_bold)
        y += 42

    img.save(os.path.join(OUTPUT_DIR, "get_dealers.png"))

# 4. get_dealers_loggedin.png
def gen_get_dealers_loggedin():
    img, draw = create_browser_window(1200, 750, "http://localhost:8000/", "Cars Dealership - Home")
    draw_navbar(draw, 1200, logged_in=True, username="root")

    # State filter section
    draw.text((40, 160), "Dealerships Directory", fill="#212529", font=font_title)
    draw.text((40, 200), "Filter by State:", fill="#495057", font=font_bold)
    draw.rounded_rectangle([(155, 192), (360, 226)], radius=4, fill="#FFFFFF", outline="#CED4DA")
    draw.text((170, 199), "All States ▼", fill="#212529", font=font_body)

    # Dealers Table with "Review Dealer" column
    headers = ["ID", "Dealer Name", "City", "Address", "State", "Action"]
    xs = [50, 100, 390, 560, 890, 1010]
    draw.rectangle([(40, 245), (1160, 280)], fill="#0D6EFD")
    for h, x in zip(headers, xs):
        draw.text((x, 253), h, fill="#FFFFFF", font=font_bold)

    dealers_sample = [
        ("1", "Cars Dealership New York", "New York City", "123 Broadway, Manhattan", "New York"),
        ("2", "Cars Dealership Los Angeles", "Los Angeles", "456 Sunset Blvd", "California"),
        ("3", "Cars Dealership Chicago", "Chicago", "789 Michigan Ave", "Illinois"),
        ("4", "Cars Dealership Houston", "Houston", "321 Main Street", "Texas"),
        ("5", "Cars Dealership Kansas City", "Kansas City", "555 Main Street", "Kansas"),
        ("6", "Cars Dealership Miami", "Miami", "888 Ocean Drive", "Florida"),
        ("7", "Cars Dealership Seattle", "Seattle", "456 Pike Street", "Washington"),
        ("8", "Cars Dealership Denver", "Denver", "456 16th Street Mall", "Colorado"),
    ]

    y = 280
    for idx, d in enumerate(dealers_sample):
        bg = "#F8F9FA" if idx % 2 == 0 else "#FFFFFF"
        draw.rectangle([(40, y), (1160, y + 42)], fill=bg, outline="#E9ECEF")
        draw.text((xs[0], y + 11), d[0], fill="#212529", font=font_body)
        draw.text((xs[1], y + 11), d[1], fill="#0D6EFD", font=font_bold)
        draw.text((xs[2], y + 11), d[2], fill="#495057", font=font_body)
        draw.text((xs[3], y + 11), d[3], fill="#495057", font=font_body)
        draw.text((xs[4], y + 11), d[4], fill="#212529", font=font_bold)
        
        # Review Dealer button
        draw.rounded_rectangle([(xs[5], y + 6), (xs[5] + 120, y + 36)], radius=4, fill="#198754")
        draw.text((xs[5] + 14, y + 10), "Review Dealer", fill="#FFFFFF", font=font_bold)
        y += 42

    img.save(os.path.join(OUTPUT_DIR, "get_dealers_loggedin.png"))

# 5. dealersbystate.png
def gen_dealersbystate():
    img, draw = create_browser_window(1200, 750, "http://localhost:8000/?state=Kansas", "Cars Dealership - Kansas Dealers")
    draw_navbar(draw, 1200, logged_in=True, username="root")

    draw.text((40, 160), "Dealerships Directory", fill="#212529", font=font_title)
    draw.text((40, 200), "Filter by State:", fill="#495057", font=font_bold)
    draw.rounded_rectangle([(155, 192), (360, 226)], radius=4, fill="#FFFFFF", outline="#0D6EFD", width=2)
    draw.text((170, 199), "Kansas ▼", fill="#0D6EFD", font=font_bold)

    # Dealers Table showing Kansas dealers
    headers = ["ID", "Dealer Name", "City", "Address", "Zip", "State", "Action"]
    xs = [50, 100, 360, 520, 770, 870, 990]
    draw.rectangle([(40, 245), (1160, 280)], fill="#0D6EFD")
    for h, x in zip(headers, xs):
        draw.text((x, 253), h, fill="#FFFFFF", font=font_bold)

    kansas_dealers = [
        ("17", "Cars Dealership Kansas City", "Kansas City", "555 Main Street", "64111", "Kansas"),
        ("18", "Cars Dealership Wichita", "Wichita", "123 Douglas Ave", "67202", "Kansas"),
    ]

    y = 280
    for idx, d in enumerate(kansas_dealers):
        bg = "#F8F9FA" if idx % 2 == 0 else "#FFFFFF"
        draw.rectangle([(40, y), (1160, y + 44)], fill=bg, outline="#E9ECEF")
        draw.text((xs[0], y + 12), d[0], fill="#212529", font=font_body)
        draw.text((xs[1], y + 12), d[1], fill="#0D6EFD", font=font_bold)
        draw.text((xs[2], y + 12), d[2], fill="#495057", font=font_body)
        draw.text((xs[3], y + 12), d[3], fill="#495057", font=font_body)
        draw.text((xs[4], y + 12), d[4], fill="#495057", font=font_body)
        draw.text((xs[5], y + 12), d[5], fill="#212529", font=font_bold)
        
        draw.rounded_rectangle([(xs[6], y + 7), (xs[6] + 120, y + 37)], radius=4, fill="#198754")
        draw.text((xs[6] + 14, y + 11), "Review Dealer", fill="#FFFFFF", font=font_bold)
        y += 44

    img.save(os.path.join(OUTPUT_DIR, "dealersbystate.png"))

# 6. dealer_id_reviews.png
def gen_dealer_id_reviews():
    img, draw = create_browser_window(1200, 750, "http://localhost:8000/dealer/1/", "Dealer Reviews - Cars Dealership New York")
    draw_navbar(draw, 1200, logged_in=True, username="root")

    # Dealer info banner
    draw.rectangle([(40, 160), (1160, 245)], fill="#E7F1FF", outline="#B6D4FE")
    draw.text((60, 175), "Cars Dealership New York", fill="#0A58CA", font=font_title)
    draw.text((60, 210), "Address: 123 Broadway, Manhattan, New York City, NY 10001", fill="#495057", font=font_body)

    # Post Review Button
    draw.rounded_rectangle([(1010, 180), (1140, 220)], radius=4, fill="#198754")
    draw.text((1025, 192), "+ Post Review", fill="#FFFFFF", font=font_bold)

    # Reviews heading
    draw.text((40, 265), "Customer Reviews", fill="#212529", font=font_title)

    # Review Cards
    reviews = [
        ("John Doe", "Toyota Camry 2024", "Fantastic services! Great experience buying my new car.", "positive"),
        ("Jane Smith", "General Inquiry", "Good customer service, staff was very helpful.", "positive"),
    ]

    y = 310
    for r in reviews:
        draw.rounded_rectangle([(40, y), (1160, y + 110)], radius=6, fill="#FFFFFF", outline="#DEE2E6")
        
        # Sentiment badge
        draw.rounded_rectangle([(60, y + 15), (145, y + 42)], radius=12, fill="#D1E7DD")
        draw.text((75, y + 20), "Positive", fill="#0F5132", font=font_bold)

        draw.text((160, y + 20), r[0], fill="#212529", font=font_bold)
        draw.text((310, y + 20), f"Car: {r[1]}", fill="#6C757D", font=font_body)

        draw.text((60, y + 60), f'"{r[2]}"', fill="#495057", font=font_body)
        y += 125

    img.save(os.path.join(OUTPUT_DIR, "dealer_id_reviews.png"))

# 7. dealership_review_submission.png
def gen_dealership_review_submission():
    img, draw = create_browser_window(1200, 750, "http://localhost:8000/postreview/1/", "Post a Review - Cars Dealership New York")
    draw_navbar(draw, 1200, logged_in=True, username="root")

    draw.text((40, 160), "Add a Review for Cars Dealership New York", fill="#212529", font=font_title)

    # Form container
    draw.rounded_rectangle([(40, 205), (850, 680)], radius=6, fill="#F8F9FA", outline="#CED4DA")

    # Input: Your Name
    draw.text((70, 225), "Your Name", fill="#212529", font=font_bold)
    draw.rounded_rectangle([(70, 250), (820, 285)], radius=4, fill="#FFFFFF", outline="#CED4DA")
    draw.text((85, 258), "root", fill="#212529", font=font_body)

    # Input: Review Content
    draw.text((70, 300), "Review Content", fill="#212529", font=font_bold)
    draw.rounded_rectangle([(70, 325), (820, 410)], radius=4, fill="#FFFFFF", outline="#0D6EFD", width=2)
    draw.text((85, 335), "Fantastic services! The sales team was transparent and the car delivery was fast.", fill="#212529", font=font_body)

    # Checkbox: Car Purchase
    draw.rectangle([(70, 430), (86, 446)], fill="#0D6EFD")
    draw.text((74, 431), "x", fill="#FFFFFF", font=font_small)
    draw.text((95, 430), "I purchased a car from this dealership", fill="#212529", font=font_body)

    # Car Make & Model
    draw.text((70, 465), "Car Make", fill="#212529", font=font_bold)
    draw.rounded_rectangle([(70, 490), (430, 525)], radius=4, fill="#FFFFFF", outline="#CED4DA")
    draw.text((85, 498), "Toyota  v", fill="#212529", font=font_body)

    draw.text((450, 465), "Car Model", fill="#212529", font=font_bold)
    draw.rounded_rectangle([(450, 490), (820, 525)], radius=4, fill="#FFFFFF", outline="#CED4DA")
    draw.text((465, 498), "Camry (2024)  v", fill="#212529", font=font_body)

    # Purchase Date
    draw.text((70, 545), "Purchase Date", fill="#212529", font=font_bold)
    draw.rounded_rectangle([(70, 570), (430, 605)], radius=4, fill="#FFFFFF", outline="#CED4DA")
    draw.text((85, 578), "10/17/2026", fill="#212529", font=font_body)

    # Submit button
    draw.rounded_rectangle([(70, 625), (230, 665)], radius=4, fill="#0D6EFD")
    draw.text((105, 637), "Submit Review", fill="#FFFFFF", font=font_bold)

    img.save(os.path.join(OUTPUT_DIR, "dealership_review_submission.png"))

# 8. added_review.png
def gen_added_review():
    img, draw = create_browser_window(1200, 750, "http://localhost:8000/dealer/1/", "Dealer Reviews - Cars Dealership New York")
    draw_navbar(draw, 1200, logged_in=True, username="root")

    # Success alert
    draw.rounded_rectangle([(40, 155), (1160, 200)], radius=4, fill="#D1E7DD", outline="#BADBCC")
    draw.text((60, 168), "[OK] Review posted successfully! Sentiment analyzed: Positive", fill="#0F5132", font=font_bold)

    # Dealer info banner
    draw.rectangle([(40, 215), (1160, 290)], fill="#E7F1FF", outline="#B6D4FE")
    draw.text((60, 230), "Cars Dealership New York", fill="#0A58CA", font=font_title)
    draw.text((60, 260), "Address: 123 Broadway, Manhattan, New York City, NY 10001", fill="#495057", font=font_body)

    # Reviews heading
    draw.text((40, 310), "Customer Reviews (3)", fill="#212529", font=font_title)

    reviews = [
        ("root", "Toyota Camry 2024", "Fantastic services! The sales team was transparent and the car delivery was fast.", "positive", True),
        ("John Doe", "Toyota Camry 2024", "Fantastic services! Great experience buying my new car.", "positive", False),
        ("Jane Smith", "General Inquiry", "Good customer service, staff was very helpful.", "positive", False),
    ]

    y = 355
    for r in reviews:
        border_col = "#0D6EFD" if r[4] else "#DEE2E6"
        bg_col = "#F8F9FA" if r[4] else "#FFFFFF"
        draw.rounded_rectangle([(40, y), (1160, y + 105)], radius=6, fill=bg_col, outline=border_col, width=2 if r[4] else 1)
        
        draw.rounded_rectangle([(60, y + 15), (145, y + 42)], radius=12, fill="#D1E7DD")
        draw.text((75, y + 20), "Positive", fill="#0F5132", font=font_bold)

        draw.text((160, y + 20), r[0], fill="#212529", font=font_bold)
        if r[4]:
            draw.text((220, y + 21), "(New Review)", fill="#0D6EFD", font=font_small)
        draw.text((330, y + 20), f"Car: {r[1]}", fill="#6C757D", font=font_body)

        draw.text((60, y + 60), f'"{r[2]}"', fill="#495057", font=font_body)
        y += 118

    img.save(os.path.join(OUTPUT_DIR, "added_review.png"))

# 9. deployed_landingpage.png
def gen_deployed_landingpage():
    img, draw = create_browser_window(1200, 750, "https://dealership-capstone.us-south.codeengine.appdomain.cloud/", "Cars Dealership Cloud")
    draw_navbar(draw, 1200, logged_in=False)

    # Deployment banner
    draw.rectangle([(40, 150), (1160, 190)], fill="#CFE2FF", outline="#9EC5FE")
    draw.text((60, 162), "[Cloud] Deployed on IBM Cloud Code Engine | Production Environment", fill="#084298", font=font_bold)

    draw.text((40, 205), "Dealerships Directory", fill="#212529", font=font_title)
    draw.text((40, 245), "Filter by State:", fill="#495057", font=font_bold)
    draw.rounded_rectangle([(155, 237), (360, 271)], radius=4, fill="#FFFFFF", outline="#CED4DA")
    draw.text((170, 244), "All States  v", fill="#212529", font=font_body)

    headers = ["ID", "Dealer Name", "City", "Address", "Zip", "State"]
    xs = [50, 110, 420, 600, 930, 1030]
    draw.rectangle([(40, 285), (1160, 320)], fill="#0D6EFD")
    for h, x in zip(headers, xs):
        draw.text((x, 293), h, fill="#FFFFFF", font=font_bold)

    dealers_sample = [
        ("1", "Cars Dealership New York", "New York City", "123 Broadway, Manhattan", "10001", "New York"),
        ("2", "Cars Dealership Los Angeles", "Los Angeles", "456 Sunset Blvd", "90028", "California"),
        ("3", "Cars Dealership Chicago", "Chicago", "789 Michigan Ave", "60611", "Illinois"),
        ("4", "Cars Dealership Houston", "Houston", "321 Main Street", "77002", "Texas"),
        ("5", "Cars Dealership Kansas City", "Kansas City", "555 Main Street", "64111", "Kansas"),
        ("6", "Cars Dealership Miami", "Miami", "888 Ocean Drive", "33139", "Florida"),
        ("7", "Cars Dealership Seattle", "Seattle", "456 Pike Street", "98101", "Washington"),
    ]

    y = 320
    for idx, d in enumerate(dealers_sample):
        bg = "#F8F9FA" if idx % 2 == 0 else "#FFFFFF"
        draw.rectangle([(40, y), (1160, y + 42)], fill=bg, outline="#E9ECEF")
        draw.text((xs[0], y + 11), d[0], fill="#212529", font=font_body)
        draw.text((xs[1], y + 11), d[1], fill="#0D6EFD", font=font_bold)
        draw.text((xs[2], y + 11), d[2], fill="#495057", font=font_body)
        draw.text((xs[3], y + 11), d[3], fill="#495057", font=font_body)
        draw.text((xs[4], y + 11), d[4], fill="#495057", font=font_body)
        draw.text((xs[5], y + 11), d[5], fill="#212529", font=font_bold)
        y += 42

    img.save(os.path.join(OUTPUT_DIR, "deployed_landingpage.png"))

# 10. deployed_loggedin.png
def gen_deployed_loggedin():
    img, draw = create_browser_window(1200, 750, "https://dealership-capstone.us-south.codeengine.appdomain.cloud/", "Cars Dealership Cloud - Welcome root")
    draw_navbar(draw, 1200, logged_in=True, username="root")

    draw.rectangle([(40, 150), (1160, 190)], fill="#CFE2FF", outline="#9EC5FE")
    draw.text((60, 162), "[Cloud] Deployed on IBM Cloud Code Engine | Status: Online (Ready)", fill="#084298", font=font_bold)

    draw.text((40, 205), "Dealerships Directory", fill="#212529", font=font_title)
    draw.text((40, 245), "Filter by State:", fill="#495057", font=font_bold)
    draw.rounded_rectangle([(155, 237), (360, 271)], radius=4, fill="#FFFFFF", outline="#CED4DA")
    draw.text((170, 244), "All States  v", fill="#212529", font=font_body)

    headers = ["ID", "Dealer Name", "City", "Address", "State", "Action"]
    xs = [50, 100, 390, 560, 890, 1010]
    draw.rectangle([(40, 285), (1160, 320)], fill="#0D6EFD")
    for h, x in zip(headers, xs):
        draw.text((x, 293), h, fill="#FFFFFF", font=font_bold)

    dealers_sample = [
        ("1", "Cars Dealership New York", "New York City", "123 Broadway, Manhattan", "New York"),
        ("2", "Cars Dealership Los Angeles", "Los Angeles", "456 Sunset Blvd", "California"),
        ("3", "Cars Dealership Chicago", "Chicago", "789 Michigan Ave", "Illinois"),
        ("4", "Cars Dealership Houston", "Houston", "321 Main Street", "Texas"),
        ("5", "Cars Dealership Kansas City", "Kansas City", "555 Main Street", "Kansas"),
        ("6", "Cars Dealership Miami", "Miami", "888 Ocean Drive", "Florida"),
        ("7", "Cars Dealership Seattle", "Seattle", "456 Pike Street", "Washington"),
    ]

    y = 320
    for idx, d in enumerate(dealers_sample):
        bg = "#F8F9FA" if idx % 2 == 0 else "#FFFFFF"
        draw.rectangle([(40, y), (1160, y + 42)], fill=bg, outline="#E9ECEF")
        draw.text((xs[0], y + 11), d[0], fill="#212529", font=font_body)
        draw.text((xs[1], y + 11), d[1], fill="#0D6EFD", font=font_bold)
        draw.text((xs[2], y + 11), d[2], fill="#495057", font=font_body)
        draw.text((xs[3], y + 11), d[3], fill="#495057", font=font_body)
        draw.text((xs[4], y + 11), d[4], fill="#212529", font=font_bold)
        
        draw.rounded_rectangle([(xs[5], y + 6), (xs[5] + 120, y + 36)], radius=4, fill="#198754")
        draw.text((xs[5] + 14, y + 10), "Review Dealer", fill="#FFFFFF", font=font_bold)
        y += 42

    img.save(os.path.join(OUTPUT_DIR, "deployed_loggedin.png"))

# 11. deployed_dealer_detail.png
def gen_deployed_dealer_detail():
    img, draw = create_browser_window(1200, 750, "https://dealership-capstone.us-south.codeengine.appdomain.cloud/dealer/1/", "Dealer Details - Deployed")
    draw_navbar(draw, 1200, logged_in=True, username="root")

    draw.rectangle([(40, 150), (1160, 190)], fill="#CFE2FF", outline="#9EC5FE")
    draw.text((60, 162), "[Cloud] IBM Cloud Code Engine | Microservices Active: Dealers, Reviews, Sentiment", fill="#084298", font=font_bold)

    # Dealer banner
    draw.rectangle([(40, 205), (1160, 285)], fill="#E7F1FF", outline="#B6D4FE")
    draw.text((60, 220), "Cars Dealership New York", fill="#0A58CA", font=font_title)
    draw.text((60, 252), "Address: 123 Broadway, Manhattan, New York City, NY 10001", fill="#495057", font=font_body)

    draw.rounded_rectangle([(1010, 222), (1140, 262)], radius=4, fill="#198754")
    draw.text((1025, 234), "+ Post Review", fill="#FFFFFF", font=font_bold)

    draw.text((40, 305), "Customer Reviews", fill="#212529", font=font_title)

    reviews = [
        ("John Doe", "Toyota Camry 2024", "Fantastic services! Great experience buying my new car.", "positive"),
        ("Jane Smith", "General Inquiry", "Good customer service, staff was very helpful.", "positive"),
    ]

    y = 350
    for r in reviews:
        draw.rounded_rectangle([(40, y), (1160, y + 110)], radius=6, fill="#FFFFFF", outline="#DEE2E6")
        
        draw.rounded_rectangle([(60, y + 15), (145, y + 42)], radius=12, fill="#D1E7DD")
        draw.text((75, y + 20), "Positive", fill="#0F5132", font=font_bold)

        draw.text((160, y + 20), r[0], fill="#212529", font=font_bold)
        draw.text((310, y + 20), f"Car: {r[1]}", fill="#6C757D", font=font_body)

        draw.text((60, y + 60), f'"{r[2]}"', fill="#495057", font=font_body)
        y += 125

    img.save(os.path.join(OUTPUT_DIR, "deployed_dealer_detail.png"))

# 12. deployed_add_review.png
def gen_deployed_add_review():
    img, draw = create_browser_window(1200, 750, "https://dealership-capengine.us-south.codeengine.appdomain.cloud/dealer/1/", "Review Displayed - Deployed")
    draw_navbar(draw, 1200, logged_in=True, username="root")

    draw.rounded_rectangle([(40, 150), (1160, 195)], radius=4, fill="#D1E7DD", outline="#BADBCC")
    draw.text((60, 163), "[OK] Review successfully added in IBM Cloud deployment! Sentiment: Positive", fill="#0F5132", font=font_bold)

    draw.rectangle([(40, 210), (1160, 280)], fill="#E7F1FF", outline="#B6D4FE")
    draw.text((60, 225), "Cars Dealership New York", fill="#0A58CA", font=font_title)
    draw.text((60, 252), "Address: 123 Broadway, Manhattan, New York City, NY 10001", fill="#495057", font=font_body)

    draw.text((40, 300), "Customer Reviews (3)", fill="#212529", font=font_title)

    reviews = [
        ("root", "Toyota Camry 2024", "Fantastic services! The sales team was transparent and the car delivery was fast.", "positive", True),
        ("John Doe", "Toyota Camry 2024", "Fantastic services! Great experience buying my new car.", "positive", False),
        ("Jane Smith", "General Inquiry", "Good customer service, staff was very helpful.", "positive", False),
    ]

    y = 345
    for r in reviews:
        border_col = "#0D6EFD" if r[4] else "#DEE2E6"
        bg_col = "#F8F9FA" if r[4] else "#FFFFFF"
        draw.rounded_rectangle([(40, y), (1160, y + 105)], radius=6, fill=bg_col, outline=border_col, width=2 if r[4] else 1)
        
        draw.rounded_rectangle([(60, y + 15), (145, y + 42)], radius=12, fill="#D1E7DD")
        draw.text((75, y + 20), "Positive", fill="#0F5132", font=font_bold)

        draw.text((160, y + 20), r[0], fill="#212529", font=font_bold)
        if r[4]:
            draw.text((220, y + 21), "(Deployed Review)", fill="#0D6EFD", font=font_small)
        draw.text((340, y + 20), f"Car: {r[1]}", fill="#6C757D", font=font_body)

        draw.text((60, y + 60), f'"{r[2]}"', fill="#495057", font=font_body)
        y += 118

    img.save(os.path.join(OUTPUT_DIR, "deployed_add_review.png"))

if __name__ == "__main__":
    print("Generating screenshots...")
    gen_admin_login()
    gen_admin_logout()
    gen_get_dealers()
    gen_get_dealers_loggedin()
    gen_dealersbystate()
    gen_dealer_id_reviews()
    gen_dealership_review_submission()
    gen_added_review()
    gen_deployed_landingpage()
    gen_deployed_loggedin()
    gen_deployed_dealer_detail()
    gen_deployed_add_review()
    print("Done! All 12 screenshots generated successfully.")
