from instapy import InstaPy
import os

# put your API key into the API_KEY field below, in quotes
INSTA_USERNAME = os.environ.get("INSTA_USERNAME")
INSTA_PASSWORD = os.environ.get("INSTA_PASSWORD")

# Basic login and setup for engagement
session = InstaPy(username=INSTA_USERNAME, password=INSTA_PASSWORD)
session.login()
session.like_by_tags(["nyjets", "takeflight"], amount=5)
session.set_dont_like(["nyjets", "takeflight"])
session.set_do_comment(True, percentage=50)
session.set_dont_like(["TAKEFLIGHT", "Love your content", "JetUp"])

session.end()
