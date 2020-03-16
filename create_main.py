import sqlite3
import urllib.request
import os,csv
import re
import xlrd
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urlparse
import urllib.request
import datetime
#Connecting to the file in which we want to store our db
conn = sqlite3.connect('onepiece1.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Character''')
cur.execute('''
DROP TABLE IF EXISTS Sex''')
cur.execute('''
DROP TABLE IF EXISTS Ship''')
cur.execute('''
DROP TABLE IF EXISTS Consellation''')
cur.execute('''
DROP TABLE IF EXISTS Blood_type''')
cur.execute('''
DROP TABLE IF EXISTS Birthplace''')
cur.execute('''
DROP TABLE IF EXISTS Haki_haou''')
cur.execute('''
DROP TABLE IF EXISTS Haki_kenbun''')
cur.execute('''
DROP TABLE IF EXISTS Haki_busou''')
cur.execute('''
DROP TABLE IF EXISTS Tribes''')
#Creating the table we're going to use
cur.execute('''
CREATE TABLE IF NOT EXISTS Character (id INTEGER PRIMARY KEY, name TEXT UNIQUE, sex_id INTEGER, ship_id INTEGER, birthday TEXT, age INTEGER, height	INTEGER, constellation_id INTEGER, blood_type_id INTEGER, birthplace_id INTEGER, favorite_food TEXT, bounty INTEGER, cv TEXT, debut INTEGER, aliace TEXT, devil_fruit TEXT, haki_haou_id INTEGER, haki_kenbun_id INTEGER, haki_busou_id INTEGER, tribe_id INTEGER, other TEXT, belonging TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Sex
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Ship
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Consellation
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Blood_type
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Birthplace
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Haki_haou
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Haki_kenbun
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Haki_busou
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Tribe
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')

filepath1 = 'chara_number.htm'
dataurl = 'chara_number.htm'
with open(filepath1 , encoding='utf-8') as f1:
    html1 = f1.read()
soup1 = BeautifulSoup(html1, 'html.parser')
uls1 = soup1.select(".theContentWrap-ccc ul")
serviceurl = "https://dic.pixiv.net/a/"
prev_id = 0
for ul in uls1[1:2]:
    li_list = ul.select('li') #list-type
    for li in li_list[0:10]:
        num_chara = li.getText('li')
        chara_number = int(num_chara.split("\u3000")[0])
        if prev_id == chara_number:
            continue
        print(chara_number)
        prev_id = chara_number
        name, ship, birthday, age, height, blood_type, birthplace, favorite_food, bounty, cv, aliace, devil_fruit, haki_haou, haki_kenbun, haki_busou, belonging = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None

        name = num_chara.split("\u3000")[1]
        if "（" in name:
            name = name.split("（")[0]
        url = serviceurl + urllib.parse.quote_plus(name, encoding='utf-8')
        response = urllib.request.urlopen(url).read()
        soup2 = BeautifulSoup(response, 'html5lib')
        tb_list = soup2.select("table")
        for tb in tb_list[0]:
            tr_list = tb.select("tr")
            for tr in tr_list:
                th_list = tr.select("th")
                td_list = tr.select("td")
                for th in th_list:
                    tag = th.getText("th")
                for td in td_list:
                    text = td.getText("td").replace("td","")
                if tag == "通り名" or tag == "異名":
                    aliace = text
                elif tag == "年齢":
                    age = text
                    if "→" in age:
                        age = age.split("→")[-1]
                    age = re.findall("([0-9 ０-９]{1,3})[歳]", age)[0]
                    age = int(age)
                elif tag == "身長":
                    height = text
                    if "→" in height:
                        height = height.split("→")[-1]
                    height = re.findall("([0-9 ０-９]{1,3})cm", height)[0]
                    height = int(height)
                elif tag == "懸賞金":
                    bounty = text
                    if "→" in bounty:
                        bounty = bounty.split("→")[-1]
                    bounty = bounty.split("ベリー")[0]
                    if "万" in bounty and "億" in bounty:
                        oku = bounty.split("億")[0]
                        mann = bounty.split("億")[1].split("万")[0]
                        bounty = oku + mann + "0000"
                    elif "万" in bounty:
                        mann = bounty.split("万")[0]
                        bounty = mann + "0000"
                    elif "億" in bounty:
                        oku = bounty.split("億")[0]
                        bounty = oku + "00000000"
                    bounty = int(bounty)
                elif tag == "肩書き":
                    title = text
                elif tag == "所属":
                    belonging = text
                    if "→" in belonging:
                        belonging = belonging.split("→")[-1]
                elif tag == "所属船":
                    ship = text
                    ship = ship.split("→")[-1]
                elif tag == "悪魔の実":
                    devil_fruit = text
                elif tag == "覇気":
                    haki = text
                    if "（" in haki:
                        haki = haki.split("（")[0]
                    if "、" in haki:
                        haki_list = haki.split("、")
                        for haki in haki_list:
                            if haki == "覇王色":
                                haki_haou = "あり"
                            elif haki == "見聞色":
                                haki_kenbun = "あり"
                            elif haki == "武装色":
                                haki_busou = "あり"
                elif tag == "出身地":
                    birthplace = text
                elif tag == "誕生日":
                    date = text
                    date_list = re.findall('([0-9０-９]{1,2})[月]{1}([0-9０-９]{1,2})[日]',date)[0]
                    m = int(date_list[0])
                    d = int(date_list[1])
                    if m == 1 and d <= 19:
                        constellation = "やぎ座"
                    elif m == 1 and d >= 20:
                        constellation = "みずがめ座"
                    elif m == 2 and d <= 18:
                        constellation = "みずがめ座"
                    elif m == 2 and d >= 19:
                        constellation = "うお座"
                    elif m == 3 and d <= 20:
                        constellation = "うお座"
                    elif m == 3 and d >= 21:
                        constellation = "おひつじ座"
                    elif m == 4 and d <= 19:
                        constellation = "おひつじ座"
                    elif m == 4 and d >= 20:
                        constellation = "おうし座"
                    elif m == 5 and d <= 20:
                        constellation = "おうし座"
                    elif m == 5 and d >= 21:
                        constellation = "ふたご座"
                    elif m == 6 and d <= 21:
                        constellation = "ふたご座"
                    elif m == 6 and d >= 22:
                        constellation = "かに座"
                    elif m == 7 and d <= 22:
                        constellation = "かに座"
                    elif m == 7 and d >= 23:
                        constellation = "しし座"
                    elif m == 8 and d <= 22:
                        constellation = "しし座"
                    elif m == 8 and d >= 23:
                        constellation = "おとめ座"
                    elif m == 9 and d <= 22:
                        constellation = "おとめ座"
                    elif m == 9 and d >= 23:
                        constellation = "てんびん座"
                    elif m == 10 and d <= 23:
                        constellation = "てんびん座"
                    elif m == 10 and d >= 24:
                        constellation = "さそり座"
                    elif m == 11 and d <= 21:
                        constellation = "さそり座"
                    elif m == 11 and d >= 22:
                        constellation = "いて座"
                    elif m == 12 and d <= 21:
                        constellation = "いて座"
                    elif m == 12 and d >= 22:
                        constellation = "やぎ座"
                    birthday = "{0:02d}".format(int(date_list[0])) + "-" + "{0:02d}".format(int(date_list[1]))
                elif tag == "血液型":
                    blood_type = text
                elif tag == "好きな食べ物":
                    favorite_food = text
                elif tag == "CV":
                    cv = text
                else:
                    continue
        if len(tb_list) > 1:
            for tb in tb_list[1]:
                tr_list = tb.select("tr")
                for tr in tr_list:
                    th_list = tr.select("th")
                    td_list = tr.select("td")
                    for th in th_list:
                        tag = th.getText("th")
                    for td in td_list:
                        text = td.getText("td").replace("td","")
                    if tag == "悪魔の実":
                        devil_fruit = text
                    else:
                        continue
        print(name, ship, birthday, age, height, constellation, blood_type, birthplace, favorite_food, bounty, cv, aliace, devil_fruit, haki_haou, haki_kenbun, haki_busou, belonging)

        cur.execute('''INSERT OR IGNORE INTO Sex (name) VALUES(?)''',(None,))

        cur.execute('''INSERT OR IGNORE INTO Ship (name) VALUES(?)''',(ship,))
        cur.execute('SELECT id FROM Ship WHERE name = ? ', (ship, ))
        ship_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Consellation (name) VALUES(?)''',(constellation,))
        cur.execute('SELECT id FROM Consellation WHERE name = ? ', (constellation, ))
        constellation_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Blood_type (name) VALUES(?)''',(blood_type,))
        cur.execute('SELECT id FROM Blood_type WHERE name = ? ', (blood_type, ))
        blood_type_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Birthplace (name) VALUES(?)''',(birthplace,))
        cur.execute('SELECT id FROM Birthplace WHERE name = ? ', (birthplace, ))
        birthplace_id = cur.fetchone()[0]

        if haki_haou == None:
            haki_haou = "なし"
        cur.execute('''INSERT OR IGNORE INTO Haki_haou (name) VALUES(?)''',(haki_haou,))
        cur.execute('SELECT id FROM Haki_haou WHERE name = ? ', (haki_haou, ))
        haki_haou_id = cur.fetchone()[0]
        print(haki_haou_id)

        if haki_kenbun == None:
            haki_kenbun = "なし"
        cur.execute('''INSERT OR IGNORE INTO Haki_kenbun (name) VALUES(?)''',(haki_kenbun,))
        cur.execute('SELECT id FROM Haki_kenbun WHERE name = ? ', (haki_kenbun, ))
        haki_kenbun_id = cur.fetchone()[0]

        if haki_busou == None:
            haki_busou = "なし"
        cur.execute('''INSERT OR IGNORE INTO Haki_busou (name) VALUES(?)''',(haki_busou,))
        cur.execute('SELECT id FROM Haki_busou WHERE name = ? ', (haki_busou, ))
        haki_busou_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Tribe (name) VALUES(?)''',(None,))

        cur.execute('''INSERT INTO Character (name, sex_id, ship_id, birthday, age, height, constellation_id, blood_type_id, birthplace_id, favorite_food, bounty, cv, debut, aliace, devil_fruit, haki_haou_id, haki_kenbun_id, haki_busou_id,  tribe_id, other, belonging) VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', (name, None, ship_id, birthday, age, height, constellation_id, blood_type_id, birthplace_id, favorite_food, bounty, cv, None, aliace, devil_fruit, haki_haou_id, haki_kenbun_id, haki_busou_id, None, None, belonging))


conn.commit()
"""
# Getting results and showing them in the user-friendly form.
f = cur.execute('''SELECT Character.id, Character.name, Ship.所属船, Character.birthday, Character.age, Character.height, Blood_type.血液型, Birthplace.出身地, Character.favorite_food, Character.bounty, Character.cv, Character.aliace, Character.devil_fruit, Haki_haou.覇王色の覇気, Haki_kenbun.見聞色の覇気,  Haki_busou.武装色の覇気, Character.belonging, Gender.性別,  Story.初登場 FROM Character JOIN Ship JOIN Blood_type JOIN Birthplace JOIN Haki_haou JOIN Haki_kenbun JOIN Haki_busou JOIN Gender JOIN Story ON Character.ship_id = Ship.id and Character.blood_type_id = Blood_type.id and Character.birthplace_id = Birthplace.id and Character.haki_haou_id = Haki_haou.id and Character.haki_kenbun_id = Haki_kenbun.id and Character.haki_busou_id = Haki_busou.id and Character.gender = Gender.id and Character.debut = Story.id''')

WHERE favorite_food LIKE "%肉%" ORDER BY height DESC

for line in f:
    print(line[0],line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13])
"""
#Closing the DB
cur.close()
