#     <div align="center"><img src="static/images/company-logo.png" alt="Site Logo"></div>
[Esports Epics](https://esports-epics.herokuapp.com/) is a website to share the most nail biting, clutch 
and incredible competitive moments that occur in a variety of different genres of video games. When your opponents back 
is against the wall, they are forced to pull off epic feats to turn the odds back in their favour. Esports Epics is a 
place to capture these feats so that myself and you can learn and enjoy the best moments esports has to offer.
<h2 align="center"><img src="static/images/readme-images/mock-ups.gif" alt="Site Mock ups"></h2>

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Stories**](#user-stories)
    - [**Wireframe mock-ups**](#wireframe-mock-ups)
2. [**Features**](#features)
    - [**Home Page**](#home-page)
    - [**Source Code**](#source-code)
    - [**Existing Features**](#existing-features)
3. [**Technologies Used**](#technologies-used)
4. [**Testing**](#testing)
5. [**Deployment**](#deployment)
6. [**Credits**](#credits)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)
    
## UX
### Project Goals
- The primary goal of this project is to create a hub/library where fans of Esports across a variety of games can submit their favorite Esports moments, browse other submissions and 
watch epic comebacks, clutch moments and impossible plays.
- The website will allow fans to search/browse all the submissions by different categories such as which game, genre, notable player etc.
- Users will be able to create posts and provide context and information to readers who click into the post, so they can understand what makes this moment special.
- Esports fans can view upcoming events in various games so they can view and submit the most recent clips when they watch currently running tournaments.
- This Website will:
    * Be responsive on multiple platforms such as desktops, tablets and smartphones
    * Allow users to add, edit and delete their posts using CRUD operations so they can contribute to the site.
    * Allow users to browse new and old posts so they can view epic moments for enjoyment or to learn from so they can also get better in that game.

### Business & Developer Goals
* Create a esports website that allows visitors to view or contribute incredible esports clips and videos for learning and entertainment purposes.
* This website will be for users who enjoy playing video games, who enjoy watching competitive matches in their favorite video games and want a place they can watch recent tournaments highlights and epic moments .
* Get esports fans traffic to the website for advertisements or merchandise sales for revenue.
* As a developer I would like to 
    - Learn Flask, noSQL using MongoDB and designing a database by creating an exciting project visitors would like to interact with.
    - A challenging project for the developer but also one that I have a passion for. I have followed Esports for over 10 years.

### User Stories
As a video game or Esports enthusiast I would like:
1. To be able to navigate the website efficiently and intuitively so that I can find posts that capture my interest or make a new post myself.
2. A place / library of the best esports moments so that I can view them for enjoyment and share them with others. 
3. Read the context behind the clip or moment so that I can understand why it is an amazing play.
4. The ability to add clips / competitive moments so I can contribute to the collections of great esports moments so others can view them.
5. Be able to edit or delete esports posts that I added incase I made a mistake or the post already exists.
6. To be able to filter all the moments by intuitive categories such as game, genre or date so I can quickly navigate to games / clips that interest me.
7. View upcoming esports tournaments that so I know when they will be live in order to watch them.
8. Add upcoming esports tournaments so that other users can benefit from knowing when tournaments are live.
9. Be able to edit or delete tournament posts that I have added to keep the information reliable and up to date.
10. Find the contact information and social media links easily so I can keep up to date with the website and posts.

### Wireframe mock-ups
- [Home Page](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/home.png)
- [Create Account](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/create-account.png)
- [Log In](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/log-in.png)
- [Profile](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/profile.png)
- [Profile With News/Events Posted](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/profile-moderator-journalist.png)
- [Add/Edit Esports Moment](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/add-esports-moment.png)
- [Add/Edit Event](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/add-event.png)
- [Add/Edit News](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/add-news.png)
- [Browse](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/browse.png)
- [Manage Site](https://github.com/jamesr1775/esports-epics/blob/master/assets/wireframes/manage-site.png)

## Features
### NavBar
1. The Nav Bar is a part of the base template and will be present in all webpages of this website. 
2. The navigation bar links are different under certain conditions.
    - When no user is logged in the links available are:
        - Home
        - Browse
        - Log In
        - Register
    - When a user is logged in the available links are:
        - Home
        - Browse
        - Add Event
        - Submit Epic
        - Profile
        - Log Out
    - When an admin account is logged in they also get access to:
        - Manage Site
    - When a journalist is logged in they also get access to:
        - Submit News
3. The admin account can allow a user to get the Journalist account status using the manage website page. This is to allow for integrity of the story and/or any claims made in the news post.
4. The NavBar becomes a expandable button when the website is accessed on small screens.

### Home Page
1. The site logo will be at the top of the page and link back/ refresh the home page.
2. Underneath the navbar a contrasting colorful hero image is loaded to grasp the visitors interest and attention.
3. A carousel of the 5 most recent esports video posts is located below the hero image. The user can see what others are watching and if potentially recent tournaments clutch moments occurred.
    - Each item in the carousel can be clicked to load description of the post
    - A button to load the modal that contains the embedded video player is also presented.
4. A materialize collapsible container is used to store all the news stories journalists can write and submit to the website.
5. A materialize collapsible container is used to store all ongoing and upcoming esports tournaments for users to so they know when to watch live streams and matches.

### Log In/Out and Registering
1. Upon logging in to the website the user gets a welcome message that disappears after a short period.
2. They are brought to home page of the website.
3. When a use logs out they are brought back to the log in page.
4. They receive a confirmation message to let them know they have logged out that disappears after a short period.
5. When a person visits the website, they can register by clicking the register button in the navbar or the don't have an account button in the log in page.
6. They are brought to a form to create a new account.
<div align="center">
<img src="static/images/readme-images/log-in-out-register.gif" alt="Browsing Page" >
</div>

### Browse

1. The browse page provides access to all the esports epics submitted by the community.
2. The search bar can be used to filter all the posts.
3. Each search modifies the epics displayed with out refreshing the page for better user experience. 
4. The reset button will display all the epics once more.
5. Each post when submitted required game, game category, player, description, tournament and year which are all indexes used to filter the posts displayed.
<div align="center">
<img src="static/images/readme-images/browse-page.gif" alt="Browsing Page" >
</div>

### Profile

1. The profile page displays the users account information
2. A button to delete your account is also available if users wish to.
3. All the esports posts the user made is displayed and they are given the option to delete or update their post as required.
4. If the user is a journalist, the news stories they posted will also be displayed with buttons to edit or delete the news post.
5. If the user is a moderator, he/she is responsible for keeping the events information up to date and should remove old posts or correct mistakes with events added.
6. A confirmation modal for any delete action is there to prevent any misclicks or mistakes when users are managing their posts or account.
7. The edit buttons will take the user to an edit webpage and load the previous data they submitted when they created the post or last edited it.
<div align="center">
<img src="static/images/readme-images/profile.gif" alt="Browsing Page" >
</div>

### Submitting / Editing Site Content
1. All users can submit esports epics to the website using the submit epic route that brings them to a form with input validation.
2. All users can submit events epics to the website using the add event route that brings them to a form with input validation.  
3. Users with the journalist status on their account can post and edit their news stories using the route submit news in the navigation bar. The route brings them to a form with input validation.
4. Editing and Deleting data contributed to the site can be done via the users profile.
5. Users with the moderator status can edit or delete any events users add to remove duplicates or events that are finished and no longer running.

### Manage Site
1. The manage site route is available to the admin account.
2. This page allows the admin to give / remove certain accounts moderator or journalist status.
3. Users who contribute a lot and are active could become moderators so they can keep the site up to date with the latest events and tournaments.
4. Journalists can email the admin or site owner for the right to post news. This is done to protect the integrity of stories and news posted to the website.
5. The admin can click the appropriate checkboxes for each account and click update to change their account privileges.

<div align="center">
<img src="static/images/readme-images/manage-site.png" alt="Browsing Page" >
</div>

### Esports Epics Modal
1. The main attraction to the website is to be able to browse and learn more about the esports play with context of the match and tournament.
2. The description text provides this context.
3. A modal that autoplays the video of the epic moment is loaded when the play button or VOD button is pressed. 
4. The user can close this modal with the close button or clicking out of it.

<div align="center">
<img src="static/images/readme-images/esports-epics.gif" alt="Browsing Page">
</div>

### Features to implement in the future
1. Make a comment section for each esports post so that more discussion and community engagement can occur.
2. Allow the users the ability to favorite clips and store their favorites in a section in their profile page or browse page.
3. Have an up vote and down vote system so good, enjoyable content is easier to find. 
4. If required have moderators remove / delete content that is negatively down voted, written poorly or potential duplicate that provides no new value.
5. Have an online merchandise shop that could put some epic moments in to images for t-shirts or other goods.

### Database Design
This project required the use of NoSQL and seems fine for the type of data that will be collected the users. There are 3 collections that are required and they are:
1. User Account information
2. Esports Posts Information/Content
3. Upcoming Esports Events & Tournaments

The type of data for each of these collections are detailed below.

#### User Account information

Data Base Key | Data Type | Description
:----:|:-----------:|:-------:
_id | ObjectId | MongoDB generated
username | String | Account login username.
email | String | The email for this account.
password | String | Users password.
submittedPosts | Array | User submitted esports posts.
submittedEvents | Array | User submitted esports events/tournaments.
favoritePosts | Array | User favorited esports posts.


#### Esports Posts Information/Content

Data Base Key | Data Type | Description
:----:|:-----------:|:-------:
_id | ObjectId | MongoDB generated
username | String | User who created post.
postTitle | String | Title to be displayed for post.
game | String | Name of the video game.
gameCategory | String | Game genre. (FPS, Moba, Fighting etc.)
featuredPlayer | String | Name of the pro player in the clip.
description | String | Descriptive text for other readers for context.
shortDescription | String | Shorter Descriptive text for mobile users.
tournamentName | String | Name of the tournament.
tournamentDate | TimeStamp | Date the esports game occurred.
video | String | Link to the video or clip to embed in post.
postImage | String | Image to go with description for post.

#### Upcoming Esports Events & Tournaments

Data Base Key | Data Type | Description
:----:|:-----------:|:-------:
_id | ObjectId | MongoDB generated
username | String | User who created event.
eventTitle | String | Event title to be displayed.
game | String | Name of the video game.
startDate | TimeStamp | Starting date of the tournament.
endDate | TimeStamp | Ending date of the tournament.
broadcastStartTime | TimeStamp | Starting time of the live broadcast.
tournamentsURL | String | Link to the tournaments website.
tournamentsImage | String | Image to go with event title.

#### News Stories

Data Base Key | Data Type | Description
:----:|:-----------:|:-------:
_id | ObjectId | MongoDB generated
username | String | User who created event.
title | String | News title to be displayed.
postBody | String | News story body of text.
postImage | String | Image to go with news title.


## Technologies Used
* [Materializecss:](https://materializecss.com/)
    - Materialize was used to assist with the responsiveness and styling of the website.
* [MongoDB:](https://www.mongodb.com/)
    - Database used for this project.
* [Heroku:](https://www.heroku.com/)
    - Cloud platform service used to deploy and host the website.
* [Flask:](https://flask.palletsprojects.com/en/1.0.x/)
    - Use templates and rendering webpages in response to user interaction.
* [Pip:](https://pip.pypa.io/en/stable/installation/)
    - Used to install packages and libraries to run/build the project.
* [Pymongo:](https://pymongo.readthedocs.io/en/stable/)
    - Interact with a mongo database in python.
* [Jinja:](https://jinja.palletsprojects.com/en/3.0.x/)
    - Jinja is used to simplify displaying dynamic data / elements in a html element / webpage.
* [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes.
* [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto' and the 'Merienda' font into the style.css.
* [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive.
* [GitPod:](https://gitpod.io/)
    - GitPod was used as my Editor/ Development Environment.
* [GitHub:](https://github.com/)
    - GitHub is used to store the projects code with version control.
* [responsivedesign](http://ami.responsivedesign.is/#)
    - Used to generate the mockups.
* [ezgif](https://ezgif.com/video-to-gif)
    - Used to generate gifs used throughout testing, readme and tutorial.
* [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used throughout to add icons for a more pleasing UX.
* [loading.io](https://loading.io/)
    - Used to create loader.gif

## Testing
Testing details can be viewed here [Testing.md](https://github.com/jamesr1775/esports-epics/blob/master/Testing.md)

## Deployment

### Creating your own local copy of the source code
- To get a copy of this repo, go to [Esports Epics Repo](https://github.com/jamesr1775/esports-epics), make sure your logged in. You can either 
    - Click the fork button which will create a copy of the repo into your account which is located in the top right hand corner of the link above.
    - If you have git installed on your machine, you can clone the repo with the command
        - git clone https://github.com/jamesr1775/esports-epics
    - Download the zip file of the source code by clicking on the "Code" drop down button located in the top right and clicking "Download Zip"
### Running locally
- In order to run this application locally you must have the following installed on your machine.
    - An Integrated Development Environment such as [Pycharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/)
    - [Python3](https://www.python.org/downloads/)
    - [MongoDB](https://www.mongodb.com/)
    - [Git](https://github.com/git-guides/install-git)
    - [PIP](https://pip.pypa.io/en/stable/installation/)
- The next step is to install everything listed in the requirements.txt document of the repo. To do that run the command in terminal of the IDE with the project opened:
    - pip -r requirements.txt.
- If you do not already have a mongoDB account go and create one [here](https://www.mongodb.com/)
    - Create a database named esports_epics and create the collections events, users, epics and news.
    - Create an env.py file in the repository.
    - This file should never be pushed to the repo and is already added to the gitignore file!
    - Inside the env.py file put the following information below.
    ```
    import os
    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "<secret_key>")
    os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>.vcsxb.mongodb.net/esports_epics?retryWrites=true&w=majority")
    os.environ.setdefault("MONGO_DBNAME", "esports_epics")
    ``` 
    - Replace the following with your correct values:    
        - `<secret_key>` (a key you create yourself in order to use session and flash functionality in flask)
        - `<username>` (your mongodb username)
        - `<password>` (your mongodb database password)
        - `<cluster_name>` (cluster name to the esports_epics database)
    - Refer to [mongodb's documentation](https://docs.atlas.mongodb.com/getting-started/) for more information.

### Using Heroku to deploy an application
1. A requirements.txt file should be created and kept updated, you can use the terminal command 
    - pip3 freeze > requirements.txt.
2. A Procfile is also required and can be create with the terminal command 
    - echo web: python app.py > Procfile.
3. Commit these files to your repo if they are not already committed.
4. Log in to your [Heroku](https://www.heroku.com/) account
5. Select New button and then select to create a new app.
6. Give your application a name and choose a region located nearest to you.
7. Make sure the is linked and is selecting the correct branch on your git repository.
8. Click the settings button of the app and click the reveal convig vars button.
9. Enter the following config variables:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
SECRET KEY | `<secret_key>`
PORT | 5000
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>.vcsxb.mongodb.net/esports_epics?retryWrites=true&w=majority"`
10. Your app should be ready for deployment now so click on Deploy button.
11. Enable automatic deployment so new changes get deployed automatically.

## Credits

Big thanks to my mentor Miguel Martinez with great feedback and help throughout the project. He always motivates me to learn new things and do a little more improvements that
go a long way to my learning and to raising the quality of my projects.

### Acknowledgements
- [1] Obtained the javascript for confirming the passwords match from [jsfiddle](http://jsfiddle.net/SirusDoma/ayf832td/).
- [2] Needed a larger input box for the description field for submitting an event. Got information from [w3schools](https://www.w3schools.com/tags/tag_textarea.asp).
- [3] Wanted to have a youtube video in a modal using bootstrap. Bootstrap documentation pointed to [stackoverflow](https://stackoverflow.com/questions/18622508/bootstrap-3-and-youtube-in-modal). Had issues with using both bootstrap and materialize so cut out bootstrap but used the data- tag from this page idea to pass the src url to the iframe.
- [4] Wanted to hide the flashed images after a certain delay. Obtained the information from [stackoverflow](https://stackoverflow.com/questions/31176402/how-to-hide-flash-message-after-few-seconds)
- [5] I needed the manage user forms data in the app.py route and found out I can receive it as a dictionary based off the input names and values here [seanbehan](http://www.seanbehan.com/how-to-get-a-dict-from-flask-request-form/)
- [6] The centering of the play icon over the images for the esports post was obtained from [stackoverflow](https://stackoverflow.com/questions/43299877/center-icon-over-img-in-bootstrap/43299938)
- [7] Found out to use include when creating a block/ template of code to be reused multiple times from [stackoverflow](https://stackoverflow.com/questions/55841442/can-you-create-components-in-flask-jinja-to-insert-in-various-templates).
- [8] Wanted to resize the the posts cards to be all the same height so I found useful information here to loop through elements by class and apply height changes. [stackoverflow](https://stackoverflow.com/questions/44092012/loop-through-same-class-elements-and-assign-width-and-height).
- [9] The pattern/ Regex for the images input form was obtained from the following webpage. [stackoverflow](https://stackoverflow.com/questions/40687546/html-input-require-url-to-end-in-specific-filetype).
- [10] The pattern/ Regex for the video input form was obtained from the following webpage and only allows youtube links. [codegrepper](https://www.codegrepper.com/code-examples/javascript/javascript+validate+url+to+match+youtube+video).
- [11] In order to not have the search refresh the page this youtube video helped me use flask, javascript and fetch to pass data to my webpage to display. [Julian Nash Youtube](https://www.youtube.com/watch?v=QKcVjdLEX_s).
- [12] Wanted the hero text to be animated and slide in from left to right. Got some information here [stackoverflow](https://stackoverflow.com/questions/16989585/css-3-slide-in-from-left-transition)
- [13] Obtained the hero text color animation from [SHINE by Andreas Storm](https://freefrontend.com/css-text-animations/). 
- [14] Got a reminder for putting text over an image from [stackoverflow](https://stackoverflow.com/questions/5758642/how-to-put-text-over-images-in-html)
- [15] Got some information on pagination from these youtube  video [Pretty Printed Youtube](https://www.youtube.com/watch?v=Lnt6JqtzM7I)   [Corey Schafer Youtube](https://www.youtube.com/watch?v=PSWf2TjTGNY)
- [16] Got the scrolling up code from [stackoverflow](https://stackoverflow.com/questions/12125883/jquery-pagination-scroll-to-top)
- [17] Fixed a html validator error where src="" in an iframe was invalid so instead it need to be src="about:blank". Found this fix from  [stackoverflow](https://stackoverflow.com/questions/5946607/is-an-empty-iframe-src-valid)
- [18] The site pre loader code was obtained from [stackoverflow](https://stackoverflow.com/questions/30478549/pre-loader-image-at-page-load-issue) and [smallenvelop](https://smallenvelop.com/display-loading-icon-page-loads-completely/).