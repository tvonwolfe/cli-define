'''main execution. this script grabs a definition

for a word from the Oxford Dictionary API.'''

import json
import urllib.request
from sys import argv, exit

if len(argv) != 2:
    print("Usage: dict <word>")
    exit(0)

WORD_TO_DEFINE = argv[1]

HTTP_HEADER = {
    "app_id": "c66a3308",
    "app_key": "f5edc82cb32a01b2c448c7253646ccb7"
}

URL = "https://od-api.oxforddictionaries.com/api/v1/entries/en/" + WORD_TO_DEFINE + "/regions=us"

CONTENTS = urllib.request.urlopen(urllib.request.Request(URL, headers=HTTP_HEADER)).read()
print("Getting definition...\n")

JSON_DATA = json.loads(CONTENTS)

if "results" in JSON_DATA:
    RESULTS = JSON_DATA["results"][0]
    WORD = RESULTS['id']
    LEX_ENTRIES = RESULTS['lexicalEntries'][0]
    LEX_CAT = LEX_ENTRIES['lexicalCategory']
    ENTRIES = LEX_ENTRIES['entries'][0]
    SENSES = ENTRIES['senses'][0]
    DEF = SENSES['definitions'][0]
    print(WORD + ": " + LEX_CAT + "\n")
    print(DEF)
else:
    print("Could not find definition.")
