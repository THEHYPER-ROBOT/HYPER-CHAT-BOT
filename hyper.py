from pyrogram import Client, filters, idle
from pyrogram.types import *
from pymongo import MongoClient
from pyrogram import enums
import requests
import random
import os
import re


API_ID = os.environ.get("API_ID", "21134445") 
API_HASH = os.environ.get("API_HASH", "231c18ea7273824491d6bf05425ab74e") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "none") 
MONGO_URL = os.environ.get("MONGO_URL", "none")
BOT_IMAGE = os.environ.get("BOT_IMAGE", "none")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "none")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "@THEHYPER_ACX")
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "none")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "none")


bot = Client(
    "Nobita_Chat_Bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.get_chat_members(
            chat_id, filter="administrators"
        )
    ]


@bot.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐢  𝐈'𝐦 𝐀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷.\n\n📌 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 𝐍𝐨𝐛𝐢𝐭𝐚 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷 𝐅𝐨𝐫𝐦 𝐈𝐧𝐝𝐢𝐚 🇮🇳 \n\n🌷 𝐈'𝐦 𝐀 𝐀𝐫𝐭𝐢𝐟𝐢𝐜𝐢𝐚𝐥 𝐈𝐧𝐭𝐞𝐥𝐥𝐢𝐠𝐞𝐧𝐜𝐞 🌷\n\n /chatbot - [on|off] 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐔𝐬𝐞 𝐎𝐧𝐥𝐲 𝐀𝐧𝐲 𝐆𝐫𝐨𝐮𝐩

┏━━━━━━━━━━━━━━━━━┓
┣❥︎ ♕︎𝐎𝐰𝐧𝐞𝐫♕︎   » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/{OWNER_USERNAME})
┣❥︎ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/NOBITA_MUSIC_SUPPORT)
┣❥︎ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/+sIl5s2_0xvAyMjhl)
┣❥︎ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 ➪ » [𝚴 𝐎 𝐁 𝚰 𝐓 𝚲](https://t.me/ll_YOURR_NOBITA_ll)
┗━━━━━━━━━━━━━━━━━┛

💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐂𝐡𝐚𝐭.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Bᴀʙʏ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@bot.on_message(filters.command(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#nobita", "#nobita"]) & filters.group)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""Hɪ! I ᴀᴍ ᴀ Aᴅᴠᴀɴᴄᴇ Cʜᴀᴛ Bᴏᴛ 🌷.\n\n📌 Mʏ Nᴀᴍᴇ Is Hʏᴘᴇʀ Cʜᴀᴛ Bᴏᴛ🌷 Fʀᴏᴍ Iɴᴅɪᴀ🇮🇳 \n\n🌷 I ᴀᴍ ᴀ ᴀʀᴛɪғɪᴄɪᴀʟʟʏ Iɴᴛᴇʟʟɪɢᴇɴᴛ ʟɪᴋᴇ ᴀ Hᴜᴍᴀɴ 🌷\n\nAɴʏ Pʀᴏʙʟᴇᴍ Tᴏ [Rᴇᴘᴏʀᴛ 🥀](https://t.me/ACX_OWNER_DM_ROBOT)  🥀\n\n[Uᴘᴅᴀᴛᴇs ✨️](https://t.me/ACXBOTZ_UPDATE) 🌷\n\n /chatbot - [on|off]""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Jᴏɪɴ Oᴜʀ Cʜᴀᴛ Gʀᴏᴜᴘ 🥀", url=f"https://t.me/ACX_DISCUSSION")
                ]
            ]
        ),
    )



@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "Hᴀʏ Dᴜᴅᴇ Yᴏᴜ Aʀᴇ Nᴏᴛ A ᴀᴅᴍɪɴ 😒"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:
        v.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"🌷 Hʏᴘᴇʀ Cʜᴀᴛ Bᴏᴛ Is Aʟʀᴇᴀᴅʏ Dɴᴀʙʟᴇ🥀!\n\nAɴʏ Pʀᴏʙʟᴇᴍ Tᴏ [Rᴇᴘᴏʀᴛ 🥀](https://t.me/{SUPPORT_GROUP})  🥀\n\n[Uᴘᴅᴀᴛᴇs ✨️](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        await message.reply_text(f"🌷Hʏᴘᴇʀ Cʜᴀᴛ Bᴏᴛ Is Aʟʀᴇᴀᴅʏ Dɴᴀʙʟᴇ 🥀!\n\nAɴʏ Pʀᴏʙʟᴇᴍ Tᴏ [Rᴇᴘᴏʀᴛ 🥀](https://t.me/{SUPPORT_GROUP})  🥀\n\n[Uᴘᴅᴀᴛᴇs ✨️](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:           
        await message.reply_text(f"💥 Hʏᴘᴇʀ Cʜᴀᴛ Bᴏᴛ Is Aʟʀᴇᴀᴅʏ Eɴᴀʙʟᴇ🌷!\n\nAɴʏ Pʀᴏʙʟᴇᴍ Tᴏ [Rᴇᴘᴏʀᴛ 🥀](https://t.me/ACX_OWNER_DM_ROBOT)  🥀\n\n[Uᴘᴅᴀᴛᴇs ✨️](https://t.me/ACXBOTZ_UPDATE) 🌷")
    if is_v:
        v.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"💥 Hʏᴘᴇʀ Cʜᴀᴛ Bᴏᴛ Is Eɴᴀʙʟᴇ 🌷!\n\nAɴʏ Pʀᴏʙʟᴇᴍ Tᴏ [Rᴇᴘᴏʀᴛ 🥀](https://t.me/ACX_OWNER_DM_ROBOT)  🥀\n\n[Uᴘᴅᴀᴛᴇs ✨️](https://t.me/ACXBOTZ_UPDATE) 🌷")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**🇮🇳 Usᴀɢᴇ 🌷 :**\n/chatbot [on|off] Oɴʟʏ Gʀᴏᴜᴘ 🇮🇳 !\n\nAɴʏ Pʀᴏʙʟᴇᴍ Tᴏ [Rᴇᴘᴏʀᴛ 🥀](https://t.me/ACX_DISCUSSION)🥀\n\n[Uᴘᴅᴀᴛᴇs ✨️](https://t.me/ACXBOTZ_UPDATE) 🌷")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                   
               await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                    
               await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
       
bot.start()
print("HYPER CHAT BOT BOOTED SUCCESSFULLY")
idle()
