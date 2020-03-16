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

conn = sqlite3.connect('onepiece4のコピー.sqlite')
cur = conn.cursor()


cur.execute('''
DROP TABLE IF EXISTS Story''')
#Creating the table we're going to use

cur.execute('''CREATE TABLE IF NOT EXISTS Story
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')

filepath = 'onepiece_stories.htm'

with open(filepath , encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html5lib')
trs = soup.select("body .container .content table tbody tr")

for tr in trs:
    a_list = tr.select('a') #number of index = 2
    st_num = int(a_list[0].getText(''))
    st_name = a_list[1].getText('')
    if st_num >= 1 and st_num <= 8:
        cs_num = 1
    elif st_num >= 9 and st_num <= 17:
        cs_num = 2
    elif st_num >= 18 and st_num <= 26:
        cs_num = 3
    elif st_num >= 27 and st_num <= 35:
        cs_num = 4
    elif st_num >= 36 and st_num <= 44:
        cs_num = 5
    elif st_num >= 45 and st_num <= 53:
        cs_num = 6
    elif st_num >= 54 and st_num <= 62:
        cs_num = 7
    elif st_num >= 63 and st_num <= 71:
        cs_num = 8
    elif st_num >= 72 and st_num <= 81:
        cs_num = 9
    elif st_num >= 82 and st_num <= 90:
        cs_num = 10
    elif st_num >= 91 and st_num <= 99:
        cs_num = 11
    elif st_num >= 100 and st_num <= 108:
        cs_num = 12
    elif st_num >= 109 and st_num <= 117:
        cs_num = 13
    elif st_num >= 118 and st_num <= 126:
        cs_num = 14
    elif st_num >= 127 and st_num <= 136:
        cs_num = 15
    elif st_num >= 137 and st_num <= 145:
        cs_num = 16
    elif st_num >= 146 and st_num <= 155:
        cs_num = 17
    elif st_num >= 156 and st_num <= 166:
        cs_num = 18
    elif st_num >= 167 and st_num <= 176:
        cs_num = 19
    elif st_num >= 177 and st_num <= 186:
        cs_num = 20
    elif st_num >= 187 and st_num <= 195:
        cs_num = 21
    elif st_num >= 196 and st_num <= 205:
        cs_num = 22
    elif st_num >= 206 and st_num <= 216:
        cs_num = 23
    elif st_num >= 217 and st_num <= 226:
        cs_num = 24
    elif st_num >= 227 and st_num <= 236:
        cs_num = 25
    elif st_num >= 237 and st_num <= 246:
        cs_num = 26
    elif st_num >= 247 and st_num <= 255:
        cs_num = 27
    elif st_num >= 256 and st_num <= 264:
        cs_num = 28
    elif st_num >= 265 and st_num <= 275:
        cs_num = 29
    elif st_num >= 276 and st_num <= 285:
        cs_num = 30
    elif st_num >= 286 and st_num <= 295:
        cs_num = 31
    elif st_num >= 296 and st_num <= 305:
        cs_num = 32
    elif st_num >= 306 and st_num <= 316:
        cs_num = 33
    elif st_num >= 317 and st_num <= 327:
        cs_num = 34
    elif st_num >= 328 and st_num <= 336:
        cs_num = 35
    elif st_num >= 337 and st_num <= 346:
        cs_num = 36
    elif st_num >= 347 and st_num <= 357:
        cs_num = 37
    elif st_num >= 358 and st_num <= 367:
        cs_num = 38
    elif st_num >= 368 and st_num <= 377:
        cs_num = 39
    elif st_num >= 378 and st_num <= 388:
        cs_num = 40
    elif st_num >= 388 and st_num <= 399:
        cs_num = 41
    elif st_num >= 400 and st_num <= 409:
        cs_num = 42
    elif st_num >= 410 and st_num <= 419:
        cs_num = 43
    elif st_num >= 420 and st_num <= 430:
        cs_num = 44
    elif st_num >= 431 and st_num <= 440:
        cs_num = 45
    elif st_num >= 441 and st_num <= 449:
        cs_num = 46
    elif st_num >= 450 and st_num <= 459:
        cs_num = 47
    elif st_num >= 460 and st_num <= 470:
        cs_num = 48
    elif st_num >= 471 and st_num <= 481:
        cs_num = 49
    elif st_num >= 482 and st_num <= 489:
        cs_num = 50
    elif st_num >= 490 and st_num <= 502:
        cs_num = 51
    elif st_num >= 503 and st_num <= 512:
        cs_num = 52
    elif st_num >= 513 and st_num <= 522:
        cs_num = 53
    elif st_num >= 523 and st_num <= 532:
        cs_num = 54
    elif st_num >= 533 and st_num <= 541:
        cs_num = 55
    elif st_num >= 542 and st_num <= 551:
        cs_num = 56
    elif st_num >= 552 and st_num <= 562:
        cs_num = 57
    elif st_num >= 563 and st_num <= 573:
        cs_num = 58
    elif st_num >= 574 and st_num <= 584:
        cs_num = 59
    elif st_num >= 585 and st_num <= 594:
        cs_num = 60
    elif st_num >= 595 and st_num <= 603:
        cs_num = 61
    elif st_num >= 604 and st_num <= 614:
        cs_num = 62
    elif st_num >= 615 and st_num <= 626:
        cs_num = 63
    elif st_num >= 627 and st_num <= 636:
        cs_num = 64
    elif st_num >= 637 and st_num <= 646:
        cs_num = 65
    elif st_num >= 647 and st_num <= 656:
        cs_num = 66
    elif st_num >= 657 and st_num <= 667:
        cs_num = 67
    elif st_num >= 668 and st_num <= 678:
        cs_num = 68
    elif st_num >= 679 and st_num <= 690:
        cs_num = 69
    elif st_num >= 691 and st_num <= 700:
        cs_num = 70
    elif st_num >= 701 and st_num <= 711:
        cs_num = 71
    elif st_num >= 712 and st_num <= 721:
        cs_num = 72
    elif st_num >= 722 and st_num <= 731:
        cs_num = 73
    elif st_num >= 732 and st_num <= 742:
        cs_num = 74
    elif st_num >= 743 and st_num <= 752:
        cs_num = 75
    elif st_num >= 753 and st_num <= 763:
        cs_num = 76
    elif st_num >= 764 and st_num <= 775:
        cs_num = 77
    elif st_num >= 776 and st_num <= 785:
        cs_num = 78
    elif st_num >= 786 and st_num <= 795:
        cs_num = 79
    elif st_num >= 796 and st_num <= 806:
        cs_num = 80
    elif st_num >= 807 and st_num <= 816:
        cs_num = 81
    elif st_num >= 817 and st_num <= 827:
        cs_num = 82
    elif st_num >= 828 and st_num <= 838:
        cs_num = 83
    elif st_num >= 839 and st_num <= 848:
        cs_num = 84
    elif st_num >= 849 and st_num <= 858:
        cs_num = 85
    elif st_num >= 859 and st_num <= 869:
        cs_num = 86
    elif st_num >= 870 and st_num <= 879:
        cs_num = 87
    elif st_num >= 880 and st_num <= 889:
        cs_num = 88
    elif st_num >= 890 and st_num <= 900:
        cs_num = 89
    elif st_num >= 901 and st_num <= 910:
        cs_num = 90
    elif st_num >= 911 and st_num <= 921:
        cs_num = 91
    elif st_num >= 922 and st_num <= 931:
        cs_num = 92
    elif st_num >= 932 and st_num <= 942:
        cs_num = 93
    else:
        cs_num = 94
    st_name = '第' + str(cs_num) + '巻　' + '第' + str(st_num) + '話　' + st_name
    print(st_num, st_name)

    cur.execute('''INSERT OR IGNORE INTO Story (id, name) VALUES(?,?)''',(st_num,st_name))
"""
    cur.execute('SELECT id FROM Ship WHERE name = ? ', (ship, ))
    ship_id = cur.fetchone()[0]

        cur.execute('''INSERT INTO Character (name, sex_id, ship_id, birthday, age, height, constellation_id, blood_type_id, birthplace_id, favorite_food, bounty, cv, debut, aliace, devil_fruit, haki_haou_id, haki_kenbun_id, haki_busou_id,  tribe_id, other, belonging) VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', (name, None, ship_id, birthday, age, height, constellation_id, blood_type_id, birthplace_id, favorite_food, bounty, cv, None, aliace, devil_fruit, haki_haou_id, haki_kenbun_id, haki_busou_id, None, None, belonging))
"""

conn.commit()

"""
f = cur.execute('''SELECT Character.id, Character.name, Ship.name, Character.birthday, Character.age, Character.height, Blood_type.name, Birthplace.name, Character.favorite_food, Character.bounty, Character.cv, Character.aliace, Character.devil_fruit, Haki_haou.name, Haki_kenbun.name,  Haki_busou.name, Character.belonging, GENDER.name FROM Character JOIN Ship JOIN Blood_type JOIN Birthplace JOIN Haki_haou JOIN Haki_kenbun JOIN Haki_busou JOIN GENDER ON Character.ship_id = Ship.id and Character.blood_type_id = Blood_type.id and Character.birthplace_id = Birthplace.id and Character.haki_haou_id = Haki_haou.id and Character.haki_kenbun_id = Haki_kenbun.id and Character.haki_busou_id = Haki_busou.id and Character.gender = GENDER.id LIMIT 5''')

for line in f:
    print(line[0],line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13])
"""

cur.close()
