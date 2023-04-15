# News & Stocks SMS App

This is a simple Python application that fetches data from two different APIs, one for the latest news and another for the stock trading, and sends news alerts via SMS about the user's selected company. The application uses the [News API](https://newsapi.org/) to get the latest news about companies and the [Alpaca API](https://alpaca.markets/) to get real-time stock market data.

## Requirements

To run the application, you will need the following:

- Python 3.6+
- [pipenv](https://pipenv.pypa.io/) for package management
- Twilio account for sending SMS messages

## Installation

To install the application, clone this repository and install the dependencies using pipenv:

```bash
git clone https://github.com/your-username/news-stocks-sms-app.git
cd news-stocks-sms-app
pipenv install
```

## Configuration


Before running the application, you need to set up the environment variables for your Twilio account and your preferred company. Rename the .env.example file to .env and fill in your Twilio account details and the company's ticker symbol:

```bash
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
RECIPIENT_PHONE_NUMBER=your_phone_number
COMPANY_SYMBOL=aapl
```

## Usage

To run the application, activate the pipenv shell:

```bash
Copy code
pipenv shell
```

Then, run the following command:

```bash
python app.py
```

The application will fetch the latest news about the specified company and check its current stock price. If the price reaches a certain threshold, the application will send an SMS alert to the specified phone number.

Contributing
Contributions are welcome! If you find a bug or want to suggest a new feature, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

This README explains what the application does, what are its requirements and how to use it. It also includes instructions for configuration, installation, and usage. Finally, it invites contributions and specifies the license.
