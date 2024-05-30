# Running Stories - Introduction

Running Stories is a platform for runners to share their unique experiences, inspire one another, and build community. This is a Full Stack website built using the Django framework with full CRUD functionality. Users can share their stories and comment on others’ stories, expressing their passion for running.

View the full website [here](https://running-stories-252b86d688ca.herokuapp.com/).

<img src="static/img/responsive.png">

## Table of Content

- [Running Stories - Introduction](#running-stories---introduction)
- [Table of Content](#table-of-content)
- [User Experience - UX](#user-experience---ux)
    - [User Stories](#user-stories)
    - [Project Planning](#project-planning)
        - [Agile Methodologies](#agile-methodologies)
            - [Kanban Board](#kanban-board)
            - [MoSCoW Prioritization](#moscow-prioritization)
            - [Milestones](#milstones)
            - [Epics](#epics)
            - [User Storeis in GitHub](#user-stories-in-github)
    - [Design](#design)
        - [Wireframes](#wireframes)
        - [Entity Relationsship Diagrams (ERD)](#entity-relationship-diagrams-erd)
- [Features](#features)
    - [Hompe Page](#home-page)
    - [View full story](#view-full-story)
    - [The About page](#the-about-page)
    - [Register](#register)
    - [Sign In](#sign-in)
    - [Comment on a Story](#comment-on-a-story)
    - [Edit and Delete Comments](#edit-and-delete-comments)
    - [Create a Running Story](#create-a-running-story)
    - [Edit and Delete a Running Story](#edit-and-delete-a-running-story)
    - [Navigate and Logout](#navigate-and-logout)
- [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Database Used](#database-used)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Tools & Programs](#tools--programs)
- [Testing](#testing)
- [Credits](#credits)
    - [Code Used](#code-used)

## User Experience - UX

### User Stories

1. User Registration - As a new user, I want to register on the website so that I can create and share my running stories.
    
    AC1 - Given that I am on the registration page, when I provide valid details (username, email, password), then I should be successfully registered.

    AC2 - Given that I am on the registration page, when I provide invalid or incomplete details, then I should receive an error message indicating the issue.

2. Create a Running Story - As a registered user, I want to create a running story to share my experiences.

    AC1 - Given that I am logged in, when I navigate to the “Share Story” page, then I should see a form to input my story details (title, content).

    AC2 - Given that I have filled in the story details, when I submit the form, then my story should be saved and visible to other users.

3. View Running Stories - As a user, I want to view running stories posted by others so that I can get inspired of other runners.

    AC1 - Given that I am on the homepage, then I should see a list of running stories with titles and brief summaries.

    AC2 - Given that I click on a story, then I should be taken to the full story page.

4. Comment on Running Stories - As a user, I want to leave comments on running stories.

    AC1 - Given that I am logged in, when I read a story, then I should see a comment section.

    AC2 - Given that I enter a comment and submit it, then my comment should be visible to others.

5. Edit and Delete Stories - As a story creator, I want to edit or delete my own stories so that I can change or delete the content I posted.

    AC1 - Given that I am logged in and viewing my own story, then I should see options to edit or delete it.

    AC2 - Given that I choose to edit, when I make changes and save, then the story should be updated.
    
    AC3 - Given that I choose to delete, when I confirm, then the story should be removed.

6. Ask Questions - As a runner, I want to ask questions about running so that I can learn from others.
    
    AC1 - The user can access a form or input field where they can type their running-related question.
    
    AC2 - Upon submitting the question, it is stored in the database.
    
    AC3 - The question appears on the website’s question feed or list.
    
    AC4 - The user receives a confirmation message after submitting the question.
    
    AC5 - The question form includes validation to prevent empty or invalid submissions.

7. Answer Questions - As a runner, I want to answer questions from fellow runners to share my knowledge and experiences.
    
    AC1 - The user can view a list of existing questions on the website.

    AC2 - Each question displays the question text and relevant details (e.g., date posted, author).

    AC3 - The user can click on a question to view its details and any existing answers.
    
    AC4 - The user can submit an answer to a specific question.
    
    AC5 - After submitting an answer, it appears alongside the question.
    
    AC6 - The answer form includes validation to prevent empty or invalid submissions.

8. View Questions and Answers - As a user, I want to see questions and answers related to running on the website so that I can participate in discussions.

    AC1 - The website homepage or a dedicated “Questions” section displays a list of recent questions.
    
    AC2 - Each question shows the question text, author, and the number of answers.
    
    AC3 - The user can click on a question to view its details and answers.
    
    AC4 - Answers are displayed below the question, sorted by date (most recent first).
    
    AC5 - The website provides pagination or infinite scrolling for long lists of questions.


9. Visitor View Running Stories - As a visitor, I want to be able to read running stories so that I can be inspired by others’ experiences.
    
    AC1 - When I visit the website, I should see a list of running stories.
    
    AC2 - I should be able to click on a story to read its full content.

10. View My Stories - As a user, I want to be able to view my running stories on a single page so that I can easily track my progress and share my experiences with others.
    
    AC1 - The “My Stories” section should list all the running stories associated with my account.
    
    AC2 - If I haven’t posted any running stories yet, the section should display a message indicating that there are no stories available.
    
    AC3 - When I create a new running story, it should appear immediately in the “My Running Stories” section.
    
    AC4 - The running stories should be sorted in reverse chronological order (most recent first).

11. The About Page - As a website visitor, I want to understand the purpose of the running stories website so that I can engage with the content effectively.
    
    AC1 - The “About” page prominently displays a brief overview of the website’s purpose.
    
    AC2 - The content is written in plain language, avoiding technical jargon.
    
    AC3 - The “About” page provides a link or button to explore more running stories.
    
    AC4 - The page layout is visually appealing and easy to read.

12. Edit and Delete Comments - As a comment creator, I want to be able to edit or delete my own comments so that I can change or delete the content I posted.
    
    AC1 - Given that I am logged in and viewing my own comment, then I should see options to edit or delete it.
    
    AC2 - Given that I choose to edit, when I make changes and save, then the comment should be updated.
    
    AC3 - Given that I choose to delete, when I confirm, then the comment should be removed.

13. Handle Drafts - As a user, I want to be able to save my stories as drafts so that I can work on them later.
    
    AC1 - Users should be able to save their stories as drafts.
    
    AC2 - When editing a story, users should have the option to publish it.
    
    AC3 - The system should provide a way to view all published stories.
    
    AC4 - There should be a way to identify stories that are still in draft mode.

### Project planning

#### Agile Methodologies 

##### Kanban Board

I have used the [project board in Git Hub](https://github.com/users/SofiaNords/projects/5/views/1) for my project planning. It has helped me to get an overview of the project and to see the progress. Thanks to the MoSCoW method (see below), I realized quite early in the project that User Story 6, 7 and 8 would not be included in this release.

<img src="static/img/kanban.png">

##### MoSCoW Prioritization

The User Stories are labeled with one of the following categories according to the MoSCoW prioritization method:

- Must Have: Requirements that are absolutely necessary for the product to function. These have the highest priority.

- Should Have: Important requirements that should be included if possible, but they are not critical.

- Could Have: Desirable requirements that can be added if time and resources allow.

- Won’t Have (this time): Requirements that will not be included in the current version of the product.

##### Milstones

I also wanted to try using Milstones in Github Projects but realize now in retrospect that for a project of this size, a Kanban Board with User Stories and MoSCoW labels were enough.

<img src="static/img/milstones.png">

##### Epics

Even Epics felt a bit over-ambitious in this project but it has been educational to use it.
<img src="static/img/epics.png">

##### User Stories in GitHub

You can access User Stories in Git Hub [here](https://github.com/SofiaNords/running-stories/issues). In the picture below you can see how I have labeled the User Stories with Epics, MoSCoW Prioritization and Milstones.

<img src="static/img/user_stories.png">

### Design

#### Wireframes

<img src="static/img/wireframe_1.png">

<img src="static/img/wireframe_2.png">

<img src="static/img/wireframe_3.png">

<img src="static/img/wireframe_4.png">

<img src="static/img/wireframe_5.png">

<img src="static/img/wireframe_6.png">

<img src="static/img/wireframe_7.png">

<img src="static/img/wireframe_8.png">

#### Entity Relationship Diagrams (ERD)

When I initially planned this project, I also intended to include a Questions and Answers section as you can see from the user stories. Therefore there are also models for Questions and Answers in my ERDs. 

<img src="static/img/erd_1.png">

The models that actually was created are the ones below. I realized during the project that the About model is redundant but I decided to keep it as it is part of my learning journey. 

<img src="static/img/erd_2.png">

## Features

### Home Page

<img src="static/img/home-page.png">

- The hero image welcomes the page visitor with a runner running in an inspiring environment.
- The page visitors has direct access to the Running Stories below the hero image where they can read a excerpt that will give them a brief summary of the story. 
- The visitor can click on an optional story and access the complete story.

### View full Story

<img src="static/img/story-detail.png">

- A page visitor can view the full story and comments related to the story.
- The page visitor can see that you have to log in to be able to leave a comment.

### The About page

<img src="static/img/about-page.png">

- A page visitor or user can read about the website's purpose and get instructions in how to get started sharing stories and or leave comments on others stories.

### Register

<img src="static/img/sign-up.png">

- A page visitor can click on Register in the navigation menu and fill out the Sign up form.

### Sign in

<img src="static/img/sign-in.png">

- A registered user can sign in by filling in the Sign in form.

### Comment on a Story

<img src="static/img/leave-a-comment.png">

- A logged-in user can leave a comment on a story.

### Edit and Delete Comments

<img src="static/img/edit-delete-comments.png">

- A logged-in user can edit or delete their own comments.

### Create a Running Story

<img src="static/img/create-story.png">

- A logged-in user can create a Running Story on the Share Story page. The user can create a draft that is only visible for that user under My Stories. When the user changes status to Published the story will become visible on the Home Page.

### Edit and Delete a Running Story

<img src="static/img/edit-story.png">

- A logged-in user can edit or delete a story they have created themselves.

### Navigate and Logout

<img src="static/img/log-out.png">

- A user can easily navigate on the website using the navigation menu.
- A logged-in user can logout by clicking on the Logout link in the navigation menu and then confirm to Sign Out. 

## Technologies Used

### Languages Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Database Used

- [PostgreSQL](https://dbs.ci-dbs.net/manage/) - Used to store the data

### Frameworks and Libraries

- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Used to design the website and make it responsive
- [Crispy Bootstrap](https://pypi.org/project/crispy-bootstrap5/) - Used to create and style forms
- [Django](https://www.djangoproject.com/) - Used for rapid, reusable and secure development
- [Django allauth](https://docs.allauth.org/) - Used for account registration and authentication
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/) - Used to control the rendering behavior of my Django forms in a elegant and DRY way


### Tools & Programs

- [Balsamiq](https://balsamiq.cloud/) - Used to create wireframes
- [Lucidchart](https://www.lucidchart.com/) - Used to create Entity Relationship Diagrams (ERD)

## Testing

View testing User Stories [here.](https://docs.google.com/spreadsheets/d/16GrrTfA8aQ79KI6y7XLdAuZSGlR_fDgHIUbQLkWweuM/edit#gid=0)

## Credits

### Code Used

- [How to keep your footer where it belongs?](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/) by Dominic Fraser. I followed Dominics instruction for the placement of the footer.

