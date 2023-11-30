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

## Logic Glow Chart
Below is a comprehensive visual representation of the logic flow within this project. This flowchart outlines the sequential steps, that define the functionality and processes implemented in the system. It serves as a helpful guide to understand the underlying logic and workflow of the project.

![Event Lits ERD](docs/readme/media/logic-map.png)  

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

Host Error Page

When the server was launched, the website failed to load due to a disallowed host error.
I resolved this issue by adding a different host header to the Allowed Hosts section within settings.py.

![landing](docs/readme/media/html-home-page-error.png)

Bug 2

When I oppened the website for the first time, the static files : css and javascript was not applied.
The error displayed is shown beloe. However, I managed to resolve it by removing the 'Disable_Collectstatic=1' on Heroku.

![landing](docs/readme/media/Static-Errors2.png)

## Technologies Used

### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")

### Frameworks, Libraries & Programs Used

- [Balsamiq](https://balsamiq.com/) for wireframing
- [GitHub](https://github.com/) for repo storage and Agile project management using Kanban boards/issue tracking.
- [Heroku](https://id.heroku.com/) for project deployment to the world wide web.
- [Python3 ](https://docs.python.org/3/) with the following modules
    - asgiref==3.5.0
    - dj-database-url==0.5.0
    - Django==3.2
    - django-summernote==0.8.20.0
    - gunicorn==20.1.0
    - psycopg2==2.9.3
    - pytz==2022.1
    - sqlparse==0.4.2
- [Bootstrap](https://getbootstrap.com/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Testing

Manual Testing.
- manual testing
- Lighthouse site performance checks
- linter checks on HTML, CSS, JavaScript and Python code

Home Page

A manual test was conducted on the home page. Upon clicking the home page link, it loaded the page successfully.

![landing](docs/readme/testing/homepage.test.png)

View Tab on Event List Home Page

When clicking the 'View' button on the home page, it effectively enables users to access the list of created events.

![landing](docs/readme/testing/evenlist-view-test.png)

Edit Event Page

A manual test was performed on the Edit Page. When clicking the edit button, it successfully loads the edit form.

![landing](docs/readme/testing/editevent.png)

Add Event Page

The Add Event page effectively displays the event creation form. Upon creating events, it accurately confirms the successful creation of events.

![landing](docs/readme/testing/add-eventsuccess.png)

LightHouse Test

The Lighthouse tests show the following results

![landing](docs/readme/testing/lighthouse-addevent-form.png)

![landing](docs/readme/testing/lighthouse-event-listing.png)

![landing](docs/readme/testing/lighthouse-login.png)
