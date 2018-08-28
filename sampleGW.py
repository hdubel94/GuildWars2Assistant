import requests
from pprint import pprint

def requestURL(url):
	r = requests.get(url = url)
	data = r.json()
	return data

def getDailyID(type):
	dailyURL = "https://api.guildwars2.com/v2/achievements/daily"
	requestJson = requestURL(dailyURL)[type]

	achID = []
	for achievement in requestJson:
		achID.append(achievement['id'])

	return achID

def getAchievement(id):
	achievementURL = "https://api.guildwars2.com/v2/achievements?id=" + str(id)
	requestJson = requestURL(achievementURL)

	achInfo = {"name":requestJson['name'],
				"desc":requestJson['description'],
				"req":requestJson['requirement']}

	return achInfo


def main():
	# dailyJson = getDailyID('pvp')
	# getAchievement(1861)



if __name__ == '__main__':
	main()