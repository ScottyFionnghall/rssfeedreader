# Requirements
# The user can input a RSS feed URL.
# The reader will display the title, description, and link of the original content.
# For an extra challenge
# The user can add more than one RSS feed URL.

# Example links:
# https://rss.art19.com/apology-line, https://feeds.simplecast.com/54nAGcIl, https://feeds.fireside.fm/bibleinayear/rss

import feedparser
import re
def get_stuff(def_user_input):
    def_user_input = str(def_user_input).strip(' ')
    d = feedparser.parse(def_user_input)
    title = d.feed.title
    description = str(d.feed.description)
    description = re.sub('[</p>]','',description)
    link = d.feed.link
    print("Title: ",title,'\nDescription: ',description,'\nLink: ',link)
user_input = str(input("Paste RSS link (if multiple links seperate by commas):"))
user_input = user_input.split(',')
for i in range(len(user_input)):
    get_stuff(user_input[i])