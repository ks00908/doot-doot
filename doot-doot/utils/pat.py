import random
import json

# This imports messages which will be used by a bot for the hug command

with open("./utils/pat-assets/pat_messages.json", "r", encoding="utf-8") as file:
    lovely_jubbly_content = json.load(file)


class pat:
    # actual method for hugs
    @staticmethod
    async def send_love(sender, the_being_loved_human):
        chosen_msg = random.choice(lovely_jubbly_content)
        chosen_msg = chosen_msg.replace('%%target%%', str(the_being_loved_human))
        chosen_msg = chosen_msg.replace('%%sender%%', str(sender))
        return chosen_msg
