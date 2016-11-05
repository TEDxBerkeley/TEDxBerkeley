import json
import urllib.request


with open('speakers.json') as json_data:
    d = json.load(json_data)
    count = 0
    for year in d:
    	if year == "2010":
    		continue
    	for speaker in d[year]:
    		count += 1
    		if speaker["speaker_title"] == "Jodi Lomask/Capacitor" or speaker["speaker_title"] == "Mallika Chopra" or speaker["speaker_title"] == "Celli@Berkeley":
    			continue
    		print(speaker["speaker_title"])
    		urllib.request.urlretrieve(speaker["speaker_image_uri"], speaker["speaker_title"] + ".jpg")
    print(count)
