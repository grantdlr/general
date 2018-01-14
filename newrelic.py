#from newrelic_api import Applications, Servers, Users

#server = Servers(api_key='fba3858c9eeedb92727d2166fed5a5489187fb576ebee0a')
#srv= server.list()
#apps = Applications(api_key='fba3858c9eeedb92727d2166fed5a5489187fb576ebee0a')
#app = apps.list()
#user = Users(api_key='fba3858c9eeedb92727d2166fed5a5489187fb576ebee0a')
#usr = user.list(filter_email='Grant.delaRosa@kmart.com.au')

import requests
import json

#GET NewRelic API
url = 'https://api.newrelic.com/v2/alerts_policies.json'
headers = {'X-Api-Key': 'fba3858c9eeedb92727d2166fed5a5489187fb576ebee0a'}
g = requests.get(url, headers=headers)

#work with JSON
f = json.loads(g.text)
#the '0' is for the first object in the list within the json dict
f['policies'][0]['id']
#foreach
d = f['policies']
for i in d:
  print(i['id'])
  
#POST  Alert Policy NewRelic API
url = 'https://api.newrelic.com/v2/alerts_policies.json'
payload = {
  "policy": {
    "incident_preference": "PER_POLICY",
    "name": "grant"
  }
}
#headers = {'X-Api-Key': 'fba3858c9eeedb92727d2166fed5a5489187fb576ebee0a'}
headers = {'X-Api-Key': '1a0b038f2879e22460f27632dea5bf2b', 'Content-Type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)

#POST  Alert Infrastructure Policy NewRelic API
url = 'https://infra-api.newrelic.com/v2/alerts/conditions'
payload = {
   "data":{
      "type":"infra_host_not_reporting",
      "name":"Cassandra Host Reporting Condition",
      "enabled":True,
      "policy_id":174348,
      "critical_threshold":{
         "duration_minutes":12
      }
   }
}
headers = {'X-Api-Key': '1a0b038f2879e22460f27632dea5bf2b', 'Content-Type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
