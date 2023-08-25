# GA Project 3: Summit
#### Full-stack Django Appication - Group Project

Summit is a web application designed to allow likeminded people to discuss topics in an open forum. With the ever increasing restrictions on platforms like Reddit and Tumblr, we aimed to create something where people knew their opinions are heard and valued.

**[Visit Summit here!](https://summitworking-337be49da67f.herokuapp.com/)**

## Contents
- [Features](#features)
- [Technical Aspects](#tech-aspects)
- [Relationship Diagrams](#diagrams)
- [Screenshots](#screenshots)
- [Technology](#tech-used)
- [Reviews](#review)

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
[Summit's Relational Diagram](https://lucid.app/lucidchart/8239c4a1-d71c-4a1d-8d63-a7bf82b44b2d/edit?viewport_loc=-239%2C-33%2C2113%2C972%2C0_0&invitationId=inv_a1e80f03-0140-49c3-bbea-017a450fe4b0)<br>
[Summit Layout Figma](https://www.figma.com/file/fPHAIua7h1JcssuY9xO8ii/Summit?type=design&node-id=0%3A1&mode=design&t=LF2e2iKVNughUG4C-1)

Interest and Group models have a 1:M relationship<br>
Group and Topic models have a 1:M relationship<br>
Topic and Post models have a 1:M relationship


<a name="screenshots"></a>
### Screenshots

![Log In Page](/readme_assets/images/Home.png) <br>
![Home Page](/readme_assets/images/about.png) <br>
![Interest Page](/readme_assets/images/interest.png) <br>
![Group View](/readme_assets/images/group.png) <br>
![Topic View](/readme_assets/images/topiclist.png) <br>
![Post View](/readme_assets/images/Topic.png)


<a name="tech-used"></a>
### Technologies Used
* HTML & EJS templates
* Tailwind CSS
* Python
* Django
* AWS
* Git
* Heroku

<a name="review"></a>
## Personal Reviews

### Bharat
I thoroughly enjoyed my involvement in this collaborative group project where a strong emphasis was placed on effective structuring and task delegation. This experience proved to be immensely valuable, as it not only allowed us to optimize our workflow but also fostered a heightened sense of accountability for individual contributions.

When I contemplate an idea or undertake a coding implementation on my own, there are certain perspectives and potential issues that might not come to light. However, collaborating within a group setting has enabled me to identify these challenges and utilize my time more effectively. Moreover, it has facilitated the enhancement of my initial concepts, particularly in refining specific aspects of the code.

I particularly relished the synergy that emerged while collaborating with my esteemed teammates, Nick and Toby, both of whom demonstrated exceptional prowess. Our collaborative dynamic enabled us to engage in meaningful discussions about code, seamlessly share innovative concepts, and ultimately transform these ideas into tangible outcomes. The process was truly exhilarating and left me with a profound sense of accomplishment.


----

### Nick
When it was announced that Project 3 was going to be completed in groups, I was initially nervous due to my previous experience with group assessments at university. However, this time around I can safely say that I enjoyed working within a team. 

The support you receive when working with other developers was invaluable. During my last project, I ran into blockers during the initial stages of the project which slowed me down. However, working together as a team we were able to overcome many individual blockers and make fast progress. We complemented each other's strengths and were not afraid to seek help and learn in areas we lacked confidence in.

Like most new developers, I get easily frustrated when I’m building a project only to be met by a continuous run of errors. In solo projects, I would spend too much time trying to solve one problem, wasting precious time and energy. In this project, my time was accountable to my team members. Procrastinating was out the question,  I either had to solve the bug  or lean on my team mates to move past the issue. As a team, we worked well together. No problem was too small, and we always helped each other. Often, the solution was staring us right in the face, but another set of eyes was needed to see it.

Overall, I was pleasantly surprised by the lack of conflict, both in our code and interpersonally, during this project. We had a goal and a straightforward path to achieving it. All we had to do was focus on the work.

-----


### Toby
Throughout this project, the support and encouragement from my group members has been incredible and I feel I have gained experience similar to that of a real world collaborative project. Compared to other solo projects, the ability to both lean on others for support and provide help to other group members was extremely beneficial.

As our group worked together well, we were able to implement changes and reach development goals either on time or ahead of time, whenever we set goals. This allowed our workflow to snowball during the week especially and we could proudly boast that our CRUD functions were all working by Tuesday. This was a huge change from solo projects where I often get wrapped up in solving smaller issues or trying to tackle problems all at once, and I was able to see how crucial things like mob coding and debugging for other people are.

All projects in the course so far have differed from my expectations of the concept, as some have been easier than I anticipated and some have been much harder. Even though I would say Summit is an ambitious app to have created in a week, being able to share the workload with others allowed us to be able to implement all extra features we planned for and all styling, which was an amazing feeling. Since there was so much trust within the group, we sometimes worked separately on different issues, moreso towards the end of the week, which sometimes caused git conflict issues. However these small issues here and there were the only setbacks we really had, so it was great to not have some huge blocker for multiple days of this project.

Despite a few minor communication hiccups, I was pleasantly surprised at the amount we were able to achieve with just 3 developers, and would gladly work in a team this size for another project.






