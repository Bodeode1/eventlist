# EventList

## Table Of Contents
1. [Introduction](#Introduction)

2. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Design Thinking](#Design-Thinking)
    3. [Scope Plane](#Scope-Plane)
3. [Features](#Features)
    1. [Design Features](#Design-Features)
    2. [Existing Features](#Existing-Features)
    3. [Future Adaptations](#Future-Adaptations)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
    1. [Main Languages Used](#Main-Languages-Used)
    2. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
    1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
    1. [Deployment.md](DEPLOYMENT.md)
8. [Credits](#Credits)
    1. [Content](#Content)
    2. [People](#People)
9. [Acknowledgements](#Acknowledgements)
***

## Introduction
# EventList

Welcome to EventList, your destination for event listings and management.

## UX Development Plane
### User-Stories

Site user needs can broadly be split 2 epics:

- authentication
- events creation

AUTHENTICATION
- **As a** Administrator, **I want** to be able create user accounts from the command line, **so that** I can efficiently manage user access to the system
- **As a** website User, **I want** to be able create an account on the website by providing my username, email, password, and confirming the password **so that** I can access and use the platform

- **As a** website User , **I want** to receive a confirmation message after registering for an account **so that**  I can be assured that my account has been successfully created and I can start managing my events

- **As a** Website User, **I want** the ability to login in to the website using the provided login form  **so that** I can engage with the platform

- **As an** Adminiatrator, **I want** the ability to access the administrative dashboard through a dedicated URL login  **so that** it allows for a secure and convenient means of managing the system

EVENT CREATION

- **As an** Account User , **I want** to create events on the platform **so that**  I can share the events information with others

- **As an**  Account User, **I want**  I want to see a list of events I have created **so that** I can keep track of my events and make any necessary updates

- **As an** Account User, **I want** the ability to delete events I have created **so that**  I can remove events that are no longer relevant

- *As an* Account User, **I want** to ensure that only administrators can delete events that I have created **so that** unauthorized deletions are prevented

- *As an* Account User, **I can** I want to see a list of attendees for events I have created **so that** I an see the guest list and make event preparations

- *As an* Accont User, **I want** to be able to edit details of events I have created **so that** I can make updates or corrections as needed

- *As a* Guest User, **I want**  to be able to book tickets for a specific event **so that**  I can secure my spot and attend the event that I am interested in

### Design Thinking

Employing a Design Thinking methodology, the student developer opts to explore various features perceived as most valuable by users on the finalized site. As specified in the assessment criteria, this project mandates the use of CRUD functionality, providing a fundamental structure for necessary functionalities. A preliminary evaluation has generated the following insights:

| Feature                                 | Importance | Feasibility |
|:----------------------------------------|:----------:|:-----------:|
| Creating an event                       |     5      |    5        |
| Viewing events created                  |     5      |    4        |
| Deleting events                         |     5      |    5        |
| Viewing events attendee                 |     4      |    5        |
| Editing events                          |     5      |    5        |
| Searching for an Event                  |     5      |    4        |
| Booking a Ticket to attend Event        |     5      |    4        |
| Account User Registration               |     5      |    5        |
| Admin login                             |     5      |    5        |
| **Overall Score**                       |   **44**   | **42**      |

### **Color Schema**   
The  color shema was selected from [Coolors](https://coolors.co). The idea was to have combinations of colors.   

![Color Schema](docs/readme/media/colorpallete.png)  

### **Typography**  
All of the fonts were sourced from [Google Fonts](https://fonts.google.com).   
* Main fonts: Verdana sans-serif   
  A sans-serif type of font was chosen to give a simple, clean, and modern look to the site. 

## Database Design

Database schema was designed using [dbdesigner](https://erd.dbdesigner.net/).   
![Event Lits ERD](docs/readme/agile/erd-mapping.png)  

## Scope Plane

* **Functional Requirements**   
User Authentication:  
    - The system shall allow an Administrator to create user accounts via the command line interface.
    - Users shall be able to create accounts on the website by providing username, email, password, and confirming the password.
    - Upon successful registration, users should receive a confirmation message to verify account creation.

    ### Login Functionality:
    - Users shall be able to log in to the website using the provided login form.
    - An Administrator should access the administrative dashboard via a dedicated URL login for secure system management.

Event Management:
    - Account Users shall have the capability to create events on the platform.
    - Users must have visibility of a list of events they've created, enabling them to track and update event details
    - Users should be able to delete events they've created, with restrictions to ensure only administrators can delete events created by others.
    - Account Users should view and manage the attendee list for events they've created.
    - Editing functionalities for event details should be available to Account Users.

Ticket Booking:
    - Guest Users must be able to book tickets for specific events.

* **Non-Functional Requirements**  
Security:
   - User authentication and sensitive information transmission (e.g., passwords) should be encrypted and secure.
   - Access control mechanisms should restrict unauthorized access to sensitive functionalities (e.g., event deletion).

Performance:
   - The system should respond promptly to user actions, ensuring minimal latency during event creation, updates, and bookings.

User Experience (UX):
   - The user interface should be intuitive, guiding users through registration, event creation, and management processes.

   - Responsive design principles should be employed to ensure usability across various devices and screen sizes.

Compatibility:
   - The web application should be compatible with major browsers (Chrome, Firefox, Safari, etc.) to ensure a seamless user experience.

Skeleton
Wireframes were made to showcase the appearance of the site pages while keeping a positive user experience in mind. The wireframes were created using a desktop version of [Balsamiq](https://balsamiq.com/).

<details>
<summary>Balsamiq Wireframes</summary>
    
![Site Wireframes](docs/readme/wireframes/00-index-page.png)

![Site Wireframes](docs/readme/wireframes/01-our-services.png)

![Site Wireframes](docs/readme/wireframes/02-join-us.png)

![Site Wireframes](docs/readme/wireframes/03-my-account.png)

![Site Wireframes](docs/readme/wireframes/04-book-now.png)

![Site Wireframes](docs/readme/wireframes/05-my-appointments.png)

![Site Wireframes](docs/readme/wireframes/06-daily-calender.png)

</details>   

[Back to top](#Mutts-Cuts)

## Features

**MAIN SITE FEATURES**
### Design Features

### Existing Features

Home Page
The home page immediately inform the users of the purpose of the webite. 
![landing](docs/readme/features/homepage-feature.png)

Navigation 
The navigation bar included hypertext links to four pages: the home page (represented by the logo), the Add Event page, the login page, and the sign-up page."

![landing](docs/readme/features/navigation-bar.png)

Add Event Page
The "Add Event" page enables registered users to create an event for listing purposes.

![Event Listing](docs/readme/features/add-event-feature.png)

The Logout Page
The logout page redirects users back to the home page.

![landing](docs/readme/features/login-feature.png)

View Event Button on Home Page
Once users have added events, they can access the event list by clicking a button on the home page.

![landing](docs/readme/features/viewevent-button.png)

View Tab on Event List Table
The 'View' tab within the Event List table enables users to access comprehensive details of the entire event list.

![landing](docs/readme/features/viewevent-fullpage.png)

Edit Event Page
The 'Edit Event' button on the event editing page enables users to modify and save changes made to the listed event

![landing](docs/readme/features/edit-yourevent-feature.png)

## **Features to be implemented in the future** 
Due to time constraints on the current work project, certain features I intended to include could not be incorporated. Nevertheless, in future development phases, the following features could be considered for addition:

1. Search and Filtering Options: Enhance the search functionality by allowing users to filter events based on categories, dates, locations, or event types.

2. Interactive Event Maps: Implement interactive maps to display event locations and provide directions or additional information.

3. Social Media Integration: Enable users to share events on social media platforms and promote events through social media integration.

4. Event Reminders and Notifications: Implement reminders and notifications for users regarding upcoming events, ticket purchases, or event changes.

## Issues and Bugs
The developer ran into several issues during the development of the website, with the noteworthy ones listed below, along with solutions or ideas to implement in the future.

Bug 1

Testing Issue Checking static folder is working on deployed site #28

this is in Sprint 2 of my projects. Any images stored in static/img/ folder should display when deployed. Remember to delete the DISABLE_COLLECTSTATIC config var in Heroku Settings by clicking on the X.
When I deleted this config var and tried to redeploy, the build log stated python manage.py collectstatic --noinput.
This prompted a different approach to handling static files by installing the dotenv python package. From there I updated the requirements.txt file and settings.py and env.py files in the project before pushing them to GitHub again.
https://github.com/Becky139/mutts-cuts/issues/28

Bug 2

Carousel images change dimensions when transitioning #52

Found in Sprint 4. Carousel image resizes when transitioning despite being of similar/size dimension to other images.
It produces an unwanted jumping effect.
Resolved by setting height of parent element (class="carousel-inner height-640px") to match height of carousel items.
https://github.com/Becky139/mutts-cuts/issues/52

Bug 3

Write view logic in booking view to prevent created and updated bookings from clashing an existing booking #56

This can be found in Sprint 8. The answer to this conundrum lay within Django documentation.
Querysets. It's abstracted so there is no need to open the database connection, perform actions, or close the connection.
Applied logic within the bookings/views.py function.
Essentially, if a record exists for a specific date AND specific time, the program can branch to tell the user their attempt to create or edit an appointment to the same time cannot be done. The business can only perform one appointment at a time as there is 1 member of staff.
(https://github.com/Becky139/mutts-cuts/issues/56)

Bug 4

Content cut off when viewing on a small mobile device #58

This can be found in Sprint 8 Issues found on two pages Services and View Bookings This can be found in Sprint 8.
In MDN docs I found the following to test
1. Remove the following properties from the viewport in the head.html file
2. user-scalable=no, maximum-scale=1.0, minimum-scale=1.0
But then found the solution below to fix the issue
Services page x-overflow solved. Container fluid was applied to multiple sections and a number of stray divs. Resolved.
Table in view bookings cannot be viewed properly below 768px. Research suggests if was a poor choice to use table elements with so many fields when responsive design was a feature. This can be resolved by using a combination of display: block and flexbox to stack td elements. This could compact information to less than 500px and still be effective.
https://github.com/Becky139/mutts-cuts/issues/58

Bug 5

Appointment now available message when editing an appointment and not changing any details #57

This can be found in Sprint 8. In this scenario, if no details at changed, a separate 'info' message should be displayed stating no details were changed. Additional code will need to be added to the edit booking function in bookings/views.py.
Changed message and status from error to warning in bookings/views.py.
Now displaying a yellow bootstrap message stating No appointment available or this is your booking.
https://github.com/Becky139/mutts-cuts/issues/57