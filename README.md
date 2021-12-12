# Gift Of Giving

## ![GiftOfGiving](/static/images/hero-img.webp)

[GiftOfGiving](https://gift-of-giving.herokuapp.com/) is a website which allows charities to request gifts for the children during the holiday season as well as for the donators to support the charities by choosing the gift they would like to donate.  

![Site display on different screens]()

---

## Contents

- [Gift Of Giving](#gift-of-giving)
  - [!GiftOfGiving](#)
  - [Contents](#contents)
  - [UX](#ux)
    - [Project Goals](#project-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [Site Visitor/User Goals](#site-visitoruser-goals)
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
      - [**Requirements**](#requirements)
      - [**Expectations**](#expectations)
    - [Design Choices](#design-choices)
      - [**Fonts**](#fonts)
      - [**Colours**](#colours)
  - [Wireframes](#wireframes)
    - [**Site Layout**](#site-layout)
  - [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Database Modelling](#database-modelling)
      - [**Profiles App**](#profiles-app)
        - [Profile](#profile)
        - [Charity Address](#charity-address)
      - [**Gifts App**](#gifts-app)
        - [Gift](#gift)
      - [**Contact App**](#contact-app)
        - [Contact](#contact)
  - [Technologies](#technologies)
    - [Languages](#languages)
    - [Libraries & Frameworks](#libraries--frameworks)
    - [Tools](#tools)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
      - [**User Account**](#user-account)
      - [**Super User**](#super-user)
    - [Future Features](#future-features)
    - [Redundant features](#redundant-features)
  - [Changes applied since planning](#changes-applied-since-planning)
  - [Testing](#testing)

---

## UX

### Project Goals

The main goal of this project is to support less fortunate children during holiday season by ensuring they don't go without presents. We are achieving this by offering the charities an opportunity to request gifts for the children as well as giving an opportunity to the donators to contribute towards a good cause by buying and sending the presents to the charities.

### Site Owner Goals

- Provide the users with a professional web application
- Connect charities with the donators
- Spread holiday cheer

### Site Visitor/User Goals

- View the mission purpose and how it works
- View the required gifts for the children
- Ability to add required gifts for the children
- Ability to choose which gifts they would like to donate
- Create a an account/profile
- Contact the site owners

### User Stories

**Applies to all site users:**

- As a user, I am able to access the site on my mobile, tablet, and desktop which is adapted to provide the best experience.

- As a user, I am able to easily navigate through the website without too much thought and find what I am looking for quickly.

- As a user, I am able to identify instantly what the site is all about and what it has to offer.

- As a user, I am able to contact the site owner using a simple form.

- As a user, I am able to find key information about the required gifts I am interested in buying (Charity name, age group, estimated price, etc)

**Applies to new site users:**

- As a user, I am able to  create an account.

**Applies to all returning users:**

- As a user, I am able to login to my existing account.

- As a user, I am able to view, save and update my personal information.

- As a user, I am able to add new required gifts, except if I am a donator.

- As a user, I am able to edit information about the gifts, except if I am a donator.

- As a user, I am able to mark the gift as received, except if I am a donator.

- As a user, I am able to see a list of the gifts that donors have reserved when I navigate to my profile, except if I am a donator.

- As a user, I am able to see a list of the gifts that I still require when I navigate to my profile, except if I am a donator.

- As a user, I am able to reserve required gifts, except if I am a charity.

- As a user, I am able to see list of the gifts I have reserved when I navigate to my profile, except if I am a charity.

- As a user, I am able to change or reset my password securely.

**Applies to a superuser (site owner):**

- As a user, I am able to verify the users that are charities to allow them to add gift requests.

- As a user, I am able to receive inquiries from the site users after they fill in the contact form straight to the database.

[Back to content](#contents)

### User Requirements and Expectations

#### **Requirements**

- Visually pleasant app design
- Easy site navigation
- Information of the content layed out in a simple and clear way on both mobile and larger screens
- Self-explanatory icons where text is absent

#### **Expectations**

- User information is protected by the site
- User can manipulate elements of the particular page
- Quick app load time

[Back to content](#contents)

### Design Choices

#### **Fonts**

- *All fonts*

  ```font-family: Baloo Bhaijaan 2', sans-serif;```

- *Special font - welcome container*

  ```font-family: ''Meow Script', cursive;```

#### **Colours**

![Colour palette](/docs/colour-pallette.PNG)

[Back to content](#contents)

## Wireframes

### **Site Layout**

Site moc-ups were designed using [balsamiq wireframes](https://balsamiq.com/). The focus was on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as mobile, tablet and larger screens.

You can view the wireframes created for this project in [site wireframes](/docs/wireframes.pdf) folder.

  **Please note, as we were developing the project, we have identified some weaknesses in the UX and therefore made the required changes. The deployed site looks somewhat different in comparison to the wireframes. These changes will allow the user to have a better experience and allow easier navigation. The design theme of the features is a close match to the overall site to ensure continuation and flow.*

[Back to content](#contents)

---

## Information Architecture

### Database Choice

### Database Modelling

#### **Profiles App**

##### Profile

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Username | user | ForeignKey | 'User', on_delete=models.CASCADE
Name | name | CharField | max_length=100, null=False, blank=False
Organisation Name | organisation_name | CharField | max_length=150, null=False, blank=False
Type | type | CharField | max_length=25, choices=USER_TYPE_CHOICES, null=False, blank=False
Verified | verified | BooleanField | default=False

##### Charity Address

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Username | user | ForeignKey | 'User', on_delete=models.CASCADE
Organisation Name | organisation_name | CharField | max_length=150, null=False, blank=False
Address Line 1 | address_line_one | CharField | max_length=150, null=False, blank=False
Address Line 2 | address_line_two | CharField | max_length=150, null=True, blank=True
Address Line 3 | address_line_three | CharField | max_length=150, null=True, blank=True
County | county | CharField | max_length=150, null=False, blank=False
Country | country | CharField | max_length=150, null=False, blank=False
Postcode | postcode | CharField | max_length=150, null=True, blank=True

#### **Gifts App**

##### Gift

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
ID | id | UUIDField | primary_key=True, default=uuid.uuid4, editable=False, max_length=36
Organisation Name | organisation_name | CharField | max_length=150, null=False, blank=False
Description | description | CharField | max_length=150, null=False, blank=False
Estimated Price | estimated_price | DecimalField | decimal_places=2, default=0, max_digits=6
Age Range | age_range | CharField | max_length=25, choices=AGE_RANGE_CHOICES, null=False, blank=False
Image | image | ImageField | upload_to='gift_images/', blank=True
Needed | needed | BooleanField | default=True
Committed | committed | BooleanField | default=False
Committed By | committed_by | ForeignKey | User, on_delete=models.CASCADE, null=True, blank=True
Received | received | BooleanField | default=False

#### **Contact App**

##### Contact

| **Title** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name | name | CharField | max_length=80, null=False, blank=False
Email | email | CharField | max_length=80, null=False, blank=False
Comments | comments | CharField | max_length=1500, null=False, blank=False

[Back to content](#contents)

---  

## Technologies

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Libraries & Frameworks

- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
- [jQuery](https://jquery.com/)
- [Popper JS](https://popper.js.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Gunicorn](https://pypi.org/project/gunicorn/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Google fonts](https://fonts.google.com/)
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)

### Tools

- [PIP](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Color editor](https://coolors.co/)
- [Favicons](https://fontawesome.com/icons?d=gallery)
- [Balsamiq](https://balsamiq.com/)

[Back to content](#contents)

---

## Features

The website is designed using four applications: `Home`, `Gifts`, `Profiles`,  and `Contact`.

### Implemented Features

- The site has **responsive design** when viewed on a mobile, tablet, and desktop.
- **Easy navigation** to external sites, such as social media accounts.
- The user is given feedback when they interact with the website (i.e. login to the website, add new gift, commit to buying a gift etc).

#### **User Account**

- The users can **create** an account where they can store account information such as their address and **edit** their details.
- The user can request a **password re-set**.

#### **Super User**

- The **Super User** can verify that the charity's information in the database, which would then allow the charities to add gifts once verified.

### Future Features

### Redundant features

[Back to content](#contents)

---

## Changes applied since planning

---

## Testing

Testing was done manually throughout the development process. The full rundown of the testing can be found in a separate [TESTING.md](TESTING.md) file.

[Back to content](#contents)

---
