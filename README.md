# Summit

Summit is a web application designed to allow likeminded people to discuss topics in an open forum. With the ever increasing restrictions on platforms like Reddit and Tumblr, we aimed to create something where people knew their opinions are heard and valued.

**[Visit Summit here!](https://summitdb-84480e3e02b3.herokuapp.com/)**

# Contents
- [Features](#features)
- [Technical Aspects](#tech-aspects)
- [Relationship Diagrams](#diagrams)
- [Screenshots](#screenshots)
- [Technology](#tech-used)

<a name="features"></a>
### Features
* Log in or create an account
* Create an interest page, or a group of people within that interest
* Submit a topic that people can respond to - start a conversation
* Post images, text or both in response to somebody's inquiry
* Edit and delete interests, groups, topics and posts at any time
* Clean, simple and user-friendly design makes Summit easy to use


<a name="tech-aspects"></a>
### Technical Aspects
* Built with Python, CSS and HTML using the Django framework
* Connects to Amazon Web Services in order to store images posted
* Code uses efficient MVC design philosophy
* Demonstrates user CRUD operations using RESTful routing
* Utilises authentication to lock logged-out users from functions
* Both Tailwind/DaisyUI and self-written CSS for UI
* Pushed to GitHub
* Deployed via Heroku


<a name="diagrams"></a>
### Relationship Diagram
![Summit's Relational Diagram](https://lucid.app/lucidchart/8239c4a1-d71c-4a1d-8d63-a7bf82b44b2d/edit?viewport_loc=-239%2C-33%2C2113%2C972%2C0_0&invitationId=inv_a1e80f03-0140-49c3-bbea-017a450fe4b0)<br>
![Summit Layout Figma](https://www.figma.com/file/fPHAIua7h1JcssuY9xO8ii/Summit?type=design&node-id=0%3A1&mode=design&t=LF2e2iKVNughUG4C-1)

Interest and Group models have a 1:M relationship<br>
Group and Topic models have a 1:M relationship<br>
Topic and Post models have a 1:M relationship


<a name="screenshots"></a>
# Screenshots
![Home Page]() <br>
![Log In Page]() <br>
![Interest Page]() <br>
![Group View]() <br>
![Topic View]()


<a name="tech-used"></a>
# Technologies Used
* HTML & EJS templates
* Tailwind CSS
* Python
* Django
* AWS
* Git
* Heroku

