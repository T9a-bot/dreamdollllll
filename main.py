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

  
  async def on_chat(self, user: User, message: str):


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

   

    
    if message.lower().startswith("!help"):
      await self.highrise.send_whisper(
          user.id,
          " celebrate , macarena , charging , shopp , maniac , snake  , frog , superpose , cute , tiktok9 , weird , cutey ,  punkguitar , zombierun , fashi , gravity , icecream , wrong , uwu , tiktok4 , shy2 , anime"
      )
