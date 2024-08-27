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
    "2": 15,
    "3": 10,
    "4": 10,
    "5": 15,
    "6": 15,
    "7": 15,
    "8": 15,
    "9": 4,
    "10": 3,
    "11": 5,
    "12": 5,
    "13": 10,
    "14": 7,
    "15": 5,
    "16": 6,
    "17": 4,
    "18": 7,
    "19": 5,
    "20": 10,
    "21": 4,
    "22": 4,
    "23": 10,
    "24": 6,
    "25": 6,
    "26": 4,
    "27": 4,
    "28": 10,
    "29": 10,
    "30": 10,
    "31": 10,
    "32": 3,
    "33": 10,
    "34": 10,
    "35": 9,
    "36": 10,
    "37": 4,
    "38": 10,
    "39": 10,
    "40": 4,
    "41": 10,
    "42": 10,
    "43": 10,
    "44": 10,
    "45": 10,
    "46": 10,
    "47": 10,
    "48": 10,
    "49": 10,
    "50": 10,
    "51": 10,
    "52": 10,
    "53": 10,
    "54": 10,
    "55": 10,
    "56": 10,
    "57": 9, 
    "58": 10,
    "59": 10,
    "60": 8,
    "61": 10,
    "62": 10, 
    "63": 10,
    "64": 10,
    "65": 10,
    "66": 10,
    "67": 10,
    "68": 10,
    "69": 10,
    "70": 6,
    "71": 10,
    "72": 10,
    "73": 10,
    "74": 10,
    "75": 10,
    "76": 10,
    "77": 10,
    "78": 10,
    "79": 10,
    "80": 10,
    "81": 10,
    "82": 10,
    "83": 10,    

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
        user_position = None
        user_in_room = False
        room_users = (await self.highrise.get_room_users()).content
        for room_user, position in room_users:
            if room_user.id == user.id:
                user_position = position
                start_position = position
                user_in_room = True
                break
        if user_position == None:
            await self.highrise.chat("User not found")
            return
        await self.highrise.chat(f"@{user.username} is looping {emote_name}")
        while start_position == user_position:
            try:
                await self.highrise.send_emote(emote_id, user.id)
            except:
                await self.highrise.chat(f"Sorry, @{user.username}, this emote isn't free or you don't own it.")
                return
            await asyncio.sleep(10)
            room_users = (await self.highrise.get_room_users()).content
            user_in_room = False
            for room_user, position in room_users:
                if room_user.id == user.id:
                    user_position = position
                    user_in_room = True
                    break
            if user_in_room == False:
                break
    try:
        splited_message = message.split(" ")
        
        emote_name = " ".join(splited_message[1:])
    except:
        await self.highrise.chat("Invalid command format. Please use '/loop <emote name>")
        return
    else:   
        taskgroup = self.highrise.tg
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_name() == user.username:
                # Removes the task from the task group
                task.cancel()

        room_users = (await self.highrise.get_room_users()).content
        user_list  = []
        for room_user, pos in room_users:
            user_list.append(room_user.username)

        taskgroup.create_task(coro=loop_emote(self, user, emote_name))
        task_list : list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_coro().__name__ == "loop_emote" and not (task.get_name() in user_list):
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

  async def on_user_join(self, user: User, position: Position | AnchorPosition):
        room_users = await self.highrise.get_room_users()
        if any(room_user.id == user.id for room_user, _ in room_users.content):
            try:
                await self.highrise.send_whisper(user.id,
                    f"Welcome {user.username},To 🇮🇳 INDIANS 🚩"
                )
                await self.highrise.send_whisper(
                    user.id,
                    f"{user.username}, for emotes type !help, or check bot for info"
                )
            except Exception as e:
                print(f"Failed to send whisper: {e}")

  async def run(self, room_id, token):
    definitions = [BotDefinition(self, room_id, token)]
    await __main__.main(definitions)

  async def teleport_user_next_to(self, target_username: str,
                                  requester_user: User):

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


  
  async def on_chat(self, user: User, message: str):
    
    if message.startswith("!come") and user.username in ["T9s", "JAVA32"]:
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

    allowed_users = [
        "T9s", "JAVA32", "_HYDRA_","TheezNuts","___ARKO___","MrNakhreBaaj","__JENNY","LEGENDBULL","NH28"
    ]
    if message.startswith("!summon") and user.username in [
        "T9s", "JAVA32", "_HYDRA_","TheezNuts","___ARKO___","MrNakhreBaaj","__JENNY","LEGENDBULL","NH28"
    ]:
      allowed_users = message.split("@")[-1].strip()
      if allowed_users in allowed_users:
        await self.teleport_user_next_to(allowed_users, user)

    if message.lower().startswith("!help"):
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

    if message.lower().startswith("!help"):
      await self.highrise.send_whisper(
          user.id,
          "Model , Penny , Tiktok10 , Telekinesis , Hot , Weird , Pose7 , Pose8 , Pose3 , Pose5 , kis , Laughing , cursing , flex , gagging , Blackpink , Tiktok8"
      )

    if message.startswith("!to"):
      words = message.split(" ")
      if len(words) > 1:
          target_username = words[1].replace("@", "")
          if target_username in self.user_positions:
              target_position = self.user_positions[target_username]
              await self.highrise.teleport(user.id, target_position)
              await self.highrise.chat(f"تم سحبك إلى موقع {target_username}")
          else:
              await self.highrise.chat("المستخدم غير موجود.")
      else:
          await self.highrise.chat("يجب تحديد اسم المستخدم.")

    
    if message.lower().startswith("!help"):
      await self.highrise.send_whisper(
          user.id,
          " celebrate , macarena , charging , shopp , maniac , snake  , frog , superpose , cute , tiktok9 , weird , cutey ,  punkguitar , zombierun , fashi , gravity , icecream , wrong , uwu , tiktok4 , shy2 , anime"
      )

    if message.lower().startswith("/loop1"):
      dance_list_part1 = [
          "0 = sleep",
          "2 = sad",
          "4 = sitfloor",
          "5 = shy",
          "6 = enthusiastic",
          "7 = headbobbing",
          "8 = wave",
          "9 = tired",
          "10 = think",
          "11 = theatrical",
          "12 = snowangel",
          "13 = shy",
          "14 = sad",
          "15 = peace",
          "16 = model",
          "17 = lust",
          "18 = laughing2",
          "19 = laughing",
          "20 = kiss",
      ]

      # تحويل القائمة إلى سلسلة نصية مفصولة بفواصل
      dance_list_str1 = ", ".join(dance_list_part1)

      # إرسال الرسالة
      await self.highrise.send_whisper(user.id, dance_list_str1)

    if message.lower().startswith("/loop2"):
      dance_list_part2 = [
          "21 Kick = kicking",
          "22 = jumpb",
          "23 = judochop",
          "24 Jetpack = jetpack",
          "25 = hot",
          "26 = hello",
          "27 = happy",
          "28 = exasperatedb",
          "29 = exasperated",
          "30 = death2",
          "31 = death",
          "32 = dab",
          "33 = curtsy",
          "34 = confused",
          "35 = cold",
          "36 = charging",
          "37 = bunnyhop",
          "38 = bow",
          "39 = boo",
          "40 = baseball",
      ]

      # تحويل القائمة إلى سلسلة نصية مفصولة بفواصل
      dance_list_str2 = ", ".join(dance_list_part2)

      # إرسال الرسالة
      await self.highrise.send_whisper(user.id, dance_list_str2)

    if message.lower().startswith("/loop3"):
      dance_list_part3 = [
          "41 = apart", "42 = thumbsup", "43 = there", "44 = sneeze",
          "45 = smirking", "46 = sick", "47 = scared", "48 = punch",
          "49 = dizzy", "50 = cursing", "51 = crying", "52 = clapping",
          "53 = celebrate", "54 = arrogance", "55 = angry", "56 = voguehands",
          "57 = tiktok8", "58 = tiktok2", "59 = spiritual",
          "60 = shoppingcart", "61 = russian", "62 = macarena",
          "63 = blackpink", "64 = enthusiastic"
      ]

      # تحويل القائمة إلى سلسلة نصية مفصولة بفواصل
      dance_list_str3 = ", ".join(dance_list_part3)

      # إرسال الرسالة
      await self.highrise.send_whisper(user.id, dance_list_str3)

    if message.lower().startswith("loop "):
      await self.loop(user, message)
    elif message.lower().startswith("stoploop"):
      await self.stop_loop(user, message)

    if message == "!1st":
      await self.highrise.teleport(user.id, Position(18.5, 0.0, 8.5))

    if message == "!2nd":
      await self.highrise.teleport(user.id, Position(12.0, 9.0, 8.5))

    if message == "!3rd":
      await self.highrise.teleport(user.id, Position(10.0, 18.0, 11.5))

    if message.lstrip().startswith('Move'):
      if user.username.lower() in ["t9s", "java32", "_hydra_","theeznuts","___arko___", "mrnakhrebaaj","__jenny","legendbull","nh28"]:
        response = await self.highrise.get_room_users()
        users = [content[0] for content in response.content]
        usernames = [user.username.lower() for user in users]

        parts = message[1:].split()
        args = parts[1:]

        if len(args) < 2:
          await self.highrise.send_whisper(user.id,"Use: Command > Name > Place ")
          return
        elif args[0][0] != "@":
          await self.highrise.send_whisper(user.id,f" Incorrect format  '@username'.  ")
          return
        elif args[0][1:].lower() not in usernames:
          await self.highrise.send_whisper(user.id,f"{args[0][1:]}Not in the room.")
          return

        position_name = " ".join(args[1:])
        if position_name == '!1st':
          dest = Position(18.5, 0.0, 8.5)

        elif position_name == '!2nd':
          dest = Position(12.0, 9.0, 8.5)

        elif position_name == '!3rd':
          dest = Position(10.0, 18.0, 11.5)

        else:
          return await self.highrise.send_whisper(user.id,f"  The site is wrong ")
        user_id = next(
            (u.id for u in users if u.username.lower() == args[0][1:].lower()),
            None)
        if not user_id:
          await self.highrise.send_whisper(user.id,f"User {args[0][1:]} unavailable ")
          return

        await self.highrise.teleport(user_id, dest)
        await self.highrise.send_whisper(
            user.id, f" move  {args[0][1:]} to ({dest.x}, {dest.y}, {dest.z})")
      else:
        await self.highrise.send_whisper(user.id, " You can't fix this ")
    else:
      pass
      
    