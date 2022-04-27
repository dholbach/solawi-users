import json
import os

DIRECTORY = os.path.join(
    os.path.dirname(__file__), '..', 'snapshots')
SNAPSHOTS_FN = os.path.join(DIRECTORY, 'data.json')


def create_dir():
    if not os.path.isdir(DIRECTORY):
        os.mkdir(DIRECTORY)


def read_snapshot():
    create_dir()
    if not os.path.isfile(SNAPSHOTS_FN):
        return {}
    with open(SNAPSHOTS_FN, 'r') as f:
        data = json.loads(f.read())
    return data


def save_snapshot(data):
    create_dir()
    if os.path.isfile(SNAPSHOTS_FN):
        os.remove(SNAPSHOTS_FN)
    with open(SNAPSHOTS_FN, 'w') as f:
        f.write(json.dumps(data))
