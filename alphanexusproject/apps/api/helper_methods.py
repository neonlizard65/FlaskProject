from flask import request
from extensions import mysql
import json
import random
import base64
from os import path

def generate_key():
    
    allowed_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    while True:
        new_key = ""
        for i in range(16):
            new_key += random.choice(allowed_symbols)
    
        connect = mysql.connect()       
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM CDKey WHERE Content = %s", new_key)
        res = cursor.fetchone()
        cursor.close()
        if res.count == 0:
            return new_key    
            
            
def generate_token():
    allowed_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtsuvwxyz0123456789'
    while True:
        new_token = ""
        for i in range(16):
            new_token += random.choice(allowed_symbols)
        
        connect = mysql.connect()       
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM User WHERE UserBotToken = %s", new_token)
        res = cursor.fetchall()
        cursor.close()
        if res.count == 0:
            return new_token    


def save_image(img_data: str, name: str) -> str:
    fpath = path.abspath(path.join(path.dirname(__file__), "..", "..", "static", "img", f"{name.replace(' ', '')}.png"))
    with open(fpath, "wb") as iw:
        iw.write(base64.b64decode(img_data))
    return f"../static/img/{name}.png"
    
    
    
    
    