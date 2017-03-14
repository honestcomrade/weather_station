import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/1cae8cac6d18a68a/geolookup/conditions/q/CA/Benicia.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Morning Jes!"
print "Here's today's conditions:"
print "Working on it..."
print "Current temperature in %s is %s degrees" % (location, temp_f)
f.close()
