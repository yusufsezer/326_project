# PlayWithMe

### Developed by Team RudyOnRails

# Overview

PlayWithMe provides a platform for gamers to find and game with each other, locally and online. The platform will allow users to create and post “sessions” for other users to find and join. Each session will have various attributes associated with it, such as number of participants, game(s), platform, local vs. online etc. When a user wants to game with others, they can simply use the application’s search function to find sessions that best match their ideal gaming experience.
For example, a user may post a local session for others who want to play Halo. Other users can search for this session via filtering criteria in the search function (such as geographic distance) or by entering the session’s unique ID. Once a user finds the session, they can communicate with the session host via the built in chat function. If the user wants to participate in the session, they can request to join the session. Upon approval, the session will reflect that the user is now part of the session.
Although our idea revolves around gaming--similar to platforms like Twitch--it does not revolve around streaming. Rather, our application is focused on providing a way for gamers to find a group to play with, both locally and online.

# Team Members

* Yusuf Sezer, YusufSezer
* Nithin Mahesh, NithinMahesh1
* Navin Lal, nlal43
* Rudy Pikulik, RudyPikulik
* Christopher Rybicki, Chriscbr
* Panav Setia, PanavSetia

# Video

https://www.youtube.com/watch?v=EjqJ5SRd8bA

# Design Overview

A visual diagram of our data model can be viewed [here](https://www.lucidchart.com/invitations/accept/5ef16b3e-0a54-475d-b911-4d69bd5f28bf).

Our data model as it stands has six major components: games, game platforms, sessions, users, and messages.

Games are simple items that contain basic information like a name, the platforms it can be played on, as well as a description. Platforms (like Playstation, PC, etc.) can each be associated with one or more games.

Users can sign up for an account on our website, which can then be used to host and find groups and message other people. Each user (with a username and password) is associated with 0 or more sessions that they are a member of, and zero or more sessions that they are the owner of. Users can also add information about which games they play and what game platforms they use.

Sessions are each assigned a unique ID, and are associated with 1 or more users, of which one of is the owner. A session also has one or more games and one or more platforms associated with it. Lastly, each session is associated with messages sent between members, and a sessioncan have a location associated with, as well as a boolean indicating if the members are playing online or offline games.

Finally, messages are simple data items that are associated with a sender (user), one or more receivers (users), and the time the message was sent.

# Problems and Successes

One problem that we ran into was that we first implemented our data model incorrectly. While fixing this, we also discovered that our data model was not totally correct itself. We had to deviate from our original data model design because it did not behave as we would have liked it to.

Another struggle we faced was passing information between views. For example, on the “My Sessions” page, we allow the user to view all of the Sessions that they belong to. The user is then able to click the “view” button next to a Session in order to view its details. In the backend, we had trouble passing the id of the Session that the user is trying to view. Once we figured out how to pass the Session id to the next view, we are able to render the details of the correct Session on the page.

Other hiccups occurred with displaying the raw pages correctly. Some stylesheets and images were not displaying correctly due to the fact that we were not using Django's built-in static URL library.

We ran into an issue with obtaining certain data in init.py. For example, when trying to find a user who belonged to a given session, we originally were not able to iterate through the list sessions that belonged to each user. In other words, we were having problems programmatically querying data that we had already produced.

One major success was our use of Faker to correctly generate random data for our application. We were able to apply it to all areas, including generating usernames, messages, sessions, and even latitudes and longitudes. Once we had this data, we managed to display them all in the admin site correctly which involved correctly grouping games and platforms, along with messages, users, and sessions.

We were also able to get the faker data from our database to render on our html pages including sessions, users, platforms, games, and locations in dropdown menus, and messages in a chat box.

