import requests
import xml.etree.ElementTree as ET

from .secrets import USER, PASSWORD, HOST


def nextcloud_request(url):
    return requests.get(
        '{}/ocs/v1.php/cloud/{}'.format(HOST, url),
        auth=(USER, PASSWORD),
        headers={'OCS-APIRequest': 'true'})


def get_user_names(group):
    x = nextcloud_request('groups/{}/users'.format(group))
    root = ET.fromstring(x.text)
    users = [a.text for a in root.find('data').find('users')]
    return users


def get_user(username):
    x = nextcloud_request('users/{}'.format(username))
    root = ET.fromstring(x.text)
    email = root.find('data').find('email').text
    return {
        'mail': email,
        'id': username
    }


def get_group_emails(groupname, skip_these_users=[]):
    users = []
    usernames = get_user_names(groupname)
    for username in usernames:
        if not skip_these_users or \
           username not in [a['id'] for a in skip_these_users]:
            user = get_user(username)
            users += [user]
    return users
