### Final Team Submission

Title: RudyOnRails  
Subtitle: PlayWithMe  
Semester: Fall 2018  
Team Members: Navin Lal, Nithin Mahesh, Rudy Pikulik, Chris Rybiki, Panav Setia, Yusuf Sezer  

## Overview:

PlayWithMe is an online web platform that allows its users to find or create groups for gaming. Our users will be able to log in to our website and create gaming sessions that allows users to join and communicate with the rest of the group. In addition to creating a group, a user will also be able to login and search for a group to join. PlayWithMe brings all kinds of gamers together allowing collaboration between people across campuses.

Currently the gaming industry has platforms such as Steam, Playstation Network, and Xbox Live. Our platform however, compared to the competition, is currently centered around the UMass Campus. Since we were focused on creating an application for avid gamers within a college campus our application is it’s own standalone entity unlike other platforms currently available. 

No other gaming platform at the moment connects players with not only games, but incorporates a facebook messenger like chat system to communicate more efficiently and get to gaming! 

### User Interface:  

Sign Up - This page allows users to create an account.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/SignUpPage326.png?raw=true)

Log In - This is the page where users must log into their account to access the multiple pages of our website.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/LoginPage326.png?raw=true)

Home Page - This is the main page users are directed to when they log in. From here they can access other main pages while being shown latest news such as new games that have been released.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/HomePage.PNG?raw=true)

Create A Group - This page allows user to create a gaming session that will be visible to other users. The page allows the user to select to create either a local or online session and input the required fields to create the session.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/PostSessionPage.PNG?raw=true)

My Groups - This page shows users which gaming session they belong to. From here they can select any of their groups to view the specific session view page.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/MyGroups326.png?raw=true)

Session View - This page shows the the multiple users in a specific session and also contains a chat box that allows the users of the session to talk with each other.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/SessionDetailView326.png?raw=true)

Find A Group - This page allows the user to search for gaming sessions by specifying fields such as location, platform, game, etc.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/FindGroups326.png?raw=true)

Search Results - This page shows the user the results of their search. From this page the user can view each group and choose to join any session.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/SearcResults326.png?raw=true)

About Us - This page gives a brief description of the PlayWithMe team and shows a picture of all of us.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/AboutUs326.png?raw=true)

 
### Data Model:  

Our data model as it stands has six major components: games, platforms, sessions, django users, messages, and profiles.

Games are simple items that contain basic information like a name, the platforms it can be played on, as well as a description. Platforms (like Playstation, PC, etc.) can each be associated with one or more games.

Users can sign up for an account on our website, storing a username and passoword. Each user is associated with a Profile which can  be used to host and find groups and message other people. Each profile (with a username and password) is associated with 0 or more sessions that they are a member of, and zero or more sessions that they are the owner of. Profiles can also add information about which games they play and what game platforms they use.

Sessions are each assigned a unique ID, and are associated with 1 or more profiles, of which one of is the owner. A session also has one or more games and one or more platforms associated with it. Lastly, each session is associated with messages sent between members, and a sessioncan have a location associated with, as well as a boolean indicating if the members are playing online or offline games.

Finally, messages are simple data items that are associated with a sender (profile), one or more receivers (profile), and the time the message was sent.

![alt text](https://github.com/yusufsezer/PlayWithMe/blob/master/docs/imgs/DataModel.png?raw=true)  

### URL Mappings/Paths  

No Path - Leads to our home page. This website shows users our “What’s New” section and allows all users to access the find a group page. If the user is not logged in, then trying to access any other page will redirect the user to our sign up page.  

/signup - This leads to the signup page which allows users to create an account.  

/accounts/login - This directs the user to the login page.  

/search - this page, accessible to anyone is our find a group page. From here users can search for sessions.  

/results/?query=result - this page shows the user their search results. This is also accessible to anyone.  

/session/[session#] - This page does require a user to be logged in and shows the Session View of the selected group that the user is either viewing or joining.  

/post_session - This path takes the user to the Create A Group page only if the user is logged in.  

/my_groups - This path takes the user to the My Groups page only if the user is logged in.  

/about_us - This path takes the user to the About Us page and can be viewed by anyone.  

### Authentication

User authentication can take place on the sign-up (/signup) and login (/accounts/login) pages. The user authentication process is built on top of the Django authentication modules (django.contrib.auth), which are used with other modules to give users permissions based on their role. Other modules (django.contrib.sessions.middleware.SessionMiddleware, django.contrib.auth.middleware.AuthenticationMiddleware) are used to ensure users stay logged in during a continuous browsing session.

We developed the user authentication in Django by creating a one-to-one mapping between Django User objects and our data model's Profile objects. By doing so, the information of users is automatically obscured in the admin panel, so even as developers we cannot see the passwords or credentials of user accounts. The login page used the form of Django’s token authentication to provide the functionality. View classes can then provide a direct instance given a request from the database.

We also added separate logic to ensure the app's behavior was consistent according to the user's logged in status. This ensures users who are logged out cannot create groups or interact with parts of the website that only logged in users should be able to access. This is all dependent on the user authentication system.

### Team Choice

The team choice component of our final submission was to notify session owners by email when someone joins their group. This did not require any other url mapping or UI view but instead the use of Django’s emailing client and some backend code to send the email at the proper time with the proper text.

### Conclusion

Throughout working on this project, our entire team learned full stack web development using html, bootstrap, django, and other associated technologies. We, as a team, learned how to implement and manage user auth and interaction to allow controlled interaction of users and our application. In addition to that, we learned to develop software as a team using version control systems such as git. Some difficulties we encountered had to do with debugging with limited knowledge of Django and its objects. Some things we would have liked to know beforehand would be more about data model design as we ended up implementing ours incorrectly and later forced to change our data model. Something else would be knowing more about user authentication, specifically using django’s User model. One last thing we would have liked to know was django’s block structure for reuse instead of having to copy and paste.