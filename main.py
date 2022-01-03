from internetSpeedTwitterBot import InternetSpeedTwitterBot


twitterBot = InternetSpeedTwitterBot()

twitterBot.get_internet_speed()
if twitterBot.promised_up > twitterBot.up or twitterBot.promised_down > twitterBot.down:
    twitterBot.tweet_at_provider()
twitterBot.driver.quit()
