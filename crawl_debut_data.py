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

#cur.execute('''ALTER TABLE Character ADD COLUMN debut[INTEGER]''')

filepath = 'onepiece_chara_list.htm'
with open(filepath , encoding='utf-8') as f:
    html = f.read()
soup1 = BeautifulSoup(html, 'html5lib')
trs = soup1.select("body .container .content table tbody tr")
chara_list = [x for x in range(1149)]
for i in chara_list[:700]:
    try:
        cur.execute('SELECT name FROM Character WHERE id = ? ', (i, ))
        chara_name = cur.fetchone()[0]
        print(chara_name)
        for tr in trs:
            a_list = tr.select('a') #number of index = 2
            print(a_list[0])
            name = a_list[0].getText('')
            if "（EX）" in name:
                name = name.split("（EX）")[0]
            if name == chara_name:
                relative_path = a_list[0].get("href").split('../')[1]
                url = 'http://onepiecedb.web.fc2.com/' + relative_path
                print(url)
                response = urllib.request.urlopen(url).read()
                soup2 = BeautifulSoup(response, 'html5lib')
                uls = soup2.select("body .container .content ul")
                story = uls[0].select('li')[0].getText('')
                story_id = int(story.split('話')[0])
                print(story_id)
                cur.execute("UPDATE Character SET debut = ? where id = ?",(story_id, i))

                break
            else:
                continue
    except:
        pass

conn.commit()
cur.close()
