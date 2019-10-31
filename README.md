         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!
# Soundable
Hello, My name is Daniel and through this project I am excited present to you yet 
another in a series of web applications on my journey through Full-Stack web development. Welcome to fullstack frameworks with django this is the final project in my fullstack web development course journey. I have learned and utilized many new skills and technologies in order to get to this point.
This project is basically an application which allows the user to create a profile, and was intded so the user can upload original songs and instrumentals for sale through this plaform for free.
This application allows for the sharing and collaboration of artists writers and producers in a way that is mutally beneficial for all parties involved.

Singing covers is great but can only take you so far. If you want to take your career as a musical artist to the next level you need to sing original songs.
Once you have finishedd your song thats a hit, you can then share them and proliferate your material from itunes to youtube to, live perfomance to thriving career with the heavyweights of the industry.
Here at Soundable we are fully aware of this necessity to set careers apart from the rest, and aimed to fill the gap in the marketplace with our offering a web application by muscians and for musicians, that is new business model and will help revolutionize
the ways that new artist can carve their path uniquely and get heard in a notoriously over crowded marketplace.

Welcome to my portfolio Data Centric Development application! 

 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

This website is desgned for the to be user focused allowing the user to really take advantage of the website, by adding music, and or and buying music. Thus enabling songwriters, producers and instramentalists of earning real income from their commercial creations.
I am excited to offer this as a service because there are only a few others out there. I belive what helps Soundable stand apart from others is the ease of use. Also the fact that we are not tied to a big company which 
would require us to charge for the service to our customers rather the platform is created for the community to continue being creative and find a way to make a living from their art.
The Ux design is simple to navigate with simple dropdowns and click through menus.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
<a href= "files/Conceptual design soundable.pdf">Conceptual design pdf</a>
- As a user type, I want to perform an action, so that I can achieve a goal.
- As a user I want to listen to many songs
- A song has many users
- A user can upload many songs
- An upload can be purchased by one user
- A user had a profile 
- Each profile has a user which store their download purchased songs
- A user can purchase many songs, but each song can only be purchesed by one user


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
The artist page allows you to view a single song and all the information related to that title.
The artists(music page) is simply the combination of all music downloaded across the website by all users, you can view our enitre library from this page. Also it allows for 
filtering on  a high level or a very low level depending on how many fields of filtering are selected.
The base page is the base template for the website look and feel which is atemplate taken from <a href= "colorlib.com">here</a>.
Then we have the contact page wich consists of a simple contact page and call to action to enter your email in and recieve notifications.
The profile page contains the user registration information.
The songupload page has the featrues to upload your song and place it in a category for viewing on the website.
Finally we have the login and logout functionalities which give acces to other options such song submission only when the user is logged in.
### Existing Features
- Feature 1 - allows users to preview songs from various creators for sale
- Feature 2 allows users to a make a browse, and search for a particular song throughout various genres...
- Feature 3 allows users to update thier profile and information 
- Feature 4 allows users to view lyrics and other important information related to the current song they are previewing
- Feature 5 allows users to have an acccount and upload their own songs
- Feature 6 login and lougout functions
- Feature 7 Most recent uploads shown on home page

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Feature to pay with stripe
- upgraded user interface with eyecatching design
- Shorten song preview to 1 minute in lenghth
- form validation to return error message when registration form is not completed properly
- View downloads and uploads in user profile page (keep counts and names)


## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com) library
- The project uses **JQuery** to simplify DOM manipulation.
- Django framework, 
- Bootstrap v4.3.2
- Fontawsome
- SQLite3,
- JavaScript, 
- HTML, 
- python
- CSS, 
- heroku, 
- stripe
- MySQL relational database management system
- MySQL workbench (used for crud operations)


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.
For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

The testing proces for this project was ongoing throughout making sure data was being saved,login and login functionalilty worked as expected, 
ensureing that songs were being shown on the most recently added section of the ohome page, and also added to my playlist also making sure that the user profile was updatable and 
information was being save d to the database.


1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.
2. Login/Logout
    1.Confirm that login works and login validation message is diplayed on the home page
    2.Try access profile without logining in
    3.Try to fill out registration form with incomplete fields and verify it does not create a user account
    4.Try to logout and login using and different password but same username and verify that display message is; your password is incorrect!
3.Registration
    1. Try to see if i can register without filling the form and verify its not possible by submiting
    2. Try to register again if I already have an account
4.Song submission
    1.Try to submit a incomplete song form verify it doesnt submit
    2.Try to unsubmit my song by going back on the page link
5.Edit profile
    1.Try Django templating form verify it is updating registration information on click of submit
    2.Try user profile an make sure song information and user information are the same 
6.Search
    1.Try the filtered search feature by genre,mood,soundslike,type,gender,tempo.

I have also test my project on various screen sizes from a laptop to a desktop it seemed to work flawlessly on both due to bootstraps intelligent sizing feaatures.
Everything is able to collapse neatly when on a phone screen to yeild a functional user interface.

Here is a list of interesting bugs and problems Iencounted and their solutions during the development process:

error-
'str' object has no attribute '_meta'

error-
Invalid block tag: 'static'
https://bootstrapious.com/p/bootstrap-search-bar -this is a source
https://unsplash.com/photos/gUK3lA3K7Yo
https://www.w3schools.com/howto/howto_css_social_login.asp

error-
when creating login page
'function' object has no attribute 'form' django

error-
name 'make_password' is not defined
user profile error! 3 sources
AttributeError at /accounts/profile/

password errors-
how to check confirm password field in form without reloading page-stackoverflow eresource answer
https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page

How to filter-
https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html (filter)
https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html (filter)
https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html crispy forms at bottom follow to design template custom field
placement with crispy forms

order objects by date-
https://stackoverflow.com/questions/12759594/getting-recently-added-object-django

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits
I would like to credit numerous cites for inspiration in ux design as I could 
not have done this with inspiration and at times a little persperation. Cites 
used for application inspiration <a href="https://www.rocketsongs.com/">here.</a> 
I would also like to credit the stackoverflow community for any methods and 
code snippets used, it was a really awesome resource to roll up my sleeves and 
learn on the website.
### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
 http://watchout4snakes.com/wo4snakes/Random/RandomParagraph

### Media
- The photos used in this site were obtained from ...
https://unsplash.com/
http://watchout4snakes.com/wo4snakes/Random/RandomParagraph
### Acknowledgements
https://www.bensound.com/-music source

- I received inspiration for this project from X
- ## Acknowledgements

I would like to acknowledge the use of bootstrap components. As well as 
w3schools.com for when I got stuck. I also searched stackoverflow.com countless
times for more information to solve problems with my application when I was stuck 
on the harder portions. I am thankful that my project is finally exactly as I  
had envsioned.  Thank you for viewing this presentation of my 
Data Centric Development project and hope to 
present to you many in the future.Until then that wraps up my skills as 
as a brand new Full-Stack web developer.
                                                <a href="#top">Back to top</a>
### This is for educational use.




<!--error-->
<!--'str' object has no attribute '_meta'-->
<!--error-->
<!--Invalid block tag: 'static'-->
<!--https://bootstrapious.com/p/bootstrap-search-bar -this is a source-->
<!--https://unsplash.com/photos/gUK3lA3K7Yo-->
<!--https://www.w3schools.com/howto/howto_css_social_login.asp-->
<!--error when creating login page-->
<!--'function' object has no attribute 'form' django-->
<!--error-->
<!--name 'make_password' is not defined-->
<!--user profile error! 3 sources-->
<!--AttributeError at /accounts/profile/-->
<!--how to check confirm password field in form without reloading page-stackoverflow eresource answer-->
<!--https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page-->
<!--https://www.bensound.com/-music source-->
https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html (filter)
https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html (filter)
https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html crispy forms at bottom follow to design template custom field
placement with crispy forms
<!--order objects by date-->
https://stackoverflow.com/questions/12759594/getting-recently-added-object-django
https://stackoverflow.com/jobs/149252/full-stack-developer-top-hat
<!--image didnt make the cut-->
<!--images/tim-mossholder-eivYBKv3MAs-unsplash.jpg-->
http://watchout4snakes.com/wo4snakes/Random/RandomParagraph
strip
https://stackoverflow.com/jobs/149252/full-stack-developer-top-hat