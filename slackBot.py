import slack
import os
from dotenv import load_dotenv
from datetime import date
import time
from slack.errors import SlackApiError

env_path=".env"
load_dotenv(env_path)
client=slack.WebClient(os.environ['SLACK_BOT_TOKEN'])
t=time.localtime()
current_time=time.strftime("%H%M%S",t)
client.chat_postMessage(channel="#hackathontest",text="Hi the current date is"+str(date.today())+" and time is:"+str(current_time))

try:
    filepath = "C:/Users/ashiva/Downloads/REPORT/API4/emailable-report.html"
    response = client.files_upload(channels='#hackathontest', file=filepath)
    assert response["file"]  # the uploaded file
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")
