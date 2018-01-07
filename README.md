# Luke McDuff Portfolio
_A collection of projects emphasizing engineering, data and technical research._
---

### Engineering

[ASESP16_CliniConnect_1-master](https://github.com/ljm7b2/Portfolio/tree/master/ASESP16_CliniConnect_1-master)
* This was my capstone engineering project for the course Advanced Engineering at UMKC. The concept inspiration came from my work at Cerner in building home health/community software as well as from my wife who was working as an RN in an inner city/low-income area clinic. A large problem for the population being served at my wife’s clinic was that the clinic was having trouble communicating with the patients via traditional methods like phone calls; and very few patients were actually able to access their info on the patient portal the clinic had setup for each patient. The goal was to find a way to make clinic-patient communication easier. In short: creating a system that was much more streamlined and simpler than a full-blown patient portal and less traditional than having to constantly field phone calls. The app seeks to improve communication by simply streamlining the essentials (as determined for low-income patients): Appointment reminders, GPS directions to the clinic, upload ability for daily vitals including BP and Blood Sugar, and lab orders sent directly to phone (emphasis Coumadin patients and those who have weekly lab draws). The app also provides a back-end administration application to faciliate the communication with patients. 
* The patient app is written in Java, the server application uses Java servlets as well as Mongo DB database to facilitate client-clinic COM, the administration application is written in Javascript, using Ionic framework
* This was a team based project. I was responsible for the project concept as well as the overall majority of engineering and architecture for the project
* The specific project ReadMe file should provide a substantial overview of the project. For a sample workflow, see the YouTube video linked at the bottom of the ReadMe file. Source code is provided and is broken into the three main components of the project.

### Data

[Mining Twitter data from the first 2016 presidential debate](https://github.com/ljm7b2/Portfolio/tree/master/Mining%20Twitter%20data%20from%20the%202016%20presidential%20debate)
* This was the final project for the course Principles of Big Data at UMKC. The requirements of the assignments stipulated that Twitter Data should be collected and mined for insight into whatever topic was chosen. Based on the timeframe (Fall 2016) at which the course was taken, one of the largest twitter events to take place that fall was the presidential debate between the two front runner candidates Hillary Clinton and Donald Trump. A wide filter was setup for grabbing Tweets based on candidate name keyword and popular debate hashtags being used at the time. The Tweets were filtered to a final set of 200,000 total. The following questions were then proposed: Which candidate is dominating the Twittersphere by having their name or hashtag mentioned the most number of times? Who is generating these Tweets: Is it a few individuals tweeting a lot or a lot of individual Tweeters? What is the overall sentiment score that can be assigned to Trump Tweets versus Hillary Tweets? Queries were then generated using Scala language and leveraging Scala's Dataframe and RDD data types as well Stanford's NLP library for sentiment analysis. The answer to queries were rather interesting and make more sense in hindsight (at the time many thought Donald Trump would lose the election) since Donald Trump was declared the winner. Donald Trump dominated the discussion on Twitter, garnering the most quotes and references from Tweets. To our surprise Trump and Clinton showed almost identical sentiment ratings either skewing towards neutral or negative. The results surprised all the members on the team, as we were convinced that Hillary would have performed better, however the analysis pointed towards a growing momentum behind Donald Trump, who would go on to win the November 2016 election.


