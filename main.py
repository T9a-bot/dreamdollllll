from highrise import BaseBot
from highrise import __main__
from collections import UserDict
from asyncio import run as arun
from highrise.models import SessionMetadata, User
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
from highrise import BaseBot, User, Position, SessionMetadata
import random
import asyncio
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import *
from highrise.models import *
import time
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (AnchorPosition, CurrencyItem,Item,Position,SessionMetadata,User,)

emote_list : list[tuple[str, str]] = [('Sleep', 'idle-sleep'), ('Singalong', 'idle_singing'), ('Greedy', 'emote-greedy'), ('Snow', 'emote-snowball'), ('Teleport', 'emote-teleporting'), ('Swordfight', 'emote-swordfight'), ('Pennywise', 'dance-Pennywise'), ('Telekinesis', 'emote-telekinesis'), ('Pose8', 'emote-pose8'), ('Pose7', 'emote-pose7'), ('Pose3', 'emote-pose3'), ('Pose5', 'emote-Pose5'), ('Flex', 'emoji-flex'), ('Gagging', 'emoji-gagging'), ('Maniac', 'emote-maniac'), ('Snake', 'emote-snake'), ('Frog', 'emote-frog'), ('Superpose', 'emote-superpose'), ('Cute', 'emote-cute'), ('Weird', 'dance-weird'), ('Icescream', 'dance-icescream'), ('Gravity', 'emote-gravity'), ('Fashion', 'emote-fashionista'), ('Uwu', 'idle-uwu'), ('Sayso', 'idle-dance-tiktok4'), ('Tiktok10', 'dance-tiktok10'), ('Anime', 'dance-anime'), ('Bashful', 'emote-shy2'), ('Pouty', 'idle-sad'), ('Sleepy', 'idle-loop-tired'), ('Sit', 'idle-loop-sitfloor'), ('Shy', 'idle-loop-shy'), ('Enthused', 'idle-enthusiastic'), ('Feel The Beat', 'idle-dance-headbobbing'), ('Yes', 'emote-yes'), ('The Wave', 'emote-wave'), ('Tired', 'emote-tired'), ('Think', 'emote-think'), ('Theatrical', 'emote-theatrical'), ('Snowangel', 'emote-snowangel'), ('Shy', 'emote-shy'), ('Sad', 'emote-sad'), ('Peace', 'emote-peace'), ('No', 'emote-no'), ('Model', 'emote-model'), ('Flirty', 'emote-lust'), ('Amused', 'emote-laughing2'), ('Laugh', 'emote-laughing'), ('Kiss', 'emote-kiss'), ('Super Kick', 'emote-kicking'), ('Jump', 'emote-jumpb'), ('Judo Chop', 'emote-judochop'), ('Hot', 'emote-hot'), ('Hello', 'emote-hello'), ('Happy', 'emote-happy'), ('Face Palm', 'emote-exasperatedb'), ('Exasperated', 'emote-exasperated'), ('Collapse', 'emote-death2'), ('Revival', 'emote-death'), ('Dab', 'emote-dab'), ('Curtsy', 'emote-curtsy'), ('Confusion', 'emote-confused'), ('Cold', 'emote-cold'), ('Charging', 'emote-charging'), ('Bunny Hop', 'emote-bunnyhop'), ('Bow', 'emote-bow'), ('Boo', 'emote-boo'), ('Home Run!', 'emote-baseball'), ('Falling Apart', 'emote-apart'), ('Thumbs Up', 'emoji-thumbsup'), ('Point', 'emoji-there'), ('Sneeze', 'emoji-sneeze'), ('Smirk', 'emoji-smirking'), ('Sick', 'emoji-sick'), ('Gasp', 'emoji-scared'), ('Punch', 'emoji-punch'), ('Stunned', 'emoji-dizzy'), ('Cursing', 'emoji-cursing'), ('Sob', 'emoji-crying'), ('Clap', 'emoji-clapping'), ('Raise', 'emoji-celebrate'), ('Arrogance', 'emoji-arrogance'), ('Angry', 'emoji-angry'), ('Vogue Hands', 'dance-voguehands'), ('Savage', 'dance-tiktok8'), ("Dontstartnow", 'dance-tiktok2'), ('Yoga Flow', 'dance-spiritual'), ("Shopping", 'dance-shoppingcart'), ('Russian', 'dance-russian'), ('Macarena', 'dance-macarena'), ('Blackpink','dance-blackpink'),]


emote_durations = { 
    "Sleep": 15,
    "Pouty": 10,
    "Sleepy": 10,
    "Sit": 15,
    "Shy": 15,
    "Enthused": 15,
    "Feel The Beat": 15,
    "Yes": 4,
    "The Wave": 3,
    "Tired": 5,
    "Think": 5,
    "Theatrical": 10,
    "Snowangel": 7,
    "Sad": 5,
    "Peace": 6,
    "No": 4,
    "Model": 7,
    "Flirty": 5,
    "Amused": 10,
    "Laugh": 4,
    "Kiss": 4,
    "Jump": 10,
    "Judo Chop": 6,
    "Hot": 6,
    "Hello": 4,
    "Happy": 4,
    "Face Palm": 10,
    "Exasperated": 10,
    "Collapse": 10,
    "Dab": 10,
    "Curtsy": 3,
    "Confusion": 10,
    "Cold": 10,
    "Charging": 9,
    "Bunny Hop": 10,
    "Bow": 4,
    "Boo": 10,
    "Falling Apart": 10,
    "Thumbs Up": 4,
    "Point": 10,
    "Sneeze": 10,
    "Smirk": 10,
    "Sick": 10,
    "Stunned": 10,
    "Cursing": 10,
    "Clap": 10,
    "Raise": 10,
    "Angry": 10,
    "Savage": 10,
    "Dontstartnow": 10,
    "Yoga Flow": 10,
    "Shopping": 10,
    "Russian": 10,
    "Macarena": 10,
    "Blackpink": 10,
    "Bashful": 9, 
    "Anime": 10,
    "Tiktok10": 10,
    "Sayso": 8,
    "Uwu": 10,
    "Fashion": 10, 
    "Gravity": 10,
    "Icescream": 10,
    "Weird": 10,
    "Cute": 10,
    "Superpose": 10,
    "Frog": 10,
    "Snake": 10,
    "Maniac": 6,
    "Gagging": 10,
    "Flex": 10,
    "Pose5": 10,
    "Pose3": 10,
    "Pose7": 10,
    "Pose8": 10,
    "Telekinesis": 10,
    "Pennywise": 10,
    "Teleport": 10,
    "Swordfight": 10,
    "Snow": 10,
    "Greedy": 10,
    "Singalong": 10,    

}
class BotDefinition:
  def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token


class MyBot(BaseBot):


  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.following_user = None
    self.banned_users = {}
    self.following_username = None
    super().__init__()
    self.user_positions = {}

  async def on_user_move(self, user: User, pos: Position) -> None:
     self.user_positions[user.username] = pos
     print (f"{user.username} moved to {pos}")

 
  async def on_whisper(self, user: User, message: str):
    if user.username == "T9s":
      await self.highrise.chat(message)

  async def teleport_user_next_to(self, target_username: str,requester_user: User):

    room_users = await self.highrise.get_room_users()
    requester_position = None
    
    for user, position in room_users.content:
      if user.id == requester_user.id:
          requester_position = position
          break
    for user, position in room_users.content:
      if user.username.lower() == target_username.lower():
          z = requester_position.z
          new_z = z + 1
        
          user_dict = {
            "id":
            user.id,
            "position":
            Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
          }
          await self.highrise.teleport(user_dict["id"], user_dict["position"])

  async def on_user_join(self, user: User, position: Position | AnchorPosition):
        room_users = await self.highrise.get_room_users()
        if any(room_user.id == user.id for room_user, _ in room_users.content):
            try:
                await self.highrise.send_whisper(user.id,
                    f"Welcome to Find Love {user.username}"
                )
                await self.highrise.send_whisper(
                    user.id,
                    f"{user.username}, for emotes type !help"
                )
            except Exception as e:
                print(f"Failed to send whisper: {e}")

  async def run(self, room_id, token):
    definitions = [BotDefinition(self, room_id, token)]
    await __main__.main(definitions)

  async def loop(self: BaseBot, user: User, message: str) -> None:
    async def loop_emote(self: BaseBot, user: User, emote_name: str) -> None:
        emote_id = ""
        for emote in emote_list:
            if emote[0].lower() == emote_name.lower():
                emote_id = emote[1]
                break
        if emote_id == "":
            await self.highrise.chat("Invalid emote")
            return

        await self.highrise.chat(f"@{user.username} is looping {emote_name}")

        # الحصول على مدة الرقصة
        emote_duration = emote_durations.get(emote_name)
        if emote_duration is None:
            await self.highrise.chat(f"The emote {emote_name} does not have a specified duration.")
            return

        while True:
            try:
                await self.highrise.send_emote(emote_id, user.id)
            except:
                await self.highrise.chat(f"Sorry, @{user.username}, this emote isn't free or you don't own it.")
                return

            # فترة انتظار لمدة الرقصة
            await asyncio.sleep(emote_duration)

            room_users = (await self.highrise.get_room_users()).content
            user_in_room = False
            for room_user, position in room_users:
                if room_user.id == user.id:
                    user_in_room = True
                    break
            if not user_in_room:
                break

    try:
        splited_message = message.split(" ")
        # The emote name is every string after the first one
        emote_name = " ".join(splited_message[1:])
    except:
        await self.highrise.chat("Invalid command format. Please use '/loop <emote name>.")
        return
    else:   
        taskgroup = self.highrise.tg
        task_list: list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_name() == user.username:
                # Removes the task from the task group
                task.cancel()

        room_users = (await self.highrise.get_room_users()).content
        user_list = [room_user.username for room_user, pos in room_users]

        taskgroup.create_task(coro=loop_emote(self, user, emote_name))
        task_list: list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_coro().__name__ == "loop_emote" and task.get_name() not in user_list:
                task.set_name(user.username)

  async def stop_loop(self: BaseBot, user: User, message: str) -> None:
    taskgroup = self.highrise.tg
    task_list: list[Task] = list(taskgroup._tasks)
    for task in task_list:
        print(task.get_name())
        if task.get_name() == user.username:
            task.cancel()
            await self.highrise.chat(f"Stopping your emote loop, {user.username}!")
            return
    await self.highrise.chat(f"You're not looping any emotes, {user.username}")
    return

  async def on_chat(self, user: User, message: str):
    if message.lower().startswith("loop"):
      await self.loop(user, message)
    elif message.lower().startswith("stop loop"):
      await self.stop_loop(user, message)

    if message.startswith("!to"):
      words = message.split(" ")
      if len(words) > 1:
          target_username = words[1].replace("@", "")
          if target_username in self.user_positions:
              target_position = self.user_positions[target_username]
              await self.highrise.teleport(user.id, target_position)
              await self.highrise.chat(f"You have been pulled to {target_username}")
          else:
              await self.highrise.chat("User not found.")
      else:
          await self.highrise.chat("Username must be specified.")

    if message.startswith("!come") and user.username in ["T9s", "dreamdollllll"]:
      response = await self.highrise.get_room_users()
      your_pos = None
      for content in response.content:
        if content[0].id == user.id:
          if isinstance(content[1], Position):
            your_pos = content[1]
            break
      if not your_pos:
        await self.highrise.send_whisper(user.id, f"احداثيات غير صالحه")
        return
      await self.highrise.chat("I,m coming ")
      await self.highrise.walk_to(your_pos)

    if message == "1st":
      await self.highrise.teleport(user.id, Position(13.5, 0.0, 19.5))

    if message == "2nd":
      await self.highrise.teleport(user.id, Position(15.0, 7.25, 21.5))

    if message == "3rd":
      await self.highrise.teleport(user.id, Position(15.5, 14.5, 20.0))

    
    if message.startswith("Float"):
      await self.highrise.send_emote("emote-float", user.id)
    if message.startswith("Tiktok2"):
      await self.highrise.send_emote("dance-tiktok2", user.id)
    if message.startswith("pose1"):
      await self.highrise.send_emote("emote-pose1", user.id)
    if message.startswith("Russian"):
      await self.highrise.send_emote("dance-russian", user.id)
    if message.startswith("Sing"):
      await self.highrise.send_emote("idle_singing", user.id)
    if message.startswith("Enth"):
      await self.highrise.send_emote("idle-enthusiastic", user.id)
    if message.startswith("Casual"):
      await self.highrise.send_emote("idle-dance-casual", user.id)
    if message.startswith("sit"):
      await self.highrise.send_emote("idle-loop-sitfloor", user.id)
    if message.startswith("Lust"):
      await self.highrise.send_emote("emote-lust", user.id)
    if message.startswith("Creedy"):
      await self.highrise.send_emote("emote-greedy", user.id)
    if message.startswith("Bow"):
      await self.highrise.send_emote("emote-bow", user.id)
    if message.startswith("Curtsy"):
      await self.highrise.send_emote("emote-curtsy", user.id)
    if message.startswith("Snow"):
      await self.highrise.send_emote("emote-snowball", user.id)
    if message.startswith("Angel"):
      await self.highrise.send_emote("emote-snowangel", user.id)
    if message.startswith("Confused"):
      await self.highrise.send_emote("emote-confused", user.id)
    if message.startswith("Teleport"):
      await self.highrise.send_emote("emote-teleporting", user.id)
    if message.startswith("Swordfight"):
      await self.highrise.send_emote("emote-swordfight", user.id)
    if message.startswith("Energy"):
      await self.highrise.send_emote("emote-energyball", user.id)
    if message.startswith("Tiktok8"):
      await self.highrise.send_emote("dance-tiktok8", user.id)
    if message.startswith("Blackpink"):
      await self.highrise.send_emote("dance-blackpink", user.id)
    if message.startswith("Model"):
      await self.highrise.send_emote("emote-model", user.id)
    if message.startswith("Penny"):
      await self.highrise.send_emote("dance-pennywise", user.id)
    if message.startswith("Tiktok10"):
      await self.highrise.send_emote("dance-tiktok10", user.id)
    if message.startswith("Telekinesis"):
      await self.highrise.send_emote("emote-telekinesis", user.id)
    if message.startswith("Hot"):
      await self.highrise.send_emote("emote-hot", user.id)
    if message.startswith("Weird"):
      await self.highrise.send_emote("dance-weird", user.id)
    if message.startswith("Pose7"):
      await self.highrise.send_emote("emote-pose7", user.id)
    if message.startswith("Pose8"):
      await self.highrise.send_emote("emote-pose8", user.id)
    if message.startswith("Pose3"):
      await self.highrise.send_emote("emote-pose3", user.id)
    if message.startswith("Pose5"):
      await self.highrise.send_emote("emote-pose5", user.id)
    if message.startswith("kiss"):
      await self.highrise.send_emote("emote-kiss", user.id)

    if message.startswith("Laughing"):
      await self.highrise.send_emote("emote-laughing", user.id)
    if message.startswith("cursing"):
      await self.highrise.send_emote("emoji-cursing", user.id)
    if message.startswith("flex"):
      await self.highrise.send_emote("emoji-flex", user.id)
    if message.startswith("gagging"):
      await self.highrise.send_emote("emoji-gagging", user.id)
    if message.startswith("celebrate"):
      await self.highrise.send_emote("emoji-celebrate", user.id)
    if message.startswith("macarena"):
      await self.highrise.send_emote("dance-macarena", user.id)
    if message.startswith("charging"):
      await self.highrise.send_emote("emote-charging", user.id)
    if message.startswith("shopp"):
      await self.highrise.send_emote("dance-shoppingcart", user.id)
    if message.startswith("maniac"):
      await self.highrise.send_emote("emote-maniac", user.id)
    if message.startswith("snake"):
      await self.highrise.send_emote("emote-snake", user.id)
    if message.startswith("frog"):
      await self.highrise.send_emote("emote-frog", user.id)
    if message.startswith("superpose"):
      await self.highrise.send_emote("emote-superpose", user.id)
    if message.startswith("cute"):
      await self.highrise.send_emote("emote-cute", user.id)
    if message.startswith("tiktok9"):
      await self.highrise.send_emote("dance-tiktok9", user.id)
    if message.startswith("weird"):
      await self.highrise.send_emote("dance-weird", user.id)
    if message.startswith("cutey"):
      await self.highrise.send_emote("emote-cutey", user.id)
    if message.startswith("punkguitar"):
      await self.highrise.send_emote("emote-punkguitar", user.id)
    if message.startswith("zombierun"):
      await self.highrise.send_emote("emote-zombierun", user.id)
    if message.startswith("fashi"):
      await self.highrise.send_emote("emote-fashionista", user.id)
    if message.startswith("gravity"):
      await self.highrise.send_emote("emote-gravity", user.id)
    if message.startswith("icecream"):
      await self.highrise.send_emote("dance-icecream", user.id)
    if message.startswith("wrong"):
      await self.highrise.send_emote("dance-wrong", user.id)
    if message.startswith("uwu"):
      await self.highrise.send_emote("idle-uwu", user.id)
    if message.startswith("tiktok4"):
      await self.highrise.send_emote("idle-dance-tiktok4", user.id)
    if message.startswith("shy2"):
      await self.highrise.send_emote("emote-shy2", user.id)
    if message.startswith("anime"):
      await self.highrise.send_emote("dance-anime", user.id)

    if message.lower().startswith("!dancelist"):
      dance_list = [
          "Float",
          "Tiktok2",
          "pose1",
          "Russian",
          "Sing",
          "Enth",
          "Casual",
          "sit",
          "Lust",
          "Creedy",
          "Bow",
          "Curtsy",
          "Snow",
          "Angel",
          "Confused",
          "Teleport",
          "Swordfight",
          "Energy",
      ]

      # Convert the list to a comma-separated string
      dance_list_str = ", ".join(dance_list)

      # Send the message
      await self.highrise.send_whisper(user.id, dance_list_str)

    if message.lower().startswith("!dancelist"):
      await self.highrise.send_whisper(
          user.id,
          "Model , Penny , Tiktok10 , Telekinesis , Hot , Weird , Pose7 , Pose8 , Pose3 , Pose5 , kis , Laughing , cursing , flex , gagging , Blackpink , Tiktok8"
      )

   

    
    if message.lower().startswith("!dancelist"):
      await self.highrise.send_whisper(
          user.id,
          " celebrate , macarena , charging , shopp , maniac , snake  , frog , superpose , cute , tiktok9 , weird , cutey ,  punkguitar , zombierun , fashi , gravity , icecream , wrong , uwu , tiktok4 , shy2 , anime"
      )

    if message.lower().startswith("!looplist"):
      await self.highrise.send_whisper(
          user.id,
          "Sleep, Pouty, Sleepy, Sit, Shy, Enthused, Feel The Beat, Yes, The Wave, Tired, Think, Theatrical, Snowangel, Sad, Peace, No, Model, Flirty, Amused, Laugh, Kiss, Jump, Judo Chop"
      )

    if message.lower().startswith("!looplist"):
      await self.highrise.send_whisper(
          user.id,
          "Hot, Hello, Happy, Face Palm, Exasperated, Collapse, Dab, Confusion, Cold, Charging, Bunny Hop, Bow, Boo, Falling Apart, Thumbs Up, Point, Sneeze, Smirk, Sick, Stunned, Cursing, Clap, Raise"
      )

    if message.lower().startswith("!looplist"):
      await self.highrise.send_whisper(
          user.id,
          "Angry, Savage, Dontstartnow, Yoga Flow, Shopping, Russian, Macarena, Blackpink, Bashful, Anime, Tiktok10, Sayso, Uwu, Fashion, Gravity, Icescream, Weird, Cute, Superpose, Frog, Snake, Gagging, Flex, Pose5, Pose3, Pose7, Pose8, Telekinesis, Pennywise, Teleport, Swordfight, Snow, Greedy, Singalong"
      )

    if message.lower().startswith("!help"):
      await self.highrise.send_whisper(
          user.id,
          "For dances > !dancelist  \n For loop > !looplist \n For teleport > !to @user \n To transport yourself > 1st , 2nd , 3rd "
      )