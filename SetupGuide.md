### Installing The Dependencies
This bot requires the [Tweepy](https://github.com/tweepy/tweepy) python library, the following instructions are from the guide provided in its repository.

The easiest way to install the latest version is by using pip/easy_install to pull it from PyPI:
```cmd
pip install tweepy
```
You may also use Git to clone the repository from GitHub and install it manually:
```cmd
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python setup.py install
```

### Setting Up A Twitter Developer Account

You will also need to create an app account [here](https://apps.twitter.com/), follow the instructions bellow to get your login infomation.
1. Sign in with your Twitter account
2. Create a new app account
3. Modify the settings for that app account to allow read & write
4. Generate a new OAuth token with those permissions

Once you have your 4 tokens you will need to paste them into the config section of the bot

### How Implement Auth Tokens Into Code
Simply paste the tokens into their respective variable in the config, like so

```python
consumer_key = 'de9A1DsFACdJKfg5DDG6Xrtld'
consumer_secret = 'Dda5a0DfH25HegDb2GGk4H11wDb21GHFDSVBeABlp2GSG2xAH'
access_token = '224289154627621231-x623zxEreTfAKecOdeaD5dgea3dG5'
acess_token_sectret = 'ThgfS2hLdgK4FgNDTAGB5dfk2Xt3g2FF1fY5FAA2XtoaG'
```
###### NOTE: These access tokens are fake, do not try to use them
