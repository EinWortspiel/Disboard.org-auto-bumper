class Auto_bumper:
    dev = "EinWortspiel 3#9998"
    github = "https://github.com/EinWortspiel" #There is also a discord Selfbot Base btw

#import ...
import discord
import asyncio
import colorama
import ctypes
import json
import os

#from ... import ...
from discord.ext import commands
from colorama import Fore, Style, init
from ctypes import * 
init()

#Important things from the config
with open("config.json", "r", encoding="UTF-8") as f:
    config = json.load(f)

token = config["token"]
prefix = config["prefix"]

#Bot configuration
intents = discord.Intents.all()
auto_dumper = commands.Bot(command_prefix = prefix, intents = intents, self_bot = True)

#Logo function
def logo():
    os.system("mode 190, 30")
    print(f"""{Fore.BLUE}{Style.BRIGHT}
██████╗ ██╗███████╗██████╗  ██████╗  █████╗ ██████╗ ██████╗     ██████╗ ██████╗  ██████╗      █████╗ ██╗   ██╗████████╗ ██████╗     ██████╗ ██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██║██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗   ██╔═══██╗██╔══██╗██╔════╝     ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ██║██║███████╗██████╔╝██║   ██║███████║██████╔╝██║  ██║   ██║   ██║██████╔╝██║  ███╗    ███████║██║   ██║   ██║   ██║   ██║    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║  ██║██║╚════██║██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║   ██║   ██║██╔══██╗██║   ██║    ██╔══██║██║   ██║   ██║   ██║   ██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██║███████║██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██╗╚██████╔╝██║  ██║╚██████╔╝    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║     ███████╗██║  ██║
╚═════╝ ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                                                                                                                                                                                                                                                                                                      
    \n""")
    print(f"{Fore.BLUE}{Style.BRIGHT}Disboard.org auto bumper made by {Auto_bumper.dev}\n")
    print(f"{Fore.BLUE}{Style.BRIGHT}Logged in as {auto_dumper.user.name}#{auto_dumper.user.discriminator} | {auto_dumper.user.id}\n")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Disboard.org Auto Bumper | Logged in as {auto_dumper.user} | Made by {Auto_bumper.dev}")

#on_connect event
@auto_dumper.event
async def on_connect():
    print(f"{Fore.BLUE}{Style.BRIGHT}Connected...")

#on_ready event
@auto_dumper.event
async def on_ready():
    logo()

#start cmd
@auto_dumper.command()
async def start(ctx, channel_id : int):
    await ctx.message.delete()
    try:
        dump_channel = auto_dumper.get_channel(int(channel_id))
    except:
        print(f"{Fore.BLUE}{Style.BRIGHT}Channel does not exist | Invalid Channel ID")
        return 
    else:
        while True:
            try:
                await dump_channel.send("!d bump")
                await asyncio.sleep(7200)
                print(f"{Fore.BLUE}{Style.BRIGHT}Bumped")
            except:
                pass

#Main | run | function
def main():
    try:
        auto_dumper.run(token, bot = False)
    except discord.LoginFailure:
        print(f"{Fore.BLUE}{Style.BRIGHT}Wrong Token! | Token does not exist")

#Call Main function
if __name__ == "__main__":
    main()