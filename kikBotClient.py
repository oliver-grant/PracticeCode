from kik import KikApi, Configuration

BOT_USERNAME = "og400bot"
BOT_API_KEY  = "93b639a3-dd17-49be-b9ce-ad55129f564c" 

kik = KikApi(BOT_USERNAME, BOT_API_KEY)
config = Configuration(webhook="127.0.0.1:8080")
print(config.webhook)


