import os
from pyrogram.types import KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton,WebAppInfo,ReplyKeyboardMarkup

#get from https://my.telegram.org/auth
API_ID:int =(os.environ.get("API_ID",15191874"))))
API_HASH:str = os.environ.get("API_HASH", "3037d39233c6fad9b80d83bb8a339a07")
BOT_TOKEN:str = os.environ.get("BOT_TOKEN", "6420356438:AAEZCItHjzerPRBpHYUTP9746Gbc4DrPIB0")





REFER_BONUS=int(1)
NEW_USER_BONUS=int(1)
#minimum withdrawal amount
WITHDRAWAL=int(2) 


#username without @
UPDATE_CHNL:str = os.environ.get("UPDATE_CHNL", "jn_bots")
SUPPORT_GRP:str = os.environ.get("SUPPORT_GRP", "-1002195994803")

#get it from @username_to_id_bot this bot 

log_channel = int(os.environ.get("LOG_CHANNEL", "-1001918482012"))
OWNER_ID=5597521952


# search on youtube "how to create mongodburl""

MONGO_DB_URI:str = os.environ.get(
    "MONGO_DB_URI",
    "")
	

# all channels list you can add more 
links = ["https://t.me/jn_bots", "https://t.me/jn_family", "https://t.me/channel3"]













INR_IMG="https://graph.org/file/591e034f3ebaca25e0692.jpg"
START_IMG= "https://graph.org/file/877838e68ea8e3099f343.jpg"
start_img2="https://graph.org/file/e1f08dea685a9051b264c.jpg"
photo="https://graph.org/file/8e2df166f47509590c88e.jpg"
deposit_IMG="https://graph.org/file/d46f6efe8fe5c991491ed.jpg"



                


main_button = ReplyKeyboardMarkup(
        [
            [KeyboardButton("🪪 ᴍʏ ᴘʀᴏꜰɪʟᴇ"), KeyboardButton("🤑 ꜰʀᴇᴇ ᴍᴏɴᴇʏ 🤑")],
            [KeyboardButton("⚡️ ᴡɪᴛʜᴅʀᴀᴡᴀʟ ⚡️")], 
            [KeyboardButton("ᴄʀᴇᴀᴛᴏʀ 😉", web_app=WebAppInfo(url="https://jnbots.netlify.app"))]
        ],
        resize_keyboard=True
    )

all_platform = ReplyKeyboardMarkup(
        [
        [KeyboardButton("⚽️ ꜰᴏᴏᴛʙᴀʟʟ "), KeyboardButton("ᴅɪᴄᴇ ɢᴀᴍᴇ 🥳")],
            [KeyboardButton("❤️‍🔥 ʀᴇꜰᴇʀ ᴀɴᴅ ᴇᴀʀɴ")],
            [ KeyboardButton("〄 ᴍᴀɪɴ ᴍᴇɴᴜ 〄")]
        ],
        resize_keyboard=True
    )
    
    
    
    

