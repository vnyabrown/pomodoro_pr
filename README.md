# Pomodoro-Project
Personal Dev Project Winter 2024

This project…Is to create a pomodoro app with the main functionalities: a functional pomodoro timer allowing for 25 minute sessions, 5 minute short breaks, and 10-30 minute long breaks; assigning tasks for each set of sessions, the user can decide how many sessions they want/need for that task and adjust the needed number of sessions it as they please, the user can save a template with a session they previously created, the user can view analytics about their time using the app (how much time focused in a day? Week? month?) and the user can schedule regular sessions for upcoming days up to a month.

### App Functionalities
The system should carry out these tasks: <br/>
Database of Sessions<br/>
Database of Users<br/>
Database of Session Templates<br/>
Built-in Pomodoro Timer<br/>

### User Functionalities
The system should allow the user to carry out these tasks:<br/>
Create a new session<br/>
Delete an existing session<br/>
Create a session template (from an existing session)<br/>
Mark a session completed<br/>
Create session from a session template<br/>
View weekly analytics (How much time spent focusing in a week, what sessions were completed each day) <br/>
View monthly analytics (How much time spent focusing in a month, what sessions were completed in each week) <br/>

### Data Model
**User**<br/>
ID (Integer) (Auto generated)<br/>
Username (Text) <br/>
Password (Text) <br/>
Name (Text) <br/>
Session History (Time per day, time per week, time per month) <br/>

**Pomodoro Session**
ID (Integer) (Auto generated)<br/>
User (Foreign Key: User ID) <br/>
Task Title (Text) <br/>
Task Description (Text)<br/>
Task Time (Number of Pomodoros) (Integer)<br/>
Task Completion Time (Number of Pomodoros)<br/>
Task Total Time Elapsed (Real)<br/>
Status (Uncomplete/Complete - Default: Complete)<br/>

**Pomodoro Session Template**
ID (Integer) (Auto generated)<br/>
User (Foreign Key: User ID)<br/>
Task Title (Text)<br/>
Task Description (Text)<br/>
Task Time (Number of Pomodoros) (Integer) <br/>

### Tools / Stack
**Framework:** Flask<br/>
**Database:** SQlite<br/>
**Frontend/Serverside:** HTML/CSS, Javascript<br/>
**Backend:** Python<br/>
