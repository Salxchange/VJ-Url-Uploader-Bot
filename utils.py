import asyncio
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from typing import Union
import pytz
import random 
import re
import os
from datetime import datetime, date
import string
from typing import List
from database.users_chats_db import tech_vj
from bs4 import BeautifulSoup
import requests
import aiohttp
import json
from config import Config


TOKENS = {}
VERIFIED = {}

LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

