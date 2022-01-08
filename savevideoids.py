from telethon.sync import TelegramClient, events

from decouple import config

from ytapi import save_videos

'''
how this code works:

you send the id of a youtube channel ( like this: UCBJycsmduvYEL83R_U4JriQ )
to a telegram bot ( t.me/realtgbackuperbot ), and the rest of the this is 
taken care of...

send message like this:
/savevideos [cahnnel_id]
/saveplaylist [playlist_id]
/savevideo [video_id]

the id of all videos are grabbed from youtube api and sent to a mongo database

later the ids will be used to download vides one bt one and be sent to a
telegram channel

'''

bot_name = 'b'
TG_API_ID = config('TG_API_ID')
TG_API_HASH = config('TG_API_HASH')
TG_BOT_TOKEN = config('TG_BOT_TOKEN')

bot = TelegramClient(bot_name, TG_API_ID, TG_API_HASH)

bot.start(bot_token=TG_BOT_TOKEN)

@bot.on(events.NewMessage(incoming=True))
async def bnmh(event):
  if event.original_update.message.peer_id.user_id != 79713563: return
  
  if event.raw_text.startswith('/savevideos'):
    channel_id = event.raw_text.split(' ')[1]

    await event.reply('saving ids...')

    save_videos(channel_id)

    await event.reply('vidoes added')

bot.run_until_disconnected()
