import tkinter, pymysql, pymysql.cursors, threading, tkinter, turtle, pandas as pd, tkinter as tk, socket
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import *
from threading import Thread as process

def data_connect():
    try:
        connect = pymysql.Connect(host='localhost',
          port=3306,
          user='root',
          passwd='root',
          db='test_py',
          charset='utf8')
        cursor = connect.cursor()
        data_connect = tkinter.Tk()
        data_connect.title('数据库操作界面')
        data_connect.geometry('500x360+50+10')
        data_connect_labelframe = tkinter.LabelFrame(data_connect, text='请输入SQL语句')
        data_connect_labelframe.grid(column=0, row=0, padx=10, pady=10)
        input_sql_text = Entry(data_connect_labelframe, width=50)
        input_sql_text.grid(row=0, column=0)
        src = scrolledtext.ScrolledText(data_connect, width=65, height=5)
        src.grid(column=0, row=1)
        btn2 = tkinter.Button(data_connect_labelframe, text='执行SQL语句操作', command=(lambda : process(target=(button_sql(input_sql_text, cursor, src, connect))).start()))
        btn2.grid(row=0, column=1)
        data_connect_labelframe2 = tkinter.LabelFrame(data_connect, text='根据表名和条件进行简单查询')
        data_connect_labelframe2.grid(column=0, row=2, padx=10, pady=10)
        input_table_name = Label(data_connect_labelframe2, text='请输入要查询的表名')
        input_table_name.grid(row=0, column=0)
        input_table_condtion = Label(data_connect_labelframe2, text='请输入要查询的条件')
        input_table_condtion.grid(row=1, column=0)
        input_name = Entry(data_connect_labelframe2, width=48)
        input_name.grid(row=0, column=1)
        input_condtion = Entry(data_connect_labelframe2, width=48)
        input_condtion.grid(row=1, column=1)
        btn2 = tkinter.Button(data_connect_labelframe2, text='连接数据库进行查询', command=(lambda : process(target=(button_connect_select(input_name, input_condtion, cursor, src2, connect))).start()))
        btn2.grid(row=2, column=0)
        src2 = scrolledtext.ScrolledText(data_connect, width=65, height=5)
        src2.grid(column=0, row=3)
        data_connect.mainloop()
    except Exception as e:
        try:
            tkinter.messagebox.showinfo('提示', '连接地址异常')
        finally:
            e = None
            del e


def button_connect_select(input_name, input_condtion, cursor, src, connect):
    try:
        connect = pymysql.Connect(host=user_host,
          port=user_port,
          user=user_name,
          passwd=user_passwd,
          db=user_database,
          charset='utf8')
        cursor = connect.cursor()
        sql = 'SELECT * FROM %s WHERE %s '
        table_name = input_name.get()
        table_condtion = input_condtion.get()
        data = (table_name, table_condtion)
        cursor.execute(sql % data)
        desc = cursor.description
        connect.commit()
        for field in desc:
            src.insert(tkinter.END, field[0] + '  ')

        src.insert(tkinter.END, '\n')
        for row in cursor.fetchall():
            src.insert(tkinter.END, row)
            src.insert(tkinter.END, '\n')
            src.update()

    except Exception as e:
        try:
            tkinter.messagebox.showinfo('提示', '请尝试重新运行')
        finally:
            e = None
            del e


def button_sql(input_sql_text, cursor, src, connect):
    sql = input_sql_text.get()
    rows = cursor.execute(sql)
    src.insert(tkinter.END, pd.read_sql(sql, connect))
    src.insert(tkinter.END, '\n')
    src.update()
# okay decompiling sqlPage.cpython-37.pyc
