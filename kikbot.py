from kik import KikApi, Configuration
kik = KikApi("og400bot", "93b639a3-dd17-49be-b9ce-ad55129f564c")
config = Configuration(webhook = "https://example.com/incoming")
kik.set_configuration(config)
print(config.webhook)

