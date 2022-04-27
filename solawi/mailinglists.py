
HOST = 'https://ml-cgn12.ispgateway.de'
URL = 'mailman/admin'
URL_ADD = 'members/add'

MAPPING = {
    'Cuvry': '',
    'Eberty': '',
    'Endorphina': '',
    'Hofangehörige': '',
    'Kreutziger': '',
    'Mitglieder:innen': '',
    'Peace of Land': '',
    'Potsdam West': '',
    'Potsdam freiland': '',
    'Preddöhl': '',
    'Ratibor': 'ratibor-liste_solawi-waldgarten.de',
    'Rigaer': '',
}

def members_url(listname):
    if not listname:
        return ''
    return '{}/{}/{}/{}'.format(HOST, URL, listname, URL_ADD)