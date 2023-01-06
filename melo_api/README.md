# Smart House Inventory

## Portfolio Project 4: Full Stack Toolkit

![Multi screen mockup](static/images/multi-device-mockup.png)

This project is built as part of the Code Institute Full Stack Software Development course. For this course, Dirk Ornee had to built a fourth Portfolio Project. Since his cousin just started a nail salon and was in dire need of a website with booking capabilities, what better way to build a fourth Portfolio Project and help somebody at the same time! Important note: this is not the actual live version that is used by the nail salon, this version is used purely as a project for Code Institute and users can book appointments freely (you won't suddenly be expected to show up at a nail salon).

## Live Site

[NailsbyFaar](https://nailsbyfaar.herokuapp.com/)

## Github Repository

[PortfolioProjectFour](https://github.com/DOdrums/PortfolioProjectFour)


<!-- TOC -->

- [Smart House Inventory](#smart-house-inventory)
    - [Portfolio Project 4: Full Stack Toolkit](#portfolio-project-4-full-stack-toolkit)
    - [Live Site](#live-site)
    - [Github Repository](#github-repository)
    - [UX](#ux)
        - [Business Goals](#business-goals)
        - [Target Audience](#target-audience)
        - [User Stories](#user-stories)
        - [Structure of the app](#structure-of-the-app)
        - [Logic/Database Diagram](#logicdatabase-diagram)
        - [Color Scheme](#color-scheme)
        - [Features](#features)
            - [Book page](#book-page)
            - [User dashboard](#user-dashboard)
            - [Home](#home)
            - [Nav bar](#nav-bar)
            - [Hero Image](#hero-image)
            - [Treatments](#treatments)
            - [About](#about)
            - [Footer](#footer)
            - [About](#about)
            - [Treatments](#treatments)
            - [Gallery](#gallery)
            - [Contact](#contact)
            - [Login/Logout](#loginlogout)
            - [Admin](#admin)
        - [Future Features](#future-features)
            - [Notifications](#notifications)
    - [Credits](#credits)
        - [Code](#code)
        - [Images](#images)
        - [Technologies used](#technologies-used)
    - [Testing](#testing)
    - [Security Features and Defensive Design](#security-features-and-defensive-design)
        - [User authentication](#user-authentication)
        - [Form Validation](#form-validation)
        - [Database Security](#database-security)
    - [Deployment](#deployment)
        - [Local Deployment](#local-deployment)
        - [Production Deployment Initial](#production-deployment-initial)
            - [Create Heroku app:](#create-heroku-app)
            - [Connect Postgres Database:](#connect-postgres-database)
            - [Deploy App on Heroku:](#deploy-app-on-heroku)
        - [Production Deployment Update](#production-deployment-update)
            - [PostgreSQL database:](#postgresql-database)
    - [Acknowledgements](#acknowledgements)

<!-- /TOC -->


## UX

### Business Goals

The main goal of this project is to give a user the ability to book appointments at the NailsbyFaar nail salon. User should also get a good feeling for the salon and know what to expect from the treatments. If the user books an appointment, they should be able to make updates to their appointments in a user dashboard.

### Target Audience

It might be obvious, but the target audience of this website is people who love getting their nails done! There isn't much more to be said about it, it can be people who go get their nails done for the first time, people who've gotten their nails done hundreds of times or people who are recurring customers at this specific salon. As long as they like pretty nails!

### User Stories

User stories were written together with salon owner and were all written to fit within the agile methodology. They have the following criteria:

* title
* clear description
* acceptance criteria
* tasks, when acceptance criteria alone weren't clear enough
* story points
* epic
* priority (must have, should have, could have)

In the picture below you can see an example of the user stories before work on the project was started:

![user stories board](static/images/user-stories-1.png)

And the user stories board after finishing the project:

![user stories board updated](static/images/user-stories-2.png)

As you can see, only one user story was left, which didn't fit in the scope of the project in the end. Since it was a 'could have' the decision to leave it out was easily made. To view all the user stories in detail, visit the project page: [user stories board](https://github.com/users/DOdrums/projects/3/views/1)


### Structure of the app

The app is designed to have a natural flow, with a strong focus on the booking functionality. Most pages include booking buttons or calls to book an appointment. The home page specifically features a booking button right on top, so a user doesn't have to scroll at all to make an appointment. This is especially handy and necessary for recurring customers, who will be the gross of the clientele.

### Logic/Database Diagram

The logic of the app was thought out by making a database diagram, to visualize which objects will need to be created for this app to be functional and how they will be connected to each other. Notably, the initial database diagram was incomplete, which was discovered during production of the app. See the images below:

Initial database diagram:

![database diagram](static/images/database-diagram.png)

Updated database diagram:

![database diagram](static/images/database-diagram-updated.png)

Django's Class-Based Generic Views were used, to build the models in an Object Oriented way. For the User model specifically, the Django package 'AllAuth' was used. This does a lot of the work for you, like creating unstyled login, sign-up and forgot password pages and functionality and creating the User model and User Manager model. For the purposes of this project, these two models had to be overridden, since a email address is used for authentication, instead of a username. Furthermore, phone number was added to  the user model.

Let's quickly go through the other models:

The Treatment model:

* used to make a treatment object (the different kind of available treatments at the salon).
* has a 'display' parameter, meaning: to be displayed on the homepage and treatments page or not.
* has an 'active' parameter, meaning: to be displayed in the booking tool or not.
* images are stored in Cloudinary via a CloudinaryField.

The User model:

* built with Django AllAuth.
* added phone_number, first_name and last_name.

The Appointment model:

* has foreign key relationships with the user model and treatment model.
* any appointment will always have a treatment object selected as a foreign key.
* any appointment can have a user selected as foreign key.

The Planning model:

* is used to configure available/bookable times in the datepicker
* allow_times takes a comma separated list of time values, for example: 10:00, 10:15, 10:30 etc. This indicates which times on any given day are bookable.
* disabled_days takes a comma separated list of dates, for example: 10.10.2022, 10.11.2022, 10.12.2022, etc. This indicates days that are off, like holidays.
* disabled_weekdays takes a comma separated list of numbers, for example: 0, 3, 6. This indicates, with sunday starting at value '0', the days in any given week that are off. So, in the example given, sunday, wednesday and saturday are off days. This will repeat every week.
* in the datepicker itself, all available times are calculated by using the values available in the active Planning Object and by removing any times from the datepicker where appointments already exist.

The Gallery model:

* used to upload images to Cloudinary, for use on the gallery page.
* can be added, removed and set to active from the admin panel.


### Color Scheme

The color scheme of the salon itself was used, see the image below. It creates a very feminine and calm look, which perfectly fits the nail polish theme.

![color scheme](static/images/color-scheme.png)

### Features

The app's biggest feature is of course the booking page and consequently, the user dashboard. These two pages are all you need, to book an appointment, cancel the booked appointment or change its date. This is where we will start our journey:

#### Book page

This page is where most users, especially the recurring ones, will spent the grunt of their time. When you first open the page, you will be welcomed by a simple form with datepicker. You are urged to select a treatment first, since the duration of the treatment is relevant for which times are bookable.

![book page](static/images/book.png)

After selecting a treatment, the datepicker will become fully visible and usable and users can now select a date. When you select a date, the available times in the time picker will be rendered and user can scroll through the available times. After user picks a time, the time gets entered automatically in the date field of the booking form. The other fields in the form are either auto-filled when user is logged in, or filled in by user upon booking.

![book page treatment selected](static/images/book-selected-treatment.png)

After hitting the book button, user will get confirmation of their booking and are urged to go to their account dashboard.

![book page confirmation](static/images/book-confirmation.png)

#### User dashboard

When the user goes to their account dashboard, they are greeted by two sections: a personal info section and a section with all their booked appointments (if any).

![user dashboard](static/images/dashboard.png)

By default, the user's personal info is not editable, to limit the chance of user-error. If the user decides they want to chance some of their info, they can hit the edit button, which will cause the 'First name', 'Last name' and 'Phone number' field to pop open.

![user dashboard personal info edit](static/images/dashboard-personal-info.png)

After hitting 'save', the fields will now all become uneditable again and a little alert will slide in view confirming the edits were saved to the database. After 4 seconds this alert will slide out of the way, but a user can also close the alert themselves if they wish.

![user dashboard personal info edit confirmation](static/images/dashboard-personal-info-confirmation.png)

On the other side of the dashboard, user will find all their booked appointments. Which they can expand like an 'accordion' by clicking on the element.

![user dashboard booked appointments](static/images/dashboard-appt.png)

When the date of an appointment is less than 48 hours in the future, it's not possible to change or cancel an appointment, which is indicated by greyed out buttons.

![user dashboard cancel blocked](static/images/dashboard-cancel-blocked.png)

When an appointment lays further in the future, user can can cancel the appointment by clicking on the cancel button.
When cancel gets clicked, user will be asked to confirm their choice, by a modal that pops up. This is to make sure the user really meant to click the cancel button, since cancelling an appointment by mistake would be very inconvenient.

![user dashboard cancel modal](static/images/dashboard-cancel.png)

The other button present in the appointment accordions is a 'Change date' button. This button will allow the user to change the date of the appointment. After clicking the button, they will be redirected to a page similar to the booking page, except the treatment is pre-selected. Furthermore, the only thing they can change is the date.

![user dashboard edit](static/images/dashboard-edit.png)

#### Home

Let's get on with the rest of the website. The home page features a few elements. We'll look at them from top to bottom.

#### Nav bar 

At the top of the page you'll find a nav bar. This bar has two appearances, for being displayed either on top of the hero-image of the homepage, or above the content of the other pages.

![homepage-nav](static/images/nav-home.png)

![homepage-other](static/images/nav-other.png)

The nav bar will display either a login button, or when user is logged in, their name. When user clicks their name, a menu will pop out with the options to log out or go to their user dashboard.

![nav-user-logged-in](static/images/nav-user.png)

#### Hero Image

The hero image will probably be the very first element that catches the users eye when visiting this website. It's a stunning image shot at the Nail Salon.

![hero-image](static/images/home-hero-image.png)

#### Treatments

After user scrolls down a bit, they will see the highlighted treatments. Clicking on the element will bring them to the treatments page, where they can read more about the treatment. Clicking on the book button will bring them to the book page.

![home-treatments](static/images/home-treatments.png)

#### About

Below the treatments, user will find a little text about the salon, with a photo.

![home-about](static/images/home-about.png)

#### Footer

At the bottom of the page, there is a footer. The footer houses a map with the location of NailsbyFaar, some contact info and the social links.

![home-footer](static/images/home-footer.png)

#### About

The next page is the about page. This is simply an extension of the about section on the home page and features an image and some text about the owner of the salon.

![about](static/images/about.png)

#### Treatments

The treatments page features the main treatments with explanations of what they are. There is also a book button for the user to immediately book an appointment.

![treatments](static/images/treatments.png)

#### Gallery 

The gallery page displays a little gallery with some images of recent work done by Nailsbyfaar. On the bottom of the page, the user is encouraged to visit her instagram.

![gallery](static/images/gallery.png)

![gallery-insta](static/images/gallery-insta.png)

#### Contact

The contact page displays a simple form for the user to fill out in order to send a message to the owner.

![contact](static/images/contact.png)

#### Login/Logout

If a user doesn't have an account yet, they can sign up, by filling in the form.

![signup](static/images/sign-up.png)

Once a user has an account, they can login.

![login](static/images/login.png)

If the user wants to logout via the navbar, they'll have to confirm this decision.

![logout](static/images/logout.png)


#### Admin

Site owner has a lot of control over the website and database entries via the admin panel. If they login as a superuser, they can edit/delete/add a whole range of objects:

![admin](static/images/admin.png)

The user can look at registered email-adresses, appointments, gallery images, planning, treatments and users. The social accounts are not in use and groups can be used if wanted. Let's have a look at some of them.

The first thing you would probably add is a planning, so users know which times they can book. This is what the planning object looks like:

![admin-planning](static/images/admin-planning.png)

After adding a planning, some treatments should be added, so a user can actually book a treatment. The treatments can be displayed in the booking module, on the home page and treatment page, both or neither. This is what the overview of different treatments will look like:

![admin-treatments](static/images/admin-treatments.png)

A treatment object looks as follows:

![admin-change-treatment](static/images/admin-change-treatment.png)

After adding these object, a user should now be able to see a fully functional book page and be able to book an appointment. After some appointments are booked, you'll see a list of appointments in the admin panel:

![admin-appointments](static/images/admin-appointments.png)

Which when opened, look as follows:

![admin-change-appointment](static/images/admin-change-appointment.png)

The final thing that can be added is some images for the gallery page.

![admin-gallery](static/images/admin-gallery.png)

### Future Features

An important feature for the admin, is a link to a google agenda that displays all appointments in a calender. This way, there is a clear and easy oversight in the planning. This was also the only remaining user story.

#### Notifications

Users can already receive notifications via email, but it would be great to have the option of enabling sms notifications, since these tend to reach the user better (no danger of ending up in the spam folder).


## Credits

### Code

* [Stackoverflow(answer from 'Aaron')](https://stackoverflow.com/a/61139427/16545052) - for the regex validation on the 'allowed_times' model.
* [Stackoverflow(answer from 'xyres')](https://stackoverflow.com/a/43305140/16545052) - for using Django context variables in Javascript.
* [Reddit(answer from OP himself)](https://www.reddit.com/r/django/comments/ma35nu/django_allauth_custom_signup_form_doesnt_save_all/) - to allow allauth adapter to be overriden, for saving of phone numbers in database.
* [Medium article](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56) - for adding extra fields to allauth.
* [Medium article](https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318) - for making a custom user model connected to allauth.
* [Stackoverflow(answer from 'Stilian')](https://stackoverflow.com/a/67664840/16545052) - for the clean method in the booking form
* [Stackeroverflow(answer from 'Colin')](https://stackoverflow.com/a/36925822/16545052) - for making a workaround for the disabled field in the booking form
* [Stackeroverflow(answer from 'Devang Padhiyar')](https://stackoverflow.com/a/55561290/16545052) - to add two querysets together in Dashboard view
* [Stackeroverflow(answer from 'fceruti')](https://stackoverflow.com/a/9957402/16545052) - to update a user instances information in the POST method of the Dashboard view.
* [Stackeroverflow(answer from 'Alex Fuentes')](https://stackoverflow.com/a/25319333/16545052) - to make the alert message that appears when editing user data slide up after 4 seconds. 
* [Codepen](https://codepen.io/dotproto/pen/mdOXve) - for the css code of a divider used on homepage.
* [Stackeroverflow(answer from 'Griffosx')](https://stackoverflow.com/a/13624393/16545052) - to check if loop index is even or uneven in treatments page. 
* [Stackoverflow(answer from 'vee')](https://stackoverflow.com/a/70415401/16545052) - to listen to the mobile navbar events.
* [Github(responsive-html-email-template)](https://github.com/leemunroe/responsive-html-email-template) - for a basic html template for emailing.


### Images

All images used in the readme are screenshots of the project and a multi device mock up generated with [mockup generator](https://techsini.com/multi-mockup/index.php)
Images inside the app are either royalty free stock imagery, or courtesy of NailsbyFaar.

### Technologies used

[HTML](https://html.spec.whatwg.org/) - for the structure of the website and mocking of the terminal (written by Code Institute)

[HTMLemail/inline](https://htmlemail.io/inline/) - for making the email html template into inline html.

[CSS](https://www.w3.org/Style/CSS/Overview.en.html) - to provide styling to the page.

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - for the structure of the website and mocking of the terminal (written by Code Institute)

[Python](https://www.python.org/) - to write all the logic of the app

[Django](https://www.djangoproject.com/) - used as main framework for the app, which both all backend and most frontend elements are built on. The following notable libraries/packages were added to django:

* django-ses: for handling emails with Amazon's SES.
* django-allauth: for handing all user models and login functionality.
* cloudinary: for saving images in cloudinary and serving them to the client.
* django-crispy-forms: for making the django forms look better.

[ElephantSQL](https://www.elephantsql.com/) - used to manage a PostgreSQL database.

[Bootstrap 5.2](https://getbootstrap.com/) - used to style the grunt of the project.

[Jquery](https://jquery.com/) - to make DOM manipulation a bit less painful.

[Lucidchart](https://www.lucidchart.com/pages/) used to make a database diagram.

[Gitpod](https://www.gitpod.io/) - used to connect a browser based VScode to github.

[Github](https://github.com/) - used for version control and deployment of the website.

[Heroku](https://dashboard.heroku.com/) - to deploy the app.

[JShint](https://jshint.com/) - used to validate javascript.

[NuHtmlChecker](https://validator.w3.org/nu/) - used to validate HTML.

[Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php) - to create an image of the website shown on different devices.

## Testing

Extensive testing was done to make sure all the features work as expected. To read all about this, please go to the separate [testing document](TESTING.md).

## Security Features and Defensive Design

### User authentication

* Django's all auth was used for login and sign up functionality.
* Django's superuser is used to limit access to admin panel.

### Form Validation

Extensive form validation is used on front end as well as backend.

### Database Security

All secret keys connecting the database are stored in a env.py file that is never pushed to github. Furthermore, Cross-Site Request Forgery (CSFR) tokens were used on all forms throughout the project.

## Deployment

### Local Deployment

To test the app locally, the terminal within VScode was used. The steps to run this:

* In your project workspace folder, open a terminal
* Run the command: ```python3 manage.py runserver```
* Hit the 'open browser' button or visit ```http://localhost:8000/``` in the browser.
* Use the website as usual.

A local database was used for most of the local deployment usage, since it was necessary for the automated tests to run. However, the switch to using the production database could be easily made, in case migrations needed to be performed or otherwise. Furthermore, in the development version, DEBUG was set to False, so error messages would show follow.

### Production Deployment Initial

Before starting work, the project was deployed to Heroku. This was done early in the process, to prevent having to deal with difficulties of deployment close to the project deadline. The following steps needed to be performed:

#### Create Heroku app:

* Login in to Heroku
* Create a new app.
* Select "New" and "Create new app".
* Give the new app a name and click "Create new app".
* Select a region (Europe for this app).

#### Connect Postgres Database:

* Open your app on the main dashboard of Heroku.
* Open the Resources tab and scroll to the add-ons section.
* Type 'Postgres' and select the Heroku Postgres option.
* Copy the DATABASE_URL in the Config Vars section of the Settings tab.
* To use the Postgres database in your development environment, copy the DATABASE_URL in your env.py file.

#### Deploy App on Heroku:

* Click "Settings".
* Navigate to the "Config Vars" section and click "Reveal Config Vars"
* Add SECRET_KEY variable
* Add CLOUDINARY_URL variable
* Add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY variables.
* Under "Deployment Method" click on "GitHub" to get access to your repository.
* Enable Automatic Deploys" or click "Deploy Branch" to deploy your app.

### Production Deployment Update

Since Heroku stopped offering free tiers on the 28th of november 2022, it was necessary to make a few adjustments to the whole production deployment of the app. 

#### PostgreSQL database:

The Postgres database add-on that was previously used within Heroku was now no longer free and thus a different service had to be used. The choice went to [ElephantSQL](https://www.elephantsql.com/), since they offer a free tier. A [script](https://github.com/Code-Institute-Org/postgres-migration-tool) written by Code Institutes team was used to copy the original database to the new database. The steps are described in the [github readme](https://github.com/Code-Institute-Org/postgres-migration-tool) of that script.

After that, the steps were as follows:

* remove database add on from Heroku.
* remove old DATABASE_URL config var from settings and post new url from ElephantSQL database in its place.
* transform app from free tier to an eco dyno.

## Acknowledgements

This website was built as part of the Full Stack Software Development course from Code Institute. I would like to thank my mentor Adeye Adegbenga, for his excellent feedback and guidance throughout the development of the project. I would also like to thank friends and family, who all took a look at the finished project to make sure it worked well and checked if I could improve things.
