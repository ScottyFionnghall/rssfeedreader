# Requirements
# The user can input a RSS feed URL.
# The reader will display the title, description, and link of the original content.
# For an extra challenge
# The user can add more than one RSS feed URL.

# Example links:
# https://rss.art19.com/apology-line, https://feeds.simplecast.com/54nAGcIl, https://feeds.fireside.fm/bibleinayear/rss

from multiprocessing.sharedctypes import Value
import rssparser # import custom made parser
# ask user for one or multiple link to rss
user_input = str(input("Paste RSS link (if multiple links separated by commas):"))
user_input = user_input.split(',') # separate all links and convert them into list
for i in range(len(user_input)): # for every link in the 'user_input' parse it
    try:
        rssparser.parse(user_input[i])
    except ValueError:
        print('Not a link')