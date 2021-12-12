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
  - [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Deployment to Heroku](#deployment-to-heroku)
  - [Credits](#credits)
    - [Images](#images)
    - [Image editing](#image-editing)
    - [Code ideas](#code-ideas)
  - [Acknowledgements](#acknowledgements)

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
- [Cloudinary](https://cloudinary.com/)

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

## Deployment

**GiftOfGiving** project was deployed using the **VS Code IDE**, using **Git** and **GitHub** for version control. It is hosted on **Heroku** and all media files are hosted in **Cloudinary**.

Before deploying the application, install the following:

- Python 3
- PIP
- Git
- Heroku CLI

### Local Deployment

To deploy Art-ial locally, take the following steps:

1. From the applications [repository](https://github.com/Daisy-McG/GiftOfGiving), click the *code* button and download the zip file.

    Alternatively, you can clone the repository using the following line in your terminal:

```terminal
git clone https://github.com/Daisy-McG/GiftOfGiving.git
```

2. Access the folder in your terminal window and install the application's required modules with the following command:

```terminal
pip3 install -r requirements.txt
```

3. Create `env.py` file to hold your environmental variables in the root level of the application:

```python

import os

os.environ.setdefault('DATABASE_URL', 'YOUR_DATABASE_URL')
os.environ.setdefault('SECRET_KEY', 'YOUR_DJANGO_SECRET_KEY')
os.environ.setdefault('DEVELOPMENT', '1')
os.environ.setdefault('CLOUDINARY_URL', 'YOUR_CLOUDINARY_KEY')
os.environ.setdefault('EMAIL_HOST_USER', 'YOUR_EMAIL_USER')
os.environ.setdefault('EMAIL_HOST_PASSWORD', 'YOUR_EMAIL_PASSWORD')
os.environ.setdefault('EMAIL_HOST', 'smtp.google.com') # if you use gmail 

```

If you plan to make your repository public, ensure you add `.env` file to `.gitignore` before committing.

4. If your IDE terminal, migrate the models to create the database using the following commands:

```terminal
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser to access the admin panel using the following command:

```terminal
python manage.py createsuperuser
```

Then follow the instructions to create the superuser.

6. After you login to the admin panel, you can add data to be displayed in your app for `GIFTS` app if required. Refer to [database modeling](#database-modelling).


7. To initiate the application, type the command `python manage.py runserver` in your terminal. The application is now available in your browser at the address: `http://localhoset:8000`

[Back to content](#contents)

### Deployment to Heroku

To deploy the app to Heroku, use the following steps:

1. Ensure you have the following dependancies installed in your app, such as PostgressSQL driver for Python, WSHI HTTP Server and dj database url that connects the the app with the database:

```terminal
pip3 install psycopg2-binary

pip3 install install gunicorn

pip3 install dj_database_url
```

2. If you haven't already, create `requirements.txt` file containing all of the dependancies:

```terminal
pip3 freeze > requirements.txt
```

3. Create a `Procfile` that contains the following: `web: gunicorn main.wsgi:application`.
4. Push these newly created files to your repository master.
5. Login to Heroku and create a new app.
6. In Heroku dashboard of the new app, click **deploy**, then **deployment** method and select **GitHub** to connect your app to your github repository for automatic deployment.
7. In Heroku Resources tab, navigate to **Add-Ons** section and search for **Heroku Postgres**. I recommend you choose hobby level for this application. You should also search for **Cloudinary - Image and Video Management** to ensure your media files load to Cloudinary.
8. In settings tab, navigate to **Reveal Config Vars** and add the following variables:

| **KEY**               | **VALUE**                          |
| --------------------- | -----------------------------------|
| CLOUDINARY_URL        | YOUR_CLOUDINARY_URL                |
| DATABASE_URL          | YOUR_DATABASE_URL                  |
| EMAIL_HOST            | smtp.google.com (if using gmail)   |
| EMAIL_HOST_PASS       | YOUR_EMAIL_PASSWORD                |
| EMAIL_HOST_USER       | YOUR_EMAIL_USER                    |
| SECRET_KEY            | YOUR_DJANGO_SECRET_KEY             |

9. In settings.py in your IDE, temporarily comment out the database and use below code instead (make sure you do not commit!):

```python
DATABASES = {
        'default': dj_database_url.parse('POSTGRESS URL')
    }
```

10. In terminal, migrate the models to create the Postgress database using the following commands:

```terminal
python manage.py makemigrations
python manage.py migrate
```

11. Create a superuser to access the admin panel using the following command:

```terminal
python manage.py createsuperuser
```

Then follow the instructions to create the superuser.

12.  After you login to the admin panel, you can add data to be displayed in your app for `GIFTS` app if required.

13. Remove the temporary database from settings.py and uncomment the original code, then push the code to origin.
14.  Back to in **Heroku dashboad**, deploy the application.
15.  To view the site, click on **View App**.

[Back to content](#contents)

---

## Credits

### Images

### Image editing

### Code ideas

[Back to content](#contents)

---

## Acknowledgements

[Back to content](#contents)
