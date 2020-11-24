# ACT & SAT Analysis on Participation rates and scores across states for the year 2017-2018

---
### Problem statement

Where is money best spent on to increase participation rate?

---
### Executive Summary
The new format for the SAT was released in March 2016. As an employee of the College Board - the organization that administers the SAT - I am part of a team that tracks statewide participation and recommends where money is best spent to improve SAT participation rates. 

Based on our analysis below, I will seek to identify trends in the data and combine data analysis with outside research to identify likely factors influencing participation rates and scores in various states.

While it has been observed that the ACT had continued to enjoy popularity in the recent years, we had observed an increased participation rate in the 2018 SATs.

---
### Methodology

The College Board needed to find out how to increase SAT participation rates.

Data was obtained from the following credible sources:<br>
[2017 SAT Scores](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/) <br>
[2017 ACT Scores](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows)<br>
[2018 SAT Scores](https://reports.collegeboard.org/sat-suite-program-results/state-results)<br>
[2018 ACT Scores](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows)<br>

Importing was performed for ACT & SAT 2017 - 2018 data for analysis, and data cleaning to check for any discrepancies between source data and data imported, as well as the accuracy of datatypes. This minimises human error in the process.

An exploratory data analysis was conducted to determine statistical parameters, data distribution etc. Data visualisation was also performed by plotting charts for a better visual understanding to identify relationships between each data series.

Inferential statistical analyses were then made based on the above to describe any trends in the data.

Other research was done on SAT and documented when relevant.

Based on all of the above, a recommendation was made and concluded on the overall findings on the problem statement.

---
### Data Dictionary

|Feature|Type|Dataset|Description|
|:---|:---|:---|:---|
|**state**|*object*|ACT/SAT|State name| 
|**act17_part**|*integer*|ACT|2017 ACT Participation rate of each State (Values: 0-100)| 
|**act17_eng**|*float*|ACT|Average 2017 ACT English score of each State (Values: 0-36)| 
|**act17_math**|*float*|ACT|Average 2017 ACT Math score of each State (Values: 0-36)| 
|**act17_reading**|*float*|ACT|Average 2017 ACT Reading score of each State (Values: 0-36)| 
|**act17_sci**|*float*|ACT|Average 2017 ACT Science score of each State (Values: 0-36)| 
|**act17_composite**|*float*|ACT|Average 2017 ACT Composite score of each State (Values: 0-36)| 
|**sat17_part**|*integer*|SAT|2017 SAT Participation rate of each State (Values: 0-100)|  
|**sat17_erw**|*float*|SAT|Average 2017 SAT Evidence-Based Reading and Writing score of each State (Values: 200-800)| 
|**sat17_math**|*float*|SAT|Average 2017 SAT Math score of each State (Values: 200-800)| 
|**sat17_total**|*float*|SAT|Average 2017 SAT Total score of each State (Values: 400-1600)| 
|**act18_part**|*integer*|ACT|2018 ACT Participation rate of each State (Values: 0-100)| 
|**act18_eng**|*float*|ACT|Average 2018 ACT English score of each State (Values: 0-36)| 
|**act18_math**|*float*|ACT|Average 2018 ACT Math score of each State (Values: 0-36)| 
|**act18_reading**|*float*|ACT|Average 2018 ACT Reading score of each State (Values: 0-36)| 
|**act18_sci**|*float*|ACT|Average 2018 ACT Science score of each State (Values: 0-36)| 
|**act18_composite**|*float*|ACT|Average 2018 ACT Composite score of each State (Values: 0-36)| 
|**sat18_part**|*integer*|SAT|2018 SAT Participation rate of each State (Values: 0-100)| 
|**sat18_erw**|*float*|SAT|Average 2018 SAT Evidence-Based Reading and Writing score of each State (Values: 200-800)| 
|**sat18_math**|*float*|SAT|Average 2018 SAT Math score of each State (Values: 200-800)| 
|**sat18_total**|*float*|SAT|Average 2018 SAT Total score of each State (Values: 400-1600)| 
|**act_chng**|*integer*|ACT|Year on year change in ACT participation rate from 2017-2018 of each State (Values: -100-100)|
|**sat_chng**|*integer*|SAT|Year on year change in SAT participation rate from 2017-2018 of each State (Values: -100-100)|

---

### External Research

Winning competitive bids after state contracts with ACT has ended had attributed to an overall increase in SAT participation rates from 2017 to 2018. Based on the data we gathered, two states ([Colorado](https://www.coloradokids.org/colorado-switches-from-act-to-sat-for-high-school-college-entrance-assessments/) and [Illinois](http://blogs.edweek.org/edweek/high_school_and_beyond/2016/02/illinois_finalizes_decision_to_switch_from_act_to_sat.html)) has shown an increase in more than 70% from 2017 to 2018. This was in fact a huge shift since both states had made ACT complusory since more than a deacade ago, until a new bid was awarded to SAT.

Such efforts had indeed increased participation rates, but the inverse relationship between the average test scores and participation rate become a deterring factor for other to follow suit. 

This is apparent since there is a wider range of scores from a statewide student population rather than students who opt to take the test on their own accord; they would have likely been more prepared to take the test, rather than students who participate in the test because it is mandatory. This is evident by observing the correlation between test scores and participation rates.<br>
- [North Carolina](https://www.newsobserver.com/news/local/article220102340.html)<br>
- [South Carolina](https://www.thestate.com/news/politics-government/article236809728.html)<br>


---
### Conclusion & Recommendation

Recommendations on increasing rates:

Currently, only 25 states requires students to take either ACT or SAT.

Through contracts with state and schools, the College Board would be able to increase the SAT participation rate statewide by making it manadatory.

In our research, it became evident that state policies heavily influence the participation rates in the tests in the case of Colorado and Illinois. The SAT participation rate sore close to a 100% after a selection committee chose SAT over ACT in a competitive bidding exercise held by each state education board. These were states that once had approximately 100% participation rate in ACT, while a mere 9~11% participation rate in the 2017 SAT before the new state policy was introduced.

Other recommendations to increase participation rates across the states could include fee waivers, providing coursework materials, and campaigning to the students.

Deciding where to focus efforts on:

The cases of Colorado and Illinois had shown that the College Board made it possible by winning state contracts to secure a high SAT participation rate. Hence, there is no one state that we can recommend to focus resources on.

However, they could shortlist states that have made ACT a mandatory test (in which their state contracts are soon to expire), or states that do not show a dominant test preference among the test-takers in the region.

It could mean that once the College Board wins over these state contracts, the participation rates automatically rises in their favor, or they could focus campaigning efforts in states that do not show a dominant test preference in order to win a larger market share in the area.

However, it could become more apparent if there is more data collected on possible factors influencing the participation rates such as: test-takers' household income and participation rates on district and school level.


