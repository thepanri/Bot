import telebot
import datetime
import time
import os, sys, re
import subprocess
import requests
import random
import io 
import zipfile
import html
import traceback
import json
import threading
from telebot.types import User
from gtts import gTTS
from bs4 import BeautifulSoup
from telebot import types
from translate import Translator
from telebot.types import ReactionTypeEmoji
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


bot_token = os.getenv("BOT_TOKEN")  # Lấy token từ biến môi trường
bot = telebot.TeleBot(bot_token)
#bot_token =  "7896551296:AAGVbUQpMzProDaMFg11M15vOVJRpP5w7JA" 

 
   # '7178812917:AAEUayKCUnt-iU0SWRdhUNt--6AssXaBaB0' # '7078161982:AAFrl7q2A-qyFWnhTOH1qBx66on-p2omtIg'   
openweathermap_api_key = 'a96625bdbdd9dca03d4f073780531e37'
bot = telebot.TeleBot(bot_token)
processes = []
ADMIN_ID = '7484921732'
themvip =[ '7484921732']
last_spam_time = {}
user_info = {}  # Dictionary to store user-specific info

shared_key = "TrHiepk7"
users = {}
is_active = True
GROUP_ID = [ 7484921732, -1002427257416, -1002422843821]
#, -1002103359217luz chat, -1002365599501 luz new

cccc = False

hieuung1 = '5107584321108051014' 
hieuung2 = '5104858069142078462'
hieuung3 = '5159385139981059251'
hieuung4 = '5104841245755180586'
hieuung5 = '5046509860389126442'
hieuung6 = '5046589136895476101'
#bot.reply_to(message, 'Hello!', message_effect_id = hieuung5  )

blocklist_dir = 'blocklist'
if not os.path.exists(blocklist_dir):
    os.makedirs(blocklist_dir)




#allowed_groups = [-1002059438762, , ... , ...]
#emojis = ['🔥', '🤡', '🤩', '😍', '❤️', '🎉', '💯', '🍻', '🏆']
# Command handler for /key <user_key>


#@bot.message_handler(commands=['free'])
#def free(message):
#    if len(message.text.split()) == 1:
#        bot.reply_to(message, '🙅 Bạn Chưa Lấy Key Ngày Hôm Nay. Vui Lòng Sử Dụng /getkey Để Lấy Key Và Dùng /key Để Nhập Key.')
#        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
#        return

#    user_key = message.text.split()[1]

#    if user_key == shared_key:
#        bot.reply_to(message, '⚡ Key Hợp Lệ. Bạn Đã Được Phép Sử Dụng Lệnh /free.')
#    else:
#        bot.reply_to(message, '❌ Key Không Hợp Lệ, Vui Lòng Xem Lại. Dùng /getkey Để Lấy Key !!!')
#        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
#        


# Command handler for /spam <user_key> <phone_number> <lap>
############# bỏ
@bot.message_handler(commands=['ndjdjdjud'])
def sp(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    if len(message.text.split()) < 4:
        bot.reply_to(message, ' <blockquote>❌ Thiếu Thông Tin. Vui Lòng Nhập Đầy Đủ: \n/sp [user_key] [phone_number] [lap] </blockquote>' , parse_mode='HTML', message_effect_id = hieuung5  )
        return

    user_key = message.text.split()[1]
    phone_number = message.text.split()[2]
    lap = message.text.split()[3]

    if user_key != shared_key:
        bot.reply_to(message, '⛔ Key Không Hợp Lệ, Vui Lòng Kiểm Tra Lại. Dùng /getkey Để Lấy Key !!!')
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    if not re.match(r"^\d{10}$", phone_number):
        bot.reply_to(message, '⛔ Số Điện Thoại Phải Đủ 10 Số !!!')
        return

    if not lap.isnumeric():
        bot.reply_to(message, "⛔ Số Lần Spam Vui Lòng Chỉ Nhập Số !!!")
        return

#    if not can_spam_again(phone_number):
#        bot.reply_to(message, '⏰ Vui Lòng Đợi 60s Trước Khi Spam Lại Số Này !!!')
    user_id = message.from_user.id
    current_time = time.time()
    if user_id in users:
        last_used_time = users[user_id]
        time_elapsed = current_time - last_used_time
        if time_elapsed < 60:
            remaining_time = 60 - int(time_elapsed)
            bot.reply_to(message, f'⏳ Vui Lòng Đợi {remaining_time}s Để Tiếp Tục Dùng Lệnh Này. ')
            return
    users[user_id] = current_time

    # Assuming you have SMS sending logic here
    # Replace this with your actual spam logic


    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
#    video_files = [f for f in os.listdir(video_folder_path) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
#    if not video_files:
#        bot.reply_to(message, '⛔ Không Tìm Thấy Video Nào Để Gửi.')
#        return
#    random_video = random.choice(video_files)
#    video_path = os.path.join(video_folder_path, random_video)
    
    bot.reply_to(message, f'⊂🚀⊃ Successful Attack ⊂🚀⊃\n↣ Bot 🤖:  \n↣ Số Tấn Công 📱: {phone_number}\n↣ Lặp Lại : {lap}\n↣ Thời Gian Chờ ⏳: 60s\n↣ Chủ Sở Hữu 👑: @trn_hwp2\n↣ Loại Spam : Free')
    ###########################
    




def TimeStamp():
    now = str(datetime.date.today())
    return now

def can_spam_again(phone_number):
    now = datetime.datetime.now()
    if phone_number in last_spam_time:
        last_time = last_spam_time[phone_number]
        if (now - last_time).total_seconds() < 60:
            return False
    last_spam_time[phone_number] = now
    return True 




#TẠO KEY
@bot.message_handler(commands=['getkey'])
def startkey(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Để Lấy Key Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 
    chat_id = message.chat.id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
#        
    #bot.reply_to(message, text='⏰ Vui Lòng Đợi Trong Giây Lát !!!')
    if is_active:
        bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('🎉')], is_big=True)
        time.sleep(0.5)
        message_id = bot.send_message(chat_id=chat_id, text='⏰ Vui Lòng Đợi Trong Giây Lát !!!').message_id
        key = str(int(message.from_user.id) * int(datetime.date.today().day) - (int(datetime.date.today().day))*3 - 1266)
        
        #key = f"{user_id}" + str(in
#    key_url = "https://tranhiep.x10.mx?key=" + key
#    api_token = 'a78d8bfaf599f40466aa15af00e4873b1d3d9c0a46ff9ecd989881954abbcb76'''

#    # Shorten the URL using yeumoney.com API
#    api_url = f'https://yeumoney.com/QL_api.php?token={api_token}&url={key_url}&format=json'
#    response = requests.get(api_url)
#    if response.status_code == 200:
#        user_id = message.from_user.id
#        first_name = message.from_user.first_name
#        url_data = response.json()
#        url_key = url_data.get('shortenedUrl', 'URL_SHORTENING_FAILED')



        text = f'''<blockquote>╭━━━━━━━━━━━━━╮
➯ Key Của {first_name}:
➯ <code>{key}</code>
➯ Sử Dụng /key &lt;key&gt;
➯ Ví Dụ: /key 123456789
╰━━━━━━━━━━━━━╯</blockquote>
        '''
        
    #else:
#        text = "Failed to shorten URL. Please try again later."
#ngày {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Là:
    #bot.reply_to(message, text, parse_mode='HTML')
        time.sleep(1)
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, parse_mode='HTML', disable_web_page_preview=True)
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 
        
        
emoji_list_yes = ["🥰", "👏",  "🎉", "🤩",  "👌", "😍", "❤‍🔥", "⚡",  "💋", "✍",  "😘", "😎"]
              
emoji_list_no = [ "🤬", "😢",
              "💩", "🙏","🤡", "💔", "😭", "😨",  "🤪", "🗿", 
              "🤷‍♂", "🤷", "🤷‍♀", "😡"]
              
#nhập KEY
@bot.message_handler(commands=['key'])
def keyy(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    chat_id = message.chat.id
    if is_active:
        if len(message.text.split()) == 1:
            bot.reply_to(message, ' <blockquote>📥 Vui Lòng Nhập Đúng Định Dạng: /key [key] !!\nNếu Chưa Lấy Key Vui Lòng Dùng /getkey !!</blockquote> ' , parse_mode='HTML' )
            return

        user_id = message.from_user.id
        first_name = message.from_user.first_name
        key = message.text.split()[1]
        username = message.from_user.username
        expected_key = str(int(message.from_user.id) * int(datetime.date.today().day) - (int(datetime.date.today().day))*3 - 1266)
       
   # bot.reply_to(message, f"Đã nhận key: {key}")
        message_id = bot.send_message(chat_id=chat_id, text="⏳ Đợi Xử Lý Key.").message_id     #{expected_key}")
        time.sleep(0.2)
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='⏳ Đợi Xử Lý Key..')
        time.sleep(0.2)
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='⏳ Đợi Xử Lý Key...')

        if key == expected_key:
            random_emoji_yes = random.choice(emoji_list_yes)
            bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji(random_emoji_yes)], is_big=True)
            time.sleep(0.2)
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='<blockquote>✅ Key Hợp Lệ. Bạn Đã Được Phép Sử Dụng Các Lệnh. \nNhập /help Để Xem Danh Sách Lệnh.</blockquote>', parse_mode='HTML')
            os.makedirs(f'./user/{datetime.date.today().day}', exist_ok=True)
            with open(f'./user/{datetime.date.today().day}/{user_id}.txt', "w") as fi:
                fi.write("")
        else:
            random_emoji_no = random.choice(emoji_list_no)
            bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji(random_emoji_no)], is_big=True)
            time.sleep(0.4)
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='<blockquote>❌ Key Không Hợp Lệ, Vui Lòng Xem Lại !!!</blockquote>', parse_mode='HTML')
           # chat_id = message.chat.id
            #if int(chat_id) not in GROUP_ID:
#            	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#            	return 
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 



#SPAM VIP
@bot.message_handler(commands=['spamvip'])
def superspam(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    if int(chat_id) not in GROUP_ID:
    	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    	return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./vip/{user_id}.txt"):
            bot.reply_to(message, '<blockquote>❌ Bạn Chưa Đăng ký Vip.\n↣ Vui Lòng Liên Hệ Admin Để Mua\n↣ Dùng /plan Để Xem Giá Gói Vip\n↣ Admin DUY NHẤT: <a href="tg://user?id=7484921732">TrHiep</a> </blockquote>', parse_mode='HTML')
            return
        with open(f"./vip/{user_id}.txt") as fo:
            data = fo.read().split("|")
        qua_khu = data[0].split('-')
        qua_khu = datetime.date(int(qua_khu[0]), int(qua_khu[1]), int(qua_khu[2]))
        ngay_hien_tai = datetime.date.today()
        so_ngay = int((ngay_hien_tai - qua_khu).days)
        if so_ngay < 0:
            bot.reply_to(message, ' <blockquote>📆 Key Vip Cài Vào Ngày Khác !!! </blockquote>' , parse_mode='HTML' )
            return
        if so_ngay >= int(data[1]):
            bot.reply_to(message, ' <blockquote>📆 Key Vip Hết Hạn Vui Lòng ib Admin !!! </blockquote>' , parse_mode='HTML' )
            os.remove(f"./vip/{user_id}.txt")
            return
        if len(message.text.split()) == 1:
            bot.reply_to(message, ' <blockquote>📱 Vui Lòng Nhập Số Điện Thoại !!! \nVí Dụ: \n/spamvip 0987654321 150</blockquote>' , parse_mode='HTML')
            return
        if len(message.text.split()) == 2:
            bot.reply_to(message, ' <blockquote>❌ Vui Lòng Nhập Số Lần Spam!!! \nVí Dụ: \n/spamvip 0987654321 150</blockquote>' , parse_mode='HTML' )
            return
        lap = message.text.split()[2]
        if lap.isnumeric():
            if not (int(lap) > 0 and int(lap) <= 150):
                bot.reply_to(message, " <blockquote>⚡ Vui Lòng Spam Trong Khoảng 1-150 Lần.Spam Nhiều Hơn T Cắn Chet. </blockquote>" , parse_mode='HTML' )
                return
        lap = message.text.split()[2]
        if not lap.isnumeric():
            bot.reply_to(message, " <blockquote>❌ Số Lần Spam Phải Là Số !!! </blockquote>" , parse_mode='HTML')
            
        phone_number = message.text.split()[1]
        if not re.match(r"^\d{10}$", phone_number):
            bot.reply_to(message, ' <blockquote>⛔ Số Điện Thoại Phải Đủ 10 Số !!! </blockquote>' , parse_mode='HTML' )
            return
        if phone_number in ["38384848362636"]:
            bot.reply_to(message, f'<pre>❓Thằng <a href="tg://user?id={user_id}">{first_name}</a> Spam Admin Làm Cặc Gì, Thích Mute À??\n\n🚨 @trn_hwp2</pre>' , parse_mode='HTML' )
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            return
        #if not can_spam_again(phone_number):
    #        bot.reply_to(message, '⏳ Vui Lòng Đợi 60s Trước Khi Spam Lại Số Này.')
        current_time = time.time()
        if user_id in users:
            last_used_time = users[user_id]
            time_elapsed = current_time - last_used_time
            if time_elapsed < 60:
                remaining_time = 60 - int(time_elapsed)
                bot.reply_to(message, f' <blockquote>⏳ <a href="tg://user?id={user_id}">{first_name}</a> Vui Lòng Đợi {remaining_time}s Để Có Thể Tiếp Tục Dùng Lệnh Spam. </blockquote>', parse_mode='HTML') 
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                return
        # Nếu người dùng chưa sử dụng lệnh hoặc đã qua 60 giây, cập nhật thời gian và thực hiện lệnh
        users[user_id] = current_time
        
        #api_url = f"http://1451d890-ccd1-41d7-99dc-9c5279bba7f9-00-tfuwyuivbajs.pike.replit.dev/api/sms?phone={phone_number}&loop={lap}"
#        response = requests.get(api_url)
#        
#        if response.status_code == 200:
#            print ( '✅ Đã Gửi Yêu Cầu Spam Đến API.')
#        else:
#            print ( '❌ Đã Xảy Ra Lỗi Khi Gửi Yêu Cầu. ')

        
        file_path = os.path.join(os.getcwd(), "smshdt1vip.py")
        process = subprocess.Popen(["python", file_path, phone_number, lap])
        processes.append(process)
        
        file_path2 = os.path.join(os.getcwd(), "spamtessttt.py")
        process = subprocess.Popen(["python", file_path2, phone_number])
        processes.append(process)
                
            
            

##############
    #bot.reply_to(message, 
#<a href="tg://user?id=6090590456">TrHiep</a>
        text_vip= f''' <blockquote>⊂🚀⊃Successful Attack⊂🚀⊃
↣ Bot🤖: @datienich2_bot
↣ SĐT📱: {phone_number}
↣ Người Dùng👤: <a href="tg://user?id={user_id}">{first_name}</a>
↣ Lặp Lại🔁: {lap}
↣ Thời Gian Chờ⏳: 60s
↣ Loại Spam :<b> Vip </b></blockquote> '''
        bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('🏆')], is_big=True)
        bot.reply_to(message, text_vip, parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML' ) 



#SPAM THƯỜNG
@bot.message_handler(commands=['spam'])
def spam(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    if int(chat_id) not in GROUP_ID:
    	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    	return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        #if message.chat.id not in GROUP_ID:      
#            bot.reply_to(message, f' <blockquote>⛔Bot Này Chỉ Hoạt Động Trong Nhóm @Tien_Ich2 \nVui Lòng Tham Gia Nhóm Và Sử Dụng Bot\n Link Nhóm <a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#            return 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        if len(message.text.split()) == 1:
            bot.reply_to(message, ' <blockquote>⛔ Vui Lòng Nhập [Số Điện Thoại] [Số Lần Spam] !!! \nVí Dụ: /spam 0987654321 30</blockquote>' , parse_mode='HTML')
            return
        if len(message.text.split()) == 2:
            bot.reply_to(message, ' <blockquote>⛔ Số Điện Thoại Vui Lòng Nhập Đủ 10 Số\nSố Lần Spam 1-30!!! \nVí Dụ: /spam 0987654321 30</blockquote>' , parse_mode='HTML')
            return
        if len(message.text.split()) != 3:
            bot.reply_to(message, ' <blockquote>⛔ SĐT 10 Số Viết Liền Đcm Ngu Vl🤡\nVí Dụ: /spam 0987654321 30</blockquote>' , parse_mode='HTML')
            return
        lap = message.text.split()[2]
        if lap.isnumeric():
            if not (int(lap) > 0 and int(lap) <= 30):
                bot.reply_to(message, " <blockquote>⚡ Vui Lòng Spam Trong Khoảng 1-30 Lần. Muốn Nhiều Hơn Vui Lòng Mua Vip. </blockquote>" , parse_mode='HTML' )
                return
        else:
            bot.reply_to(message, " <blockquote>⛔ Vui Lòng Nhập Số Lần Spam !!! \nVí Dụ: /spam 0987654321 30</blockquote>" , parse_mode='HTML' )
            return
        phone_number = message.text.split()[1]
        if not re.match(r"^\d{10}$", phone_number):
            bot.reply_to(message, ' <blockquote>⛔ Số Điện Thoại Vui Lòng Nhập Đủ 10 Số\nSố Lần Spam 1-30!!! \nVí Dụ: /spam 0987654321 30</blockquote>' , parse_mode='HTML' )
            return
    
        if phone_number in ["467895467"]:
            
            bot.reply_to(message, f'<pre>❓Thằng <a href="tg://user?id={user_id}">{first_name}</a> Spam Admin Làm Cặc Gì, Thích Mute À??\n\n🚨 @trn_hwp2 Ơi Có Thằng Tính Spam M Này</pre>' , parse_mode='HTML' )
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            return
    
    #    if not can_spam_again(phone_number):
    #        bot.reply_to(message, '⏰ Vui Lòng Đợi 30s Trước Khi Spam Lại Số Này.')
    #        return
        
        current_time = time.time()
        if user_id in users:
            last_used_time = users[user_id]
            time_elapsed = current_time - last_used_time
            if time_elapsed < 100:
                remaining_time = 100 - int(time_elapsed)
                bot.reply_to(message, f' <blockquote>⏳  30 Lần Khoảng 10p Mới Xong, Spam Lắm Làm Cặc Gì\n\n<a href="tg://user?id={user_id}">{first_name}</a> Đợi {remaining_time}s Nữa Để Có Thể Tiếp Tục Dùng Lệnh Spam.</blockquote>' , parse_mode='HTML')
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                return
        users[user_id] = current_time
        file_path0 = os.path.join(os.getcwd(), "smshdt1vip.py")
        process = subprocess.Popen(["python", file_path0, phone_number, '1'])
        file_path1 = os.path.join(os.getcwd(), "sms.py")
        process = subprocess.Popen(["python", file_path1, phone_number, lap])     
        processes.append(process)
        
        text_spam = f''' <blockquote>⊂🚀⊃Successful Attack⊂🚀⊃
↣ Bot🤖: @datienich2_bot
↣ SĐT📱: {phone_number}
↣ Người Dùng👤: <a href="tg://user?id={user_id}">{first_name}</a>
↣ Lặp Lại🔁: {lap}
↣ Thời Gian Chờ⏳: 100s
↣ Loại Spam : Free 
↣ <b>Mua Vip Để Spam Cháy Máy👽</b></blockquote> '''
        
        bot.reply_to(message, text_spam, parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML' ) 


#def kiem_tra_vip(idvip):
#    filepath = f"./vip/{idvip}.txt"
#    if os.path.exists(filepath):
#        # Nếu file tồn tại, người dùng là VIP
#        return "VIP"
#    else:
#        # Nếu file không tồn tại, người dùng không phải là VIP
#        return "Free"



#BÓI BÀI
API_URL = 'https://api.sumiproject.net/text/thayboi'
def capitalize_words(url):
    # Tách các phần của URL dựa trên dấu gạch ngang và gạch dưới
    parts = url.replace('-', ' ').replace('_', ' ').split()
    # Viết hoa chữ cái đầu của mỗi từ
    capitalized_parts = [part.capitalize() for part in parts]
    # Ghép các phần lại thành URL mới
    new_url = ' '.join(capitalized_parts)
    return new_url
@bot.message_handler(commands=['bdbdhthayboi'])
def handle_thayoi(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        try:
            # Gửi yêu cầu đến API
            response = requests.get(API_URL)
            # Kiểm tra mã trạng thái của phản hồi
            if response.status_code == 200:
                data = response.json()
                url = data.get('url', 'Không có URL trong phản hồi.')
                
                # Chuyển các từ trong URL thành chữ cái đầu viết hoa
                capitalized_url = capitalize_words(url)
                # Gửi URL đã thay đổi tới người dùng
                bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('🕊')], is_big=True)
                bot.reply_to(message, f' <blockquote>Kết Quả: \n{capitalized_url} </blockquote>' , parse_mode='HTML')
            else:
                bot.reply_to(message, f' <blockquote>Có lỗi xảy ra với API: </blockquote>\n<blockquote>{response.status_code} - {response.text} </blockquote> ' , parse_mode='HTML' )
        except Exception as e:
            bot.reply_to(message, f' <blockquote>💢 Lệnh Đang Được Bảo Trì, Vui Lòng Dùng Các Lệnh Khác!</blockquote>' , parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')


  
#CHECK INFO
def kiem_tra_vip(idvip):
    filepath = f"./vip/{idvip}.txt"
    if os.path.exists(filepath):
        # Nếu file tồn tại, người dùng là VIP
        return "VIP"
    else:
        # Nếu file không tồn tại, người dùng không phải là VIP
        return "Free"

# Hàm để lấy thông tin người dùng
def get_user_info(user: User):
    user_id = user.id
    username = user.username
    first_name = user.first_name
    is_vip = kiem_tra_vip(user_id)
  #  current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if user.last_name:
        first_name += f" {user.last_name}"
    if username is None:
        
        return f'''<blockquote>📂 Thông Tin Người Dùng:
👱 Name: {first_name}
🆔 User ID: <code>{user_id}</code>
👤 User Name: ❌
📄 User Link: <a href="tg://user?id={user_id}">{first_name}</a>
🔑 Trạng Thái: {is_vip} </blockquote>'''
    else:
        return f'''<blockquote>📂 Thông Tin Người Dùng:
👱 Name: {first_name}
🆔 User ID: <code>{user_id}</code>
👤 UserName: @{username}
📄 User Link: <a href="tg://user?id={user_id}">{user.first_name}</a>
🔑 Trạng Thái: {is_vip} </blockquote>'''

def send_user_info(chat_id, user):
    try:
        user_info = get_user_info(user)
        photos = bot.get_user_profile_photos(user.id, limit=1)
        if photos.photos:
            photo_file_id = photos.photos[0][0].file_id
            bot.send_photo(chat_id, photo_file_id, caption=user_info, parse_mode='HTML')
        else:
            bot.send_message(chat_id, f"<blockquote>📷 Người Dùng Không Có Avt.</blockquote>\n\n{user_info} ", parse_mode='HTML' , disable_web_page_preview=True)
    except Exception as e:
        bot.send_message(chat_id, f"<blockquote>Error: {str(e)}</blockquote>", parse_mode='HTML')




# Hàm xử lý khi người dùng gửi URL
@bot.message_handler(commands=['video'])
def get_video(message):
    # Lấy URL video từ tin nhắn của người dùng
    url = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else ''
    
    if not url:
        bot.reply_to(message, "<blockquote>Vui lòng gửi URL video Facebook.\n/video &lt;url_video&gt; </blockquote>" , parse_mode='HTML' )
        return
    
    # Cookies và headers cần thiết cho yêu cầu POST
    processing_msg = bot.reply_to(message, "<blockquote>Đang Xử Lý, Vui Lòng Đợi...\n(Tối Đa 30s) </blockquote>" , parse_mode='HTML' )
    cookies = {
        '_ga': 'GA1.1.427890337.1736005843',
        'PHPSESSID': 'q1lnbriv8a0saqat1bb8iug442',
        '__gads': 'ID=be0e447360774697:T=1746033899:RT=1746033899:S=ALNI_MZy-kogX3P4BRwQK8fcRxLEk2orPw',
        '__gpi': 'UID=000010155407710a:T=1746033899:RT=1746033899:S=ALNI_MZ5B849KezQm8zgoKiosjfa--rYGA',
        '__eoi': 'ID=06d2bc6fa7570432:T=1746033899:RT=1746033899:S=AA-Afja2zmbKwtHRGEUEXlQqJXeU',
        'FCNEC': '%5B%5B%22AKsRol-F24SCFx2fWq_eGeG1es0d5J5XiHBkUs2mSpwd5wOnQz8Qm4IspTUjal6oDxwrvWMamMzQz9uDzwYP9z9o72SRZKRxIe-4vLgeJ0C8UEKWhpMgXi-nhb5jvkNERoCY21mbsTAWLrUl4it7nUBWd1XuUGlptg%3D%3D%22%5D%5D',
    }
    
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://fsave.net',
        'priority': 'u=1, i',
        'referer': 'https://fsave.net/vi',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-requested-with': 'XMLHttpRequest',
    }

    # Dữ liệu cần gửi
    data = {
        'url': url,
    }

    # Gửi yêu cầu POST đến API và nhận phản hồi JSON
    response = requests.post('https://fsave.net/proxy.php', cookies=cookies, headers=headers, data=data)
    
    # Kiểm tra nếu phản hồi từ API có dữ liệu
    try:
        if response.status_code == 200:
            video_data = response.json()
    
            # Trích xuất thông tin video
            title = video_data['api']['title']
            description = video_data['api']['description']
            video_url = video_data['api']['previewUrl']
            thumbnail_url = video_data['api']['imagePreviewUrl']
            permanent_link = video_data['api']['permanentLink']
    
            userinfo = video_data['api']['userInfo']
            ten = userinfo['name']
            lienket = userinfo['externalUrl']
    
            # Trích xuất thông tin mediaItems
            media_items = video_data.get('api', {}).get('mediaItems', [])
            media_info = ""
            
            for item in media_items:
                if item['type'] == 'Video':
                    if '144p' in item['mediaRes'] or '360p' in item['mediaRes'] or '720p' in item['mediaRes']:
                        continue
                    media_url = item['mediaUrl']
                    #print (media_url)
                    for _ in range(10):
                        r = requests.get(media_url, headers=headers, cookies=cookies)
                        if r.ok:
                            file_url = r.json().get('fileUrl')
                            if file_url and 'In Processing' not in file_url:
                                break
                        time.sleep(3)
                    else:
                        file_url = None

                    media_info += f"📹 Xem Video 1080p: <a href='http://tranhiep.x10.mx/video?url={file_url}'>link Video</a>\n"
                    media_info += f"🗂 File Size: {item['mediaFileSize']}"
                else:
                    pass
                    # media_info += f"\n\nAudio {item['name']}:\n"
                    # media_info += f"Download URL: <a href='{item['mediaUrl']}'>link</a>\n"
                    # media_info += f"Thumbnail: <a href='{item['mediaThumbnail']}'>link</a>\n"
            
            # Tạo câu trả lời cho người dùng
            response_message = f"""
<blockquote>{title}</blockquote>
<blockquote>📸 Ảnh Chụp: <a href='{thumbnail_url}'>link</a>
🔗 Link Gốc: <a href='{permanent_link}'>link</a>
📹 Video 720p gốc: <a href='{video_url}'>video</a>
👤 Tác Giả: <a href='{lienket}'>{ten}</a></blockquote>
<blockquote>{media_info}</blockquote>"""
            
            # Gửi thông tin trả về cho người dùng trên Telegram
            bot.reply_to(message, response_message, parse_mode='HTML')
        
        else:
            bot.reply_to(message, "Không thể lấy dữ liệu video. Vui lòng thử lại sau.")
    except Exception as e:
        bot.reply_to(message, '<blockquote>Hãy Thử Bằng Link Video\nKhông Dùng Link Str Hay Reels </blockquote>' , parse_mode='HTML' )
    bot.delete_message(message.chat.id, processing_msg.message_id)





@bot.message_handler(commands=['id'])
def send_user_id(message):
    if message.reply_to_message:
        replied_user = message.reply_to_message.from_user
        full_name = replied_user.first_name
        if replied_user.last_name:
            full_name += f" {replied_user.last_name}"

        bot.reply_to(message, f"ID của {full_name} là: <code>{replied_user.id}</code>" , parse_mode='HTML', disable_web_page_preview=True)
        
    else:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        if message.from_user.last_name:
            user_name = f"{message.from_user.last_name} {message.from_user.first_name}"
        bot.reply_to(message, f"Id Của {user_name} Là:\n<code>{user_id}</code>" , parse_mode='HTML' )
        
        
        
@bot.message_handler(commands=['info'])
def handle_info(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    # Xử lý lệnh /info {user_id}
    if len(message.text.split()) == 2:
        user_id = message.text.split()[1]
        try:
            user_id = int(user_id)
            user = bot.get_chat(user_id)
            send_user_info(message.chat.id, user)
        except Exception as e:
            bot.reply_to(message, f"<blockquote>❌ Lỗi Không Thể Tìm Thấy Người Dùng Bằng Id Đó. Vui Lòng Xem Lại Id.</blockquote>", parse_mode='HTML')
            #chat_id = message.chat.id
#            if int(chat_id) not in GROUP_ID:
#            	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#            	return 
            
            #bot.reply_to(message, f"<blockquote>Lỗi: {str(e)}</blockquote>", parse_mode='HTML')
    else:
        # Xử lý lệnh /info mà không có ID
        send_user_info(message.chat.id, message.from_user)
        chat_id = message.chat.id
        #if int(chat_id) not in GROUP_ID:
#        	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        	return 
        
        
# Hiển thị người dùng <a href="http://t.me/{username}">{first_name}</a>
#one_time_keyboard=True
#⏰ Time : {current_time}
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Nhìn Cc, Chọn Đi :)))")
keyboard2.add(KeyboardButton("/getkey Lấy Key Free "))
keyboard2.add( KeyboardButton("/tiktok"), KeyboardButton("/catbox"), KeyboardButton("/idfb"))
keyboard2.add(KeyboardButton("/help Full Lệnh"), KeyboardButton("/hdsd"), KeyboardButton("/code"))
keyboard2.add(KeyboardButton("/info - Thông Tin Tele"))

@bot.message_handler(commands=['start','help', 'cachdung'])
def help(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        bot.reply_to(message, '<blockquote>📣Bạn Đã Bị Bot Band, Vui Lòng Ib @trn_hwp2📣</blockquote>', parse_mode='HTML') 
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
#    	bot.reply_to(message, f'<blockquote> <b>Vui Lòng Ib @trn_hwp2 Cấp Quyền \nBot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#    	return 
    help_text = '''
<blockquote expandable>┏━━━━━━━━━━━━━┓
 ━━━Danh Sách Lệnh━━━
┗━━━━━━━━━━━━━┛
┏➤/hdsd - Hướng Dẫn Dùng.
┣➤/help - Danh Sách Lệnh.
┣➤/getkey - Lấy Key.
┣➤/key - Nhập Key.
┣➤/film - Tìm Film + Xem
┣➤/avtfb-GetAvtFBXuyên🛡️
┣➤/idfb - Lấy Id Fb.
┣➤/video-Tải Video Fb.
┣➤/id-Lấy ID Người Dùng.
┣➤/spam - Spam SMS Call.
┣➤/spamvip - Spam VIP.
┣➤/catbox - Upload Ảnh, 
┣     Video, File Lên Catbox.
┣➤/mocky - Upload Văn Bản 
┣                 Lên Mocky.
┣➤/voice - Text ➯ Voice.
┣➤/tiktok - Tải Video Tiktok.
┣➤/code - Get HTML Code.
┣➤/ask - Chat GPT.🔒Die api:)
┣➤/rutgon - Rút Gọn Link.
┣➤/random - Random Anime.
┣➤/tuoi - Tính Tuổi.
┣➤/fact - Thú Vị Về Mèo.
┣➤/info - Thông Tin User.
┣➤/time : Time Onl Bot
┣➤/thoitiet - Thời Tiết.
┣➤/plan - <b>Mua Vip.</b>
┗━━━━━━━━━━━━━➤</blockquote>
'''
#┣➤/chat - <b>🔒Tạm Khóa</b>
#┣➤/fb - Info Fb. <b>🔒Tạm Khóa</b>
#┣➤/2fa - Lấy 2fa FB. <b>🔒Khóa</b>

    bot.reply_to(message, help_text,  parse_mode='HTML' , reply_markup=keyboard2) 

  #  time.sleep(0.5)
    #bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
   # ┗➤/mua - Mua Vip.
   

@bot.message_handler(['hdsd'])
def huong_dan(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    text ='''<blockquote expandable>Lệnh /getkey:
Dùng /getkey Để Lấy Key
Sau Đó Dùng /key {Dấu Cách} [Nhập Key Vừa Nhận Được] Để Bot Xác Thực Key

Lệnh /spam, /spamvip:
/spam [Số Điện Thoại] [Số Lần Spam Trong Khoảng 1-30]
/spamvip [Số Điện Thoại] [Số Lần Spam Trong Khoảng 1-150] 
( Mua Vip Mới Dùng Được )

Lệnh /film:
[/film + tên film] để tìm film muốn xem
ra film rồi chỉ cần nhấp vào tên film là được

Lệnh /voice:
/voice {Dấu Cách} [Nhập Văn Muốn Chuyển Thành Giọng Nói]

Lệnh /tiktok:
/tiktok [Nhập Link Video Tiktok Muốn Tải]
Có thể dùng /tiktok [id] để tải video mà không cần link!!, id lấy khi tải video bằng link, nếu muốn tải lại lần sau, hãy hưu lại id nheee


Lệnh /code:
/code [Nhập Link Trang Web Muốn Chuyển Thành File HTML]

Lệnh /ask:
/ask [Nhập Văn Bản Để Hỏi AI]

Lệnh /rutgon:
/rutgon [Nhập Link Dài Cần Rút Gọn] {Dấu Cách} [Nhập Tên Miền Tùy Chọn]
Ví dụ:
<code>/rutgon https://tiktok.com tuyyyy</code>
👉Bot Trả Kết Quả
<code>https://ulvis.net/tuyyyy</code>

Lưu Ý: Chỉ Rút Link Dài Thành Link Ngắn, Không Có Tác Dụng Vượt Link Đâu Mà Mấy Đứa Cứ Gắn Link Vượt Vào Làm Gì 🤡🤡🤡


Lệnh /catbox:
dùng /catbox 
reply tin nhắn của bot vừa gửi bằng ảnh, video, file để bot upload lên web catbox


Lệnh /avtfb:
/avtfb + [link fb]
Ví Dụ:
<code>/avtfb https://www.facebook.com/profile</code>

Lệnh /random:
Gửi /random Rồi Chọn 1 Trong 4 Loại Ảnh (Chọn 1 Trong 4 Loại Luôn Không Cần Dùng /random Cũng Được =))))  )

Lệnh /tuoi:
Nhập Đúng Định Dạng
/tuoi DD-MM-YYYY

Lệnh /info:
Gửi /info Để Xem Thông Tin Và Trạng Thái Vip Hay Free Của Bản Thân
Có Thể Dùng /info [user id] 

Lệnh /plan: 
Dùng /plan Để Xem Giá Gói Vip

Lệnh /thoitiet:
Gửi /thoitiet [Tên Thành Phố], Ví Dụ: 
/thoitiet Hà Nội  </blockquote>'''

#Lệnh /chat:
#Gửi /chat Rồi Reply Tin Nhắn Thứ 2 Bot Gửi Và Nhập Nội Dung Mong Muốn Để Gửi Admin 

    bot.reply_to(message, text , parse_mode='HTML' )
    #chat_id = message.chat.id
#    if int(chat_id) not in GROUP_ID:
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 
    
    




###############################
#-------------------------------------------#
#----------------ADMIN---------------------#
#-------------------------------------------#
###############################

#SỐ LỆNH ĐANG CHẠY
@bot.message_handler(commands=['status'])
def status(message):
    user_id = str(message.from_user.id)

    if any(user_id in file for file in os.listdir(blocklist_dir)):
        return

    #if user_id != ADMIN_ID:
#        bot.reply_to(message, '<blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này.</blockquote>', parse_mode='HTML')
#        return

    # Chỉ đếm những process còn đang chạy
    alive_processes = [p for p in processes if p.poll() is None]
    process_count = len(alive_processes)

    bot.reply_to(message, f'<blockquote>🏃 Số Lệnh Đang Chạy: {process_count} </blockquote>', parse_mode='HTML')




#ADMIN
@bot.message_handler(commands=['admin'])
def restart(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML' )
        return
    bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('🏆')], is_big=True)        
    text = '''   <blockquote>┏━━━━━━━━━━━━━┓
 ━━━🔒Lệnh Admin━━━━
┗━━━━━━━━━━━━━┛
➯/status : Lệnh Đang Chạy
➯/rs : Khởi Động Lại Bot
➯/them: Thêm Mem Vip
➯/block &lt;id&gt;: Chặn Người Dùng
➯/mem: Gửi Tin Nhắn Đến Mem
➯/delete &lt;Days&gt;: Xóa Key Free
➯/deletevip &lt;Days&gt;: Xóa Key Vip
➯/checkvip: Check Ngày Vip Còn Lại
➯/mute: Khóa mõm
➯/unmute: Mở mõm
➯/on: Bật Bot
➯/off: Tắt Bot
┗━━━━━━━━━━━━━┛</blockquote>'''
    bot.reply_to(message, text,  parse_mode='HTML' ) 



#XÓA KEY FREE
base_dir = os.path.dirname(os.path.abspath(__file__))
vip_dir = os.path.join(base_dir, 'vip')
user_dir = os.path.join(base_dir, 'user')

@bot.message_handler(commands=['delete'])
def delete_files(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML' )
        return
    try:
        day = message.text.split()[1]  # Lấy ngày từ lệnh
        user_day_dir = os.path.join(user_dir, day)  # Thư mục tương ứng với ngày

        if not os.path.exists(user_day_dir):
            bot.reply_to(message, f" <blockquote>🤡 Thư Mục {day} Không Tồn Tại. </blockquote>" , parse_mode='HTML' )
            return

        # Lấy danh sách các id từ thư mục vip
        vip_files = {f for f in os.listdir(vip_dir) if f.endswith('.txt')}
        
        # Lấy danh sách các file trong thư mục ngày
        user_files = [f for f in os.listdir(user_day_dir) if f.endswith('.txt')]

        deleted_files = []
        for file in user_files:
            if file not in vip_files:
                # Xóa file nếu không có trong thư mục vip
                os.remove(os.path.join(user_day_dir, file))
                id_in_file = file.replace('.txt', '')
                deleted_files.append(f'<a href="tg://user?id={id_in_file}">{file}</a>')

        # Trả lời kết quả
        if deleted_files:
            bot.reply_to(message, f" <blockquote> Đã Xóa Các File: {', '.join(deleted_files)} </blockquote>", parse_mode='HTML')
        else:
            bot.reply_to(message, " <blockquote>Không Có File Nào Cần Xóa. </blockquote>" , parse_mode='HTML' )

    except IndexError:
        bot.reply_to(message, " <blockquote>Vui Lòng Cung Cấp Số Ngày Cụ Thể. Ví Dụ: /delete 1 </blockquote>" , parse_mode='HTML' )
    except Exception as e:
        bot.reply_to(message, f" <blockquote>Đã xảy ra lỗi: {str(e)} </blockquote>" , parse_mode='HTML')
        
        
        
#RESTART
@bot.message_handler(commands=['rs'])
def restaart(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML' )
        return
    bot.send_message(message.chat.id, ' <blockquote>🤖 Bot Đã Khởi Động Lại. Dùng /help Để Mở Menu Bot !!! </blockquote> ' , parse_mode='HTML' )
    os.execl(sys.executable, sys.executable, *sys.argv)


def is_vip(user_id):
    return os.path.exists(f"./vip/{user_id}.txt")

#@bot.message_handler(commands=['stop'])
#def stop(message):
#    user_id = message.from_user.id
#    if str(user_id) != ADMIN_ID and not is_vip(user_id):
#        bot.reply_to(message, '🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này.')
#        return
#    bot.reply_to(message, '🤖 Bot Đã Dừng.')
#    sys.exit()



@bot.message_handler(commands=['them'])
def them(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    # Kiểm tra quyền của người dùng
    if str(user_id) not in themvip:
        bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>', parse_mode='HTML')
        return
    from datetime import datetime, timedelta
    try:
        # Tách các tham số từ lệnh
        from datetime import datetime, timedelta
        parts = message.text.split()
        if len(parts) != 4:
            bot.reply_to(message, ' <blockquote>🙅 Định Dạng Lệnh Không Đúng. Vui Lòng Sử Dụng: \n/them [ID VIP] [Ngày Bắt Đầu YYYY-MM-DD] [Số Ngày] </blockquote>', parse_mode='HTML')
            return
        
        _, idvip, start_date_str, num_days_str = parts
        num_days = int(num_days_str)

         #Kiểm tra và chuyển đổi ngày bắt đầu từ chuỗi
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        except ValueError:
            bot.reply_to(message, ' <blockquote>🙅 Định Dạng Ngày Không Đúng. Vui Lòng Sử Dụng: YYYY-MM-DD </blockquote>', parse_mode='HTML')
            return
        
        # Lặp qua các ngày và thêm tệp tin vào các thư mục tương ứng
        days_added = 0
        current_date = start_date

        while days_added < num_days:
            # Xác định thư mục cần kiểm tra
            folder_path = f'./user/{current_date.day}'
            
            # Tránh xung đột với tên tệp tin
            if os.path.isdir(folder_path):
                # Đường dẫn tệp tin
                file_path = f'{folder_path}/{idvip}.txt'
                if not os.path.exists(file_path):
                    # Tạo tệp tin rỗng
                    with open(file_path, 'w') as fi:
                        fi.write(f"{start_date_str}|{num_days_str}")
            else:
                os.makedirs(folder_path, exist_ok=True)
                file_path = f'{folder_path}/{idvip}.txt'
                with open(file_path, 'w') as fi:
                    fi.write(f"{start_date_str}|{num_days_str}")

            days_added += 1
            # Di chuyển đến ngày tiếp theo
            current_date += timedelta(days=1)
            # Quay lại ngày đầu của tháng nếu quá ngày 31
            if current_date.day > 31:
                current_date = current_date.replace(day=1)
                current_date += timedelta(days=1)
        
        # Cập nhật thông tin VIP vào tệp tin trong thư mục /vip
        vip_folder_path = f"./vip"
        os.makedirs(vip_folder_path, exist_ok=True)
        with open(f"{vip_folder_path}/{idvip}.txt", "w") as fii:
            fii.write(f"{start_date_str}|{num_days_str}")
            
        bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('🎉')], is_big=True)
        bot.reply_to(message, f' <blockquote>⚡ Thêm Thành Công <a href="tg://user?id={idvip}">{idvip}</a> Làm VIP. </blockquote>', parse_mode='HTML')

    except ValueError:
        bot.reply_to(message, ' <blockquote>🙅 Định Dạng Lệnh Không Đúng. Vui Lòng Sử Dụng: \n/them [ID VIP] [Ngày Bắt Đầu YYYY-MM-DD] [Số Ngày] </blockquote>', parse_mode='HTML')
    except Exception as e:
        bot.reply_to(message, f' <blockquote>Đã Xảy Ra Lỗi: {e}\nNhập Lại Đúng Định Dạng Xem Sao :)</blockquote>', parse_mode='HTML')




@bot.message_handler(commands=['plan'])
def mua(message):
    #user_id = message.from_user.id
#    blocklist_files = os.listdir(blocklist_dir)
#    if any(str(user_id) in file for file in blocklist_files):
#        return
    mua_text = '''<blockquote>╭━━━━━━━━━━╮
├━━Bảng Giá Vip:━━┤
| ➯     1 Tuần : 15k         
| ➯    1 Tháng : 50k
╰━━━━━━━━━━╯
╭━━━━━━━━━━╮
├━  Liên Hệ : <a href="http://t.me/trn_hwp2">TrHiep</a> ━┤
╰━━━━━━━━━━╯
Mua Người Khác Bịp Tự Chịu🤡</blockquote>
'''
    bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('💯')], is_big=True)
    bot.reply_to(message, mua_text, parse_mode='HTML')
    #chat_id = message.chat.id
#    if int(chat_id) not in GROUP_ID:      
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 

#Tắt Button
@bot.message_handler(commands=["tatbanphim"])
def top_commands(message):
    #bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    # Kiểm tra quyền của người dùng
    if str(user_id) not in themvip:
        bot.reply_to(message, '<blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>', parse_mode='HTML')
        return
    markup_remove = types.ReplyKeyboardRemove()
    heee = bot.send_message(message.chat.id, text="<blockquote>❗Đã Tắt Bàn Phím Phụ.</blockquote>" , parse_mode='HTML' , reply_markup=markup_remove)
    bot.delete_message(chat_id=message.chat.id, message_id=heee.message_id) 

#BẬT BOT
@bot.message_handler(commands=['on'])
def turn_on_bot(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id  
    global is_active
    if str(user_id) in ADMIN_ID:
        is_active = True
        bot.reply_to(message, ' <blockquote>🔈Bot Đã Hoạt Động Trở Lại. </blockquote>' , parse_mode='HTML' )
    else:
        bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML' )


#TẮT BOT
@bot.message_handler(commands=['off'])
def turn_off_bot(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id  
    global is_active
    if str(user_id) in ADMIN_ID:
        is_active = False
        bot.reply_to(message, ' <blockquote>🔇 Bot Đã Được Tắt. </blockquote>' , parse_mode='HTML')
    else:
        bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML')



#CHẶN CHÓ
@bot.message_handler(commands=['block'])
def block_user(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    if message.from_user.id == 7484921732:  
        try:
            _, user_id = message.text.split()
            user_id = int(user_id)
            
            # Tạo file .txt 
            user_block_file = os.path.join(blocklist_dir, f'{user_id}.txt')
            with open(user_block_file, 'w') as file:
                file.write(f'User {user_id} is blocked.')
            bot.reply_to(message, f' <blockquote>📣Người Dùng <a href="tg://user?id={user_id}">{user_id}</a> Đã Cút Và Không Được Dùng Bot. </blockquote>' , parse_mode='HTML' )
        except ValueError:
            bot.reply_to(message, '<blockquote>Lệnh không hợp lệ. Sử dụng: /block [id] </blockquote>' , parse_mode='HTML' )
        except Exception as e:
            bot.reply_to(message, f'Đã xảy ra lỗi: \n{e}')
    else:
        bot.reply_to(message, ' <blockquote> 🤡 Mày Làm Gì Có Quyền Mà Đòi Dùng. </blockquote>' , parse_mode='HTML' )

@bot.message_handler(commands=['checkvip'])
def check_vip(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return

    if str(user_id) != ADMIN_ID:
        bot.reply_to(
            message,
            '<blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này.</blockquote>',
            parse_mode='HTML'
        )
        return

    response = ""
    index = 1  # Số thứ tự bắt đầu từ 1
    messages = []  # Danh sách lưu từng phần tin nhắn

    for filename in os.listdir(vip_folder):
        if filename.endswith('.txt'):
            user_id = filename.split('.')[0]
            file_path = os.path.join(vip_folder, filename)
            with open(file_path, 'r') as f:
                content = f.read().strip()
                date_str, days_str = content.split('|')
                date_format = '%Y-%m-%d'
                from datetime import datetime, timedelta
                start_date = datetime.strptime(date_str, date_format)
                days = int(days_str)
                end_date = start_date + timedelta(days=days)
                remaining_days = (end_date - datetime.now()).days

                try:
                    user_info = bot.get_chat(user_id)
                    first_name = user_info.first_name
                    usernamee = user_info.username
                except Exception as e:
                    first_name = "user"

                # Hiển thị số ngày còn lại
                if remaining_days >= 0:
                    status = f"✅Còn {remaining_days} Ngày Vip."
                else:
                    status = f"❌ Vip Đã Hết Hạn {abs(remaining_days)} Ngày."

                response += f"<blockquote>{index}.\n➯ Người Dùng: <a href='tg://user?id={user_id}'>{first_name}</a> \nLink: tg://user?id={user_id}\n{status} Ngày VIP. </blockquote>\n"
                index += 1

                # Cứ 10 người, lưu nội dung hiện tại vào danh sách và bắt đầu phần mới
                if index % 6 == 1 and index > 1:
                    messages.append(response)
                    response = ""

    # Thêm phần còn lại vào danh sách nếu có
    if response:
        messages.append(response)

    # Gửi từng phần tin nhắn
    if messages:
        for msg in messages:
            bot.send_message(message.chat.id, msg, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, "Không có thông tin VIP nào.")


user_folder = 'user'  # Thư mục chứa các thư mục ngày

# Xóa file vip với ID trong tất cả các thư mục ngày
@bot.message_handler(commands=['deletevip'])
def delete_files_vip(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML' )
        return
    command_parts = message.text.split()
    if len(command_parts) != 2:
        bot.send_message(message.chat.id, "Lệnh không đúng định dạng. Vui lòng sử dụng: /xoa {id}")
        return
    user_id = command_parts[1]
    files_deleted = 0

    # Xóa file từ thư mục ngày
    for day_folder in range(1, 32):
        day_folder_path = os.path.join(user_folder, str(day_folder))
        if os.path.exists(day_folder_path):
            file_path = os.path.join(day_folder_path, f"{user_id}.txt")
            if os.path.exists(file_path):
                os.remove(file_path)
                files_deleted += 1
    # Thông báo kết quả
    if files_deleted > 0:
        bot.send_message(message.chat.id, f"Đã xóa {files_deleted} file với ID {user_id}.")
    else:
        bot.send_message(message.chat.id, f"Không tìm thấy file với ID {user_id}.")



###############################
#-------------------------------------------#
#---------KẾT THÚC LỆNH ADMIN------------#
#-------------------------------------------#
###############################






@bot.message_handler(commands=['anh', 'dich', 'film'])
def boquaaa(message):
    return
    
vip_folder = 'vip'  # Thư mục chứa file vip
user_folder = 'user' 
ADMIN_ID_THEM_VIP = [7484921732, 6964080086, 6090590456]

# Vào nhóm
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    bot.delete_message(message.chat.id, message.message_id)
    adder_user_id = message.from_user.id
    adder_first_name = message.from_user.first_name
    for new_member in message.new_chat_members:
        user_id = new_member.id
        first_name = new_member.first_name

        # Nếu người tự vào nhóm
        if adder_user_id == user_id:
            text = f" <blockquote>💭 Chào Mừng Bé <a href='tg://user?id={user_id}'>{first_name}</a> Đến Với Nhóm!\n📦 Hãy Dùng /help Để Xem Menu Lệnh. </blockquote>"
            bot.send_message(message.chat.id, text, parse_mode='HTML')
        else:
            # Nếu người dùng được mời bởi ai đó
            text = f"""<blockquote>Người Dùng <a href='tg://user?id={user_id}'>{first_name}</a>
Được Thêm Bởi <a href='tg://user?id={adder_user_id}'>{adder_first_name}</a>
Id Người Thêm: <code>{adder_user_id}</code>
Id Mem Mới: <code>{user_id}</code></blockquote>"""
            text2 =f"<blockquote>💭 Chào Mừng Bé <a href='tg://user?id={user_id}'>{first_name}</a> Đến Với Nhóm!\n📦 Hãy Dùng /help Để Xem Menu Lệnh. </blockquote>"

            # Tạo nút inline keyboard
            markup = InlineKeyboardMarkup()
            button = InlineKeyboardButton("+2 Days", callback_data=f"process_{adder_user_id}")
            markup.add(button)

               # BỎ # 2 CÁI DƯỚI ĐỂ MỞ VIP ADD MEM
            # Gửi tin nhắn chào mừng kèm inline keyboard
            #sent_message = bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=markup)
#            bot.pin_chat_message(message.chat.id, sent_message.message_id, disable_notification=True)
            bot.send_message(message.chat.id, text2, parse_mode='HTML')
            
@bot.message_handler(content_types=['pinned_message'])
def handle_pinned_message(message):
    # Xóa thông báo hệ thống sau khi bot ghim tin nhắn
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

#xử lý khi nhấn nút
@bot.callback_query_handler(func=lambda call: call.data.startswith("process_"))
def handle_button(call):
    if call.from_user.id in ADMIN_ID_THEM_VIP:  # Kiểm tra nếu người nhấn là admin
        adder_user_id = call.data.split("_")[1]
        file_path = os.path.join(vip_folder, f"{adder_user_id}.txt")

        # Kiểm tra file có tồn tại không
        if os.path.exists(file_path):
            # Đọc file và cập nhật số ngày trong file vip
            with open(file_path, 'r') as f:
                content = f.read().strip()
            date_str, days_str = content.split('|')
            from datetime import datetime, timedelta
            vip_start_date = datetime.strptime(date_str, '%Y-%m-%d')  # Ngày bắt đầu
            days = int(days_str)  # Số ngày hiện tại
            # Tính toán ngày kết thúc sau khi cộng số ngày hiện tại
            end_date = vip_start_date + timedelta(days=days - 1)  # Trừ 1 vì tính từ ngày bắt đầu
            # Tạo 3 ngày mới, bắt đầu từ ngày cuối
            for i in range(2):
                # Tính ngày mới cho từng ngày trong 4 ngày tiếp theo
                new_vip_date = end_date + timedelta(days=i + 1)
                # Xử lý để ngày không vượt quá 31
                new_day = new_vip_date.day
                if new_day > 31:
                    new_day = new_day % 31  # Quay lại ngày 1 khi vượt quá 31
                
                # Đường dẫn đến thư mục ngày tương ứng
                day_folder_path = os.path.join(user_folder, str(new_day))

                # Tạo thư mục nếu chưa tồn tại
                if not os.path.exists(day_folder_path):
                    os.makedirs(day_folder_path)

                # Đường dẫn file id trong thư mục ngày
                user_file_path = os.path.join(day_folder_path, f"{adder_user_id}.txt")

                # Tạo file với ngày mới và ghi thông tin
                with open(user_file_path, 'w') as f:
                    f.write(f"{new_vip_date.strftime('%Y-%m-%d')}|4")

            # Cập nhật file vip với số ngày mới
            new_days = days + 2  # Cộng thêm 2 ngày
            with open(file_path, 'w') as f:
                f.write(f"{vip_start_date.strftime('%Y-%m-%d')}|{new_days}")

        else:
            # Nếu file không tồn tại, tạo mới file với số ngày = 3 trong thư mục vip
            from datetime import datetime, timedelta
            today = datetime.today().strftime('%Y-%m-%d')
            with open(file_path, 'w') as f:
                f.write(f"{today}|2")

            # Thêm 2 file mới vào thư mục user
            for i in range(2):
                from datetime import datetime, timedelta
                new_vip_date = datetime.today() + timedelta(days=i + 1)
                day_folder = new_vip_date.day  # Thư mục ngày tương ứng
                day_folder_path = os.path.join(user_folder, str(day_folder))

                # Tạo thư mục nếu chưa tồn tại
                if not os.path.exists(day_folder_path):
                    os.makedirs(day_folder_path)

                user_file_path = os.path.join(day_folder_path, f"{adder_user_id}.txt")

                # Tạo file với thông tin ngày mới
                with open(user_file_path, 'w') as f:
                    f.write(f"{new_vip_date.strftime('%Y-%m-%d')}|2")

        # Sửa đổi tin nhắn ban đầu và xóa inline keyboard
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'<blockquote>{call.message.text}</blockquote>' + "\n <blockquote>Đã Xử Lý</blockquote>", parse_mode='HTML', reply_markup=None)
        bot.unpin_chat_message(call.message.chat.id)

        bot.answer_callback_query(call.id, "😎Đã +2 Ngày Vip Thành Công\nCho Người Mời.", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "Chỉ Dành Cho Admin Thôi Bạn Eii🌚", show_alert=True)

########################
########################
#@bot.message_handler(content_types=['new_chat_members'])
#def welcome_new_member(message):
#    adder_user_id = message.from_user.id
#    adder_first_name = message.from_user.first_name
#    for new_member in message.new_chat_members:
#        user_id = new_member.id
#        first_name = new_member.first_name
#        if adder_user_id == user_id:
#            bot.send_message(message.chat.id, f"<blockquote>💭 Chào Mừng Bé <a href='tg://user?id={user_id}'>{first_name}</a> Đến Với Nhóm!\n📦 Hãy Dùng /help Để Xem Menu Lệnh. </blockquote>",  parse_mode='HTML' )
#        else:
#            bot.send_message(message.chat.id, f"<blockquote> Người Dùng <a href='tg://user?id={user_id}'>{first_name}</a> Được Thêm Bởi <a href='tg://user?id={adder_user_id}'>{adder_first_name}</a> </blockquote> <blockquote>Người <a href='tg://user?id={user_id}'>{first_name}</a> vừa vào nhóm! </blockquote>" , parse_mode='HTML' )
########################
########################



# Rời nhóm
@bot.message_handler(content_types=['left_chat_member'])
def farewell_member(message):
    bot.delete_message(message.chat.id, message.message_id)
    left_member = message.left_chat_member
    user_id = left_member.id
    first_name = left_member.first_name
    bot.send_message(message.chat.id, f"<blockquote>🤡 Thằng <a href='tg://user?id={user_id}'>{first_name}</a> Vừa Rời Khỏi Nhóm.\nĐã Ít Mem Rồi Còn Out Đmmm😡</blockquote>", parse_mode='HTML')



#RÚT GỌN LINK
@bot.message_handler(commands=['rutgon'])
def shorten_link(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        if len(message.text.split(' ')) < 2:
            bot.reply_to(message, "<blockquote>🔗 Bạn Cần Gắn Thêm Link Muốn Rút Gọn Và Từ Tùy Chọn.\n Ví Dụ:\n/rutgon [link] [Từ Tùy Ý]</blockquote>" , parse_mode='HTML')
            return
    
        url = message.text.split(' ')[1]
        custom_name = message.text.split(' ')[2] if len(message.text.split(' ')) > 2 else None
    
        api_url = f"https://ulvis.net/api.php?url={url}&custom={custom_name}&private=1"
        response = requests.get(api_url, verify=True)
        
        if "Error: Custom name already taken." in response.text:
            bot.reply_to(message, " <blockquote>❌ Từ Đó Đã Có Người Đặt, Vui Lòng Chọn Từ Khác!\nVí Dụ:\n/rutgon [link] [Kí Tự Tùy Ý] </blockquote>" , parse_mode='HTML' )
        elif "Invalid Url" in response.text:
            bot.reply_to(message, "<blockquote>🔗 Liên Kết Không Hợp Lệ. Vui Lòng Xem Lại!</blockquote>" , parse_mode='HTML' )
        elif "https://" in response.text:
            short_url = response.text.strip()
            bot.reply_to(message, f"<blockquote>🤖Thành Công.\n 🔗Link Rút Gọn Của Bạn Là:</blockquote>\n<blockquote>{short_url}</blockquote>\n<blockquote>👇Nhấn Để Sao Chép👇 \n<code>{short_url}</code> </blockquote>" , parse_mode='HTML' )
            
        else:
            bot.reply_to(message, f" <blockquote>❌ Đã Xảy Ra Lỗi. API Không Nhận Diện Được Tên Miền, Vui Lòng Nhập Tên Miền Khác. \n🤖 Mã lỗi: {response.status_code} </blockquote>" , parse_mode='HTML')

    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 
        
        
        
        
#THỜI TIẾT
@bot.message_handler(commands=['thoitiet'])
def get_location(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id  
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        
        if len(message.text.split()) == 1:
            bot.reply_to(message, ' <blockquote>Vui Lòng Nhập Đúng Cú Pháp.\nVí Dụ: /thoitiet Hà Nội</blockquote>' , parse_mode='HTML')
            
            	 
            return
        location = message.text.replace('/thoitiet', '').strip()
    
    #bot.send_message(message.chat.id, " <blockquote>⚡ Tiếp Theo Hãy Reply Tin Nhắn Này Và Nhập Tên Thành Phố Bạn Muốn Xem Thời Tiết\n⚠ Không Cần Nhập /thoitiet!! </blockquote>" , parse_mode='HTML' )
#    bot.register_next_step_handler(message, get_weather)
#def get_weather(message):
#    location = message.text
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={openweathermap_api_key}&units=metric&lang=vi'
        response = requests.get(url)
        data = response.json()
        if data['cod'] != 200:
            weather_data = f"<blockquote>🙅 Không Tìm Thấy Thông Tin thời Tiết Cho {location}. Vui Lòng Kiểm Tra Lại Tên Thành Phố. </blockquote>"
            
        else:
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            pressure = data['main']['pressure']
            mayy = data['clouds']['all']
            iccon = data['weather'][0]['icon']
          #  hehe = f'http://openweathermap.org/img/wn/{iccon}.png'
            weather_data = f""" <blockquote>╭────⭓ Thời Tiết
│🌍 City: <a href="https://www.google.com/maps/search/?api=1&query={location.replace(' ', '+')}">{location}</a>
│🔗 Link Map: <a href="https://www.google.com/maps/search/?api=1&query={location.replace(' ', '+')}">{location}</a>
│⛅ Thời Tiết: {description}
│🌡 Nhiệt Độ Hiện Tại: {temp}°C
│🌡️ Cảm Giác Như: {feels_like}°C
│🫧 Độ Ẩm: {humidity}%
|🌬️ Tốc Độ Gió: {wind_speed} m/s
│🍃 Áp Suất: {pressure} hPa
|☁ Lượng Mây: {mayy}%
│🌐 Quốc Gia: {data['sys']['country']}
╰─────────────⭓ </blockquote> 
    """
    ####|🌧 Lượng Mưa 1h Qua: {muaa}mm/h
        bot.reply_to(message, weather_data, parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot đang được bảo trì. \n⏳ Vui lòng thử lại sau.</blockquote>', parse_mode='HTML') 


STICKER_QR_ID = "CAACAgQAAxkBAAEWULFnuBTsnvXbrXajZPe6rXX6zOrzlAACjhcAAhDqwVHmLKz1PKqEATYE"
@bot.message_handler(func=lambda message: 'qqqqqr' in message.text.lower())
def send_qr_code(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    bot.send_sticker(message.chat.id, STICKER_QR_ID, reply_markup=None)
    bot.send_message(message.chat.id, "QR của Trhiep")
    
    
    #bank_qr_code_path = 'mb.png'
#    #momo_qr_code_path = 'momo.jpg'

#    with open(bank_qr_code_path, 'rb') as bank_qr: #, open(momo_qr_code_path, 'rb') as momo_qr:
#        bot.send_photo(message.chat.id, bank_qr, caption="<pre>Đây là QR Code Tài Khoản Ngân Hàng Của Admin</pre>" , parse_mode='HTML' )
        #bot.send_photo(message.chat.id, momo_qr, caption="Đây Là QR Code Tài Khoản Momo Của Admin")



# Hàm gọi API và xử lý dữ liệu
def get_facebook_info(link):
    api_url = f'https://api.scaninfo.vn/facebook/info/?link={link}'
    response = requests.get(api_url)
    
    # Kiểm tra nếu có lỗi
    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 'error':
            return {'error': True, 'message': data.get('error', {}).get('message', 'Lỗi Không Xác Định')}
        return data
    else:
        return {'error': True, 'message': 'Không Thể Kết Nối Đến API😭'}

# Hàm gửi tin nhắn và ảnh
def send_message_with_photo(chat_id, message, photo_url=None):
    if photo_url:
        bot.send_photo(chat_id, photo_url, caption=message, parse_mode='HTML')
    else:
        bot.send_message(chat_id, message, parse_mode='HTML')
        
def translate_gender(gender):
    if gender == 'male':
        return 'Nam'
    elif gender == 'female':
        return 'Nữ'
    else:
        return  '<s>Không xác định</s>'




# Xử lý lệnh /fb
@bot.message_handler(commands=['fb fggtdsgb'])
def handle_infoo(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
  
    chat_id = message.chat.id
    if int(chat_id) not in GROUP_ID:
        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Để Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
        return 
    
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return

        args = message.text.split(maxsplit=1)
        if len(args) != 2:
            bot.send_message(message.chat.id, " <blockquote>🤡Vui Lòng Sử Dụng Đúng Định Dạng: \n/fb [link, id, username fb]</blockquote>" , parse_mode='HTML' )
            return
        
        link = args[1]
        data = get_facebook_info(link)
        
        if data.get('error'):
            # Nếu có lỗi, gửi tin nhắn thông báo lỗi
            bot.send_message(message.chat.id, f" <blockquote>❌ Lỗi: Không Thể Tìm Thấy Người Dùng. Vui Lòng Xem Lại. </blockquote> " , parse_mode='HTML' )
            return
        
        # Xử lý dữ liệu và tạo thông báo
        linkk = data.get('link')
        id = data.get('id', '<s>Không Công Khai</s>')
        name = data.get('name', '<s>Không Công Khai</s>')
        username = data.get('username', '<s>Chưa Thiết Lập</s>')
        verified = 'Đã Xác Minh ✅' if data.get('is_verified', False) else 'Chưa Xác Minh❌'
        created_time = data.get('created_time', '<s>Không Công Khai</s>')
        gender = translate_gender(data.get('gender'))
        relationship_status = data.get('relationship_status', '<s>Không Xác Định</s>')
        hometown = data.get('hometown',{}).get('name', '<s>Không Công Khai</s>')
        location = data.get('location', {}).get('name', '<s>Không Công Khai</s>')
        work = ', '.join([item.get('employer', {}).get('name', '<s>Không Xác Định</s>') for item in data.get('work', [])]) or '<s>Không Xác Định</s>'
        birthday = data.get('birthday', '<s>Không Công Khai</s>')
        followers = f"{data.get('Followers', '0')}"
        locale = data.get('locale', '<s>Không Công Khai</s>')
        updated_time = data.get('updated_time', '<s>Không công khai</s>')
        timezone = data.get('timezone', '<s>Không Công Khai</s>')
        photo_url = data.get('picture', {}).get('data', {}).get('url', None)
        about = data.get('about', '<s>Không Công Khai</s>')
        locked_status = "🔒Đã Khóa" if data['locked'] else "Không Khóa"
    
            # Xử lý số lượng bạn bè
        friend_count_str = data.get('friend_count', '0')  # Lấy dưới dạng chuỗi
        try:
            friend_count = int(friend_count_str)  # Chuyển đổi thành số nguyên
        except ValueError:
            friend_count = 0  # Nếu không thể chuyển đổi, gán giá trị mặc định
    
        friend_info = f'{friend_count} Bạn Bè' if friend_count > 0 else '<s>Không Công Khai</s>'
    
        message_text = (
            f"<blockquote>╭────────────⭓\n"
            f'│<a href="{photo_url}"> </a>𝗜𝗗: <code>{id}</code>\n'
            f'│ 𝗡𝗮𝗺𝗲: <a href="{linkk}">{name}\n</a>'
            f"│ 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲: {username}\n"
            f"│ 𝗩𝗲𝗿𝗶𝗳𝗶𝗲𝗱: {verified}\n"
            f"| 𝗟𝗼𝗰𝗸𝗲𝗱: {locked_status}\n"
            f"│ 𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝘁𝗶𝗺𝗲: {created_time}\n"
            f"│ 𝗚𝗲𝗻𝗱𝗲𝗿: {gender}\n"
            f"│ 𝗥𝗲𝗹𝗮𝘁𝗶𝗼𝗻𝘀𝗵𝗶𝗽𝘀: {relationship_status}\n"
            f"│ 𝗛𝗼𝗺𝗲𝘁𝗼𝘄𝗻: {hometown}\n"
            f"│ 𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻: {location}\n"
            f"│ 𝗪𝗼𝗿𝗸: {work}\n"
            f"│ 𝗕𝗶𝗿𝘁𝗵𝗱𝗮𝘆: {birthday}\n"
            f'│ 𝗙𝗼𝗹𝗹𝗼𝘄𝘀: <a href="{linkk}/followers">{followers}</a> Người Theo Dõi\n'
            f"│ 𝗙𝗿𝗶𝗲𝗻𝗱𝘀: {friend_info}\n"
            f"| 𝗔𝗯𝗼𝘂𝘁: {about}\n"
            f"├────────────⭔\n"
            f"│ 𝗟𝗼𝗰𝗮𝗹𝗲: {locale}\n"
            f"│ 𝗨𝗽𝗱𝗮𝘁𝗲 𝗧𝗶𝗺𝗲: {updated_time}\n"
            f"│ 𝗧𝗶𝗺𝗲 𝗭𝗼𝗻𝗲: GMT {timezone}\n"
            f"╰────────────⭓\n </blockquote>"
        )
        
        # Gửi ảnh cùng với thông báo
        if photo_url:
            send_message_with_photo(message.chat.id, message_text)
        else:
            bot.send_message(message.chat.id, message_text, parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')





#2FA
@bot.message_handler(commands=['2fa aahahshda'])
def get_2fa(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    if int(chat_id) not in GROUP_ID:
    	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    	return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        try:          
            phone_number = message.text.split()[1] # Ví dụ: Thay bằng số điện thoại thực tế
    
            # Gọi API để lấy mã 2FA
            response = requests.get(f"https://scaninfo.vn/api/2fa/2fa.php?key={phone_number}")
            data = response.json()
            chat_id = message.chat.id
            # Kiểm tra trạng thái của API
            if data["status"] == "success":
                code = data["code"]
                sent_message = bot.reply_to(message, '🔎')
                message_id = sent_message.message_id
                time.sleep(0.6)
                #bot.delete_message(chat_id=message.chat.id, message_id=message_id)
                bot.edit_message_text(chat_id = chat_id ,message_id = message_id, text = f" <blockquote>Mã 2FA Của Bạn Là: <code>{code}</code> </blockquote>" , parse_mode='HTML')
            else:
                bot.reply_to(message, "❌ Có Lỗi Xảy Ra Khi Lấy Mã 2FA. Vui Lòng Thử Lại Sau.")
        except Exception as e:
            bot.reply_to(message, f"Lỗi. Vui Lòng Nhập Token Để Lấy 2fa\n<blockquote>{str(e)} </blockquote>" , parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 


#HTML
@bot.message_handler(commands=['code'])
def code(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id  
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        if len(message.text.split()) == 1:
            bot.reply_to(message, ' <blockquote>Vui Lòng Nhập Đúng Cú Pháp.\nVí Dụ: /code + [link website] </blockquote>' , parse_mode='HTML')         
            return
               
        url = message.text.split()[1]
        try:
            response = requests.get(url, timeout = 10)
            if response.status_code != 200:
                bot.reply_to(message, ' <blockquote>Không Thể Lấy Mã Nguồn Từ Trang Web Này. Vui Lòng Kiểm Tra Lại URL. </blockquote>' , parse_mode='HTML')
                return
    
            content_type = response.headers.get('content-type', '').split(';')[0]
            if content_type not in ['text/html', 'application/x-php', 'text/plain']:
                bot.reply_to(message, ' <blockquote>Trang Web Không Phải Là HTML Hoặc PHP. Vui Lòng Thử Với URL Trang Web Chứa File HTML Hoặc PHP. <blockquote>' , parse_mode='HTML' )
                return
            source_code = response.text
            zip_file = io.BytesIO()
            with zipfile.ZipFile(zip_file, 'w') as zipf:
                zipf.writestr("source_code.html", source_code)  
            zip_file.seek(0)
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('👨‍💻')], is_big=True)
            bot.send_document(message.chat.id, zip_file, visible_file_name="file_web_trh.html")
        except Exception as e:
            bot.reply_to(message, f'<blockquote> Lỗi Không Thể Nhận Diện Trang Web. Vui Lòng Thử Lại\nTrang web phải có dạng https://...</blockquote> ' , parse_mode='HTML' )
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 






#TẢI VIDEO TIKTOK
@bot.message_handler(commands=['tiktok'])
def luuvideo_tiktok(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id  
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        if len(message.text.split()) == 1:
            bot.reply_to(message, ' <blockquote>❓VUI LÒNG NHẬP LINK VIDEO \n/tiktok [link video]. </blockquote>' , parse_mode='HTML')
            return
        linktt = message.text.split()[1]
        data = {
        'url': f'{linktt}',
        'count': '12',
        'cursor': '0',
        'web': '1',
        'hd': '1',
    }
        head = {
            "Host": "www.tikwm.com",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        }
        try:
            import html
            response = requests.post("https://www.tikwm.com/api/", data=data, headers=head).json()
            rq = response['data']
            tieude = rq['title']
            tieude = html.escape(tieude)
            view = rq['play_count']
            likes = rq["digg_count"]
            cmt = rq["comment_count"]
            nhac = 'https://www.tikwm.com' + rq['music']
            hd_video = rq.get('play', None)
            images = response['data'].get('images', [])
            hd_video2 = 'https://www.tikwm.com' + rq.get('hdplay', None)
            
            
            tgiaa = rq['author']
            linktgia = 'https://www.tiktok.com/@' + tgiaa['unique_id']
            tentgia = tgiaa['nickname']
            
          
            music_info = rq['music_info']
            music_url = music_info['play']
            title = music_info['title']
            author = music_info['author']
            thumb_url = 'https://www.tikwm.com' + rq['author']['avatar']
            # Tải nhạc và thumbnail tạm
            audio_file = requests.get(music_url).content
            thumb_file = requests.get(thumb_url).content

          
            timee = rq["create_time"]
            thoigiantao = time.strftime('🕛 %H:%M:%S \n📆 %d-%m-%Y', time.localtime(timee))

            keyboard = InlineKeyboardMarkup()
            btn_nhac = InlineKeyboardButton("💿 Tải Nhạc", url=f"https://api.zm.io.vn/download/?url={nhac}&extension=mp3&name=datienich2_bot&quality=audio")
            
            # Gửi thông báo ban đầu
            
            sent_message = bot.send_message( message.chat.id, f'<blockquote>➯ Xin Chờ Một Tí...!😴</blockquote>', parse_mode='HTML' ) #\n➯ Tiêu Đề: {tieude}\n➯ 👀 Số View: {view}</blockquote>', parse_mode='HTML' )
            
            #nếu ảnh
            if images:
                for i in range(0, len(images), 10):  # Gửi tối đa 10 ảnh mỗi nhóm
                    from telebot.types import InputMediaPhoto
                    group = images[i:i + 10]
                    media_group = [InputMediaPhoto(img) for img in group]
                    bot.send_media_group(message.chat.id, media_group)
                btn_tacgiaa = InlineKeyboardButton("✏ Tác Giả", url=f"{linktgia}")
                keyboard.add(btn_tacgiaa, btn_nhac)
      
                with open("temp.mp3", "wb") as f:
                    f.write(audio_file)
                with open("temp.jpg", "wb") as f:
                    f.write(thumb_file)
                with open("temp.mp3", "rb") as audio, open("temp.jpg", "rb") as thumb:
                    bot.send_audio(message.chat.id, audio=audio, title=title, performer=author, thumb=thumb, caption = f"<blockquote expandable>➯ Tác Giả: <a href='{linktgia}'>{tentgia}</a>\n➯ Tiêu Đề: {tieude}\n\n➯ 👀 Số View: {view}\n➯ ❤Số Tim: {likes}\n➯ 💬 Comment: {cmt}\n➯ Thời Gian Đăng:\n{thoigiantao}\nID <code>{rq['id']}</code></blockquote>", parse_mode='HTML', reply_markup=keyboard)
                os.remove("temp.mp3")
                os.remove("temp.jpg")
                    #bot.send_audio(message.chat.id,audio='https://sf16-ies-music-va.tiktokcdn.com/obj/tos-useast2a-ve-2774/ogzmBfxXWicoMbuccLzwiA32Ins1BbZzwAFSJm', caption=f'🔗 <a href="https://api.zm.io.vn/download/?url={nhac}&extension=mp3&name=datienich2_bot&quality=audio">📥 Download Nhạc</a>',parse_mode='HTML' )
                    
            # Nếu là video
            elif hd_video:
                linkz = 'https://www.tikwm.com' + hd_video
                try:
                    #nút tải video
                    btn_download = InlineKeyboardButton("📥 Tải video", url=f"https://api.zm.io.vn/download/?url={linkz}&extension=mp4&name=datienich2_bot&quality=audio")
                    btn_download_hd = InlineKeyboardButton("📥 Tải video HD", url=f"https://api.zm.io.vn/download/?url={hd_video2}&extension=mp4&name=datienich2_bot&quality=audio")
                    keyboard.add(btn_download, btn_download_hd)
                    keyboard.add(btn_nhac)
                    bot.send_video( message.chat.id, video=linkz, supports_streaming=True)
                    with open("temp.mp3", "wb") as f:
                        f.write(audio_file)
                    with open("temp.jpg", "wb") as f:
                        f.write(thumb_file)
                    with open("temp.mp3", "rb") as audio, open("temp.jpg", "rb") as thumb:
                        bot.send_audio(message.chat.id, audio=audio, title=title, performer=author, thumb=thumb, caption =  f"<blockquote expandable>➯ Tác Giả: <a href='{linktgia}'>{tentgia}</a>\n ➯ Tiêu Đề: {tieude}\n\n➯ 👀 Số View: {view}\n➯ ❤Số Tim: {likes}\n➯ 💬 Comment: {cmt}\n➯ Thời Gian Đăng:\n{thoigiantao}\nID <code>{rq['id']}</code></blockquote>",parse_mode='HTML', reply_markup=keyboard)
                    os.remove("temp.mp3")
                    os.remove("temp.jpg")
                    
                    #nút tải nhạc
                    #keyboard2 = InlineKeyboardMarkup()
#                    btn_nhac = InlineKeyboardButton("💿 Tải Nhạc", url=f"https://api.zm.io.vn/download/?url={nhac}&extension=mp3&name=datienich2_bot&quality=audio")
#                    keyboard2.add(btn_nhac)
#                    bot.send_audio(message.chat.id, audio=nhac,  parse_mode='HTML', reply_markup=keyboard2)
                except Exception as e:
                    #btn_down_hd = InlineKeyboardButton("📥 Tải video HD", url=f"https://api.zm.io.vn/download/?url={hd_video2}&extension=mp4&name=datienich2_bot&quality=audio")
                    #keyboard.add(btn_down_hd, btn_nhac)
                    with open("temp.mp3", "wb") as f:
                        f.write(audio_file)
                    with open("temp.jpg", "wb") as f:
                        f.write(thumb_file)
                    with open("temp.mp3", "rb") as audio, open("temp.jpg", "rb") as thumb:
                        bot.send_audio(message.chat.id, audio=audio, title=title, performer=author, thumb=thumb, caption =  f"<blockquote expandable>➯ Tác Giả: <a href='{linktgia}'>{tentgia}</a>\n ➯ Tiêu Đề: {tieude}\n\n➯ 👀 Số View: {view}\n➯ ❤Số Tim: {likes}\n➯ 💬 Comment: {cmt}\n➯ Thời Gian Đăng:\n{thoigiantao}\nID <code>{rq['id']}</code></blockquote>--------------------------------------------------<blockquote>Không Thể Gửi Video\nVui Lòng Tải Tại Đây👇</blockquote>",parse_mode='HTML', reply_markup=keyboard)
                    os.remove("temp.mp3")
                    os.remove("temp.jpg")
                    #bot.send_message(message.chat.id, f"<blockquote>Video Quá Nặng Tôi Không Thể Gửi Vui Lòng Tự Tải Tại Link Sau🤡: </blockquote>", parse_mode='HTML', reply_markup=keyboard) #\n\n<a href='https://api.zm.io.vn/download/?url={hd_video2}&extension=mp4&name=datienich2_bot&quality=audio'>📹 TẢI TẠI ĐÂY</a></blockquote>", parse_mode='HTML'   )
            
            else:
                bot.send_message(message.chat.id, "<blockquote>❗ Không tìm thấy nội dung hợp lệ (video hoặc ảnh). </blockquote>" , parse_mode='HTML' )
            bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id) 
        
        except Exception as e:
            error_chat_id = 7484921732
            bot.reply_to( message, f"<blockquote>❗Vui Lòng Xem Lại Link Tiktok </blockquote>",parse_mode='HTML' )
            bot.send_message(error_chat_id, f'TikTok:<blockquote>Lỗi: {e}</blockquote>' , parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 
        


#GET AVT FB
# Hàm lấy ảnh đại diện và tên người dùng từ liên kết Facebook
def lay_thong_tin_facebook(link):
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Tìm thẻ meta chứa tên người dùng
        name_tag = soup.find('meta', property='og:title')
        # Tìm thẻ meta chứa ảnh đại diện
        image_tag = soup.find('meta', property='og:image')
        if name_tag and image_tag:
            ten = name_tag.get('content')
            anh_dai_dien_url = image_tag.get('content')
            return ten, anh_dai_dien_url
        else:
            return None, None
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return None, None

@bot.message_handler(commands=['avtfb'])
def xu_ly_avtfb(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
    # Lấy liên kết từ lệnh
        try:
            link = message.text.split(' ', 1)[1]
            ten, anh_dai_dien_url = lay_thong_tin_facebook(link)
            sent_message = bot.send_message(message.chat.id, "🔎")
            # Chờ 0.6 giây
            time.sleep(0.5)
            if ten and anh_dai_dien_url:
                
                bot.send_photo(message.chat.id, photo=anh_dai_dien_url, caption= f'<blockquote>🔎 Thành Công\nFacebook: <a href="{link}">{ten}</a> </blockquote>' , parse_mode='HTML')           
            else:
                bot.reply_to(message, '<blockquote>❌ Không Thể Tìm Thấy Người Dùng Bằng Liên Kết Này. Vui Lòng Chắc Chắn Liên Kết Là Chính Xác Và Có Thể Truy Cập. </blockquote> ' , parse_mode='HTML' )
            bot.delete_message(message.chat.id, sent_message.message_id)
        except IndexError:
            bot.reply_to(message, ' <blockquote>❌ Vui Lòng Cung Cấp Liên Kết Facebook. </blockquote>\n<blockquote>Ví Dụ: /avtfb https://www.facebook.com/profile </blockquote>' , parse_mode='HTML' )
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')



#VOICE GOOGLE
@bot.message_handler(commands=['voice'])
def voice_command(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id  
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        chat_id = message.chat.id
        #if int(chat_id) not in GROUP_ID:
#        	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        	return
        if len(message.text.split()) == 1:
            bot.reply_to(message, ' <blockquote>⛔ Vui Lòng Nhập Đúng Định Dạng.\nVí Dụ: <code>/voice bot đz :))</code></blockquote>' , parse_mode='HTML')
            return
        text = ' '.join(message.text.split()[1:])
        if text:
            tts = gTTS(text, lang='vi', slow=False)
            tts.save('voice.mp3')
            voice_file = open('voice.mp3', 'rb')
            # Mở file âm thanh và gửi cho người dùng
            bot.send_audio(message.chat.id, voice_file)
    
            # Xóa file âm thanh sau khi gửi (tùy chọn)
            os.remove('voice.mp3')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 
        

# Hàm tính thời gian hoạt động của bot
start_time = time.time()

#THỜI GIAN ONLINE CỦA BOT
@bot.message_handler(commands=['time'])
def show_uptime(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id
    #if str(user_id) != ADMIN_ID:
  #      bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML')
     #   return
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} Giờ, {minutes} Phút, {seconds} Giây'
    bot.reply_to(message, f' <blockquote>⏰ Bot Đã Hoạt Động Được: {uptime_str} </blockquote>' , parse_mode='HTML' )



#CHAT GEMINI
@bot.message_handler(commands=['ask nfbfsk'])   #func=lambda message: True)     # 
def handle_ask(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id  
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        query = message.text.replace('/anfbfsk', '').strip()
        if not query:
            bot.reply_to(message, "Vui Lòng Nhập Câu Hỏi Của Bạn Sau Lệnh /ask.")
            return
       
        api_url = f'https://thichlaptrinh.space/gpt.php?ask={query}'   
       # 'https://tool.xwm.lol/api.php?msg={query}'
        
        try:
            # Gửi yêu cầu đến API và nhận kết quả, bỏ qua xác thực SSL
            response = requests.get(api_url, verify=True)
            
            # Kiểm tra kết quả từ API
            if response.status_code == 200:
                # result =    response.text            
    		
                api_response = response.json()
                result = api_response.get('message', {}).get("message", 'Không Có Kết Quả Từ API')
            else:
                result = 'Đã Xảy Ra Lỗi Khi Xử Lý Yêu Cầu.'
        except Exception as e:
            result = f'Có Lỗi Xảy Ra: {str(e)}'
        
        # Chuẩn bị các thông tin bổ sung
        current_time = datetime.datetime.now().strftime('%Hh %Mp %Ss')
     #   username = message.from_user.username if message.from_user.username else "Không có username"
        join_message = "🤖"
    
    # Tạo nội dung tin nhắn trả lời
        reply_text = f'''⏳ Thời Gian: {current_time}
👤 Người Dùng: [{first_name}](tg://user?id={user_id})

{result}{join_message} '''
     
    # Gửi kết quả trả về cho người dùng
        bot.reply_to(message, reply_text ,parse_mode='Markdown')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 
        


@bot.message_handler(commands=['ask'])
def handle_assk(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    # Kiểm tra người dùng có trong blocklist không
    if any(str(user_id) in file for file in blocklist_files):
        return
    first_name = message.from_user.first_name
    if is_active: 
        # Kiểm tra xem người dùng đã lấy key hôm nay chưa
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        chat_id = message.chat.id
        #if int(chat_id) not in GROUP_ID:
#        	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        	return 
        # Lấy nội dung câu hỏi từ tin nhắn
        query = message.text.replace('/ask', '').strip()
        if not query:
            bot.reply_to(message, "Vui Lòng Nhập Câu Hỏi Của Bạn Sau Lệnh /ask.")
            return
        
        # Sử dụng API mới
        api_url = f'https://tool.xwm.lol/api.php?msg={query}'
        
        try:
            # Gửi yêu cầu đến API và nhận kết quả, bỏ qua xác thực SSL
            response = requests.get(api_url, verify=False)
            
            # Kiểm tra kết quả từ API
            if response.status_code == 200:
                result = response.text
                # Đối với phản hồi dạng văn bản
                result = result.replace('\\n', '\n')  
                result = result.replace('\\"', '"')
                # Markdown sử dụng 2 khoảng trắng để hiển thị dòng mới

            else:
                result = 'Đã Xảy Ra Lỗi Khi Xử Lý Yêu Cầu.'
        except Exception as e:
            result = f'API Lỗi :)'
        
        # Chuẩn bị các thông tin bổ sung
        current_time = datetime.datetime.now().strftime('%Hh %Mp %Ss')
        join_message = "🤖"
    
        # Tạo nội dung tin nhắn trả lời
        reply_text = f'⏳ Thời Gian: {current_time}\n👤 Người Dùng: [{first_name}](tg://user?id={user_id})\n{result}\n{join_message} '
     
        # Gửi kết quả trả về cho người dùng
        bot.reply_to(message, reply_text , parse_mode='Markdown', disable_web_page_preview=True)
    
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML') 




#RANDOM
gif_url = 'https://nekos.best/api/v2/hug/5721b0f4-a2ed-4de6-9ea3-763601c72fc9.gif'
@bot.message_handler(commands=['random'])
def random_anh(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 
    user_id = message.from_user.id
    
    # Kiểm tra nếu người dùng đã lấy key hôm nay
    if is_active:
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>', parse_mode='HTML')
            return

        # Tạo bàn phím với 5 nút, sắp xếp như yêu cầu
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("/waifu1")
        button2 = types.KeyboardButton("/waifu2")
        button3 = types.KeyboardButton("/neko")
        button4 = types.KeyboardButton("/kitsune")
        button5 = types.KeyboardButton("/husbando")
        keyboard.row(button1, button2)
        keyboard.row(button3, button4)
        keyboard.add(button5)

        text = '''<blockquote>🔎 Các Loại Ảnh Random:
/waifu1 - Random Ảnh Waifu
/waifu2 - Mup Hơn =)))
/neko - Random Neko
/kitsune - Ảnh Mấy Bé Tai Mèo=))
/husbando - Anime Nam </blockquote>'''
        chat_id = message.chat.id

        # Gửi tin nhắn kèm bàn phím
        bot.send_animation(chat_id, gif_url, caption = text, reply_markup=keyboard, parse_mode='HTML')
        
#bot.send_animation(chat_id , , , parse_mode='HTML' )
    else:
        bot.reply_to(message, '🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.', parse_mode='HTML')


#ẢNH WAIFU
def get_waifu_image():
    response = requests.get("https://nekos.best/api/v2/waifu")
    data = response.json()
    image_data = data['results'][0]
    return image_data['url'], f" <blockquote>🎨 Tác Giả: <a href='{image_data['artist_href']}' a>{image_data['artist_name']}</a>\n🔗 Nguồn: {image_data['source_url']} </blockquote>"
@bot.message_handler(commands=['waifu1'])
def send_waifu_image(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('😍')], is_big=True)
        image_url, caption = get_waifu_image()
        bot.send_photo(chat_id=message.chat.id, photo=image_url, caption=caption,  parse_mode='HTML' )
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')
    


# WAIFU 2
def fetch_image_data():
    try:
        response = requests.get('https://api.waifu.im/search')
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        data = response.json()
        if 'images' in data and len(data['images']) > 0:
            image_data = data['images'][0]
            url = image_data.get('url')
            source = image_data.get('source')
            # Kiểm tra xem URL có hợp lệ không
            if url and requests.head(url).status_code == 200:
                return url, source
            else:
                return None, "❌ URL ảnh không hợp lệ hoặc không thể truy cập."
        return None, "❌ Không tìm thấy hình ảnh."
    except requests.RequestException as e:
        return None, f"❌ Lỗi HTTP: \n📌 {e.response.status_code} - {e.response.text}"
    except ValueError:
        return None, "❌ Lỗi phân tích dữ liệu JSON."

@bot.message_handler(commands=['waifu2'])
def handle_image_request(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        url, source = fetch_image_data()
        if url:
            try:
                bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('🌚')], is_big=True)
                bot.send_photo(chat_id=message.chat.id, photo=url, caption=f"<blockquote>🎉 Lấy Ảnh Thành Công\n🔗 Nguồn Ảnh: {source} </blockquote>" , parse_mode='HTML' )
            except telebot.apihelper.ApiTelegramException as e:
                bot.send_message(chat_id=message.chat.id, text=f" <blockquote>🤡 Gửi Nhanh Quá Nên Lỗi Ấy :))))\nGửi Chậm Thôiii\n\n❌ Lỗi Khi Gửi Hình Ảnh: \n{e} </blockquote> " , parse_mode='HTML' )
        else:
            bot.send_message(chat_id=message.chat.id, text=source)
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')




#Neko
def get_neko_image():
    response = requests.get("https://nekos.best/api/v2/neko")
    data = response.json()
    image_data = data['results'][0]
    return image_data['url'], f" <blockquote>🎨 Tác Giả: <a href='{image_data['artist_href']}' a>{image_data['artist_name']}</a>\n🔗 Nguồn: {image_data['source_url']} </blockquote>"
@bot.message_handler(commands=['neko'])
def send_neko_image(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
   # 	bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #	return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('😍')], is_big=True)
        image_url, caption = get_neko_image()
        bot.send_photo(chat_id=message.chat.id, photo=image_url, caption=caption,  parse_mode='HTML' )
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')
    
    
    
#chồng
def get_husbando_image():
    response = requests.get("https://nekos.best/api/v2/husbando", timeout = int('10'))
    data = response.json()
    image_data = data['results'][0]
    return image_data['url'], f" <blockquote>🎨 Tác Giả: <a href='{image_data['artist_href']}' a>{image_data['artist_name']}</a>\n🔗 Nguồn: {image_data['source_url']} </blockquote>"
@bot.message_handler(commands=['husbando'])
def send_husbando_image(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 Và @botvipfc !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"): 
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('❤️‍🔥')],is_big=True)
        image_url, caption = get_husbando_image()
        bot.send_photo(chat_id=message.chat.id, photo=image_url, caption=caption,  parse_mode='HTML' )
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')
    
    


#mocky
@bot.message_handler(commands=['mocky'])
def handle_mocky(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    if int(chat_id) not in GROUP_ID:
        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 Và @botvipfc !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
        return 
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"): 
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
    # Tách phần nội dung từ tin nhắn
        user_text = re.sub(r"^/mocky(?:@\w+)?\s*", "", message.text.strip())
        # Nếu không có nội dung, gửi hướng dẫn
        if not user_text:
            bot.reply_to( message, ("<blockquote>❓Sử Dụng Lệnh /mocky {Văn Bản} Để Upload Nội Dung Lên Mocky.</blockquote>"), parse_mode='HTML')
            return
    
        # Nếu có nội dung, gửi lên Mocky API
        MOCKY_API_URL = 'https://api.mocky.io/api/mock'
    
        payload = {
            'status': 200,
            'content': user_text,  # Nội dung từ người dùng
            'content_type': 'text/json',
            'charset': 'UTF-8',
            'secret': 'J2eEWZikLqc07FBDz97ErdwOSBmixhcvA6mj',
            'expiration': 'never',
        }
    
        try:
            response = requests.post(MOCKY_API_URL, json=payload, timeout=10)
            response_data = response.json()
            if response.status_code == 201:
                mocky_link = response_data.get('link')
                bot.reply_to( message, (f"<blockquote>✅ Upload Mocky Thành Công!\n🔗 <code>{mocky_link}</code></blockquote>"), parse_mode='HTML')
            else:
                bot.reply_to(message, (f"<blockquote>❌Upload Thất Bại! Mã Lỗi: \n{response.status_code}</blockquote>"), parse_mode='HTML')
        except Exception as e:
            bot.reply_to( message, (f"<blockquote>❌Có Lỗi Xảy Ra:\n<code>{str(e)}</code></blockquote>"),parse_mode='HTML' )
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')
        
        


#Catbox
import traceback
# Lưu trạng thái tin nhắn cần reply
tin_nhan_catbox = {}
error_chat_id = 7484921732
# Hàm tải file lên Catbox và trả về link
def upload_to_catbox(file_path, mime_type):
    url = "https://catbox.moe/user/api.php"
    files = {
        'reqtype': (None, 'fileupload'),
        'userhash': (None, ''),
        'fileToUpload': (os.path.basename(file_path), open(file_path, 'rb'), mime_type),
    }
    response = requests.post(url, files=files, timeout = 10)
    if response.status_code == 200:
        return response.text.strip()  # Link từ Catbox
    else:
        return f"Upload failed. Error: {response.status_code}"
# Lệnh /catbox
@bot.message_handler(commands=['catbox'])
def start_catbox(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    if int(chat_id) not in GROUP_ID:
        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 Và @botvipfc !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
        return 
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"): 
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        # Gửi tin nhắn yêu cầu người dùng reply
        msg = bot.reply_to(
            message, 
            "<blockquote>🌟Hãy Reply Tin Nhắn Này Bằng Ảnh, Video, File Mà Bạn Muốn Tải Lên Catbox! </blockquote>",  parse_mode = "HTML")
        # Lưu tin nhắn cần reply
        tin_nhan_catbox[msg.message_id] = message.chat.id
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')
        
# Xử lý khi người dùng gửi file
@bot.message_handler(content_types=['document', 'photo', 'video', 'audio'])
def handle_file(message):
    try:
        # Kiểm tra tin nhắn có phải là reply đúng tin nhắn yêu cầu không
        if not message.reply_to_message or message.reply_to_message.message_id not in tin_nhan_catbox:
            #bot.reply_to(message, "Bạn cần dùng lệnh /catbox và reply tin nhắn yêu cầu!")
            return
        # Kiểm tra chat ID có khớp không
        if tin_nhan_catbox[message.reply_to_message.message_id] != message.chat.id:
            #bot.reply_to(message, "Bạn không thể reply tin nhắn yêu cầu từ một chat khác!")
            return
        user_id = message.from_user.id
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"): 
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        # Lấy thông tin tệp từ Telegram
        file_info = None
        if message.document:
            file_info = bot.get_file(message.document.file_id)
            file_name = message.document.file_name
            mime_type = message.document.mime_type
        elif message.photo:
            file_info = bot.get_file(message.photo[-1].file_id)
            file_name = "photo.jpg"
            mime_type = "image/jpeg"
        elif message.video:
            file_info = bot.get_file(message.video.file_id)
            file_name = "video.mp4"
            mime_type = message.video.mime_type
        elif message.audio:
            file_info = bot.get_file(message.audio.file_id)
            file_name = message.audio.file_name or "audio.mp3"
            mime_type = message.audio.mime_type

        if not file_info:
            bot.reply_to(message, "<blockquote>❌Không Thể Xử Lí Tệp Này.</blockquote>",  parse_mode = "HTML")
            return

        # Tải file từ Telegram về máy
        downloaded_file = bot.download_file(file_info.file_path)
        local_file_path = f"downloads/{file_name}"
        os.makedirs("downloads", exist_ok=True)
        with open(local_file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        # Upload lên Catbox
        catbox_link = upload_to_catbox(local_file_path, mime_type)

        # Trả về link cho người dùng
        bot.reply_to(message, f"✅Tải Lên Thành Công!\n<code>{catbox_link}</code>", parse_mode = "HTML")
        os.remove(local_file_path) # Xóa file tạm
        
    except PermissionError:
    	return
    except Exception as e:
        bot.send_message(message ,f"Có lỗi xảy ra: <blockquote>{str(e)}</blockquote>", parse_mode = "HTML")
        error_message = (
            f"<blockquote>Lỗi xảy ra khi xử lý lệnh /catbox\n"
            f"Người dùng: @{message.from_user.username} (ID: {message.from_user.id})\n"
            f"Chat ID: {message.chat.id}\n"
            f"Lệnh: /catbox\n"
            f"Chi tiết lỗi:</blockquote>"
            f"\n<blockquote>{e}</blockquote>"
        )
        bot.send_message(error_chat_id, error_message, parse_mode="HTML")
        print(traceback.format_exc())




#mấy em tai mèo
def get_kitsune_image():
    response = requests.get("https://nekos.best/api/v2/kitsune")
    data = response.json()
    image_data = data['results'][0]
    return image_data['url'], f" <blockquote>🎨 Tác Giả: <a href='{image_data['artist_href']}' a>{image_data['artist_name']}</a>\n🔗 Nguồn: {image_data['source_url']} </blockquote>"
@bot.message_handler(commands=['kitsune'])
def send_kitsune_image(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        bot.set_message_reaction(chat_id=message.chat.id, message_id=message.id,reaction=[ReactionTypeEmoji('💯')], is_big=True)
        image_url, caption = get_kitsune_image()
        bot.send_photo(chat_id=message.chat.id, photo=image_url, caption=caption,  parse_mode='HTML' )
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')
    


#ID FB
def lay_thong_tinn_facebook(link):
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Tìm thẻ meta chứa tên người dùng
        name_tag = soup.find('meta', property='og:title')
        if name_tag:
            ten = name_tag.get('content')
            return ten
        else:
            return None
    except Exception as e:
        print(f"🤡🤡 Đã xảy ra lỗi : {e}")
        return None

def get_id(link):
    url = "https://id.traodoisub.com/api.php"
    headers = {
        "Host": "id.traodoisub.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {'link': link}
    try:
        response = requests.post(url, headers=headers, data=data, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

@bot.message_handler(commands=['idfb'])
def handle_idfb(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 
    user_id = message.from_user.id
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        try:
            parts = message.text.split(maxsplit=1)
            if len(parts) == 1 or not parts[1].strip().startswith('http'):
                bot.reply_to(message, "<blockquote>😠 Nhập Link Facebook Theo Định Dạng: \n/idfb [link fb]</blockquote>", parse_mode='HTML')
            else:
                link = parts[1].strip()
                processing_message = bot.reply_to(message, '<blockquote>⏳ Đợi Tí Tao Đang Xử Lý Link.. </blockquote>', parse_mode='HTML')
                time.sleep(0.9)  
                chat_id = message.chat.id
                message_id = processing_message.message_id
    
                bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='<blockquote>⏳ Hmmm... </blockquote>', parse_mode='HTML')
                time.sleep(0.5)
                bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='<blockquote>🔎 Đã Có Kết Quả!</blockquote>', parse_mode='HTML')
                
                result = get_id(link)
                
                if "error" in result:
                    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="<blockquote>❌ Link Lỗi Hoặc Gửi Sai Link, Tôi Không Lấy Được Uid Từ Link Đó.\nXem Lại Link Đê </blockquote>", parse_mode='HTML')
                elif "id" in result:
                    fb_id = result["id"]
                    fb_name = lay_thong_tinn_facebook(link)
                    if fb_name:
                        message_text = f'''<blockquote>╭────────────⬠
║Tên Facebook: <a href="{link}">{fb_name}</a>
║UID : <code>{fb_id}</code>
║Nhấn Để Copy👆
╰────────────⬠ </blockquote>
'''
                        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text, parse_mode='HTML', disable_web_page_preview=True)
                    else:
                        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'''
<blockquote>╭─────────────⬠
║Tên Facebook: <a href="{link}">Không Xác Định</a>
║UID : <code>{fb_id}</code>
║Nhấn Để Copy👆
╰─────────────⬠</blockquote>
''', parse_mode='HTML')
                else:
                    bot.reply_to(message, "<blockquote>😵 Lỗi Không Xác Định.\n@trn_hwp2 Lên Xử Lý Coi :))</blockquote>", parse_mode='HTML')
        except IndexError:
            bot.reply_to(message, "<blockquote>❌Gửi Link Từ Từ Thôi, Nhanh Quá Nó Lỗi Ấy :))))\n\nLỗi Định Dạng Link. Vui Lòng Nhập Lại Theo Định Dạng: /idfb [linkfb]</blockquote>", parse_mode='HTML')
        except Exception as e:
            bot.reply_to(message, f"<blockquote>😵 Đã Xảy Ra Lỗi: {str(e)}\nVui Lòng Thử Lại Sau.</blockquote>", parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')





# GỬI TIN NHẮN ĐẾN ID
user_data = {}  # Để lưu trữ tạm thời ID và nội dung tin nhắn của người dùng

@bot.message_handler(commands=['mem'])
def send_message(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    user_data[chat_id] = {}  # Khởi tạo một dictionary để lưu dữ liệu của người dùng này
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML' )
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return
    ask_for_id_message = bot.send_message(chat_id, " <blockquote>🏷 Hãy Nhập ID Người Bạn Muốn Tôi Gửi Tin Nhắn : </blockquote>" , parse_mode='HTML' )
   # ask_for_id_message_id = ask_for_id_message.message_id
    user_data[chat_id]['ask_for_id_message_id'] = ask_for_id_message.message_id
    user_data[chat_id]['state'] = 'waiting_for_id'
   # bot.delete_message(chat_id=chat_id, message_id=message.message_id)
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('state') == 'waiting_for_id')
def process_id(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    ask_for_id_message_id = user_data[chat_id]['ask_for_id_message_id']  # Lấy giá trị từ dictionary

    user_data[chat_id]['id'] = message.text
    bot.send_message(chat_id, " <blockquote>📝 Tiếp Theo Hãy Reply Tin Nhắn Này Và Nhập nội Dung Tin Nhắn: </blockquote>" , parse_mode='HTML' )
    time.sleep(1)
    bot.delete_message(chat_id=chat_id, message_id=message.message_id)
    bot.delete_message(chat_id=chat_id, message_id=ask_for_id_message_id)
    user_data[chat_id]['state'] = 'waiting_for_text'

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('state') == 'waiting_for_text')
def process_text(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    text = message.text
    target_id = user_data[chat_id]['id']
    target_user = bot.get_chat(target_id)  # Đảm bảo dòng này nằm trước khi sử dụng target_user
    target_first_name = target_user.first_name
    del user_data[chat_id]  # Xóa dữ liệu của người dùng sau khi gửi tin nhắn
    try:
        bot.send_message(chat_id=target_id,text= f'<blockquote>🐰 Đây Là Tin Nhắn Được Gửi Từ <a href="tg://user?id=7484921732">Admin</a>\n🐰 Nếu Muốn Nhắn Lại Cho <a href="tg://user?id=7484921732">Admin</a> Vui Lòng Nhắn Trực Tiếp Hoặc Sử Dụng Lệnh /chat Để Chat Nhanh.\n\n🎟 Nội Dung Tin Nhắn: </blockquote>\n<blockquote>{text}</blockquote>', parse_mode='HTML' )
        bot.send_message(chat_id, f''' <blockquote>💭 Tin Nhắn Đã Được Gửi Đi
🏷 ID Người Nhận: <code>{target_id}</code>
👤 Người Nhận: <a href="tg://user?id={target_id}">{target_first_name}</a>
🎟 Nội Dung Tin Nhắn Bạn Gửi: </blockquote>
<blockquote>{text} </blockquote>''' , parse_mode='HTML' )
        bot.delete_message(chat_id=chat_id, message_id=message.message_id)
    except telebot.apihelper.ApiException as e:
        bot.send_message(chat_id, f" <blockquote>❌ Lỗi Khi Gửi Tin Nhắn.</blockquote>\n<blockquote>{e} </blockquote>" , parse_mode='HTML' )

#import psutil
#@bot.message_handler(commands=['memory'])
#def memory_check(message):
#    ram = psutil.virtual_memory()
#    process = psutil.Process(os.getpid())
#    mem_bot = process.memory_info().rss / 1024 / 1024  # MB

#    total_gb = ram.total / 1024**3
#    used_gb = ram.used / 1024**3
#    free_gb = ram.available / 1024**3
#    percent = ram.percent

#    text = (
#        "╭──[ ⚙️ Memory Monitor ]──╮\n"
#        f"├ 🧠 Bot usage : `{mem_bot:.1f} MB`\n"
#        f"├ 💾 Total RAM : `{total_gb:.1f} GB`\n"
#        f"├ 📊 Used RAM  : `{used_gb:.1f} GB` ({percent}%)\n"
#        f"├ 🟢 Free RAM  : `{free_gb:.1f} GB`\n"
#        "╰────────────────────────╯"
#    )

#    bot.reply_to(message, text, parse_mode='Markdown')



#THÔNG TIN THÚ VỊ VỀ MÈO
def get_cat_fact():
    
    response = requests.get('https://catfact.ninja/fact', timeout = int('10'))
    if response.status_code == 200:
        return response.json().get('fact')
    else:
        return "Không thể lấy thông tin về mèo."
def translate_to_vietnamese(text):
    translator = Translator(to_lang="vi")
    return translator.translate(text)

def format_text(text):
    # Chuyển tất cả các chữ cái đầu của từng từ thành chữ hoa
    return ' '.join(word.capitalize() for word in text.split())
@bot.message_handler(commands=['fact'])
def send_cat_fact(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    chat_id = message.chat.id
    if int(chat_id) not in GROUP_ID:
        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
        return 
    user_id = message.from_user.id
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>' , parse_mode='HTML')
            return
        
        fact = get_cat_fact()
        translated_fact = translate_to_vietnamese(fact)
        formatted_fact = format_text(translated_fact)
        bot.reply_to(message, f' <blockquote>{formatted_fact} </blockquote>' , parse_mode='HTML' )
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')        


#import schedule
#import threading
#def scheduled_message():
#    bot.send_message(-1002103359217, " <blockquote><b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng❤️‍🔥 </b></blockquote>" , parse_mode='HTML' )

# Lên lịch để nhắn tin mỗi 30 phút
#schedule.every(30).minutes.do(scheduled_message)

#def run_schedule():
#    while True:
#        schedule.run_pending()
#        time.sleep(1)

#schedule_thread = threading.Thread(target=run_schedule)
#schedule_thread.start()
    

def is_admin(chat_id, user_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ['administrator', 'creator']
    except telebot.apihelper.ApiException:
        return False

@bot.message_handler(commands=['mute'])
def mute_user(message):
    try:
        # Kiểm tra quyền của bot
        bot_status = bot.get_chat_member(message.chat.id, bot.get_me().id)
        if bot_status.status not in ['administrator', 'creator']:
            bot.send_message(message.chat.id, "Bot cần quyền quản trị viên để thực hiện lệnh này.")
            return
        
        # Kiểm tra nếu người dùng không phải quản trị viên
        if not is_admin(message.chat.id, message.from_user.id):
            bot.send_message(message.chat.id, "Chỉ quản trị viên mới có thể sử dụng lệnh này.")
            return

        # Kiểm tra nếu reply tin nhắn
        if not message.reply_to_message:
            bot.send_message(message.chat.id, "Vui lòng reply tin nhắn người cần mute.")
            return

        target_user_id = message.reply_to_message.from_user.id
        args = message.text.split()

        # Kiểm tra thời gian mute
        duration = 0  # Mặc định là mute vĩnh viễn
        if len(args) > 1:
            duration_str = args[1]
            if duration_str.endswith("d") and duration_str[:-1].isdigit():
                duration = int(duration_str[:-1]) * 86400  # x ngày
            elif duration_str.endswith("h") and duration_str[:-1].isdigit():
                duration = int(duration_str[:-1]) * 3600  # x giờ
            elif duration_str.endswith("m") and duration_str[:-1].isdigit():
                duration = int(duration_str[:-1]) * 60  # x phút
            else:
                bot.send_message(message.chat.id, "Thời gian không đúng. Sử dụng: Xd (ngày), Xh (giờ), hoặc Xm (phút).")
                return

        # Kiểm tra nếu mute chính bot hoặc quản trị viên
        chat_member = bot.get_chat_member(message.chat.id, target_user_id)
        if chat_member.status in ['administrator', 'creator']:
            bot.send_message(message.chat.id, "Không thể cấm quản trị viên.")
            return
        if target_user_id == bot.get_me().id:
            bot.send_message(message.chat.id, "Không thể cấm bot.")
            return

        # Thực hiện mute
        until_date = time.time() + duration if duration > 0 else 0
        bot.restrict_chat_member(
            message.chat.id, 
            target_user_id, 
            until_date=until_date, 
            can_send_messages=False
        )
        
        # Thông báo kết quả
        mute_time = f"{args[1]}" if duration > 0 else "vĩnh viễn"
        bot.send_message(message.chat.id, f"<a href='tg://user?id={chat_member.user.id}'>{chat_member.user.first_name}</a> Đã Bị Cấm Chat Trong Thời Gian: {mute_time}." , parse_mode='HTML' )

    except telebot.apihelper.ApiException as e:
        if "Bad Request: invalid user_id specified" in str(e):
            bot.send_message(message.chat.id, "Không tìm thấy người dùng với ID này.")
        elif "Bad Request: PARTICIPANT_ID_INVALID" in str(e):
            bot.send_message(message.chat.id, "Không tìm thấy người dùng trong nhóm.")
        elif "Bad Request: not enough rights to restrict/unrestrict chat member" in str(e):
            bot.send_message(message.chat.id, "Bot không có quyền cấm người dùng. Vui lòng cấp quyền cấm người dùng cho bot.")
        else:
            bot.send_message(message.chat.id, f"Đã xảy ra lỗi: {str(e)}.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Đã xảy ra lỗi: {str(e)}.")



@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    try:
        # Kiểm tra quyền của bot
        bot_status = bot.get_chat_member(message.chat.id, bot.get_me().id)
        if bot_status.status not in ['administrator', 'creator']:
            bot.send_message(message.chat.id, "Bot cần quyền quản trị viên để thực hiện lệnh này.")
            return

        # Kiểm tra nếu người dùng không phải quản trị viên
        if not is_admin(message.chat.id, message.from_user.id):
            bot.send_message(message.chat.id, "Chỉ quản trị viên mới có thể sử dụng lệnh này.")
            return

        # Kiểm tra nếu reply tin nhắn
        if not message.reply_to_message:
            bot.send_message(message.chat.id, "Vui lòng reply tin nhắn người cần unmute.")
            return

        target_user_id = message.reply_to_message.from_user.id

        # Thực hiện unmute
        bot.restrict_chat_member(
            message.chat.id, 
            target_user_id, 
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_invite_users=True
        )
        
        # Thông báo kết quả
        bot.send_message(message.chat.id, f'Đã gỡ cấm <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>.', parse_mode='HTML' )

    except telebot.apihelper.ApiException as e:
        if "Bad Request: invalid user_id specified" in str(e):
            bot.send_message(message.chat.id, "Không tìm thấy người dùng với ID này.")
        elif "Bad Request: PARTICIPANT_ID_INVALID" in str(e):
            bot.send_message(message.chat.id, "Không tìm thấy người dùng trong nhóm.")
        elif "Bad Request: not enough rights to restrict/unrestrict chat member" in str(e):
            bot.send_message(message.chat.id, "Bot không có quyền gỡ cấm người dùng. Vui lòng cấp quyền quản lý cho bot.")
        else:
            bot.send_message(message.chat.id, f"Đã xảy ra lỗi: {str(e)}.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Đã xảy ra lỗi: {str(e)}.")



#Tính Tuổi
def validate_date_format(date_string):
    """Hàm kiểm tra định dạng ngày sinh (DD-MM-YYYY)"""
    pattern = r"^\d{2}-\d{2}-\d{4}$"
    return re.match(pattern, date_string) is not None
def get_age_details(date_string):
    """Hàm lấy thông tin tuổi từ API và trả về dưới dạng chuỗi"""
    api_url = f"https://api.sumiproject.net/date?date={date_string}"
    response = requests.get(api_url, timeout = int('10')).json()
    text = "<blockquote>📆 Bạn Đã Sống Được:\n"
    text += f"- {response['years']} Năm\n"
    text += f"- {response['months']} Tháng\n"
    text += f"- {response['weeks']} Tuần\n"
    text += f"- {response['days']} Ngày\n"
    text += f"- {response['hours']} Giờ\n"
    text += f"- {response['minutes']} Phút\n"
    text += f"- {response['seconds']} Giây </blockquote>" 
    return text

@bot.message_handler(commands=['tuoi'])
def send_welcome(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    #chat_id = message.chat.id
    #if int(chat_id) not in GROUP_ID:
#        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
#        return 
    if is_active: 
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>', parse_mode='HTML')
            return

        # Xử lý lệnh /tuoi và trả về kết quả
        try:
            date_string = message.text.split()[1]
            
           # Kiểm tra định dạng ngày sinh
            if not validate_date_format(date_string):
                bot.reply_to(message, "Bạn Cần Nhập Đúng Định Dạng Ngày Sinh\n<blockquote>DD-MM-YYYY </blockquote>\nVí Dụ: 01-01-2000" , parse_mode='HTML')
                return
            # Kiểm tra ngày, tháng, năm hợp lệ
            day, month, year = map(int, date_string.split('-'))
            if not (1 <= month <= 12 and 1 <= day <= 31):
                bot.reply_to(message, " <blockquote>Ngày Hoặc Tháng Không Hợp Lệ, Vui Lòng Nhập Lại. </blockquote>" , parse_mode='HTML')
                return
    
            # Kiểm tra năm nhuận để điều chỉnh số ngày trong tháng 2
            if month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    # Năm nhuận
                    if day > 29:
                        bot.reply_to(message, " <blockquote> Tháng 2 Năm Nhuận Chỉ Có 29 Ngày. </blockquote>" , parse_mode='HTML')
                        return
                else:
                    # Không phải năm nhuận
                    if day > 28:
                        bot.reply_to(message, " <blockquote> Năm Đó Không Phải Năm Nhuận, Tháng 2 Chỉ Có 28 Ngày. </blockquote>" , parse_mode='HTML')
                        return
    
            # Nếu vượt qua tất cả kiểm tra, mới gọi API
            result = get_age_details(date_string)
            bot.reply_to(message, result , parse_mode='HTML' )
    
        except Exception as e:
            bot.reply_to(message, "Đã Xảy Ra Lỗi. Vui Lòng Kiểm Tra Lại Định Dạng Ngày Sinh.\n <blockquote>DD-MM-YYYY</blockquote>" , parse_mode='HTML')
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')            
        
        
        

        
    # Gửi tin nhắn cho bạn (thay thế 'YOUR_ID' bằng ID của bạn)
#        bot.send_message(chat_id=ADMIN_ID , text= f'Người dùng  <a href="tg://user?id={chat_id}">{user_name}</a>  (ID: {chat_id}) đã gửi: {text}' , parse_mode='HTML' )
        
       
       
       
#NGƯỜI DÙNG NHẮN TIN QUA BOT TỚI ADMIN
reply_to_message_ids = set()
@bot.message_handler(commands=['chhhaaat'])
def start(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    chat_id = message.chat.id 
    if is_active: 
     # Lưu trữ chat_id để xóa tin nhắn sau
        if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
            bot.reply_to(message, text=' <blockquote>⛔ Dùng /getkey Để Lấy Key Và Dùng /key Để Nhập Key Hôm Nay. </blockquote>' , parse_mode='HTML')
            return
        # Gửi tin nhắn chào mừng
        welcome_message = bot.send_message(chat_id, ' <blockquote>🤖 Xin Chào!\n📥 Đây Là Lệnh Thông Qua Bot Để Nhắn Tin Tới Admin (Nhắn Với Admin Bằng Bot Này) </blockquote>' , parse_mode='HTML' )
        welcome_message_id = welcome_message.message_id
    
        
        # Gửi tin nhắn cần reply (thêm reply_markup để ẩn nút Reply)
        reply_markup = telebot.types.ReplyKeyboardRemove()  # Xóa nút Reply
        text = " <blockquote>💭Sau Khi Tin Nhắn Trên Biến Mất, Hãy Reply Tin Nhắn Này Để Gửi Tin Nhắn Tới Admin. </blockquote>"
        time.sleep(1)
        reply_message = bot.send_message(chat_id, text, reply_markup=reply_markup,  parse_mode='HTML')
        time.sleep(2)
        bot.delete_message(chat_id=chat_id, message_id=welcome_message_id)
    
        # Thêm ID của cả 2 tin nhắn vào danh sách
    #    reply_to_message_ids.add(welcome_message.message_id)
        reply_to_message_ids.add(reply_message.message_id)
    else:
        bot.reply_to(message, '<blockquote>🔒 Bot Đang Được Bảo Trì. \n⏳ Vui Lòng Thử Lại Sau.</blockquote>', parse_mode='HTML')        
        




###############################
#bot2
#########################
TOKEN2 = '7463617844:AAEDT9qo0-HBIn5l1ggVXQVmOIybRLm-HQM'
GROUP_ID2 = -1002427257416  # ID nhóm của bạn
bot2 = telebot.TeleBot(TOKEN2)

@bot2.message_handler(func=lambda message: True) 
def delete_and_mute(message):
    chat_idd = message.chat.id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if "notcoin" in message.text.lower() or "t.me/" in message.text.lower():
        try:
            # Xóa tin nhắn
            bot2.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            # Tắt tiếng người gửi (mute vĩnh viễn)
            bot2.restrict_chat_member(
                chat_id=GROUP_ID2, 
                user_id=message.from_user.id, 
                permissions=telebot.types.ChatPermissions(can_send_messages=False)
            )
            bot2.send_message(chat_idd, f"<blockquote>Thằng  <a href='tg://user?id={user_id}'>{first_name}</a> Đã Bị Mute, Muốn Mở Ib Admin. </blockquote>" , parse_mode='HTML' )
        except Exception as e:
            print(f"Lỗi khi xử lý: {e}")

##################


import json

##################
#bot3 film
##################
API_URLbot3 = "https://phimapi.com/v1/api/tim-kiem?keyword={keyword}&limit=6&page={page}"
MOVIE_DETAIL_URL = "https://phimapi.com/phim/{slug}"

bot3 = telebot.TeleBot('7616741751:AAEzdaRkFqTI7vnsogVRnQ4PB8ZlIhEaxWM')

# Lưu message_id theo từng tin nhắn riêng biệt
#message_cache_film = {}
CACHE_FILE = "message_cache_film.json"
# Lưu cache vào file JSON
def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(message_cache_film, f)

# Đọc cache từ file JSON khi bot khởi động
def load_cache():
    global message_cache_film
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            message_cache_film = {int(k): v for k, v in data.items()}  # Chuyển key thành int
    except (FileNotFoundError, json.JSONDecodeError):
        message_cache_film = {}  # Nếu lỗi, tạo cache mới


# Load cache khi khởi động bot
load_cache()

# Hàm tìm phim từ API
def search_movies(keyword, page=1):
    url = API_URLbot3.format(keyword=keyword, page=page)
    response = requests.get(url).json()

    if response["status"] == "success" and response["data"]["items"]:
        movies = response["data"]["items"]
        total_pages = response["data"]["params"]["pagination"]["totalPages"]
        return movies, total_pages
    return [], 1

# Hàm lấy thông tin phim từ slug
def get_movie_info(slug):
    url = MOVIE_DETAIL_URL.format(slug=slug)
    response = requests.get(url).json()
    
    if response.get("status"):
        return response["movie"], response["episodes"]
    return None, None
    
hieu_ung_list = [
    '5107584321108051014',  # 👍
    #'5104858069142078462',  # 👎
    '5159385139981059251',  # ❤
    '5104841245755180586',  # 🔥
    '5046509860389126442',  # 🎉
    '5046589136895476101'   # 💩
]
#bot3.reply_to(message, 'Hello!', message_effect_id = hieuung5)

# Xử lý /start với slug phim
@bot3.message_handler(commands=['start'])
def handle_start(message):
    args = message.text.split(" ", 1)
    if len(args) > 1:
        user_id = message.from_user.id
        blocklist_files = os.listdir(blocklist_dir)
        if any(str(user_id) in file for file in blocklist_files):
            return
        user_id = message.from_user.id
        #chat_id = message.chat.id
        #if int(chat_id) not in GROUP_ID:
    #        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #        return 
        #if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
#            bot3.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey trong [t.me/tien_ich2] Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>', parse_mode='HTML', disable_web_page_preview=False)
#            return
        slug = args[1].strip()
        movie, episodes = get_movie_info(slug)

        if not movie or not episodes:
            bot3.send_message(message.chat.id, "❌ Không tìm thấy phim này.")
            return

        msg_text = (
            f"<blockquote>🎬 {movie['name']} ({movie['year']})\n"
            f"📌 Thể loại: {', '.join([c['name'] for c in movie['category']])}\n"
            f"📺 Tập có sẵn hiện tại: {movie['episode_current']} / {movie['episode_total']}</blockquote>\n"
        )


        import html
        max_length = 800  # Giới hạn ký tự an toàn cho Telegram caption
        content_preview = html.unescape(movie['content'])  # Giải mã HTML entities

        # Loại bỏ thẻ <span> nếu có
        if "<span" in content_preview:
            content_preview = re.sub(r"</?span[^>]*>", "", content_preview)

        # Xóa khoảng trắng thừa
        content_preview = re.sub(r"\s+", " ", content_preview).strip()

        # Giới hạn nội dung không quá max_length ký tự
        if len(content_preview) > max_length:
            content_preview = content_preview[:max_length].rsplit(' ', 1)[0] + "..."  
        
        msg_text += f"<blockquote expandable>🌟 Nội dung: {content_preview} </blockquote>\n"

        msg_text += "🎬 Chọn phiên bản phim:"

        markup = InlineKeyboardMarkup()
        buttons = []
        for server in episodes:
            version_name = server["server_name"]
            match = re.search(r"\((.*?)\)", version_name)
            version_label = match.group(1) if match else version_name
            safe_version = version_name.replace(" ", "-")  # Đổi khoảng trắng thành "-"
            buttons.append(InlineKeyboardButton(version_label, callback_data=f"ver-{safe_version}_{slug}"))

        for i in range(0, len(buttons), 2):
            markup.row(*buttons[i:i+2])
        msg = bot3.send_photo(message.chat.id, movie["poster_url"], caption=msg_text, parse_mode="HTML", reply_markup=markup)
        
    if message.chat.type == "private":  # Nếu chat riêng
    	args = message.text.split(" ", 1)
    	if len(args) <= 1:
            hieu_ung_ngau_nhien = random.choice(hieu_ung_list)  # Chọn 1 hiệu ứng ngẫu nhiên
            bot3.reply_to(message, "<blockquote>Vui lòng nhập tên phim. Ví dụ: <code>/film Bạn Bạn Bè Bè</code>\nTham Gia [t.me/tien_ich2]</blockquote>", parse_mode="HTML", message_effect_id=hieu_ung_ngau_nhien, disable_web_page_preview=True)

@bot3.callback_query_handler(func=lambda call: call.data.startswith("ver-"))
def handle_version_selection(call):
    print(f"📢 DEBUG: Nhận callback_data -> {call.data}")

    try:
        _, version_slug = call.data.split("ver-", 1)  # Bỏ "ver-"
        version, slug = version_slug.split("_", 1)  # Chia theo "_"
        version = version.replace("-", " ")  # Trả lại dấu " " nếu có
    except ValueError:
        bot3.answer_callback_query(call.id, "❌ Dữ liệu không hợp lệ.")
        return

    print(f"📢 DEBUG: Version -> {version}")
    print(f"📢 DEBUG: Slug -> {slug}")

    movie, episodes = get_movie_info(slug)
    if not movie or not episodes:
        bot3.answer_callback_query(call.id, "❌ Không tìm thấy tập phim.")
        return

    selected_server = next((server for server in episodes if version in server["server_name"]), None)
    if not selected_server:
        bot3.answer_callback_query(call.id, "❌ Phiên bản này không có phim, vui lòng chọn lại!")
        return

    filtered_eps = selected_server["server_data"]
    if not filtered_eps:
        bot3.answer_callback_query(call.id, "❌ Không có tập nào cho phiên bản này.")
        return

    match = re.search(r"\((.*?)\)", version)
    version_label = match.group(1) if match else version  

    msg_text = (
        f"<blockquote>🎬 Film: {movie['name']} ({movie['year']})\n"
        f"📺 Tập có sẵn hiện tại: {movie['episode_current']} / {movie['episode_total']}\n"
        f"🎙 Phiên bản: {version_label}</blockquote>\n"
        "📌 Chọn tập để xem:\n"
    )

    markup = InlineKeyboardMarkup(row_width=3)
    # nút api gốc
    #buttons = [InlineKeyboardButton(f"▶️ {ep['name']}", url=ep["link_embed"]) for ep in filtered_eps]
    
    # nút api của t tự làm
    buttons = [InlineKeyboardButton(f"▶️ {ep['name']}", url=f"https://tranhiep.x10.mx/phim?url={ep['link_m3u8']}") for ep in filtered_eps]


    for i in range(0, len(buttons), 3):
        markup.add(*buttons[i:i+3])

    bot3.edit_message_caption(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        caption=msg_text,
        parse_mode="HTML",
        reply_markup=markup
    )


# Xử lý /film {tên phim}
@bot3.message_handler(commands=['film'])
def handle_filmm(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
        #chat_id = message.chat.id
        #if int(chat_id) not in GROUP_ID:
    #        bot.reply_to(message, '<blockquote> <b>Bot Này Hoạt Động Chính Trong Nhóm @Tien_Ich2 !!!. Vui Lòng Tham Gia Nhóm Và Sử Dụng. </b> \n<a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )
    #        return 
    
    
    
    #if not os.path.exists(f"./user/{datetime.date.today().day}/{user_id}.txt"):
#        if message.chat.type == "private":
#            bot3.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey trong [t.me/tien_ich2] Để Lấy Key</blockquote>', parse_mode='HTML', disable_web_page_preview=False)
#        else:
#            bot3.reply_to(message, text=' <blockquote>⛔ Bạn Chưa Lấy Key Ngày Hôm Nay.\nDùng /getkey Để Lấy Key\nDùng /key [key] Để Nhập Key. </blockquote>', parse_mode='HTML')
#        return
    args = message.text.split(" ", 1)
    if len(args) < 2:
        bot3.reply_to(message, "<blockquote>Vui lòng nhập tên phim. Ví dụ: <code>/film Bạn Bạn Bè Bè</code> </blockquote>", parse_mode="HTML")
        return

    keyword = args[1]
    send_movie_list(message.chat.id, keyword, page=1)

#message_cache_film = {}  # {message_id: {"chat_id": ..., "keyword": ..., "page": ...}}

# Hàm tạo nội dung và inline keyboard
def generate_movie_message(keyword, page):
    movies, total_pages = search_movies(keyword, page)

    if not movies:
        return "Không tìm thấy phim nào.", None

    message_text = f"🔍 Kết quả tìm kiếm: <code>{keyword}</code>\n🎟 Trang {page}/{total_pages}\n"
    for movie in movies:
        name = movie["name"]
        year = movie.get("year", "Không rõ")
        quality = movie.get("quality", "N/A")
        lang = movie.get("lang", "N/A")
        current_ep = movie.get("episode_current", "Chưa cập nhật")
        link = f"https://t.me/FilmHay_Bot?start={movie['slug']}"
        
        message_text += f"<blockquote>🎬 <a href='{link}'>{name} ({year})</a>\n📺 {current_ep} | 🎥 {quality} | 🌐 {lang}</blockquote>\n"

    # Tạo Inline Keyboard
    keyboard = InlineKeyboardMarkup()
    
    prev_button = InlineKeyboardButton("⬅️ Trước", callback_data=f"prev_{keyword}_{page}")
    page_button = InlineKeyboardButton(f"{page}/{total_pages}", callback_data="none")
    next_button = InlineKeyboardButton("➡️ Sau", callback_data=f"next_{keyword}_{page}")

    if page > 1 and page < total_pages:
        keyboard.row(prev_button, page_button, next_button)
    elif page == 1 and total_pages > 1:
        keyboard.row(page_button, next_button)
    elif page == total_pages and total_pages > 1:
        keyboard.row(prev_button, page_button)

    return message_text, keyboard
# Gửi danh sách phim
def send_movie_list(chat_id, keyword, page):
    message_text, keyboard = generate_movie_message(keyword, page)

    msg = bot3.send_message(chat_id, message_text, parse_mode="HTML", reply_markup=keyboard, disable_web_page_preview=True)

    # Lưu message_id riêng biệt cho tin nhắn này
    message_cache_film[int(msg.message_id)] = {
    "chat_id": chat_id, 
    "keyword": keyword, 
    "page": page
}
    save_cache()


#print("Cache loaded:", message_cache_film)  # Kiểm tra cache có dữ liệu không

@bot3.callback_query_handler(func=lambda call: call.data.startswith(("prev_", "next_")))
def handle_callback(call):
    data = call.data.split("_")
    
    if data[0] == "none":  # Nút không có chức năng
        return
    
    if call.message.message_id not in message_cache_film:
        return  # Không có dữ liệu tin nhắn này, bỏ qua
    keyword = message_cache_film[call.message.message_id]["keyword"]
    page = message_cache_film[call.message.message_id]["page"]
    chat_id = message_cache_film[call.message.message_id]["chat_id"]
    
    if data[0] == "prev":
        new_page = max(1, page - 1)
    elif data[0] == "next":
        new_page = page + 1
    else:
        return
    
    message_text, keyboard = generate_movie_message(keyword, new_page)
    
    bot3.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, 
                          text=message_text, parse_mode="HTML", reply_markup=keyboard, disable_web_page_preview=True)
    
    # Cập nhật trang mới vào cache
    message_cache_film[call.message.message_id]["page"] = new_page
    save_cache()  # Lưu lại thay đổi


#@bot3.message_handler(commands=['start'])
#def hehehehe(message):
#    bot3.reply_to(message, 'hello')
    
    
###################
###################
    
    
    
    
ccccccccc = -1009999992103359217
#TỪ CHỐI NHỮNG LỆNH KHÔNG HỢP LỆ 
@bot.message_handler(func=lambda message: message.text.startswith('/'))
def invalid_command(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    if message.chat.id == ccccccccc :      
   #     bot.reply_to(message, f'Bot Này đang ẻ' , parse_mode='HTML' )
        return 
    bot.reply_to(message, ' <blockquote>🙅 Lệnh Không Hợp Lệ. Vui Lòng Sử Dụng /help Để Xem Danh Sách Lệnh. Vào Nhóm Này Để Sử Dụng Bot <a href="https://t.me/Tien_Ich2">📦 Tiện Ích</a> </blockquote>' , parse_mode='HTML' )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id
    blocklist_files = os.listdir(blocklist_dir)
    if any(str(user_id) in file for file in blocklist_files):
        return
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    chat_id = message.chat.id  # Sử dụng chat_id đã lưu trữ
    if message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id:
        if message.reply_to_message.message_id in reply_to_message_ids:
            # Xóa 2 tin nhắn trước đó
            for message_id in reply_to_message_ids:
                bot.delete_message(chat_id=chat_id, message_id=message_id)

            # Xóa các ID tin nhắn khỏi danh sách
            reply_to_message_ids.clear()
            current_time = datetime.datetime.now().strftime('%Hh %Mp %Ss')
            # Gửi thông báo cho admin
            bot.send_message(chat_id=f'{ADMIN_ID}', text=f'''<blockquote>💭Tin Nhắn Đến📥
👤 Người Gửi: <a href="tg://user?id={user_id}">{first_name}</a> 
🏷 ID: <code>{user_id}</code> 
⏳ Thời Gian: {current_time}
📦 Nội Dung: </blockquote>
<blockquote>{message.text} </blockquote>''', parse_mode='HTML')

            # Gửi thông báo cho người gửi
            bot.send_message(chat_id, ' <blockquote>✅ Tin Nhắn Đã Được Gửi Thành Công Tới <a href="http://t.me/trn_hwp2">Admin</a> \n📦 Có Thể Admin Sẽ Nhắn Tin Tới Bạn Thông Qua Bot\n💬 Vui Lòng Nhắn Tin Riêng Với Bot Bằng Lệnh /start Để Mở Trò Chuyện.</blockquote>', parse_mode='HTML')

import threading
                           #else:
#                bot.reply_to(message, ' <blockquote>🚫 Bạn Không Có Quyền Sử Dụng Lệnh Này. </blockquote>' , parse_mode='HTML' )
def runbot():
    bot.infinity_polling()
def runbot2():
    bot2.infinity_polling()
def runbot3():
    bot3.infinity_polling()
thread1 = threading.Thread(target=runbot)
thread2 = threading.Thread(target=runbot2)
thread3 = threading.Thread(target=runbot3)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
