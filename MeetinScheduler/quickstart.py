from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

try:
  import argparse
  flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
  flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
  """Gets valid user credentials from storage.

  If nothing has been stored, or if the stored credentials are invalid,
  the OAuth2 flow is completed to obtain the new credentials.

  Returns:
    Credentials, the obtained credential.
  """
  home_dir = os.path.expanduser('~')
  credential_dir = os.path.join(home_dir, '.credentials')
  if not os.path.exists(credential_dir):
    os.makedirs(credential_dir)
  credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

  store = oauth2client.file.Storage(credential_path)
  credentials = store.get()
  if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    if flags:
      credentials = tools.run_flow(flow, store, flags)
    else: # Needed only for compatibility with Python 2.6
      credentials = tools.run(flow, store)
    print('Storing credentials to ' + credential_path)
  return credentials


def makeDateTime(year, month, day, hour, minute):
#  retStr = str(year) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2) + "T" + str(hour).zfill(2) + ":" + str(minute).zfill(2)
#  print(retStr)
  dtNow = date
  return retStr

def insertEvent(summary, location, description, sDateTime, eDateTime):
  event = {
    'summary': summary,
    'location': location,
    'description': description,
    'start': {
      'dateTime': sDateTime, #'2015-05-28T09:00:00-07:00',
      'timeZone': 'America/New_York',
    },
    'end': {
      'dateTime': eDateTime, #'2015-05-28T17:00:00-07:00',
      'timeZone': 'America/New_York',
    },
    'recurrence': [
    ],
    'attendees': [
    ],
    'reminders': {
      'useDefault': False,
      'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
      ],
    },
  }
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
 
  service = discovery.build('calendar', 'v3', http=http)
  event = service.events().insert(calendarId='primary', body=event).execute()
  print("Event created: %s" % (event.get('htmlLink')))



def main():
  """Basic meeting generation.
  """
  year        = int(raw_input("Year for meeting?"))
  month       = int(raw_input("Month for meeting?"))
  day         = -1
  dow         = ""
  if (raw_input("In the next week? (y/n)") == "n"):
    day       = int(raw_input("Day for meeting?"))
  else:
    dow       = raw_input("Day of the week? (m/t/w/h/f/s/u)")

  hour        = -1
  minute      = -1
  tod         = ""
  if (raw_input("Specific time? (y/n)") == "y"):
    hour      = int(raw_input("Hour? (24 Hour clock)"))
    minute    = int(raw_input("Minute? (24 hour clock)"))
  else:
    minute    = 0 #TODO
    tod       = raw_input("What time of day? (m)orning/(a)fternoon/(e)vening)")
    if (tod == "m"): #TODO
      hour = 10
    elif (tod == "a"):
      hour = 14
    else:
      hour = 19

  length      = int(raw_input("How long will the meeting take? (number of minutes)"))
  prep        = int(raw_input("How much prep/travel time will you need before? (number of minutes)")) #TODO 
  summary     = raw_input("Meeting Summary:")
  location    = raw_input("Meeting location:")
  description = raw_input("Meeting description:")
  reminder    = raw_input("Would you like a reminder 10 minutes before? (y/n)") #TODO
  email       = raw_input("Would you like an email the night before? (y/n)")    #TODO

  startTimeLocal = datetime.datetime(year, month, day, hour, minute, 0)
  startTimeUTC   = startTimeLocal + datetime.timedelta(0, 4*60*60)
  endTime        = startTimeUTC + datetime.timedelta(0, minute*60)

  insertEvent(summary, location, description, startTimeUTC.isoformat() + "Z", endTime.isoformat() + 'Z')


if __name__ == '__main__':
  main()
