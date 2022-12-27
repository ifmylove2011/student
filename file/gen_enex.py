# -*- coding: utf-8 -*-
import sqlite3 as db
import os

ENEX_HEADER = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE en-export SYSTEM " \
              "\"http://xml.evernote.com/pub/evernote-export2.dtd\">\n<en-export export-date=\"20200408T083803Z\" " \
              "application=\"Evernote/Windows\" version=\"6.x\"> "

ENEX_NOTE_TITLE = "<title>{title}</title>"
ENEX_NOTE_CONTENT = "<content><![CDATA[<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE en-note SYSTEM " \
                    "\"http://xml.evernote.com/pub/enml2.dtd\">\n\n<en-note>{content}</en-note>]]></content>"
ENEX_NOTE = "<note>{note}</note>"
ENEX_NOTE_TIME = "<created>{create_time}</created><updated>{update_time}</updated>"
ENEX_NOTE_ATTR = "<note-attributes><author>ifmylove2011@163.com</author><source>desktop.win</source><source" \
                 "-application>yinxiang.win32</source-application></note-attributes> "
ENEX_TAIL = "</en-export>"


def build_note_time(create_time, update_time):
    return ENEX_NOTE_TIME.format(create_time=format_time(create_time), update_time=format_time(update_time))


def format_time(time):
    return time.replace(" ", "T").replace("-", "").replace(":", "") + "Z"


def build_note_title(title):
    return ENEX_NOTE_TITLE.format(title=title)


def build_note_content(content):
    return ENEX_NOTE_CONTENT.format(content=content)


def build_note(title, content, create_time, update_time):
    return ENEX_NOTE.format(note=build_note_title(title) + build_note_content(content) + build_note_time(create_time,
                                                                                                         update_time) + ENEX_NOTE_ATTR)


def read_sqlite(db_path, cmd):
    conn = db.connect(db_path)
    cursor = conn.cursor()
    conn.row_factory = db.Row
    cursor.execute(cmd)
    rows = cursor.fetchall()
    return rows


def gen_enex_file():
    rows = read_sqlite("snda_maiku_v2_addtional.db", "select title,content,createTime,updateTime from notes")
    with open(os.path.join(os.getcwd(), "snda.enex"), 'a', encoding="utf-8") as file_dst:
        file_dst.write(ENEX_HEADER)
        for row in rows:
            title = row[0]
            content = row[1]
            create_time = row[2]
            update_time = row[3]
            file_dst.write(build_note(title, content, create_time, update_time))
            # print(build_note(title, content, create_time, update_time))
        file_dst.write(ENEX_TAIL)


gen_enex_file()

