import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/1cae8cac6d18a68a/geolookup/conditions/q/CA/Martinez.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
wind_str = parsed_json['current_observation']['wind_string']
wind_dir = parsed_json['current_observation']['wind_dir']
wind_mph = parsed_json['current_observation']['wind_mph']
humidity = parsed_json['current_observation']['relative_humidity']
print "Morning Jes!"
print "Here's today's conditions:"
print "Current temperature in %s is %s degrees" % (location, temp_f)
print "With %s winds from the %s of %s mph" % (wind_str, wind_dir, wind_mph)
print "And %s humidity" % (humidity)
f.close()
