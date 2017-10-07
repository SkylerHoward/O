from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import pytz

import datetime

import dateutil.parser

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

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

def dict_to_str(dict):
	start = dict['start']['dateTime']
	start = dateutil.parser.parse(start).time().strftime('%I:%M%p')
	end = dict['end']['dateTime']
	end = dateutil.parser.parse(end).time().strftime('%I:%M%p')
	summary = dict['summary']
	location = dict['location'].split(' ')[1]
	str = 'Starting at {}, you have {}, at {}, which goes until {}'.format(start, summary, location, end)
	return str
	
def today():
	today_events = []
	te = []
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)
	now = datetime.datetime.utcnow()
	eventsResult = service.events().list(
		calendarId='primary', timeMin=now.isoformat()+'Z', maxResults=10, singleEvents=True,
		orderBy='startTime').execute()
	events = eventsResult.get('items', [])

	if not events:
		print('No upcoming events found.')
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'))
		start = dateutil.parser.parse(start)
		if start.day == now.day:
			today_events.append(event)
		#te.append(event)
	event_criteria = ['start', 'end', 'location', 'description', 'summary']
	for event in te:
		today_events.append(dict_to_str(event))
	return today_events