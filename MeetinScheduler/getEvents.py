# This script gets today's events from the google calendar API and writes them
# to todayEvents.txt which can then be read from by readEventsTrello.js
# Note that there will be issue if you have more than 100 events in one day...
# Will put in all events that start after 4am and before 5:05pm, and end before
# 9pm

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from quickstart import get_credentials

import datetime
from dateutil.parser import parse as parse_date
import pytz
utc=pytz.UTC
from django.utils.timezone import localtime


try:
  import argparse
  flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
  flags = None


###### IMPORTANT CONSTANTS ######
MIN_START_TIME = 4
MAX_START_TIME = 16
###################################

# Consume an hour and minute integers and converts to US/Eastern datetime
def hourToUSEDT(hr, mnt, timeNow):
  return pytz.timezone('US/Eastern').localize(timeNow.replace(
	       hour=hr-4, minute=mnt, second=0, microsecond=0)) 

# consume date String and converts to datetime object
def strToDate(dStr):
  return parse_date(dStr).replace(tzinfo=pytz.UTC) 



def main():
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('calendar', 'v3', http=http)
  timeNow = datetime.datetime.utcnow()
  nowStr = timeNow.isoformat() + 'Z' # 'Z' indicates UTC time
  eventsResult = service.events().list(
      calendarId='primary', timeMin=nowStr, maxResults=100, singleEvents=True,
      orderBy='startTime').execute()
  events = eventsResult.get('items', [])
  if not events:
    print('No upcoming events found.')
  for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    end   = event['end'].get('dateTime', event['end'].get('date'))

    if ((strToDate(start) >=  hourToUSEDT(MIN_START_TIME,0, timeNow)) and 
	(strToDate(start) <= hourToUSEDT(MAX_START_TIME, 0, timeNow))):
      print(parse_date(start).hour, ":", parse_date(start).minute, "-",
            min(parse_date(end).hour,23),":", parse_date(end).minute, "-", event['summary'])
 
if __name__ == '__main__':
  main()
