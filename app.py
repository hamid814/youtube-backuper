# from telethon.sync import TelegramClient, events

# from decouple import config

# bot_name = 'b'
# TG_API_ID = config('TG_API_ID')
# TG_API_HASH = config('TG_API_HASH')
# TG_BOT_TOKEN = config('TG_BOT_TOKEN')

# bot = TelegramClient(bot_name, TG_API_ID, TG_API_HASH)

# bot.start(bot_token=TG_BOT_TOKEN)

# bot.send_file('@realytbackups', './video/svid.mp4', message='test')
# bot.send_message('@realytbackups', 'hola')

from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=-pTGc7cIBIA')

def p():
  print('p')

for s in yt.streams.filter(progressive=True, file_extension='mp4'):
  if s.itag == 22:
    r = s.download(output_path='./video', filename='v')
    print(r)


