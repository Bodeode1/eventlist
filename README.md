# EventList


## Table Of Contents
1. [Introduction](#Introduction)
    1. [Scenario](#Scenario)
2. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Design Thinking](#Design-Thinking)
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

- **As a** User, **I want** the ability to login in to the website using the provided login form  **so that** I can engage with the platform

EVENT CREATION

- **As an** unregistered user, **I can** provide details **so that** I can create a unique account

- **As a** registered user, **I can** provide details **so that** I can login to my account

- **As an** unregistered user, **I can** create a unique password **so that** I can protect my personal account

- *As a* logged in user, **I can** view a page **so that** I can see my personal account details by individual field 

- *As a* logged in user, **I can** click a button **so that** I can change my personal account details by individual field 

- *As a* logged in user, **I can** click a button **so that** I can delete my account

- *As a* logged in user, **I can** request an email **so that** I can reset my account password if I have forgotten it

BOOKINGS MANAGEMENT

- *As a* logged in user, **I can** provide booking details **so that** I can set up appointment

- *As a* logged in user, **I can** update details **so that** I can reschedule an appointment with the Mutts cuts

- *As a* logged in user, **I can** cancel an appointment **so that** I can cancel an appointment with the Mutts cuts

- *As a* logged in user, **I can** request an email **so that** be reminded of an appointment

- *As an** employee, **I can** view a page **so that** I can see my daily bookings or the current day
