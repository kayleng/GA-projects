# Reddit API and Classification

## Executive Summary
Reddit is a website comprising user-generated content—including photos, videos, links, and text-based posts—and discussions of this content in what is essentially a bulletin board system. As of 2018, there are approximately 330 million Reddit users, called "redditors". The site's content is divided into categories or communities known on-site as "subreddits", of which there are more than 138,000 active communities.

These subreddits are governed by moderators who set and enforce community-specific rules, remove posts and comments that violate these rules, and generally work to keep discussions in their subreddit on topic.

### Problem Statement
As the popularity of Reddit increases, the Apple subreddit had garned approx. 1.8 million members in the community. This number also represents an increased number of people who utilise reddit for advertisements unrelated to the community, or "competitor supporters" posting unrelated content onto the subreddit; especially in the season where competitors are promoting their new product launch, there is an increase in competitor related posts on the Apple community. Despite the strict rules prohibiting such activities, the moderators spend considerable time and efforts on filtering out and removing unrelated content. 

Community members also developed a sense of unhappiness as they are unable to enjoy content without disruption by at least 1 or 2 unrelated posts such as advertisements or unrelated topics which have not been promptly removed by the moderators.

As a newly promoted moderator in the subreddit: "r/Apple - the unofficial Apple community", I was tasked by the existing moderators to create a classifier model that can accurately identify if a post belongs to the Apple subreddit, or unrelated to the community as a whole. 

Since a high proportion of unrelated content belonging to the "competitor subreddit": Android have been identified by existing moderators, I have decided to create a binary classification model based on title of posts of the apple and Android subreddits.

With the development of an appropriate classifier model, any highly unusual posts will be automatically flagged out for the moderators' review. Ultimately, the goal is to decrease the amount of time moderators have to spend in order to screen through irrelevant posts, and avoid having a "spam" of unrelated topics.

### Methodology
I will be using Reddit's JSON API to collect posts (i.e. threads) from the two subreddits:
- [r/Android](https://www.reddit.com/r/Android/.json)
- [r/apple](https://www.reddit.com/r/apple/.json)

By sending "get requests" in succession, I was able to collect subreddit posts stored into a dataframe and from there, single out columns that contain significant data, and remove any duplicate data. We proceed to clean the text data to remove non-letters (i.e. punctuations, digits, symbols), stopwords, and convert text to lower cases. The cleaned 'title' data will consist of a string of text. 
Since it is a binary model, the subreddits will be replaced with binary values such that apple is 1 since it is the best value in our classification model: 
- 0: Android
- 1: apple

#### Data Dictionary
|Feature|Type|Dataset|Description|
|:---|:---|:---|:---|
|**subreddit**|*integer*|df| 0: Android subreddit, 1: apple subreddit| 
|**title**|*object*|df|contains cleaned text data extracted from the corresponding subreddits| 

In the preprocessing stage, I will take the clean data and segregate them into train and test data. I will be using train_test_split to segregate them and our test data size is set at 20%.

The train data will further undergo a round of train_test_split to create our validation set (X_train, X_test, y_train, y_test) which will aid us in testing various models to find the model that best generalizes.

The test data will remain to be our "unseen data", which will test the sucess of our final model selected.

These data will then undergo feature extraction (or vectorization) such as CountVectorizer and and Tf-idf Vectorizer, as the words need to be encoded as integers or floating point values for use as input to machine learning algorithms.

Finally, using learning algorithms such as the Naive Bayes Model and Logistic Regression, I selected a baseline model : Logistic Regression model based on performance metrics such as Accuracy and AUC scores, and further tune its hyperparamters in order to optimize it to be our production model.

With that, we tested the production model with our unseen data, and concluded the following:
  - Our model correctly predicts 92% of observations based on accuracy score.
  - Among posts that our model predicted to be in r/apple, we have 92% of them correctly classified.
  - Among posts that are in r/apple, our model has 94% of them correctly classified.
  - Among posts that are in r/Android, our model has 90% of them correctly classified.



### Conclusion

With an overall success rate of more than 90% in correctly classifying if a post belongs the apple subreddit, moderators can now utilise the model as a feature to detect if the post is correctly classified/ relevant to the Apple community.

The model can be an embedded tool into the subreddit post submission page, whereby a pop-up dialog is raised when the model detects any unusual words written in the post that is indicative of irrelevance to the apple subreddit. The dialog temporarily halts program execution and prompts the user to confirm if the user is posting in the correct subreddit, which acts as a barrier for any irrelevant "spams" to the page, and reduces the number of posts with unrelated content.

It can also act as an automation tool when the model is employed to "flag out" posts that contain highly unusual words, and halts publishing of post before moderator approval.
With the model in place, the moderator would have an easier job of "cleaning" irrelevant posts as they would most likely have been identified by the model, instead of having to spend time and resources to scan through all the posts in the subreddit which are increasing by the minute. This also reduces the chance of misclassification as moderators are humans who might mistakenly miss out screening a post once in a while.

With the restriction in place, the apple community redditors can truely enjoy new content, without having to go through irrelevant content that might have been the cause of advertising or even harassments from "competitor communities" redditors.

### Recommendations to improve the model

#### 1. Explore other features
In addition to the analyses done in the previous notebooks, we can explore other text features such as post text data and comments text data which might provide us with more features for modelling.

#### 2. Sentiment/Intent analysis
In analysing the underlying sentiment of the text data, as well as analyzing the user’s intention behind the text data, the model could be able to identify if it relates an opinion, news, marketing, complaint, suggestion, appreciation or query.

This could result in a better model built that could even extend the restriction to other posts which are against the rules of the community.

#### 3. Other Classifier Models
In our analyses, we only employed the use of Naive Bayes and Logistic Regression models to create our production model. We can include other learning algorithmns such as the k Nearest Neighbors, Decision Tree Classifier and the Random Forest Classifier to determine the best model that can be optimised to be our production model.

#### 4. Retrain model periodically
Due to the nature of the fast-changing trends in technology, we recommend that the data be pulled to retrain the model in every new season or observed change in technology trends. New trends/ products trigger new keywords, and pulling new data retrains the model to recognise these new keywords. The model should be trained to recognised new terms and therefore, better able to classify new subreddit posts in the future.


## References
https://www.businessinsider.com/what-is-a-reddit-moderator-2016-1#crocker-still-enjoys-using-the-site-herself-her-dissertation-focuses-on-voodoo-religions-so-she-keeps-an-eye-on-roccult-12
https://www.usatoday.com/story/tech/talkingtech/2017/08/31/reddit-extremely-popular-heres-how-watch-what-your-kids-doing/607996001/
https://en.wikipedia.org/wiki/Reddit

