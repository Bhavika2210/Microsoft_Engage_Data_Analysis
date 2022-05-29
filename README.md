# Microsoft_Engage_Data_Analysis


* [Why I chose Challenge-2 Data Analysis 📊](why-i-chose-challenge-2-data-analysis-📊)
* [Introduction 🌱](introduction-🌱)
* [Insights obtained from surveys 📰](insights-obtained-from-surveys-📰)
* [Approach 🎯](approach-🎯)
* [Tech stacks & API's used ⚙](tech-stacks-&-api's-used-⚙)
* [Data Driven site demo 🚗](data-driven-site-demo-🚗)
<!-- * [Demo video of website 📽](demo-video-of-website-📽)
* [Challenges Faced 💪](challenges-faced-💪)
* [Future Scope 💹](future-scope-💹)
* [References 📚](references-📚)  -->

## Why I chose Challenge-2 Data Analysis 📊
There are two reasons for choosing it:
* It seemed challenging yet an interesting topic.
* I could iterate on some real life use cases for this challenge along with the identification of problems in automotive industry.

## Introduction 🌱
Not knowing the best time to buy a car, its transmission: automatic or manual, etc. is a problem for the consumers.

There are two universal facts about buying a car that everyone needs to remember. 
First, cars are known to be depreciating assets and second, they are bound to be upgraded in a few years. Taking these two factors into consideration, choosing a brand that is known to have a good resale value is the smart way to go forward.

Indian automotive industry is expected to reach 16 trillion dollars by the year 2026 and currently contributes 6.4% to the gdp.
This clearly indicates the need for a data driven approach.

## Insights obtained from surveys 📰

- From October 2019, all cars are mandatorily required to have

   - Dual airbags

   - ABS (anti-lock braking system)

   - Reverse parking sensors, as part of standard equipment. 
- Emission Norm: only BS6 is allowed in the upcoming cars
- Additional safety features like Electronic Stability Control (helps apply brakes on individual wheels and maintain better control), Autonomous Emergency Braking and Steering are some of the preferred features.

## Approach 🎯
### I have taken inspiration from the SCRUM technique of Agile methodology, wherein I shall be dividing my project development in sprints. I’ll do my best to stick around the deadlines that I have set for each sprint.
* Sprint 1 (May 13): Research and Design: I am learning about the jargon words revolving around cars like ARAI mileage certification, cc, etc. in order to be more comfortable in analyzing the data. I am collecting resources for web development as I shall be new to that as well. Also, I am thinking of the additional functional features that I can have on my site.
* Sprint 2 (May 21): Software development and debugging - Start the development process by taking help from YouTube tutorials.  Build a decent web application . Adjust the UI.
* Sprint 3 (May 25): Debug and add additional features.
* Sprint 4 (May 27): Prepare the video required for submission. 

## Tech stacks & API's used ⚙
* Python
* HTML
* CSS
* Flask
* Heroku
* Landbot
* Git
* Google Translate API
* Power BI
* Bootstrap

## Data Driven site demo 🚗
 [DataDriven Website Link](https://engage-datadriven.herokuapp.com/)
 
![image](https://user-images.githubusercontent.com/81467761/170885151-99dd5637-0031-489a-b4bf-6e240430c94a.png)

![demo-1](https://user-images.githubusercontent.com/81467761/170885196-f810b1ea-60da-44cd-81b4-808845b5bc0b.png)

![11 ](https://user-images.githubusercontent.com/81467761/170891334-62dab346-9371-4622-a4c2-3f9ac5b4711a.png)

![12 ](https://user-images.githubusercontent.com/81467761/170891335-6e5920d2-c700-4f89-b2a6-6eea99f17781.png)

![13](https://user-images.githubusercontent.com/81467761/170891338-6c939c48-c09a-47d7-8ca6-cf7fbf435f33.png)

![14](https://user-images.githubusercontent.com/81467761/170891341-bf46f226-35a1-4faa-8266-a8ae0edd88e5.png)


## Use of Min Max Scaler ⚖
Since the values of independent variables were very diverse and had a high standard deviation, MinMax Scaler converts all the values into numbers between 0 and 1. 
This process is called Normalisation.

## Why Random Forest Regressor 🌲

![image](https://user-images.githubusercontent.com/81467761/170891523-e48104d9-e835-4ddf-9278-94523f5713bd.png)

It combines multiple decision trees in determining the final output rather than relying on individual decision trees. 

It reduces overfitting in decision trees and helps to improve the accuracy

Random Forest regression performs better when the number of noise variables is more than the number of explanatory variables.
While Linear regression works better if the noise variables are lesser.

Random Forest Regression was chosen after getting the following results:

- Using Random Forest Regressor: 92.44%
- Using Cross Validation: 15 %
- Using RandomizedSearchCV: Very Low

## Challenges Faced 💪🏻
- Cleaning of the dataset
- Improving the accuracy
- Web Integration

## Future Scope 💹
Improve the accuracy using deep learing models

## Demo video of website 📽
[Demo Link](https://drive.google.com/file/d/1yMCUg_tKdn5dOqHGC4PK_dDEd1LmpR-p/view?usp=sharing)

## References 📚
- https://www.geeksforgeeks.org/random-forest-regression-in-python/
- https://www.youtube.com/results?search_query=codebasics
- https://www.youtube.com/results?search_query=krish+naik
