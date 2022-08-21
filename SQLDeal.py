import tkinter, pymysql, pymysql.cursors, threading, tkinter, turtle, pandas as pd, tkinter as tk, socket
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import *
from tkinter import ttk
import datetime

from threading import Thread as process

def data_connect():
    try:
        connect = pymysql.Connect(
            host=user_host,
            port=user_port,
            user=user_name,
            passwd=user_passwd,
            db=user_database,
        )
        cursor = connect.cursor()
        data_connect = tkinter.Tk()
        data_connect.title('数据库操作界面')
        data_connect.geometry('600x800+50+10')
        data_connect_labelframe = tkinter.LabelFrame(data_connect, text='请输入SQL语句')
        data_connect_labelframe.grid(column=0, row=0, padx=10, pady=10)
        input_sql_text = Entry(data_connect_labelframe, width=50)
        input_sql_text.grid(row=0, column=0)
        src = scrolledtext.ScrolledText(data_connect, width=200, height=10)
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
        src2 = scrolledtext.ScrolledText(data_connect, width=200, height=10)
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

def data_show_get():
    try:
        data_show_get = tkinter.Tk()  # 定义一个窗体
        data_show_get.title('数据库参数显示界面')  # 定义窗体标题 
        data_show_get.geometry('250x120+50+10')  # 设置窗体的大小250x120像素和初始位置（50，10）
        show_label_host = Label(data_show_get, text="当前服务器地址")
        show_label_host.grid(row=0, column=2)
        show_label_port = Label(data_show_get, text="当前端口号")
        show_label_port.grid(row=1, column=2)
        show_label_account = Label(data_show_get, text="当前账号")
        show_label_account.grid(row=2, column=2)
        show_label_password = Label(data_show_get, text="当前密码")
        show_label_password.grid(row=3, column=2)
        show_label_database = Label(data_show_get, text="当前数据库")
        show_label_database.grid(row=4, column=2)

        show_host = Text(data_show_get, height=1, width=15)
        show_host.insert(1.0, user_host)
        show_host.grid(row=0, column=3)
        show_port = Text(data_show_get, height=1, width=15)
        show_port.insert(1.0, user_port)
        show_port.grid(row=1, column=3)
        show_name = Text(data_show_get, height=1, width=15)
        show_name.grid(row=2, column=3)
        show_name.insert(1.0, user_name)
        show_passwd = Text(data_show_get, height=1, width=15)
        show_passwd.grid(row=3, column=3)
        show_passwd.insert(1.0, user_passwd)
        show_database = Text(data_show_get, height=1, width=15)
        show_database.grid(row=4, column=3)
        show_database.insert(1.0, user_database)
        data_show_get.mainloop()  # 表示事件循环，使窗体一直保持显示状态
    except Exception as e:
        tkinter.messagebox.showinfo('提示', '请尝试重新运行')

def button_set(input_host,input_port,input_account,input_passwd,inut_database):
    try:
        global user_host
        global user_port
        global user_name
        global user_passwd
        global user_database
        if(input_host.get()!=''):   
            user_host=input_host.get()
        if(input_port.get()!=''):   
            user_port=int(input_port.get())
        if(input_account.get()!=''):
            user_name=input_account.get()
        if(input_passwd.get()!=''):
            user_passwd=input_passwd.get()  
        if(inut_database.get()!=''):
            user_database=inut_database.get()
        pymysql.Connect(
            host=user_host,
            port=user_port,
            user=user_name,
            passwd=user_passwd,
            db=user_database,
        )
        tkinter.messagebox.showinfo('提示', '连接成功！')
    except Exception as e:
        tkinter.messagebox.showinfo('提示', '请尝试重新设置')


def data_connect_insert():
    try:
        connect = pymysql.Connect(
            host=user_host,
            port=user_port,
            user=user_name,
            passwd=user_passwd,
            db=user_database,
            charset='utf8')
        # connect = pymysql.Connect(
        #     host='127.0.0.1',
        #     port=3306,
        #     user="root",
        #     passwd="root",
        #     db="test_py",
        # )
        cursor = connect.cursor()
        data_connect_insert = tkinter.Tk()  # 定义一个窗体
        data_connect_insert.title('理财产品信息新增')  # 定义窗体标题
        data_connect_insert.geometry('500x300+200+150')  # 设置窗体的大小250x120像素和初始位置（50，10）

        input_label_number = Label(data_connect_insert, text="请输入产品代码")
        input_label_number.grid(row=0, column=0)
        input_label_name = Label(data_connect_insert, text="请输入产品名称")
        input_label_name.grid(row=1, column=0)
        input_check_ipo = Label(data_connect_insert, text="募集开始日期")
        input_check_ipo.grid(row=2, column=0)
        input_check_ipo1 = Label(data_connect_insert, text="募集结束日期")
        input_check_ipo1.grid(row=3, column=0)
        input_check_estab = Label(data_connect_insert, text="产品成立日期")
        input_check_estab.grid(row=4, column=0)
        input_check_estab1 = Label(data_connect_insert, text="产品结束日期")
        input_check_estab1.grid(row=5, column=0)
        input_check_price = Label(data_connect_insert, text="发行价格")
        input_check_price.grid(row=6, column=0)
        input_check_risk_level = Label(data_connect_insert, text="风险等级")
        input_check_risk_level.grid(row=7, column=0)
        input_check_minBuy = Label(data_connect_insert, text="个人最小购买单位")
        input_check_minBuy.grid(row=8, column=0)
        input_check_minOwn = Label(data_connect_insert, text="个人最小持有份额")
        input_check_minOwn.grid(row=9, column=0)
        input_check_rate = Label(data_connect_insert, text="预期收益率")
        input_check_rate.grid(row=10, column=0)

        input_number = Entry(data_connect_insert, width=15)
        input_number.grid(row=0, column=1)
        input_name = Entry(data_connect_insert, width=15)
        input_name.grid(row=1, column=1)
        input_ipo = Entry(data_connect_insert, width=15)
        input_ipo.grid(row=2, column=1)
        input_ipo1 = Entry(data_connect_insert, width=15)
        input_ipo1.grid(row=3, column=1)
        input_estab = Entry(data_connect_insert, width=15)
        input_estab.grid(row=4, column=1)
        input_estab1 = Entry(data_connect_insert, width=15)
        input_estab1.grid(row=5, column=1)
        input_price = tk.Radiobutton(data_connect_insert, text = "￥ 1.00")
        input_price.grid(row=6, column=1, sticky=W)
        input_price_value = 1
        input_risk_level = ttk.Combobox(data_connect_insert, width=12, state='readonly')
        input_risk_level['values'] = ('1', '2', '3', '4', '5')
        input_risk_level.grid(row=7, column=1, sticky=W)
        input_risk_level.current(1)

        input_minBuy = ttk.Combobox(data_connect_insert, width=12, state='readonly')
        input_minBuy['values'] = (0, 100, 1000, 10000)
        input_minBuy.grid(row=8, column=1)
        input_minBuy.current(0)

        input_minOwn = ttk.Combobox(data_connect_insert, width=12, state='readonly')
        input_minOwn['values'] = (0, 100, 1000, 10000)
        input_minOwn.grid(row=9, column=1)
        input_minOwn.current(0)

        input_rate = Entry(data_connect_insert, width=15)
        input_rate.grid(row=10, column=1)

        btn2 = tkinter.Button(data_connect_insert, text='新增理财产品', command=lambda: process(
            target=button_insert(input_number, input_name, input_ipo, input_ipo1, input_estab, input_estab1,
                                 input_price_value, input_risk_level, input_minBuy, input_minOwn,
                                 input_rate, cursor, connect)).start())
        btn2.grid(row=11, column=0)

        btn3 = tkinter.Button(data_connect_insert, text='更新产品信息', command=lambda: process(
            target=button_change(input_number, input_name, input_ipo, input_ipo1, input_estab, input_estab1,
                                 input_price_value, input_risk_level, input_minBuy, input_minOwn,
                                 input_rate, cursor, connect)).start())
        btn3.grid(row=11, column=1)

        data_connect_insert.mainloop()
    except BaseException:
        tkinter.messagebox.showinfo("提示", "连接地址异常")
        print("连接地址异常")

def button_insert(input_number, input_name, input_ipo, input_ipo1, input_estab, input_estab1,
                input_price, input_risk_level,input_minBuy, input_minOwn, input_rate, cursor, connect):
    try:
        number = input_number.get()
        name = input_name.get()
        ipo = input_ipo.get()
        ipo1 = input_ipo1.get()
        estab = input_estab.get()
        estab1 = input_estab1.get()
        price = float(input_price)
        risk_level = input_risk_level.get()
        minBuy = int(input_minBuy.get())
        minOwn = int(input_minOwn.get())
        rate = float(input_rate.get())
        today = str(datetime.date.today())
        if(number != '' and name != '' and ipo != '' and ipo1 != '' and estab != '' and estab1 != ''
                and risk_level != '' and rate != ''):
            data = (number, name, ipo, ipo1, estab,
                        estab1, price, risk_level, minBuy, minOwn, rate)
            print(data)
            sql = "INSERT INTO prodbaseinfo VALUES ('%s', '%s','%s','%s','%s','%s','%.2f', '%s', '%d','%d','%.4f')"
            cursor.execute(sql % data)
            connect.commit()
            tkinter.messagebox.showinfo("提示", "数据插入成功")
        else:
            tkinter.messagebox.showinfo("提示", "请输入完整的产品信息！")
    except Exception as e:
        tkinter.messagebox.showinfo('提示', '请检查输入格式后，重新插入数据！')

# 更新数据库连接参数OK
def data_show():
    try:
        data_show = tkinter.Tk()  # 定义一个窗体
        data_show.title('数据库参数设置界面')  # 定义窗体标题
        data_show.geometry('250x120+50+10')  # 设置窗体的大小250x120像素和初始位置（50，10）
        input_label_host = Label(data_show, text="请输入服务器地址")
        input_label_host.grid(row=0, column=0)
        input_label_port = Label(data_show, text="请输入端口号")
        input_label_port.grid(row=1, column=0)
        input_label_account = Label(data_show, text="请输入账号")
        input_label_account.grid(row=2, column=0)
        input_label_password = Label(data_show, text="请输入密码")
        input_label_password.grid(row=3, column=0)
        input_label_database = Label(data_show, text="请输入数据库名字")
        input_label_database.grid(row=4, column=0)

        input_host = Entry(data_show, width=15)
        input_host.grid(row=0, column=1)
        input_port = Entry(data_show, width=15)
        input_port.grid(row=1, column=1)
        input_account = Entry(data_show, width=15)
        input_account.grid(row=2, column=1)
        input_passwd = Entry(data_show, width=15, show='*')
        input_passwd.grid(row=3, column=1)
        input_database = Entry(data_show, width=15)
        input_database.grid(row=4, column=1)
        btn1 = tkinter.Button(data_show, text='建立连接', command=lambda: process(
            target=button_set(input_host, input_port, input_account, input_passwd, input_database)).start())
        btn1.grid(row=5, column=0)
        data_show.mainloop()  # 表示事件循环，使窗体一直保持显示状态
    except Exception as e:
        tkinter.messagebox.showinfo('提示', '输入有误，请重新输入！')

def data_connect_change():
    try:
        connect = pymysql.Connect(
            host=user_host,
            port=user_port,
            user=user_name,
            passwd=user_passwd,
            db=user_database,
            charset='utf8')
        cursor = connect.cursor()

        data_connect_change = tkinter.Tk()  # 定义一个窗体
        data_connect_change.title('理财产品信息删除')  # 定义窗体标题
        data_connect_change.geometry('500x300+200+150')  # 设置窗体的大小250x120像素和初始位置（50，10）
        # 定义显示栏
        src = scrolledtext.ScrolledText(data_connect_change, width=100, height=10)
        src.grid(row=0, column=0)
        # 定义文本标签
        input_label_number = Label(data_connect_change, text="产品代码")
        input_label_number.grid(row=1, column=0, sticky=W)
        # 定义输入框
        input_name = Entry(data_connect_change, width=15)
        input_name.grid(row=2, column=0, sticky=W)
        # 定义查询按钮
        btn2 = tkinter.Button(data_connect_change, text='查询产品', command=lambda: process(
            target=button_select(input_name, src, cursor, connect)).start())
        btn2.grid(row=3, column=0, sticky=W)
        # 定义删除按钮
        btn3 = tkinter.Button(data_connect_change, text='删除产品', command=lambda: process(
            target=button_delete(input_name, src, cursor, connect)).start())
        btn3.grid(row=4, column=0, sticky=W)
        # 保持窗口运行
        data_connect_change.mainloop()
    except BaseException :
        tkinter.messagebox.showinfo("提示", "连接地址异常")
        print("连接地址异常")

def button_change(input_number, input_name, input_ipo, input_ipo1, input_estab, input_estab1,
                                 input_price, input_risk_level, input_minBuy, input_minOwn,
                                 input_rate, cursor, connect):
    try:
        number = input_number.get()
        name = input_name.get()
        ipo = input_ipo.get()
        ipo1 = input_ipo1.get()
        estab = input_estab.get()
        estab1 = input_estab1.get()
        price = float(input_price)
        risk_level = input_risk_level.get()
        minBuy = int(input_minBuy.get())
        minOwn = int(input_minOwn.get())
        rate = float(input_rate.get())
        today = str(datetime.date.today())
        if(number != '' and name != '' and ipo != '' and ipo1 != '' and estab != '' and estab1 != ''
                and risk_level != '' and rate != ''):
            data = (name, ipo, ipo1, estab, estab1, price, risk_level, minBuy, minOwn, rate, number)

            sql = "UPDATE prodbaseinfo SET 'prd_name' = '%s', 'ipo_start_date' = '%s', " \
                  "'ipo_end_date' = '%s', 'estab_date' = '%s', 'end_date' = '%s', 'iss_price' = '%.2f', " \
                  "'risk_level' = '%s', 'psub_unit' = '%d', 'pmin_hold' = '%d', 'guest_rate' =  '%.4f' " \
                  "WHERE 'prd_code' = '%s')"
            cursor.execute(sql % data)
            connect.commit()
            tkinter.messagebox.showinfo("提示", "数据更新成功")
        else:
            tkinter.messagebox.showinfo("提示", "请输入完整的产品信息！")
    except Exception as e:
        tkinter.messagebox.showinfo('提示', '请检查输入格式！')

def button_delete(input_number, src, cursor, connect):
    prd_code = (input_number.get())
    sql = "delete from prodbaseinfo where prd_code = '%s'"
    cursor.execute(sql % prd_code)
    connect.commit()
    tkinter.messagebox.showinfo("提示", "产品编号为：" + prd_code +"的理财产品已删除！")

def button_select(input_number, src, cursor, connect):
    prd_code = (input_number.get())
    sql = "select * from prodbaseinfo where prd_code = '%s'"
    cursor.execute(sql% prd_code)
    desc = cursor.description
    connect.commit()
    for field in desc:
        src.insert(tkinter.END, field[0] + '  ')

    src.insert(tkinter.END, '\n')
    for row in cursor.fetchall():
        src.insert(tkinter.END, row)
        src.insert(tkinter.END, '\n')
        src.update()