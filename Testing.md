# Esports Epics Testing
The deployed version of the Sorting Visualiser can be found at [Esports Epics](https://esports-epics.herokuapp.com/).

The source code for the project can be viewed at [github](https://github.com/jamesr1775/esports-epics).

## Table of Contents

1. [**Testing**](#testing)
    - [**Code Validation**](#code-validation)
2. [**User Stories Tests**](#testing-user-stories)
3. [**Manual Testing**](#manual-testing)
    - [**Site Header**](#site-header)
    - [**Esports Video Modal**](#esports-video-modal)
    - [**Profile**](#profile)
    - [**Browse Page**](#browse-page)
    - [**Submit and Edit Forms**](#submit-and-edit-forms)
    - [**Manage Site**](#manage-site)
    - [**Footer**](#footer)
4. [**Further Testing**](#further-testing)
5. [**Bugs and Issues Resolved**](#bugs-and-issues-resolved)
6. [**Unsolved Bugs**](#unsolved-bugs)

## Testing
### Code Validation
* The HTML passed and showed no errors in the [W3C Markup Validation](https://validator.w3.org/)
* The CSS passed and showed no errors in the [W3C CSS validation ](https://jigsaw.w3.org/css-validator)
* The Java Script was tested and no errors were found using [JSHint](https://jshint.com/)
* The python Pep8 standard was checked with the IDE and also [pep8online](http://pep8online.com/) 

### Testing User Stories
1. To be able to navigate the website efficiently and intuitively so that I can find posts that capture my interest or make a new post myself.
    - The site navigation bar is at the top of the screen and contains links to create content or browse posts by all users.
    - The home page contains hero image and a carousel of recent posts to capture the users attention and get them wanting to browse other content.
    - The text inside the hero image immediately tells the user what the site is about.
    - User account creation and logging in/out are located in the navbar and the navbar updates appropriate links to show a certain user account if they are logged in.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/log-in-out-register.gif" alt="User Story 1">
    </div>
2. A place / library of the best esports moments so that I can view them for enjoyment and share them with others.
    - The homepage has the most recent submissions by all the users in a carousel users can click on to open the information and the video itself.
    - Users can go over to the browse page to view and filter all the sites user's posts so they can find games or players they are interested in.
    - User's can share the youtube video link with the inherent share feature of the embedded youtube video.
3. Read the context behind the clip or moment so that I can understand why it is an amazing play.
    - The cards that contains the user's posts in the browse page has a section users submit descriptions for to explain the video / esports moment so others can get more incite into what is going on in the video.
    <div><br/></div>
    <div align="center">
    <img style="width:70%; margin-left:15%;" src="static/images/readme-images/esports-epics.gif" alt="User Story 2,3">
    </div>

4. The ability to add clips / competitive moments so I can contribute to the collections of great esports moments so others can view them.
    - Users can add their own epics by using the submit epic link in the navigation bar.
    - The form has validation so that users are required to submit correct and a minimum / maximum amount of information to the post.
    - Users submissions will appear in the carousel if most recent, otherwise they can be viewed on the browse page.
5. Be able to edit or delete esports posts that I added incase I made a mistake or the post already exists.
    - In a users profile page, a section exists for any content they have submitted to the site. The content they submitted is shown along with an edit button that loads up the information they previously submitted back into the same form so they may edit and update it.
    - A delete button is also present and will delete the correct content / post if pressed. A confirmation to delete is shown to prevent misclicks and mistakes.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/submit-edit.gif" alt="User Story 4,5">
    </div>

6. To be able to filter all the moments by intuitive categories such as game, genre or date so I can quickly navigate to games / clips that interest me.
    - In the browse page users can filter all the epics displayed to by game ,genre, tournament, year, player, title and description.
    - They can combine searches by typing multiple things such as two or three games or a player and a game etc.

7. View upcoming esports tournaments so I know when they will be live in order to watch them.
    -  The upcoming and ongoing tournaments are displayed on the homepage in an accordion.
    - Clicking on a tournament opens a drop down tab with the tournament information.
8. Add upcoming esports tournaments so that other users can benefit from knowing when tournaments are live.
    - All users can submit esports tournaments so that they will appear for other users benefit in the home page.
    - The input form requires important information esports viewers would want to know such as the date and time of a tournament.
9. Be able to edit or delete tournament posts that I have added to keep the information reliable and up to date.
    - There is a section in the user profile that shows a user and / or moderator account the tournaments they or others have created.
    - A moderator account can also edit and delete entries in order to not have duplicates or outdated tournaments on the home page causing clutter.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/events.gif" alt="User Story 7,8,9">
    </div>
10. Find the contact information and social media links easily so I can keep up to date with the website and posts.
    - The websites social media links are located in the footer of all the webpage routes.
    - Each button will open up the correct corresponding media link in a new tab.

### Manual Testing
* All manual tests below:
    - were ran on chrome and firefox.
    - were repeated on various screen resolutions using the chrome and firefox developer tools that include desktops, ipad, ipad pro, iphone X, 5, 6 ,7 , 8 and the plus models.
    - were repeated on the developers own smartphone (samsung) and tablet (ipad), desktop and laptop.
        <div><br/></div>
        <div align="center">
        <img style="width:70%;"  src="static/images/readme-images/test-devices.png" alt="Test iphone, Samsung and Ipad">
        </div>    

#### Site Header & Hero Image
##### Device Specific Layout Checks
- The Header responsiveness was tested by varying the screen size to see that the logo and navbar were responsive and also that the navbar becomes an expandable burger icon on smartphones and tablets.
- The logo stays to the left of the header on tablets and desktops but moves to the center for small and extra small screen sizes.
##### Site Header Tests
- The logo was tested that when it is pressed it returns / refreshes to the home page.
- Each link was tested to make sure it brings the user to the correct page or logs them in or out.
- Make sure that submit epic, add event, profile, log out pages only appear after a user is logged in.
- Make sure the register and log in buttons disappear when logged in and that the log out button appears.
- The logout button correctly hides the links shown to logged in users and shows the register and log in buttons.
##### Hero Image Tests
- The image should be responsive across multiple devices.
- The image should have a sliding animation upon reaching the home page.
- The hero text should slide in from the left to the right center of the screen on top of the image.
- The hero text should have a color changing animation.

    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/test-header.gif" alt="Test Header">
    </div>

#### Esports Video Modal
- The video modal should be shown when a user clicks on the VOD here button or the play button in the browse and profile page cards of epics.
- The title of the esports post should be above the video iframe.
- The video should autoplay when the iframe loads.
- Video controls to pause or mute the video are available to the user.
- Upon clicking the close button or dismissing the modal by clicking out of it, the modal should close and the video / audio should stop.
- The video should restart upon closing and reopening the modal.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/test-video-modal.gif" alt="Test Video Modal">
    </div>

#### Profile
##### Device Specific Layout Checks
- The number of esports posts per row should be 3 for laptops and desktops, 2 per row for tablets and 1 per row on smart phones.
- The images and cards scale to the device width.
##### Profile Tests
- The user information is displayed in a card at the top of the page under the navbar.
- The delete account button pops up a modal that asks the user to confirm the deletion of the account
    - If the user presses cancel the modal should close and the user remains on the profile page.
    - If the user confirms account deletion, their account is removed from the data base and they are returned to the default home page with no `session['user']`.
- The esports posts card titles and images all open up the video modal.
- The edit button brings the user to the edit esports epic page. 
    - The form should load all the posts information into the input fields for convenience.
    - Upon editing the user should be returned to the profile page with their updated posts.
- The delete button for a post pops up a modal that asks the user to confirm the deletion of the post.
    - If the user presses cancel the modal should close and the post should remain in the database.
    - If the user confirms post deletion, their post is removed from the data base and they are returned to updated profile page.
    - Upon deleting the user should be returned to the profile page with their updated posts.
- The news posts created by the user should be displayed along with an edit and delete button.
- The events created by the user should be displayed along with an edit and delete button.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/test-video-modal.gif" alt="Test Profile">
    </div>

#### Browse Page
##### Device Specific Layout Changes
- The number of esports posts per row should be 3 for laptops and desktops, 2 per row for tablets and 1 per row on smart phones.
- The images and cards scale to the device width.
##### Browse Tests
- The reset and search button remain centered on the screen under the input search field.
- Pagination is used to display the posts in the browse page.
    - The number of posts per page at most should be 6.
    - All the posts retrieved from the data base should be split between pages.
    - The page links displays the correct posts when clicked through.
    - The carrot navigation arrows increments or decrements the current page appropriately and displays the correct posts.
    - When the page number is at the minimum or the maximum the correct carrot navigation arrows get disabled and don't do anything when pressed.
    - Upon navigating to a new page of posts the body of html should scroll up. 
- The input search field should be tested for the indexes and combinations of:
    - Game
    - Game Category
    - Player
    - Description
    - Tournament
    - Tournament Year
    - Title
- The correct posts is retrieved when a search is made and should also be displayed with pagination.
- The cards that contain the posts have the correct title, description and image submitted by the user to the database.
- Upon clicking the image or the title button the video modal pops up with the correct video link from the database.
- If no search results are returned, the card container should indicate that to the user.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/test-browse.gif" alt="Test Browse Page">
    </div>


#### Submit and Edit Forms
The four forms for creating or editing esports epics, esports news, tournament events and registering are tested as follows.
##### Device Specific Layout Changes
- The form should be the same across desktops, laptops and computers. 
- When their are two input fields per row, these should become separate rows on 
smartphones
- The submit and cancel button will always be on the same row and be the same width across all platforms. 

##### Submit & Edit Forms Tests
- The input fields all require either a maximum or a minimum number of characters.
- These should be tested to see if the javascript can change heights and widths of the cards to fit the elements and keep the cards the same height.
    - Test the maximum and minimum acceptable lengths for all form inputs that will become text or headers in the html. Make sure they fit the cards in the browse page and the profile page.
            <div><br/></div>
            <div align="center">
            <img style="width:70%;"  src="static/images/readme-images/test-forms-input-lengths.png" alt="Test Forms">
            </div>
    - Also make sure the text fits the carousel cards for the recent submissions section also.
        <div><br/></div>
        <div align="center">
        <img style="width:70%;"  src="static/images/readme-images/test-forms-carousel.png" alt="Test Forms">
        </div>
- The input fields for images should require links that end in certain image file types such as gif, png  or jpg. Test incorrect and correct links.
- The input fields for video links should be of a certain youtube link. (i.e clicking the share button on youtube will give the right link for this input field). Test incorrect and correct links.
- If the input field is incorrect the user receives feedback as to what input is expected.
- Upon clicking cancel the user should be returned the Home page.
- Upon clicking submit the new user post should 
- When editing a event, epic or news, all of the previous submitted information stored in the database should be loaded back into the form so users can easily edit their submissions.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/test-forms.gif" alt="Test Forms">
    </div>

#### Manage Site
##### Device Specific Layout Changes
- The form and checkboxes should be the same across all devices.
##### Manage Site Tests
- The manage site link is only available to an admin account.
- The page should display all users of the website and the current status of whether they are moderators or journalists for the website.
- Unchecking or checking a account status checkbox and clicking update should either add or remove the correct account status stored in the database for a given user.
- Clicking the cancel button should do nothing to the user accounts and return the admin account to its profile page.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/test-manage-site.gif" alt="Test Manage Site">
    </div>

#### Footer
- The social media icons opens up the relevant social media platforms in a new tab.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/test-footer.gif" alt="Test Footer">
    </div>
#### Further Testing
- I asked friends and family to test and interact with the site on their own devices which included ipads, iphones and samsung phones.
- Tested myself on physical devices laptop, desktop, ipad, samsung phone, iphone.


### Bugs and Issues Resolved
- The logout button sometimes caused the site to crash because the session variables I created did not exist and I was trying to remove them from the session. I solved this by making sure the session variables such as is_journalist is set properly and removed.
- Checkboxes in forms only submit their data when they are checked, so unchecking a user from journalist status does not get sent. Learnt it from here [stackoverflow](https://stackoverflow.com/questions/54972705/sending-checkbox-value-to-flask) which gave me a workaround to just loop through users and any not checked remove their privilege. This is not the most efficient way and may need updates in the future.
- When I fixed the searching to not refresh the page, the dynamic elements could not trigger the modal as they were newly generated. I found to change the jquery for the modal trigger from [stackoverflow](https://stackoverflow.com/questions/12690142/jquery-on-not-registering-in-dynamically-generated-modal-popup)
- Fixed the issue when dismissing the video modal, the video / audio would continue to play in the background. Found information here [stackoverflow](https://stackoverflow.com/questions/37037223/bootstrap-how-to-stop-video-from-playing-after-the-modal-has-been-closed?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa) to stop the video from playing but I also needed to get rid of the autoplay in the `src` of the iframe. Also found out about the onCloseEnd from [stackoverflow](https://stackoverflow.com/questions/52877745/materializecss-modal-events-not-firing) that allowed me to replace the `src` when dismissing / closing the modal.
- The pagination navigation buttons were not triggering on click events. Found a fix for this from [stackoverflow](https://stackoverflow.com/questions/17936242/dynamically-created-buttons-not-firing-onclick-event)
- Needed to put the carousel initializer in the document load other wise it was completely misaligned.
- Ad blockers will cause embedded youtube / google errors to display in the console. These errors disappear if the ad blockers are disabled. The errors do not cause any problems with playing the videos either way.
    <div><br/></div>
    <div align="center">
    <img style="width:70%;"  src="static/images/readme-images/adblock-errors.png" alt="Test Footer">
    </div>
- Found materialize creating a hidden div for textarea inputs thats not used upon window resizing but this cause white space to be generated and the site content to be smaller. Got information from [stackoverflow](https://stackoverflow.com/questions/30609388/why-my-meteor-app-create-hiddendiv-common-div-tags) and then came up with making the div display none to fix this.
### Unsolved Bugs
Currently there are no known bugs.