import config
from discord_connector import client


# 1. connect to discord
# 2. connect to irc
# 3. connect to rabbitmq
# 4. infinite loop for rabbitmq, listen for events
# 4.1 if game has been created - create discord channels with passwords for 2 teams
# 4.2 create invitation link for channel to join
# 4.3 send invitation link via irc for players
# 5. listen for messages, turn on/off such functionality for those who doesn't want to join


