#    Copyright 2021 Vision
#    Copyright 2021 KeinShin
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import os

from cryptography.fernet import Fernet
from pymongo import MongoClient
from pyrogram import Client

print("Loading requirements")
os.system("pip install pymongo")
os.system("pip install cryptography")
os.system("pip install dnspython")
os.system("pip  install pymongo[srv]")


os.system("clear")
print(
    """

--------------------------------------------------------------------


██████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░
█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░
█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░███████████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░
█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░░░░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░
█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░
█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░░░░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░
█░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░███████████░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░
█░░░░▄▀▄▀▄▀░░░░█░░░░▄▀░░░░█░░░░░░░░░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░
███░░░░▄▀░░░░███░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░
█████░░░░░░█████░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░
██████████████████████████████████████████████████████████████████████████████████████████


-------------------------------------------------------------------

                    STRING SESSION GENERATION

-------------------------------------------------------------------
""",
)

app_id = input("Enter your api: ")

hash = input("Enter api hash: ")
mongo = input("Enter mongo db url: ")

app = Client("MyVision", api_id=app_id, api_hash=hash)

app.storage.SESSION_STRING_FORMAT=">B?256sQ?"

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)


with app:

    # with app:
    string = app.export_session_string()
    kek = Fernet.generate_key()
    client = MongoClient(mongo)
    db = client["VisionEncryption"]
    db = db["string_db"]
    db.insert_one({kek.decode(): 0})
    encryped = encrypt(string.encode(), kek)
    print("You string is sent check your saved message")
    app.send_message(
        "me",
        f"**Here's Your String**\n\n`{encryped.decode()}`\n\n**Contact @VisionTalks for help**",
        parse_mode="markdown",
    )
