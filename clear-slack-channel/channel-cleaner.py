# using
# https://github.com/sgratzl/slack_cleaner2

# Install from PyPi:
# pip install slack-cleaner2

from slack_cleaner2 import *

s = SlackCleaner('SECRET TOKEN')
# list of users
s.users
# list of all kind of channels
s.conversations

# delete all messages in -bots channels
for msg in s.msgs(filter(match('.*old'), s.conversations)):
  # delete messages, its files, and all its replies (thread)
  msg.delete(replies=True, files=True)

# delete all general messages and also iterate over all replies
# for msg in s.c.general.msgs(with_replies=True):
#   msg.delete()