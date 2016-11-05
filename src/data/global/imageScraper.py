import json
import urllib.request


with open('speakers.json') as json_data:
    d = json.load(json_data)
    for year in d:
    	for speaker in d[year]:
    		if speaker["speaker_title"] == "Jodi Lomask/Capacitor" or speaker["speaker_title"] == "Mallika Chopra":
    			break
    		urllib.request.urlretrieve(speaker["speaker_image_uri"], speaker["speaker_title"] + ".jpg")
    		
