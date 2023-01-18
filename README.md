# Fine-tuning-Hugging-face-text-classification-model

## About project
The objective of this challenge is to develop a machine learning model to assess if a Twitter post related to vaccinations is positive, neutral, or negative. This solution could help governments and other public health actors monitor public sentiment towards COVID-19 vaccinations and help improve public health policy, vaccine communication strategies, and vaccination programs across the world.

## About project data
The data comes from tweets collected and classified through Crowdbreaks.org [Muller, Martin M., and Marcel Salathe. "Crowdbreaks: Tracking Health Trends Using Public Social Media Data and Crowdsourcing." Frontiers in public health 7 (2019).]. Tweets have been classified as pro-vaccine (1), neutral (0) or anti-vaccine (-1). The tweets have had usernames and web addresses removed.

The objective of this challenge is to develop a machine learning model to assess if a twitter post that is related to vaccinations is positive, neutral, or negative.

**Variable definition:**

**tweet_id:** Unique identifier of the tweet

**safe_tweet:** Text contained in the tweet. Some sensitive information has been removed like usernames and urls

**label:** Sentiment of the tweet (-1 for negative, 0 for neutral, 1 for positive)

**agreement:** The tweets were labeled by three people. Agreement indicates the percentage of the three reviewers that agreed on the given label. You may use this column in your training, but agreement data will not be shared for the test set.

Files available for download are:

**Train.csv** - Labelled tweets on which to train your model

**Test.csv** - Tweets that you must classify using your trained model

## Project Models

 Two models were finetuned and trained from huggging face in this project to Achieve my desired model:
* bert-based-uncased
* roberta-base

# Model 1___training metrics and prediction

You can find my first model and its performance in hugging face using the link below;

https://huggingface.co/Gyimah3/Finetuned_bert

# Model 2___training metrics and prediction

You can find my second model and its performance in hugging face using the link below;

https://huggingface.co/Gyimah3/Finetuned_roberta


**Training metrics_time series**

![1](https://github.com/Gyimah3/Fine-tuning-Hugging-face-text-classification-model/blob/main/training_metrics%20screenshots-time%20series/Screenshot%202023-01-17%20210612.png)

**Training metrics_scalars**

![1](https://github.com/Gyimah3/Fine-tuning-Hugging-face-text-classification-model/blob/main/training_metrics%20screenshot-scalers/Screenshot%202023-01-17%20211512.png)










































































