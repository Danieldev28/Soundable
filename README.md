         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 

# Soundable
Hello, My name is Daniel and through this project I am excited to present to you yet 
another in a series of web applications on my journey through Full-Stack web development. Welcome to fullstack frameworks with django this is 
the final project in my fullstack web development course journey series. I have learned and utilized many new skills and technologies in order 
to get to this point.This project is basically an application which allows the user to create a profile, and was intded so the user can upload 
original songs and instrumentals for sale through this plaform for free.This application allows for the sharing and collaboration of artists writers
and producers in a way that is mutally beneficial for all parties involved.

Singing covers is great but can only take you so far. If you want to take your career as a musical artist to the next level you need to sing original songs.
Once you have finished your song thats a hit, you can then share them and proliferate your material from itunes to youtube to, live perfomance to thriving career 
with the heavyweights of the industry.Here at Soundable we are fully aware of this necessity to set careers apart from the rest, and aimed to fill the gap in the 
marketplace with our offering a web application by muscians and for musicians, that is new business model and will help revolutionize the ways that new artist can 
carve their path uniquely and get heard in a notoriously over crowded marketplace.

Welcome to my portfolio Full-Stack Frameworks with Django!

Hi my name is saleka

 
## UX
 
This website is designed for the to be user focused allowing the user to really take advantage of the website, by adding music, and or and buying music. Thus enabling 
songwriters, producers and instramentalists a way of earning real income from their commercial creations.I am excited to offer this as a service because there are only 
a few others out there. I belive what helps Soundable stand apart from others is the ease of use. Also the fact that we are not tied to a big company which would require 
us to charge for this service to our customers. Rather the platform is created for the community to continue being creative and find a way to make a living from their art.
The Ux design is simple to navigate with simple dropdowns and click through menus. All the information that you will need is stored is eaither in a dropdown or a form will 
prompt you to enter details.

 A list of user Stories:

<a href= "files/Conceptual design soundable.pdf">Conceptual design pdf</a>
- As a user type, I want to perform an action, so that I can achieve a goal.
- As a user I want to listen to many songs
- A song has many users
- A user can upload many songs
- An upload can be purchased by one user
- A user has a profile 
- Each profile has a user which stores their downloaded purchased songs
- A user can purchase many songs, but each song can only be purchesed by one user


## Features

This section describes the different parts of my project:
The artist page allows you to view a single song and all the information related to that title.
The artists(music page) is simply the combination of all music downloaded across the website by all users, you can view our enitre library from this page. Also it allows for 
filtering on a high level or a very low level depending on how many fields of filtering are selected. Can use the search bar or the filter seach.
The base page is the base template for the websites look and feel which is taken from <a href= "colorlib.com">here</a>.
Then we have the contact page wich consists of a simple contact page and call to action to enter your email in and recieve notifications from us.
The profile page contains the user registration information where they fill their personal information out.
The songupload page has the features to upload your song and place it in a category for viewing on the website.
Finally we have the login and logout functionalities which give acces to other options such as song submission, only when the user is logged in.

### Existing Features
- Feature 1 - allows users to preview songs from various creators for sale
- Feature 2 allows users to a make browse and search, for a particular song throughout various genres
- Feature 3 allows users to update their profile and information 
- Feature 4 allows users to view lyrics and other important information related to the current song they are previewing
- Feature 5 allows users to have an acccount and upload their own songs
- Feature 6 login and lougout functions
- Feature 7 Most recent uploads shown on home page (3 items)
- Feature 8 Song upload page allows user to upload a song with easy drop downs and place a download file inside

### Features Left to Implement
- Feature to pay with stripe (TBA)
- Upgraded user interface with eyecatching design
- Shorten song preview to 1 minute in lenghth
- Form validation to return error message when registration form is not completed properly
- View downloads and uploads in user profile page (keep counts and names)


## Technologies Used

- [JQuery](https://jquery.com) library
- The project uses **JQuery** to simplify DOM manipulation.
- Django framework, used as backend framework
- Bootstrap v4.3.2 used for website cross campatibility across devices
- Fontawsome used for fonts
- SQLite3, used to access my database from the console
- JavaScript, used for front end password verification
- HTML, used to dictate the structure of my web application
- python used as the primary backend language inside django framework
- CSS, used to style my pages 
- Heroku, used to deploy the project to the live server for viewing by the public
- Stripe used for payment services (TBA)
- MySQL  is a relational database management system 
- MySQL workbench (used for crud operations) used as an interface to work with MYSQL allows for a remote or local server connection


## Testing

The testing process for this project was ongoing throughout, making sure data was being saved,login and logout functionalilty worked as expected.
Ensuring that songs were being shown on the most recently added section of the home page, and also added to my playlist also making sure that the user profile was updatable and 
information was being saved to the database. As well as ensuring songs werre viewable in as search queries on the search page.


1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears
2. Login/Logout
    1.Confirm that login works and login validation message is displayed on the home page
    2.Try access profile without logining in
    3.Try to fill out registration form with incomplete fields and verify it does not create a user account
    4.Try to logout and login using and different password but same username and verify that display message is; your password is incorrect!
3.Registration
    1. Try to see if I can register without filling the form and verify its not possible by submiting
    2. Try to register again if I already have an account
4.Song submission
    1.Try to submit a incomplete song form verify it doesn't submit
    2.Try to unsubmit my song by going back on the page link (browser navigation)
5.Edit profile
    1.Try Django templating form, verify it is updating registration information on click of submit
    2.Try user profile and make sure song information and user information are the same 
    3.Verify user profile is being saved inside the Django admin panel
6.Search
    1.Try the filtered search feature by genre,mood,soundslike,type,gender,tempo.

I have also tested my project on various screen sizes from a laptop to a desktop it worked flawlessly on both due to bootstraps intelligent sizing features.
Everything is able to collapse neatly when on a phone screen to yeild a functional user interface wich clenly presentss to a user.

Here is a list of bugs encountered and their solutions during the development process:

1. error-
'str' object has no attribute '_meta'

2. error-
Invalid block tag: 'static'
https://bootstrapious.com/p/bootstrap-search-bar -this is a source
https://unsplash.com/photos/gUK3lA3K7Yo
https://www.w3schools.com/howto/howto_css_social_login.asp

3. error-
when creating login page-
'function' object has no attribute 'form' django

4. error-
name 'make_password' is not defined
user profile error! 3 sources
AttributeError at /accounts/profile/

5. password errors-
how to check confirm password field in form without reloading page-stackoverflow eresource answer
https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page

6. How to filter-
https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html (filter)
https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html (filter)
https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html crispy forms at bottom follow to design template custom field
placement with crispy forms

7. order objects by date-
https://stackoverflow.com/questions/12759594/getting-recently-added-object-django

## Deployment
Process to deploy:
- I have kept this project file in github 
- Different values for environment variables/Heroku Configuration varibales were set
- Created requiremnent.txt and procfile in order to host on Heroku  paltform
- Deployed to Heroku server for final project viewing 

## Credits
I would like to credit numerous cites for inspiration in ux design as I could 
not have done this without inspiration and at times a little persperation. Cite 
used for application inspiration <a href="https://www.rocketsongs.com/">here.</a> 
I would also like to credit the stackoverflow community for any methods and 
code snippets used, it was a really awesome resource to roll up my sleeves and 
learn on the website.
### Content
- The text for all the paragraphs was copied from  [Random articles](http://watchout4snakes.com/wo4snakes/Random/RandomParagraph)
 http://watchout4snakes.com/wo4snakes/Random/RandomParagraph

### Media
- The photos music,text used on this website were obtained from:
- https://unsplash.com/
- http://watchout4snakes.com/wo4snakes/Random/RandomParagraph
- https://www.bensound.com/-music source

### Acknowledgements

I would like to acknowledge the use of bootstrap components. As well as 
w3schools.com for when I got stuck. I also searched stackoverflow.com countless
times for more information to solve problems with my application when I was stuck 
on the harder portions. I am thankful that my project is finally closer to what I 
envisioned. Thank you for viewing this presentation of my 
Data Centric Development project and hope to present to you many more in the future.
Until then that wraps up my skills as a brand new Full-Stack software developer.
Speacial thanks goes to Abhay Barthwal for continued mentorship during and after my project.
Thank you.
                                                <a href="#top">Back to top</a>
### This is for educational use.
