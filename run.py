from highrise.__main__ import *
import time

"""Bot Settings"""
room_id = "60fbb35c2dbe67b6963cb558"
bot_token = "05eb2a770a99255a56af5002d4cff7ccea0a584889f1f24b4b4bb2970346fe14"
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