import os


class Config:

   API_ID = int(os.getenv("API_ID", "23962364"))
   API_HASH = os.getenv("API_HASH", "cbc4406919096bc5c6ae8722b0c60732")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7190413281:AAGjRpoPVqo40z4B_9Qpo-DmsasBMLJYZt0")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "EfuMusic")
   OWNER_NAME = os.environ.get("OWNER_NAME", "Feridoffical") 
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "EfuMusicPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002098118049"))
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Ferid")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/c34c2d05ce742278154cf.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/c34c2d05ce742278154cf.jpg")    
