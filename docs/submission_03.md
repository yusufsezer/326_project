### Overview
PlayWithMe is an online web platform that allows its users to find or create groups for gaming. Our users will be able to log in to our website and create gaming sessions that allows users to join and communicate with the rest of the group. In addition to creating a group, a user will also be able to login and search for a group to join. PlayWithMe brings all kinds of gamers together allowing collaboration between people across the globe. We did not stray much from our original proposal and have implemented the features we intended to.

### Team Members

* Yusuf Sezer
* Rudy Pikulik
* Christopher Rybicki
* Navin Lal
* Panav Setia
* Nithin Mahesh

### Video
[Click here!](https://www.youtube.com/watch?v=BP-et0EmPnU)

### Design Overview
Our homepage includes multiple tabs in which users can join a local party, join an online party, create groups, see their own groups, and find other groups. Users will be directed to the sign up page if they are not logged in.

The functionality of the login includes authentication, authorization, and session support. We implemented this with user authentication in Django by creating a one-to-one mapping between Django User objects and our data model's Profile objects. The login page used the form of Django’s token authentication to provide the functionality. View classes can then provide a direct instance given a request from the database.

### Problems
One of the main issues we ran into was unauthenticated users being able to interact with forms. Users could interact with forms (and thus the data model) without even being logged in, which sometimes caused errors in the backend and crashed the site. This occurred because users could see/interact with forms regardless of authentication. We fixed this problem by rendering certain parts of the page's HTML only if the active user is authenticated. Furthermore, we implemented logic that redirected unauthenticated users to the sign up page if they attempted to interact with elements of the site that require authentication.

### Successes
* Implemented user authentication
* Made all forms on the site functional, allowing users to modify the underlying data models
* Added a moderator user group so that certain users can have the ability to delete messages in any session, regardless of whether or not they are a member (to fight against inappropriate chat messages) (permissions/authorization).
* Modified the site to not render certain HTML elements based on whether or not a user is authenticated and based on the group they belong to (permissions/authorization)
* Modified certain pages to display information based on the current user. For example, "My Groups" page shows the groups that the current user belongs to.
* We were able to collaborate efficiently to finish up the remaining pieces of the website, write our script, and record on time. No issues with scheduling times to meet as a group.
* Only minor changes/polishes remain for final submission

### Team Choice
TO-DO
