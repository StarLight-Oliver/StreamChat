
import json
from twitchio.ext import commands
import threading

with open("twitch_secret.json", "r") as f:
    data = json.loads(f.read())

messages2 = []

def Setup():

    #nick = input("What is your twitch: ")
    nick = "starlightdev"

    bot = commands.Bot(
        irc_token=data[2],
        client_id=data[0],
        nick= nick,
        prefix="!!!",
        initial_channels=[nick]
    )

    @bot.event
    async def event_ready():
        print("Bot is online!")
        ws = bot._ws
        #await ws.send_privmsg(nick, f"/me has landed!")

    @bot.event
    async def event_message(ctx):

        time = ctx.timestamp

        print(ctx)

        messages2.append(
            {
                "Author": ctx.author.display_name,
                "Message": ctx.content,
                #"Time": ctx.timestamp,
                "TimeStamp":time.strftime("%H:%M"),
                "Color": "#9147FF"
            }
        )

    def startThread():
        bot.run()

    thread = threading.Thread(name="Twitch", target=startThread)

    return thread

def FetchMessages(m):

    tempMessages = m.messages2
    
    m.messages2 = []

    return tempMessages

def Name():
    return "Twitch"
