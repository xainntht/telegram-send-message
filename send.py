import requests
while True:
	f = open("chatid.txt", "r")
	message = input("Mesaj yazın:")
	token = ""
	for chatid in f:
		url = requests.get("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chatid+"&text="+message)
