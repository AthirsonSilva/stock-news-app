import requests
from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHAVANTAGE_API_KEY = 'BC8BJNID5FW45BDZ'
NEWS_API_KEY = '65e4e4d2d2294e6580ee9f660ad6323c'
TWILIO_TOKEN = '2c001171121034fffd1e08d88e3a09a2'
TWILIO_ACCOUNT_SID = 'AC3e11ff847021fcaea9eb2632457c9e71'
TWILIO_PHONE_NUMBER = '+19706808885'
MY_PHONE_NUMBER = '+5511957607177'


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': ALPHAVANTAGE_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data['4. close']
print(before_yesterday_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) -
                 float(before_yesterday_closing_price))
print(difference)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percentage = (difference / float(yesterday_closing_price)) * 100
print(difference_percentage)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if difference > 1:
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.
    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"TSLA: {int(difference)}%\nHeadline: {article['title']}, \nBrief: {article['description']}" for article in three_articles]

    # TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER,
        )


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
