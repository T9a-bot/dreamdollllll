from highrise.__main__ import *
import time

"""Bot Settings"""
room_id = "660dd538c10e75a9112f9207"
bot_token = "2b01b9cb0531945fa37416568774cf0c9d0d8017c4737415849f67674407f031"
bot_file = "main"
bot_class = "MyBot"

if __name__ == "__main__":
  definitions = [
    BotDefinition(
      getattr(import_module(bot_file), bot_class)(),
      room_id, 
      bot_token)]  # More BotDefinition classes can be added to the definitions list
  while True:
    try:
      arun(main(definitions))
    except Exception as e:
      # Print the full traceback for the exception
      import traceback
      print("Caught an exception:")
      traceback.print_exc()  # This will print the full traceback       
      time.sleep(1)       
      continue