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

TODO

# Design Overview

A visual diagram of our data model can be viewed [here](https://www.lucidchart.com/invitations/accept/5ef16b3e-0a54-475d-b911-4d69bd5f28bf).

Our data model as it stands has six major components: games, game platforms, sessions, users, and messages.

Games are simple items that contain basic information like a name, the platforms it can be played on, as well as a description. Platforms (like Playstation, PC, etc.) can each be associated with one or more games.

Users can sign up for an account on our website, which can then be used to host and find groups and message other people. Each user (with a username and password) is associated with 0 or more sessions that they are a member of, and zero or more sessions that they are the owner of. Users can also add information about which games they play and what game platforms they use.

Sessions are each assigned a unique ID, and are associated with 1 or more users, of which one of is the owner. A session also has one or more games and one or more platforms associated with it. Lastly, each session is associated with messages sent between members, and a sessioncan have a location associated with, as well as a boolean indicating if the members are playing online or offline games.

Finally, messages are simple data items that are associated with a sender (user), one or more receivers (users), and the time the message was sent.

# Problems and Successes

TODO
