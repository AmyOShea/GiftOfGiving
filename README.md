# Gift Of Giving

## ![GiftOfGiving](/static/images/hero-img.webp)

[GiftOfGiving](https://gift-of-giving.herokuapp.com/) is a website which allows charities to request gifts for the children during the holiday season as well as for the donators to support the charities by choosing the gift they would like to donate.  

![Site display on different screens]()

---

## Contents

- [UX](#ux)
  - [Project Goals](#project-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [Site Visitor/User Goals](#site-visitor-user-goals)
  - [User Stories](#user-stories)
  - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [**Requirements**](#--requirements--)
    - [**Expectations**](#--expectations--)
  - [Design Choices](#design-choices)
    - [**Fonts**](#--fonts--)
    - [**Colours**](#--colours--)
- [Wireframes](#wireframes)
  - [**Site Map**](#--site-map--)
  - [**Site Layout**](#--site-layout--)
- [Information Architecture](#information-architecture)
  - [Database Choice](#database-choice)
  - [Database Modelling](#database-modelling)
    - [**Profile App**](#--profile-app--)
      - [Profile](#profile)
    - [**Product App**](#--product-app--)
      - [Product Category](#product-category)
      - [Collection Name](#collection-name)
      - [Tag](#tag)
      - [Artwork Images](#artwork-images)
      - [Images Folder](#images-folder)
      - [Product](#product)
    - [**Checkout App**](#--checkout-app--)
      - [Order](#order)
      - [Order Line](#order-line)
    - [**Home App**](#--home-app--)
      - [About Section](#about-section)
      - [Social Media Icons](#social-media-icons)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Libraries & Frameworks](#libraries---frameworks)
  - [Tools](#tools)
- [Features](#features)
  - [Implemented Features](#implemented-features)
    - [**User Account**](#--user-account--)
    - [**Super User**](#--super-user--)
    - [**Gallery page**](#--gallery-page--)
    - [**Shop page**](#--shop-page--)
    - [**Shopping bag**](#--shopping-bag--)
    - [**Payments**](#--payments--)
  - [Future Features](#future-features)
  - [Redundant features](#redundant-features)
- [Changes applied since planning](#changes-applied-since-planning)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Deployment to Heroku](#deployment-to-heroku)
  - [Hosting Media files in AWS](#hosting-media-files-in-aws)
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
