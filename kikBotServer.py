from flask import Flask, request, Response

from kik import KikApi
from kik.messages import messages_from_json, TextMessage

app = Flask(__name__)
BOT_USERNAME = "og400bot"
BOT_API_KEY  = "93b639a3-dd17-49be-b9ce-ad55129f564c" 
kik = KikApi(BOT_USERNAME, BOT_API_KEY)


@app.route('/receive', methods=['POST'])
def incoming():
  if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
    print(403)
    return Response(status=403)

  messages = messages_from_json(request.json['messages'])

  for message in messages:
    if isinstance(message, TextMessage):
      kik.send_messages([
        TextMessage(
          to=message.from_user,
          chat_id=message.chat_id,
          body=message.body
        )
      ])

  print(200)
  return Response(status=200)


if __name__ == "__main__": 
  app.run(port=8080, debug=True)

