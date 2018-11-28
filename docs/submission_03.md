Overview:
PlayWithMe is an online web platform that allows its users to find or create groups for gaming. Our users will be able to log in to our website and create gaming sessions that allows users to join and communicate with the rest of the group. In addition to creating a group, a user will also be able to login and search for a group to join. PlayWithMe brings all kinds of gamers together allowing collaboration between people across the globe. We did not stray much from our original proposal and have implemented the features we intended to.

Members List:
Yusuf Sezer
Rudy Pikulik
Christopher Rybiki
Navin Lal
Panav Setia
Nithin Mahesh

Video Link:

https://www.youtube.com/watch?v=BP-et0EmPnU

Design Overview:
Our homepage includes multiple tabs in which users can join a local party, join an online party, create groups, see their own groups, and find other groups. Users will be directed to the sign up page if they are not logged in. 

The functionality of the login includes authentication, authorization, and session support. We implemented this with user authentication in Django through means of one-to-one mapping. The login page used the form of Django’s token authentication to provide the functionality. View classes can then provide a direct instance given a request from the database. 

Problems:
One of the main issues we ran into was users being able to interact with forms. Users could create forms and sessions without even being logged that would cause the website to crash. 
Initially we didn’t check if users were logging in, which threw an error since we assumed there was already a user. 

Successes:
We were able to collaborate efficiently to finish up the remaining pieces of the website, write our script, and record on time. No issues with scheduling times to meet as a group. 
Updated user interface and implemented more features on time. Leaving more time for debugging any on going problems well before deadline.

Team Choice:
#TODO