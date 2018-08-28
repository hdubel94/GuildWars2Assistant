import requests
from pprint import pprint

def requestURL(url):
	r = requests.get(url = url)
	data = r.json()
	return data

"""
ACHIEVEMENT DEFINITIONS
"""
# Gathers the Daily IDs for the day
def getDailyID(type):
	dailyURL = "https://api.guildwars2.com/v2/achievements/daily"
	requestJson = requestURL(dailyURL)[type]

	achID = []
	for achievement in requestJson:
		achID.append(achievement['id'])

	return achID

# Gathers the Daily IDs for tomorrow
def getDailyTomorrowID(type):
	dailyURL = "https://api.guildwars2.com/v2/achievements/daily/tomorrow"
	requestJson = requestURL(dailyURL)[type]

	achID = []
	for achievement in requestJson:
		achID.append(achievement['id'])

	return achID

# Gathers the Name, Description, and Requirements for the specified Achievement
def getAchievement(id):
	achievementURL = "https://api.guildwars2.com/v2/achievements?id=" + str(id)
	requestJson = requestURL(achievementURL)

	achInfo = {"name":requestJson['name'],
				"desc":requestJson['description'],
				"req":requestJson['requirement']}

	return achInfo


"""
EVENT SCRAPING
TODO V2 API once it is released. V1 has been deprecated.
"""

def main():
	dailyJson = getDailyTomorrowID('pvp')
	pprint(dailyJson)
	# getAchievement(1861)



if __name__ == '__main__':
	main()