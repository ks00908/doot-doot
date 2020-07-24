[![Maintainability](https://api.codeclimate.com/v1/badges/347e0974b306643c3f82/maintainability)](https://codeclimate.com/github/ks00908/doot-doot/maintainability) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![python3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://img.shields.io/badge/python-3.7-blue.svg) [![python3.7](https://img.shields.io/badge/Verified%20bot%3F-Yes-brightgreen?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgPHBhdGggZmlsbD0iIzNlNzBkZCIgZD0iTTIxLjU4IDExLjRMMTcuMyA0LjAxbC0uMzUtLjZINy4wNGwtLjM1LjYtNC4yNyA3LjM5LS4zNS42LjM1LjYgNC4yNyA3LjM5LjM1LjZoOS45MmwuMzUtLjYgNC4yOC03LjM5LjM1LS42LS4zNi0uNnpNOC41MSAxMC4zN0w2Ljg4IDEybDEuNjMgMS42M3YyLjczTDQuMTUgMTJsNC4zNy00LjM3djIuNzR6bTMuMTIgNi45M2wtMi4wNC0uNjMgMy4xLTkuOTggMi4wNC42NC0zLjEgOS45N3ptMy44Ni0uOTN2LTIuNzNMMTcuMTIgMTJsLTEuNjMtMS42M1Y3LjYzTDE5Ljg1IDEybC00LjM2IDQuMzd6Ii8+CiAgPHBhdGggZmlsbD0ibm9uZSIgZD0iTTAgMGgyNHYyNEgweiIvPgo8L3N2Zz4=)](https://support.discord.com/hc/en-us/articles/360040720412)
# DootDoot
A Discord bot that plays sound effects in voice channels on request


## Installation

### Requirements:
  * Python 3.7
  * Discord.py rewrite library
  * aiohttp library
  * Lavalink library (for YouTube support)
  * A Discord Bot account with its token (obtainable via the [Discord Developer Portal](https://discord.com/developers/applications/))
  
### Starting the bot:
  1. Make sure you correctly have installed all elements mentioned above
  2. Copy the bot files to the location where you want to store them
  3. Replace 'token' in ``main.py`` with your bot token
  4. Open CMD/PowerShell/Terminal and navigate to the folder with the files
  5. Type ``python main.py`` (if it doesn't work, try using ``python3.7 main.py``.)
  6. Wait for the bot to log in
  
  
## Adding new sound effects
Replace ``command_syntax`` with the command used to play the sound (e.g, *clap*) and ``file_name`` with the filename of the sound you'd like to add.

### Syntax
```py
    @commands.command()
    @commands.guild_only()
    async def command_syntax(self, ctx):
        """command_description"""
        await play_file(ctx, "sounds/file_name.mp3")
```
## Attributions
Our assets (such as the bot avatar or the support server icon) were created by Freepik using www.flaticon.com and are under a Creative Commons BY 3.0 licence.


## Verification

### Regarding Discord Bot Verification Program ([?](https://support.discord.com/hc/en-us/articles/360040720412))
Self hosted versions of our bot ("DootDoot") may **NOT** apply to the Discord Bot Verification progam. Specific exclusions of this rule can be requested by emailing us at dootdootbot@protonmail.com.

You might be wondering why we do not allow bot clones to be verified, and we have a simple answer. We want to keep the authenticity of the bot for it to not be lost in the plenty of clones there is out there, which would otherwise make it harder to find the official and original bot (DootDoot#2442).
However, contacting us via our [email address](dootdootbot@protonmail.com) gives you the chance to explain your case, and as long as it is reasonable, we will most likely allow you to apply on the program.

### Privacy

Any verification request will be saved on our email inbox, which is only accessible to the owner of this repository. Emails are stored on Protonmail's servers, you can learn more by reading their privacy policy on this [site](https://protonmail.com/privacy-policy).

**Note:** Please do not contact us on Discord about verification requests, you will be redirected to the aforementioned email adress for logging purposes explained above.
