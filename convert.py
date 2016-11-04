import json

with open('speakers.json') as json_data:
	a = json.load(json_data)
	t010 = []
	t011 = []
	t012 = []
	t013 = []
	t014 = []
	t015 = []
	for i in a:
		if i["year"] == "2010":
			t010 += [i]
		if i["year"] == "2011":
			t011 += [i]
		if i["year"] == "2012":
			t012 += [i]
		if i["year"] == "2013":
			t013 += [i]
		if i["year"] == "2014":
			t014 += [i]
		if i["year"] == "2015":
			t015 += [i]
	b = {"2010":t010, "2011":t011, "2012":t012, "2013":t013, "2014":t014, "2015":t015}
	print(b)

with open('speakers.json', 'w') as json_data:
	json.dump(b, json_data)