# -*- coding: utf-8 -*-
import sqlite3 as db

ENEX_HEADER = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE en-export SYSTEM " \
              "\"http://xml.evernote.com/pub/evernote-export2.dtd\">\n<en-export export-date=\"20200408T083803Z\" " \
              "application=\"Evernote/Windows\" version=\"6.x\"> "

ENEX_NOTE_ATTR = "<note-attributes><author>ifmylove2011@163.com</author><source>desktop.win</source><source" \
                 "-application>yinxiang.win32</source-application></note-attributes> "

ENEX_NOTE_TIME = "<created>time1</created><updated>time2</updated>"

def add_note_time(create_time, update_time):
    return "<created>time1</created><updated>time2</updated>".replace("time1", create_time)


def read_sqlite(db_path, cmd):
    conn = db.connect(db_path)
    cursor = conn.cursor()
    conn.row_factory = db.Row
    cursor.execute(cmd)
    rows = cursor.fetchall()
    return rows


def read_snda_db():
    rows = read_sqlite("snda_maiku_v2.db", "select title,content,createTime,updateTime from notes")
    print(len(rows))

read_snda_db()

class Note:

    def __init__(self, title, content, create_time, update_time):
        self.title = title
        self.content = content
        self.create_time = create_time
        self.update_time = update_time

    def __str__(self):
        return 'Note (%s, %s,%s, %s)' % (self.title, self.content, self.create_time, self.update_time)
