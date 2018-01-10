_A collection of projects emphasizing engineering, data and technical research_
---

### Engineering

[CliniConnect - streamlined clinic/patient communication](https://github.com/ljm7b2/Portfolio/tree/master/ASESP16_CliniConnect_1-master)
* This was my capstone engineering project for the course Advanced Engineering at UMKC. 
* The inspiration behind CliniConnect came from my work experience building home health/hospice software as well as from my wife who was working as an RN in an inner city/low-income area clinic. The clinic was spending a considerable amount of effort attempting to effectively communicate with patients via traditional methods like phone calls; and very few patients were able to access their info on the patient portal the clinic had setup. The goal was to find a way to make clinic-patient communication easier. In short: creating a system that was much more streamlined and simpler than a full-blown patient portal and less traditional than having to constantly field phone calls. The app seeks to improve communication by simply streamlining the essentials (as determined for the current patient demographic): Appointment reminders, GPS directions to the clinic, upload ability for daily vitals including BP and Blood Sugar, and lab orders sent directly to phone (emphasis Coumadin patients and those who have weekly lab draws). The app also provides a back-end administration application to facilitate the communication with patients. 
* The patient app is written in Java, the server application uses Java servlets as well as Mongo DB database to facilitate client-clinic COM, the administration application is written in Javascript, using Ionic framework
* This was a team based project. I was responsible for the project concept as well as most of engineering and architecture for the project
* The specific project ReadMe file should provide a substantial overview of the project. For a sample workflow, see the YouTube video linked at the bottom of the ReadMe file. Source code is provided and is broken into the three main components of the project.

### Data

[Mining Twitter data from the first 2016 presidential debate](https://github.com/ljm7b2/Portfolio/tree/master/Mining%20Twitter%20data%20from%20the%202016%20presidential%20debate)
* This was the final project for the course Principles of Big Data at UMKC. 
* The fall of 2016 was an exciting time in the world of American politics. It was also the time of one of the largest twitter events to take place - the presidential debate between the two front runner candidates Hillary Clinton and Donald Trump. The televised debate provided a good enough excuse to watch tv and capture Tweets too. A wide filter was setup for grabbing Tweets based on candidate name, keyword and popularly used debate hashtags being used at the time. The Tweets were filtered to a final set of 200,000 total. The following questions were then proposed: Which candidate is dominating the Twittersphere by having their name or hashtag mentioned the most number of times? What is the overall sentiment score that can be assigned to Trump Tweets versus Hillary Tweets? Who is generating these Tweets: Is it a few individuals tweeting a lot or a lot of individual Tweeters? Queries were then generated using Scala language and leveraging Scala's Dataframe and RDD data types as well Stanford's NLP library for sentiment analysis. The answer to queries were puzzling at the time and make more sense in hindsight (this could be because at the time of the first debate many thought Donald Trump would lose the election). The results showed Donald Trump dominated the discussion on Twitter, garnering the most quotes and references from Tweets. To our surprise Trump and Clinton showed almost identical sentiment ratings either skewing towards neutral or negative. The results surprised all the members on the team, as we were convinced that Hillary would have performed better (she was declared 'winner' of the debate), however the analysis pointed towards a growing momentum behind Donald Trump, who would go on to win the November 2016 election.
* Some [data visualizations](https://github.com/ljm7b2/Portfolio/blob/master/Mining%20Twitter%20data%20from%20the%202016%20presidential%20debate/Report%20Part%202.pdf) are available. They were created using the Graph library Chart.js. It should be noted that the emphasis of the project was on collecting and querying this large dataset using Scala. If the project were to be re-done the data representation could be much more effective if created using a more robust toolset as well as focusing more effort on design and effectiveness of the visualizations.
* For a thorough overview of the project see [overview document](https://github.com/ljm7b2/Portfolio/blob/master/Mining%20Twitter%20data%20from%20the%202016%20presidential%20debate/Report%20Part%201.pdf). For a view of the graphic visualizations see the [graph visualizations document](https://github.com/ljm7b2/Portfolio/blob/master/Mining%20Twitter%20data%20from%20the%202016%20presidential%20debate/Report%20Part%202.pdf).
* Main contributions were collecting data, engineering queries, generating visualizations and writing summary

[Commerce Bank Data Dashboard](https://github.com/ljm7b2/Portfolio/tree/master/Commerce%20Bank%20Data%20Dashboard)
* Taking a different approach to data processing, the Commerce Bank Data Dashboard allow users to consume data to aid in tracking various metrics via customizable data widgets. In partnership with Commerce Bank, multiple teams competed to prototype a dashboard for Commerce Bank, culminating in a presentation at the company HQ. The project delivered a customizable dashboard where data points could be visualized in a small handful of different visualizations which the user could overlay to compare with different a 'branches' data. Our team delivered one of the more complete porotypes and won the competition. The project was built using ASP.NET framework with SQL Server backend.  
* For a thorough overview of the project see section 4 - 'Main scenarios of use' in the [Productivity Analysis System User Guide](https://github.com/ljm7b2/Portfolio/blob/master/Commerce%20Bank%20Data%20Dashboard/Productivity%20Analysis%20System%20User%20Guide.pdf) created for the project submission. 
* Main contributions were design and engineering of the dashboard, documentation and final presentation. 
*  Produced as part of my senior Software Engineering Capstone project at UMKC
### Technical Research

[Calculating Reliability of Complex Systems](https://github.com/ljm7b2/Portfolio/tree/master/Calculating%20Reliability%20of%20Complex%20Systems)
* System reliability/reliability engineering is a complex and diverse area of research. To gain a deeper understanding of the complexities, a prototype was developed that can model the overall expected reliability of a system of connected nodes where the reliability of each node is known. Calculating the reliability of a complex systems is computationally 'hard' and an inefficient task at best case. Multiple algorithms exist within the space already, and the project seeks to build from the well-known Event-Space algorithm, which takes a naive approach. If the project were to be taken past proof of concept stage, then a more substantial algorithm should be selected based on desired requirements. The project was built using Python 2.7.  
* For an in depth discussion and code samples see the [Calculating Reliability Report](https://github.com/ljm7b2/Portfolio/blob/master/Calculating%20Reliability%20of%20Complex%20Systems/Calculating%20Reliability%20of%20Complex%20Systems.pdf)
* Main contributions were lead author and engineering and implementation of algorithm
* Produced as part of Applied Probability course final project at UMKC

#### Extras
* If you have reached this point and are wondering what other completely random projects I have been involved with... then I don't want to disappoint you, so the links are below, otherwise...avert your eyes.
* [EvidenceGen](https://github.com/ljm7b2/EvidenceGen) I built this tool to use in my daily work when capturing test evidence. It can grab screen shots and auto generate documents. A friendly helper for those who follow medium risk processes. 
* [Hurricane Rider: T.V. Powderly's Antistrike Position in the Knights of
Labor Movement](https://drive.google.com/open?id=1wL4bWhYrY7mHewA04KlpzoI3L4mxfgV4) An historical research paper written for Senior Capstone. It may or may not surprise you to know I have a degree in history and a minor in music.
* [Radio Moscow - 2007](https://www.allmusic.com/album/radio-moscow-mw0000738205) Can't really explain this one...


luke.mcduff@cerner.com
https://www.linkedin.com/in/luke-mcduff-7a9140152
