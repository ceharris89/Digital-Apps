#documentation: https://pypi.python.org/pypi/TwitterFollowBot/v2.0
from TwitterFollowBot import TwitterBot
my_bot = TwitterBot()
my_bot.sync_follows()
#my_bot.auto_follow_followers_of_user("nfl", count=50)
my_bot.auto_unfollow_nonfollowers()