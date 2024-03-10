import datetime as dt
import os

import scratchattach as scratch3
from online import keep_alive


session = scratch3.Session(os.environ["BOT_SESSION"], username="The_Craftor")

conn = session.connect_cloud(project_id="964103689")

client = scratch3.CloudRequests(cloud_connection=conn,
                                used_cloud_vars=["1", "2", "3", "4", "5", "6"])


@client.request
def ping(stamp=None):
  if stamp is None:
    return "pong !"
  else:
    date_today = dt.datetime(dt.datetime.now().year,
                             dt.datetime.now().month,
                             dt.datetime.now().day,
                             dt.datetime.now().hour+1,
                             dt.datetime.now().minute,
                             dt.datetime.now().second,
                             dt.datetime.now().microsecond)
    date_2000 = dt.datetime(2000, 1, 1, 0, 0, 0, 0)
    timestamp_diff = (date_today - date_2000).total_seconds()
    total = float(stamp) - timestamp_diff
    return str(total)


def plural(number: float):
  if number > 1 and number < 2:
    return ""
  else:
    return "s"


###

###


@client.event
def on_ready():
  print("Request handler is running")
  keep_alive()


###

###

client.run()
