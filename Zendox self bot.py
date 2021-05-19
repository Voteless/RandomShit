class SELFBOT():
    __linecount__ = 3528
    __version__ = "1.31C"

    
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, functools 
import aiohttp, asyncio, logging, wget, typing, psutil, uuid, wikipedia, textwrap, winsound
from discord.ext import (
    commands,
    tasks
)
from youtubesearchpython import SearchVideos
from urllib import parse, request
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from selenium import webdriver
from discord import Member
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
from gtts import gTTS
from AuthGG.client import Client as client
from os import system



def __init__(self, bot):
        self.bot = bot 
        self.saved_roles = {}

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

#<--------------Colors Start-------------->
RED_dark= 0x6a006a
RED_medium= 0xa958a5
RED_light= 0xc481fb
gold= 0xdaa520
red_dark= 8e2430
red_light= 0xf94343
blue_dark= 0x3b5998
cyan= 0x5780cd
blue_light= 0xace9e7
aqua= 0x33a1ee
green_dark= 0x2ac075
green_light= 0xa1ee33
white= 0xf9f9f6
cream= 0xffdab9
#<--------------Colors End-------------->

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
headers = {'Authorization': token}
r = requests.post(
    f'https://discordapp.com/api/v6/entitlements/gift-codes/redeem', 
    headers=headers,
    ).text

giveaway_sniper = config.get('giveaway_sniper')
nitro_sniper = config.get('nitro_sniper')
rpc_uwu = config.get('rpc_uwu')
beep = config.get('nitro_beep')
Invite = config.get('Invite')

webhooknotification = config.get('webhook-notification')
webhook = config.get('webhook')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

def Clear():
    os.system('cls')
Clear()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.CYAN}[{Fore.RED}ERROR{Fore.CYAN}]{Fore.RESET}: {Fore.RED}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Zendox.run(token, bot=False, reconnect=True)
            os.system(f'title (Zendox Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.CYAN}[{Fore.RED}ERROR{Fore.CYAN}]{Fore.RESET}: {Fore.RED}PLEASE PUT YOUR TOKEN IN THE CONFIG FILE"+Fore.RESET)
            time.sleep(2)
            print(f"{Fore.RED}EXITING PROGRAM PLEASE TRY AGAIN")
    

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.CYAN}[{Fore.RED}ERROR{Fore.CYAN}]{Fore.RESET}: {Fore.RED} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

async def SendWhook():
    url = ""
    whook = {
        "embeds": [
            {
                "title": "",
                "description": "",
                "thumbnail": {
                    "url": ""
                },
                "footer": {
                    "text": ""
                }
            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=whook)

def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
Zendox = discord.Client()
Zendox = commands.Bot(
    description='Zendox Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Zendox.remove_command('help') 

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD", 
        url="https://www.twitch.tv/", 
    )
    await Zendox.change_presence(activity=btc_stream)

@Zendox.event
async def on_command(ctx):
  print(f"[{Fore.GREEN}+{Fore.RESET}]{Fore.CYAN}Command Used {ctx.command.name}{Fore.RESET}")

@Zendox.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"[{Fore.RED}ERROR{Fore.RESET}]: {Fore.RED}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"[{Fore.RED}ERROR{Fore.RESET}]: {Fore.RED}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"[{Fore.RED}ERROR{Fore.RESET}]: {Fore.RED}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"[{Fore.RED}ERROR{Fore.RESET}]: {Fore.RED}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"[{Fore.RED}ERROR{Fore.RESET}]: {Fore.RED}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"[{Fore.RED}ERROR{Fore.RESET}]: {Fore.RED}{error_str}"+Fore.RESET)



@Zendox.event
async def on_message_edit(before, after):
    await Zendox.process_commands(after)

@Zendox.event
async def on_message(message):

    def GiveawayData():
        time = datetime.datetime.now().strftime("%H:%M %p")
        print(
            f"\n{Fore.GREEN} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.BLUE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.MAGENTA} - Prize: {Fore.WHITE}{message.embeds[0].author.name}"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(f"\n{Fore.RED} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.CYAN} - CODE: {Fore.YELLOW}{code}"
            f"\n{Fore.BLUE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            + Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'


            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}╔═══════════════════════╦══════════════════╗"
                      f"\n{Fore.CYAN}║ {Fore.RED}[{Fore.RED}X{Fore.RED}] {Fore.GREEN}False Code        {Fore.CYAN}║ {Fore.RED}{code} {Fore.CYAN}║" 
                      f"\n{Fore.CYAN}╚═══════════════════════╩══════════════════╝"+ Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}╔═══════════════════════╦══════════════════╗"
                      f"\n{Fore.CYAN}║ {Fore.RED}[{Fore.GREEN}+{Fore.RED}] R{Fore.GREEN}edeemed Code     ║ {Fore.GREEN}{code} {Fore.CYAN}║" 
                      f"\n{Fore.CYAN}╚═══════════════════════╩══════════════════╝"+ Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}╔═══════════════════════╦══════════════════╗"
                      f"\n{Fore.CYAN}║ {Fore.RED}[{Fore.BLUE}-{Fore.RED}] {Fore.GREEN}Unkown code       ║ {Fore.BLUE}{code}  {Fore.CYAN}║" 
                      f"\n{Fore.CYAN}╚═══════════════════════╩══════════════════╝"+ Fore.RESET)
                NitroData(elapsed, code)
                if beep == True:
                    winsound.PlaySound("Sniper", winsound.SND_FILENAME)
        else:
            return
    
    if 'discord.gift/' in message.content:
        if webhooknotification == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                data = {
                    "embeds": [{
                        "title": "Successfully Sniped Nitro Gift!",
                        "description": f"**This code has been redeemed already.\n\nNitro Gift Server:\n{message.guild}\n\nNitro Gift Sender:\n{message.author}\n\nNitro Gift Code:\n{code}**",
                        "color": 16732345,
                        "footer": {
                        "text": "Zendox NITRO SNIPER"
                        },
                        "image": {
                        "url": "https://i.imgur.com/9QVtF0t.png"
                        }
                        }],
                        "username": "Nitro",
                        "avatar_url": "https://cdn.discordapp.com/attachments/777893133991149588/783064116377026580/LOGO_1.png"
                        }
                requests.post(webhook, json=data)

            elif 'subscription_plan' in r:
                data = {
                    "embeds": [{
                        "title": "Successfully Sniped Nitro Gift!",
                        "description": f"**Congratulations, good job! You can view your Nitro Gifts in your inventory.\n\nNitro Gift Server:\n{message.guild}\n\nNitro Gift Sender:\n{message.author}\n\nNitro Gift Code:\n{code}**",
                        "color": 16732345,
                        "footer": {
                        "text": "Zendox NITRO SNIPER"
                        },
                        "image": {
                        "url": "https://i.imgur.com/9QVtF0t.png"
                        }
                        }],
                        "username": "Nitro",
                        "avatar_url": "https://cdn.discordapp.com/attachments/777893133991149588/783064116377026580/LOGO_1.png"
                        }
                requests.post(webhook, json=data)

            elif 'Unknown Gift Code' in r:
                data = {
                    "embeds": [{
                        "title": "Successfully Sniped Nitro Gift!",
                        "description": f"**This code is most likely fake sorry.\n\nNitro Gift Server:\n{message.guild}\n\nNitro Gift Sender:\n{message.author}\n\nNitro Gift Code:\n{code}**",
                        "color": 16732345,
                        "footer": {
                        "text": "Zendox NITRO SNIPER"
                        },
                        "image": {
                        "url": "https://i.imgur.com/9QVtF0t.png"
                        }
                        }],
                        "username": "Nitro",
                        "avatar_url": "https://cdn.discordapp.com/attachments/777893133991149588/783064116377026580/LOGO_1.png"
                        }
                requests.post(webhook, json=data)
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 396464677032427530:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 673918978178940951:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 716967712844414996:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    await Zendox.process_commands(message)

@Zendox.event
async def on_connect():
    system('mode con: cols=66 lines=26')
    Clear()
    if webhooknotification == True:
        notifications = "Active"
    else:
        notifications = "Disabled"

    if rpc_uwu == True:
        message = ('Zendox SELFBOT')
        game = discord.Game(
            name=message
        )
        await Zendox.change_presence(activity=game)

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"
    if rpc_uwu == True:
        rpc = "Active"
    else:
        rpc = "Disabled"
    if beep == True:
        nitro_beep = "Active"
    else:
        nitro_beep = "Disabled"

    print(f'''{Fore.RESET}
        {Fore.RED} ███████╗{Fore.CYAN}███████╗{Fore.RED}███╗   ██╗{Fore.CYAN}██████╗ {Fore.RED} ██████╗ {Fore.CYAN}██╗  ██╗{Fore.RESET}
        {Fore.RED} ╚══███╔ {Fore.CYAN}██╔════╝{Fore.RED}████╗  ██║{Fore.CYAN}██╔══██╗{Fore.RED}██╔═══██╗{Fore.CYAN}╚██╗██╔╝{Fore.RESET}
        {Fore.RED}   ███╔╝ {Fore.CYAN}█████╗  {Fore.RED}██╔██╗ ██║{Fore.CYAN}██║  ██║{Fore.RED}██║   ██║{Fore.CYAN} ╚███╔╝ {Fore.RESET}
        {Fore.RED}  ███╔╝  {Fore.CYAN}██╔══╝  {Fore.RED}██║╚██╗██║{Fore.CYAN}██║  ██║{Fore.RED}██║   ██║{Fore.CYAN} ██╔██╗ {Fore.RESET}
        {Fore.RED} ███████╗{Fore.CYAN}███████╗{Fore.RED}██║ ╚████║{Fore.CYAN}██████╔╝{Fore.RED}╚██████╔╝{Fore.CYAN}██╔╝ ██╗{Fore.RESET}
        {Fore.RED} ╚══════╝{Fore.CYAN}╚══════╝{Fore.RED}╚═╝  ╚═══╝{Fore.CYAN}╚═════╝ {Fore.RED} ╚═════╝ {Fore.CYAN}╚═╝  ╚═╝{Fore.RESET}
                                                   

        {Fore.RED}Connected as {Fore.CYAN}{Zendox.user.name}{Fore.RESET}
        {Fore.RED}╔═══════════════════════╦═══════════════╗
        {Fore.RED}║   {Fore.CYAN}Prefix{Fore.RESET}              {Fore.RED}║   [{Fore.CYAN}{prefix}{Fore.RED}]         ║
        {Fore.RED}║   {Fore.CYAN}Giveaway Sniper{Fore.RESET}     {Fore.RED}║   [{Fore.CYAN}{giveaway}{Fore.RED}]    ║
        {Fore.RED}║   {Fore.CYAN}Nitro Sniper{Fore.RESET}        {Fore.RED}║   [{Fore.CYAN}{nitro}{Fore.RED}]    ║
        {Fore.RED}║   {Fore.CYAN}RPC{Fore.RESET}                 {Fore.RED}║   [{Fore.CYAN}{rpc}{Fore.RED}]    ║
        {Fore.RED}╚═══════════════════════╩═══════════════╝
        {Fore.RED}COMMANDS LOGS BELOW:
    '''+Fore.RESET)
    ctypes.windll.kernel32.SetConsoleTitleW(f'Zendox')




@Zendox.command()
async def help(ctx):
    await ctx.message.delete()
    user = ctx.author.display_name,
    embed = discord.Embed(title="", description="", color=0xff0000, timestamp=ctx.message.created_at)
    embed.set_author(name='Help Commands')
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/823346417618911252/97fb87532f81e13b7fc3bf2c360b7b96.webp?size=1024')
    embed.add_field(name=f'{prefix}destroy', value='Destroys server', inline=False)
    embed.add_field(name=f'{prefix}massban', value='Bans Everyone', inline=False)
    embed.add_field(name=f'{prefix}masskick', value='Kicks Everyone', inline=False)
    embed.add_field(name=f'{prefix}massrole', value='Makes Roles', inline=False)
    embed.add_field(name=f'{prefix}delchannels', value='Deletes channels', inline=False)
    embed.add_field(name=f'{prefix}delroles', value='Deletes Roles', inline=False)
    embed.add_field(name=f'{prefix}massunban', value='unbans Everyone', inline=False)
    embed.add_field(name=f'{prefix}renamealle', value='Rename Everyone in server', inline=False)
    embed.add_field(name=f'{prefix}renamechannels', value='Renames all channels', inline=False)
    embed.add_field(name=f'{prefix}spamchannels', value='Makes Channels', inline=False)
    embed.add_field(name=f'{prefix}fun', value='fun Commands', inline=False)
    await ctx.send(embed=embed, delete_after=30)




@Zendox.command()
async def fun(ctx):
    await ctx.message.delete()
    user = ctx.author.display_name,
    embed = discord.Embed(title="", description="", color=0xff0000, timestamp=ctx.message.created_at)
    embed.set_author(name='Help Commands')
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/823346417618911252/97fb87532f81e13b7fc3bf2c360b7b96.webp?size=1024')
    embed.add_field(name=f'{prefix}cyclenick', value='Changes Nicks 1 2 3', inline=False)
    embed.add_field(name=f'{prefix}stopnick', value='Stops Nick', inline=False)
    embed.add_field(name=f'{prefix}invnick', value='invisible nick', inline=False)
    embed.add_field(name=f'{prefix}fucknick', value='fucks nick', inline=False)
    embed.add_field(name=f'{prefix}rainbow', value='Makes Role Rainbow', inline=False)
    embed.add_field(name=f'{prefix}purge', value='purges', inline=False)
    embed.add_field(name=f'{prefix}boom', value='BOOM', inline=False)
    embed.add_field(name=f'{prefix}afk', value='AFK', inline=False)
    embed.add_field(name=f'{prefix}cum', value='Cums', inline=False)
    embed.add_field(name=f'{prefix}spam', value='spams', inline=False)
    await ctx.send(embed=embed, delete_after=30)




@Zendox.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): 
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(0.5)
        except:
            break




@Zendox.command()
async def invnick(ctx):
    await ctx.message.delete()
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is invisible")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@Zendox.command()
async def fucknick(ctx):
    await ctx.message.delete()
    try:
        name = "﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽" 
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is a big mess :)")
    except Exception as e:
        await ctx.send(f"Error: {e}")


@Zendox.command()
async def purge(ctx, amount: int): 
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Zendox.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass


@Zendox.command()
async def destroy(ctx):

    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")

        except:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} has been deleted in {ctx.guild.name}")

        except:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{role.name} has been deleted in {ctx.guild.name}")

        except:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")

    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print(f"{user.name} has been banned from {ctx.guild.name}")

        except:
            print(f"{user.name} has FAILED to be banned from {ctx.guild.name}")

@Zendox.command()
async def massban(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Zendox.command()
async def masskick(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Zendox.command()
async def massrole(ctx): 
    await ctx.message.delete()
    for _i in range(1000):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@Zendox.command()
async def masschannel(ctx): 
    await ctx.message.delete()
    for _i in range(1000):
        try:
            await ctx.guild.create_text_channel(name=RandString())
            await ctx.guild.create_voice_channel(name=RandString())
        except:
            return

@Zendox.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Zendox.command() 
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Zendox.command()
async def massunban(ctx):
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Zendox.command()
async def renameall(ctx, rename_to):

    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.edit(nick=rename_to)
            print(f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")

        except:
            print(f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")

@Zendox.command()
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

@Zendox.command()
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="RAIDED BY ZENDOX SELF-BOT")
        except:
            return


@Zendox.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)


@Zendox.command()
async def cyclenick(ctx, types=None, *, text=None):
    await ctx.message.delete()
    global cycling
    if types is None:
        embed = discord.Embed(color=52479, timestamp=ctx.message.created_at)
        embed.set_author(name="Zendox SELF-BOT | PREFIX: " + str(Zendox.command_prefix))
        embed.description = f"**NICKNAME COMMANDS\n{prefix}cyclenick 1 (name)** | cycles all letters in name\n**{prefix}cyclenick 2 (nick1) (nick)** | cycles through all the nicknames you enter\n**{prefix}cyclenick 3 (nick1) (nick2)** | cycles though all the nicknames you enter\n**{prefix}stopcycle** | stops nickname cycle"
        await ctx.send(embed=embed,delete_after=30)
    elif str(types).lower() == "1":
        cycling = True
        while cycling:
            name = ""
            for letter in text:
                name = name + letter
                await ctx.message.author.edit(nick=name)

    elif str(types).lower() == "2":
        cycling = True
        while cycling:
            name = ""
            for word in text.split(","):
                name = name + word
                await ctx.message.author.edit(nick=name)

    elif str(types).lower() == "3":
        cycling = True
        while cycling:
            name = ""
            for word in text.split(","):
                name = word
                await ctx.message.author.edit(nick=name)


@Zendox.command()
async def boom(ctx):
        list = (
            "```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
            "💣",
            "💥",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@Zendox.command()
async def afk(ctx, mins):
    current_nick = ctx.author.nick
    await ctx.send(f"{ctx.author.mention} has gone afk for {mins} minutes.")
    await ctx.author.edit(nick=f"{ctx.author.name} [AFK]")

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} is no longer AFK")
            break





@Zendox.command()
async def stopnick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@Zendox.command()
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')












if __name__ == '__main__':
    Init()
