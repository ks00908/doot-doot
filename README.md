[![Maintainability](https://api.codeclimate.com/v1/badges/347e0974b306643c3f82/maintainability)](https://codeclimate.com/github/ks00908/doot-doot/maintainability) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![python3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://img.shields.io/badge/python-3.7-blue.svg)
# Doot-Doot
A Discord bot that play sound effects in voice channel on command.


## Installation

### Prerequisites:
  * Python 3.7
  * Discord.py rewrite library
  * Discord bot account with token (obtainable through the [Discord Developer Portal](https://discordapp.com/developers/applications/))
  * aiohttp library
  * Lavalink library (For youtube support)
  
### Starting bot:
  1. Install pre-requisites
  2. Copy bot files to location where you want to store them
  3. Replace 'token' in main.py with token
  4. Open CMD/PowerShell/Terminal and navigate to folder with bot files
  5. Type ``python main.py`` (if it will not work try ``python3.7 main.py``
  6. Wait until bot logs in to Discord
  
  
## Adding new sound effects
Replace command_syntax and file_name respectively with: command used to play sound and filename of sound
### Syntax
```py
    @commands.command()
    @commands.guild_only()
    async def command_syntax(self, ctx):
        """command_description"""
        await play_file(ctx, "sounds/file_name.mp3")
```
## Attributions

Bot and support server images were created by Freepik from www.flaticon.com and are under Creative Commons BY 3.0 licence


## Verification

### Licence in regard of Bot Verification program
Self hosted versions of DootDoot bot are **NOT** permitted to be verified under Discord Bot verification progam. Specific exclusions of this rule can be requested by emailing bot creator at dootdootbot@protonmail.com 

This rule exists mainly so there isn't 500 versions of this bot circling around verified as it will make harder to find official bot, contacting me through email lets you make your case, and as long as its reasonable i am sure it will end in allowing you to verify bot

### Transparency

Any verification allowance request will be saved on email inbox and only owner of this repository will be able to see it. Record of interaction in form of emails will be stored on Protonmail servers which privacy policy is avaible under: https://protonmail.com/privacy-policy

Please do not contact me on discord regarding this as you will be sent to email adress anyway due to my requirement of paper trail of whole orderal.

