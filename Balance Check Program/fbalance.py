import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

#----------------------------------------------------------------------------------------------------الأطر

def vodcash():
    #النصف العلوي (إدخال)
    #------------------------------------------------------------------------------------------------إطار العناوين
    global labelframe
    labelframe = tk.Frame(frame)
    labelframe.grid(row=1, column=1, columnspan=2, sticky="nsew")
    gridfillrow(frame, 2)
    gridfillcolumn(frame, 2)

    #------------------------------------------------------------------------------------------------العناوين
    idafaframe = tk.LabelFrame(labelframe, text="إضافات", labelanchor="ne")
    idafaframe.grid(row=1, column=8, rowspan=5, columnspan=2, padx=10, pady=(5, 5))

    idafatamilsql = "INSERT INTO omala (name) VALUES (?)"
    idafatrakamsql = "INSERT INTO vodnum (number) VALUES (?)"

    idafatamil = tk.Button(idafaframe, text=" إضافة عميل ", command=lambda: E1L1window("إضافة العميل", idafat, idafatamilsql), width=10)
    idafatrakam = tk.Button(idafaframe, text=" إضافة رقم ", command=lambda: E1L1window("إضافة الرقم", idafat, idafatrakamsql), width=10)
    idafatamil.grid(row=1, column=1, padx=5, pady=5)
    idafatrakam.grid(row=2, column=1, padx=5, pady=5)

    global moamlatframe
    moamlatframe = tk.LabelFrame(labelframe, text="إضافة معاملات", labelanchor="ne")
    moamlatframe.grid(row=1, column=1, rowspan=5, columnspan=7, padx=10, pady=(5, 5))

    sendlabel1 = tk.Label(moamlatframe, text=" استقبل العميل ")
    sendlabel2 = tk.Label(moamlatframe, text=" مبلغ ")
    sendlabel3 = tk.Label(moamlatframe, text=" من الرقم ")
    sendlabel1.grid(row=1, column=7, pady=5)
    sendlabel2.grid(row=1, column=5, pady=5)
    sendlabel3.grid(row=1, column=3, pady=5)

    recievelabel1 = tk.Label(moamlatframe, text=" أرسل العميل ")
    recievelabel2 = tk.Label(moamlatframe, text=" مبلغ ")
    recievelabel3 = tk.Label(moamlatframe, text=" على الرقم ")
    recievelabel1.grid(row=2, column=7, pady=5)
    recievelabel2.grid(row=2, column=5, pady=5)
    recievelabel3.grid(row=2, column=3, pady=5)

    #------------------------------------------------------------------------------------------------القوائم المتدلية
    tahdisomalarkam()

    #------------------------------------------------------------------------------------------------قيم المدخلات
    vodcashsend = tk.Entry(moamlatframe)
    vodcashsend.grid(row=1, column=4, padx=(20, 0), pady=5)

    vodcashrec = tk.Entry(moamlatframe)
    vodcashrec.grid(row=2, column=4, padx=(20, 0), pady=5)

    #------------------------------------------------------------------------------------------------أزرار الإضافات
    submitBt = tk.Button(moamlatframe, text=" إتمام إرسال المبلغ ", command=lambda: sglvod(vodcashsend, amilmokhtarsend, rkammokhtarsend, "عليه"), width=45)
    submitBt.grid(row=1, column=1, padx=(20, 0), pady=5)

    submitBt = tk.Button(moamlatframe, text=" إتمام استقبال المبلغ ", command=lambda: sglvod(vodcashrec, amilmokhtarrec, rkammokhtarrec, "له"), width=45)
    submitBt.grid(row=2, column=1, padx=(20, 0), pady=5)

    #النصف السفلي (الجداول)
    #------------------------------------------------------------------------------------------------أطر الجداول
    tableframe1 = tk.LabelFrame(frame, text="مديونيات العملاء", labelanchor="ne")
    tableframe1.grid(row=4, column=1, pady=5, sticky="nsew")

    tableframe2 = tk.LabelFrame(frame, text="المتاح على الأرقام", labelanchor="ne")
    tableframe2.grid(row=3, column=2, rowspan=3, sticky="nsew")

    tableframe3 = tk.LabelFrame(frame, text="سجل التعاملات اليوم", labelanchor="ne")
    tableframe3.grid(row=3, column=1, pady=5, sticky="nsew")

    #------------------------------------------------------------------------------------------------الجداول
    global ppltable, numtable, gdwlSgl
    pplorder = ("paid", "recieved", "name")
    pplcolumns = {" له ": 200, " عليه ": 200, " الاسم ": 200}

    numorder = ("available", "number")
    numcolumns = {" المتوفر ": 120, " الرقم ": 120}

    sgltartib = ("hour", "number", "reciever", "paid", "name", "id")
    sglsofof = {" الساعة ": 80, "من/على الرقم": 150," استقبل ": 150, " دفع ": 150, " اسم العميل ": 200, "الرقم":20}

    ppltable = createtable(tableframe1, pplorder, pplcolumns, "left", "e")
    numtable = createtable(tableframe2, numorder, numcolumns, "left", "e")
    gdwlSgl = createtable(tableframe3, sgltartib, sglsofof, "left", "e")

    ppltable.pack(padx=5, pady=10)
    numtable.pack(padx=5, pady=10)
    gdwlSgl.pack(padx=5, pady=10)

    vodtablefill()
    #------------------------------------------------------------------------------------------------بكرة الجدول
    createscroll(ppltable, tableframe1, 0, 5, 5, 5, "right")
    createscroll(numtable, tableframe2, 0, 5, 5, 5, "right")
    createscroll(gdwlSgl, tableframe3, 0, 5, 5, 5, "right")

def moamlat():
    #------------------------------------------------------------------------------------------------الأطر
    inputframe = tk.LabelFrame(frame, text=" رصيد داخل ", labelanchor="ne")
    inputframe.grid(row=1, column=1, sticky="nsew")

    outputframe = tk.LabelFrame(frame, text=" رصيد خارج ", labelanchor="ne")
    outputframe.grid(row=2, column=1, sticky="nsew")

    mabiatframe = tk.LabelFrame(frame, text=" المبيعات ", labelanchor="ne")
    mabiatframe.grid(row=1, column=2, sticky="nsew")

    dyonframe = tk.LabelFrame(frame, text=" ديون يومية ", labelanchor="ne")
    dyonframe.grid(row=2, column=2, sticky="nsew")

    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    #------------------------------------------------------------------------------------------------أطر الجداول
    inputtableframe = tk.Frame(inputframe)
    inputtableframe.grid(row=3, column=1, columnspan=4, sticky="nsew")

    mabiattableframe = tk.Frame(mabiatframe)
    mabiattableframe.grid(row=3, column=1, columnspan=4, sticky="nsew")

    outputtableframe = tk.Frame(outputframe)
    outputtableframe.grid(row=3, column=1, columnspan=4, sticky="nsew")

    dyontableframe = tk.Frame(dyonframe)
    dyontableframe.grid(row=3, column=1, columnspan=4, sticky="nsew")

    gridfillrow(inputframe, 4)
    gridfillcolumn(inputframe, 4)
    gridfillrow(mabiatframe, 4)
    gridfillcolumn(mabiatframe, 4)
    gridfillrow(outputframe, 4)
    gridfillcolumn(outputframe, 4)
    gridfillrow(dyonframe, 4)
    gridfillcolumn(dyonframe, 4)

    #------------------------------------------------------------------------------------------------صف عناوين المدخلات
    namelabelin = tk.Label(inputframe, text=" الاسم ")
    namelabelin.grid(row=1, column=4, padx=10, pady=5, sticky="w")

    valuelabelin = tk.Label(inputframe, text=" القيمة ")
    valuelabelin.grid(row=1, column=2, padx=(0, 10), pady=5, sticky="w")

    namelabelmabi = tk.Label(mabiatframe, text=" الاسم ")
    namelabelmabi.grid(row=1, column=4, padx=10, pady=5, sticky="w")

    valuelabelmabi = tk.Label(mabiatframe, text=" القيمة ")
    valuelabelmabi.grid(row=1, column=2, padx=(0, 10), pady=5, sticky="w")

    namelabelout = tk.Label(outputframe, text=" الاسم ")
    namelabelout.grid(row=1, column=4, padx=10, pady=5, sticky="w")

    valuelabelout = tk.Label(outputframe, text=" القيمة ")
    valuelabelout.grid(row=1, column=2, padx=(0, 10), pady=5, sticky="w")

    namelabeldyon = tk.Label(dyonframe, text=" الاسم ")
    namelabeldyon.grid(row=1, column=4, padx=10, pady=5, sticky="w")

    valuelabeldyon = tk.Label(dyonframe, text=" القيمة ")
    valuelabeldyon.grid(row=1, column=2, padx=(0, 10), pady=5, sticky="w")

    #------------------------------------------------------------------------------------------------صف قيم المدخلات
    inputname = tk.Entry(inputframe)
    inputname.grid(row=1, column=3, pady=5, sticky="ew")

    inputvalue = tk.Entry(inputframe)
    inputvalue.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="ew")

    mabiatname = tk.Entry(mabiatframe)
    mabiatname.grid(row=1, column=3, pady=5, sticky="ew")

    mabiatvalue = tk.Entry(mabiatframe)
    mabiatvalue.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="ew")

    outputname = tk.Entry(outputframe)
    outputname.grid(row=1, column=3, pady=5, sticky="ew")

    outputvalue = tk.Entry(outputframe)
    outputvalue.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="ew")

    dyonname = tk.Entry(dyonframe)
    dyonname.grid(row=1, column=3, pady=5, sticky="ew")

    dyonvalue = tk.Entry(dyonframe)
    dyonvalue.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="ew")

    #------------------------------------------------------------------------------------------------الأزرار
    inputbutton = tk.Button(inputframe, text=" أضف للرصيد الداخل ", command=lambda: moamlatdf(inputname, inputvalue, inputtable, "sgldahel"))
    inputbutton.grid(row=2, column=1, columnspan=3, padx=(10, 0), pady=5, sticky="ew")

    mabiatbutton = tk.Button(mabiatframe, text=" أضف للمبيعات ", command=lambda: moamlatdf(mabiatname, mabiatvalue, mabiattable, "sglbedaa"))
    mabiatbutton.grid(row=2, column=1, columnspan=3, padx=(10, 0), pady=5, sticky="ew")

    outputbutton = tk.Button(outputframe, text=" أضف للرصيد الخارج ", command=lambda: moamlatdf(outputname, outputvalue, outputtable, "sglhareg"))
    outputbutton.grid(row=2, column=1, columnspan=3, padx=(10, 0), pady=5, sticky="ew")

    dyonbutton = tk.Button(dyonframe, text=" أضف للديون ", command=lambda: moamlatdf(dyonname, dyonvalue, dyontable, "sgldyon"))
    dyonbutton.grid(row=2, column=1, columnspan=3, padx=(10, 0), pady=5, sticky="ew")

    #------------------------------------------------------------------------------------------------الجداول
    global inputtable, mabiattable, outputtable
    inputorder = ("hour", "value", "name", "#")
    inputcolumns = {" الساعة ": 150, " القيمة ": 150, " الاسم ": 190, "الرقم": 40}
    inputtable = createtable(inputtableframe, inputorder, inputcolumns, "left", "e")

    mabiatorder = ("hour", "value", "name", "#")
    mabiatcolumns = {" الساعة ": 150, " القيمة ": 150, " الاسم ": 190, "الرقم": 40}
    mabiattable = createtable(mabiattableframe, mabiatorder, mabiatcolumns, "left", "e")

    outputorder = ("hour", "value", "name", "#")
    outputcolumns = {" الساعة ": 150, " القيمة ": 150, " الاسم ": 190, "الرقم": 40}
    outputtable = createtable(outputtableframe, outputorder, outputcolumns, "left", "e")

    dyonorder = ("hour", "value", "name", "#")
    dyoncolumns = {" الساعة ": 150, " القيمة ": 150, " الاسم ": 190, "الرقم": 40}
    dyontable = createtable(dyontableframe, dyonorder, dyoncolumns, "left", "e")

    mofrdat = [{"nass": "إزالة دين", "dalla": izaletdyon}]
    kaymaD8taYmin(dyontableframe, dyontable, mofrdat)

    moamlattahdith(inputtable, "sgldahel")
    moamlattahdith(mabiattable, "sglbedaa")
    moamlattahdith(outputtable, "sglhareg")
    moamlattahdith(dyontable, "sgldyon")
    #------------------------------------------------------------------------------------------------بكر الجداول
    createscroll(inputtable, inputtableframe, 0, 5, 0, 0, "right")
    createscroll(mabiattable, mabiattableframe, 0, 5, 0, 0, "right")
    createscroll(outputtable, outputtableframe, 0, 5, 0, 0, "right")
    createscroll(dyontable, dyontableframe, 0, 5, 0, 0, "right")

def tasfeya():
    global rebh, tasfeyaQdm, mlkFtrd, mlkHqiq, zyada, zyadatrakom
    rebh = 0
    tasfeyaQdm = 0
    mlkFtrd = 0
    mlkHqiq = 0
    zyada = 0
    zyadatrakom = 0
    #-------------------------------------------------------------------------------------------------المكن
    global makanframe
    makanframe = tk.LabelFrame(frame, text=" المكن ", labelanchor="ne")
    makanframe.grid(row=1, column=1, sticky="ew")

    gridfillrow(frame, 8)
    gridfillcolumn(frame, 3)

    #--------------------------------------------------الملصقات
    makanlabel1 = tk.Label(makanframe, text=" فوري 1 ")
    makanlabel1.grid(row=1, column=2, padx=(0, 10), pady=5, sticky="w")

    makanlabel2 = tk.Label(makanframe, text=" فوري 2 ")
    makanlabel2.grid(row=2, column=2, padx=(0, 10), pady=(0, 5), sticky="w")

    makanlabel3 = tk.Label(makanframe, text=" أوباي ")
    makanlabel3.grid(row=1, column=4, padx=(0, 10), pady=5, sticky="w")

    makanlabel4 = tk.Label(makanframe, text=" ممكن ")
    makanlabel4.grid(row=2, column=4, padx=(0, 10), pady=(0, 5), sticky="w")

    magmo3label1 = tk.Label(makanframe, text=" مجموع المكن اليوم  ")
    magmo3label1.grid(row=3, column=3, columnspan=2, padx=(0, 10), pady=(0, 5), sticky="w")

    global makansum, magmo3makan
    makansum = 0
    magmo3makan = ttk.Label(makanframe, text=0, style="BorderedLabel.TLabel")
    magmo3makan.grid(row=3, column=1, columnspan=2, padx=10, pady=(0, 5), sticky="ew")

    #--------------------------------------------------المدخلات
    fawry1 = tk.Entry(makanframe)
    fawry1.grid(row=1, column=1, padx=(10, 0), pady=5, sticky="ew")

    fawry2 = tk.Entry(makanframe)
    fawry2.grid(row=2, column=1, padx=(10, 0), pady=(0, 5), sticky="ew")

    opay = tk.Entry(makanframe)
    opay.grid(row=1, column=3, padx=(10, 0), pady=5, sticky="ew")

    momken = tk.Entry(makanframe)
    momken.grid(row=2, column=3, padx=(10, 0), pady=(0, 5), sticky="ew")

    #--------------------------------------------------الأزرار
    sgl = tk.Button(makanframe, text=" سجل ", command=lambda: shashetgadwal("makan"))
    sgl.grid(row=4, column=3, padx=5, pady=5, sticky="ew")

    itmam = tk.Button(makanframe, text=" إتمام ", command=lambda: izhar("makan", fawry1, fawry2, opay, momken))
    itmam.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    #-------------------------------------------------------------------------------------------------رصيد داخل
    global da5elframe
    da5elframe = tk.LabelFrame(frame, text=" الرصيد الداخل ", labelanchor="ne")
    da5elframe.grid(row=2, column=1, sticky="ew")

    #--------------------------------------------------الملصقات
    magmo3label1 = tk.Label(da5elframe, text=" مجموع اليوم  ")
    magmo3label1.grid(row=1, column=4, columnspan=2, padx=5, pady=5, sticky="w")

    global da5elsum, magmo3da5el
    da5elsum = 0
    magmo3da5el = ttk.Label(da5elframe, text=0, style="BorderedLabel.TLabel", width=20)
    magmo3da5el.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

    #--------------------------------------------------الأزرار
    sgl1 = tk.Button(da5elframe, text=" سجل ", command=lambda: shashetgadwal("sgldahel"))
    sgl1.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    sgl2 = tk.Button(da5elframe, text=" إتمام ", command=lambda: sqlsum("da5el", da5elframe, "sgldahel"))
    sgl2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #-------------------------------------------------------------------------------------------------رصيد خارج
    global haregframe
    haregframe = tk.LabelFrame(frame, text=" الرصيد الخارج ", labelanchor="ne")
    haregframe.grid(row=3, column=1, pady=5, sticky="ew")

    #--------------------------------------------------الملصقات
    magmo3label1 = tk.Label(haregframe, text=" مجموع اليوم  ")
    magmo3label1.grid(row=1, column=4, columnspan=2, padx=(0, 10), pady=(0, 5), sticky="w")

    global haregsum, magmo35areg
    haregsum = 0
    magmo35areg = ttk.Label(haregframe, text=0, style="BorderedLabel.TLabel", width=20)
    magmo35areg.grid(row=1, column=3, padx=(10, 10), pady=(0, 5), sticky="ew")

    #--------------------------------------------------الأزرار
    sgl3 = tk.Button(haregframe, text=" سجل ", command=lambda: shashetgadwal("sglhareg"))
    sgl3.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    sgl4 = tk.Button(haregframe, text=" إتمام ", command=lambda: sqlsum("hareg", haregframe, "sglhareg"))
    sgl4.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #-------------------------------------------------------------------------------------------------مبيعات
    global mabiatframe
    mabiatframe = tk.LabelFrame(frame, text=" المبيعات ", labelanchor="ne")
    mabiatframe.grid(row=4, column=1, pady=5, sticky="ew")

    #--------------------------------------------------الملصقات
    magmo3label11 = tk.Label(mabiatframe, text=" مجموع اليوم  ")
    magmo3label11.grid(row=1, column=4, columnspan=2, padx=(0, 10), pady=(0, 5), sticky="w")

    global mabiatsum, magmo3mabiat
    mabiatsum = 0
    magmo3mabiat = ttk.Label(mabiatframe, text=0, style="BorderedLabel.TLabel", width=20)
    magmo3mabiat.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")

    #--------------------------------------------------الأزرار
    sgl5 = tk.Button(mabiatframe, text=" سجل ", command=lambda: shashetgadwal("sglbedaa"))
    sgl5.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    sgl6 = tk.Button(mabiatframe, text=" إتمام ", command=lambda: sqlsum("mabiat", mabiatframe, "sglbedaa"))
    sgl6.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #-------------------------------------------------------------------------------------------------دين المحل
    global dyonframe
    dyonframe = tk.LabelFrame(frame, text=" الديون ", labelanchor="ne")
    dyonframe.grid(row=5, column=1, pady=5, sticky="ew")

    #--------------------------------------------------الملصقات
    magmo3label1 = tk.Label(dyonframe, text=" مجموع اليوم  ")
    magmo3label1.grid(row=1, column=4, columnspan=2, padx=(0, 10), pady=(0, 5), sticky="w")

    global dyonsum, magmo3dyon
    dyonsum = 0
    magmo3dyon = ttk.Label(dyonframe, text=0, style="BorderedLabel.TLabel", width=20)
    magmo3dyon.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")

    #--------------------------------------------------الأزرار
    sgl5 = tk.Button(dyonframe, text=" سجل ", command=lambda: shashetgadwal("sgldyon"))
    sgl5.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    sgl6 = tk.Button(dyonframe, text=" إتمام ", command=lambda: sqlsum("dyon", dyonframe, "sgldyon"))
    sgl6.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #-------------------------------------------------------------------------------------------------فودافون كاش
    global cashframe
    cashframe = tk.LabelFrame(frame, text=" فودافون كاش ", labelanchor="ne")
    cashframe.grid(row=6, column=1, sticky="ew")

    #--------------------------------------------------الملصقات
    dyonlabel = tk.Label(cashframe, text=" مجموع ديون العملاء ")
    dyonlabel.grid(row=1, column=4, columnspan=2, padx=(0, 10), pady=(0, 5), sticky="w")

    rakamlabel = tk.Label(cashframe, text=" مجموع رصيد الأرقام ")
    rakamlabel.grid(row=2, column=4, columnspan=2, padx=(0, 10), pady=(0, 5), sticky="w")

    global omalamag, rakammag, omalamagmo3, rakammagmo3
    omalamagmo3 = 0
    rakammagmo3 = 0
    omalamag = ttk.Label(cashframe, text=omalamagmo3, style="BorderedLabel.TLabel", width=20)
    omalamag.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")

    rakammag = ttk.Label(cashframe, text=rakammagmo3, style="BorderedLabel.TLabel", width=20)
    rakammag.grid(row=2, column=3, padx=10, pady=(0, 5), sticky="ew")

    #--------------------------------------------------الأزرار
    sgl7 = tk.Button(cashframe, text="سجل", command=lambda: sglVcashW())
    sgl7.grid(row=1, column=1, padx=5, pady=(0, 5), sticky="ew")

    sgl8 = tk.Button(cashframe, text=" إتمام ", command=lambda: sqlsumvodcash("vodnum", "omala", cashframe))
    sgl8.grid(row=2, column=1, padx=5, pady=(0, 5), sticky="ew")

    #-------------------------------------------------------------------------------------------------الدرج
    global dorgframe
    dorgframe = tk.LabelFrame(frame, text=" الدرج ", labelanchor="ne")
    dorgframe.grid(row=7, column=1, sticky="ew")

    #--------------------------------------------------الملصقات
    magmo3label1 = tk.Label(dorgframe, text=" رصيد الدرج ")
    magmo3label1.grid(row=1, column=4, columnspan=2, padx=5, pady=(0, 5), sticky="w")

    global dorgmag, magmo3dorg
    dorgmag = 0
    magmo3dorg = ttk.Label(dorgframe, text=dorgmag, style="BorderedLabel.TLabel", width=20)
    magmo3dorg.grid(row=1, column=3, padx=5, pady=(0, 5), sticky="ew")

    #--------------------------------------------------المدخلات
    dorg = tk.Entry(dorgframe)
    dorg.grid(row=1, column=1, columnspan=2, padx=5, pady=(0, 5), sticky="ew")

    #--------------------------------------------------الأزرار
    sgl = tk.Button(dorgframe, text=" سجل ", command=lambda: shashetgadwal("dorg"))
    sgl.grid(row=2, column=2, padx=(5, 0), pady=5, sticky="ew")

    itmam = tk.Button(dorgframe, text=" إتمام ", command=lambda: izhar("dorg", dorg))
    itmam.grid(row=2, column=1, padx=(5, 0), pady=5, sticky="ew")

    #-------------------------------------------------------------------------------------------------التصفية
    tasfeyaframe = tk.LabelFrame(frame, text=" التصفية ", labelanchor="n")
    tasfeyaframe.grid(row=1, column=2, rowspan=7, padx=5, pady=5, sticky="nsew")

    #--------------------------------------------------تصفية اليوم السابق
    global tasfeyakablframe
    tasfeyakablframe = tk.LabelFrame(tasfeyaframe, text=" تصفية اليوم السابق ", labelanchor="ne")
    tasfeyakablframe.grid(row=1, column=2, pady=5, sticky="ew")

    tasfeyakabllabel = ttk.Label(tasfeyakablframe, text=tasfeyaQdm, style="BorderedLabel.TLabel", width=20)
    tasfeyakabllabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #--------------------------------------------------المكسب
    global maksabframe
    maksabframe = tk.LabelFrame(tasfeyaframe, text=" المكسب ", labelanchor="ne")
    maksabframe.grid(row=1, column=1, pady=5, sticky="ew")

    maksablabel = ttk.Label(maksabframe, text=rebh, style="BorderedLabel.TLabel", width=20)
    maksablabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #--------------------------------------------------الرصيد بعد المكسب
    global tasfeyabaadframe
    tasfeyabaadframe = tk.LabelFrame(tasfeyaframe, text=" الرصيد بعد المكسب ", labelanchor="ne")
    tasfeyabaadframe.grid(row=2, column=2, pady=5, sticky="ew")

    tasfeyabaadlabel = ttk.Label(tasfeyabaadframe, text=mlkFtrd, style="BorderedLabel.TLabel", width=20)
    tasfeyabaadlabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #--------------------------------------------------الرصيد الحقيقي
    global tasfeyahaqiqiframe
    tasfeyahaqiqiframe = tk.LabelFrame(tasfeyaframe, text=" الرصيد الحقيقي ", labelanchor="ne")
    tasfeyahaqiqiframe.grid(row=2, column=1, pady=5, sticky="ew")

    tasfeyahaqiqilabel = ttk.Label(tasfeyahaqiqiframe, text=mlkHqiq, style="BorderedLabel.TLabel", width=20)
    tasfeyahaqiqilabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #--------------------------------------------------العجز
    global agzframe
    agzframe = tk.LabelFrame(tasfeyaframe, text=" العجز/الزيادة ", labelanchor="ne")
    agzframe.grid(row=3, column=2, pady=5, sticky="ew")

    agzlabel = ttk.Label(agzframe, text=zyada, style="BorderedLabel.TLabel", width=20)
    agzlabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #--------------------------------------------------العجز التراكمي
    global agztrakomiframe
    agztrakomiframe = tk.LabelFrame(tasfeyaframe, text=" العجز/الزيادة التراكمية (من شهر) ", labelanchor="ne")
    agztrakomiframe.grid(row=3, column=1, pady=5, sticky="ew")

    agztrakomilabel = ttk.Label(agztrakomiframe, text=zyadatrakom, style="BorderedLabel.TLabel", width=20)
    agztrakomilabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    #--------------------------------------------------الملاحظات
    global molahzatframe, textfield
    molahzatframe = tk.LabelFrame(tasfeyaframe, text="ملاحظات", labelanchor="ne")
    molahzatframe.grid(row=4, column=1, columnspan=2, padx=5, pady=(5, 0), sticky="ns")
    textfield = tk.Text(molahzatframe, wrap="word", width=37, height=21)
    textfield.grid(row=1, column=1, padx=5, pady=(5, 0), sticky="nsew")

    gridfillrow(tasfeyaframe, 6)
    gridfillcolumn(tasfeyaframe, 2)

    itmam2 = tk.Button(molahzatframe, text=" سجل التصفيات ", command= lambda: shashetgadwal("sgltasfeya"))
    itmam2.grid(row=4, column=1, columnspan=2, padx=5, pady=(5, 0), sticky="ew")

    itmam2 = tk.Button(molahzatframe, text=" إتمام تصفية اليوم ", command=lambda: eltamam(), bg="red")
    itmam2.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

    #-------------------------------------------------------------------------------------------------الثوابت
    restframe = tk.Frame(frame)
    restframe.grid(row=1, column=3, rowspan=7, sticky="nsew")

    global thwabtframe
    gridfillrow(restframe, 7)
    gridfillcolumn(restframe, 1)
    thwabtframe = tk.LabelFrame(restframe, text=" الثوابت ", labelanchor="ne")
    thwabtframe.grid(row=1, column=1, sticky="ew")

    #--------------------------------------------------الملصقات
    magmo3label1 = tk.Label(thwabtframe, text=" المجموع ")
    magmo3label1.grid(row=1, column=5, pady=(0, 5), sticky="ew")

    global thwabtsum, magmo3thwabt
    thwabtsum = 0
    magmo3thwabt = ttk.Label(thwabtframe, text=thwabtsum, style="BorderedLabel.TLabel", width=20)
    magmo3thwabt.grid(row=1, column=4, padx=5, pady=(0, 5), sticky="ew")

    #--------------------------------------------------الأزرار
    sgl = tk.Button(thwabtframe, text=" قائمة الثوابت ", command=lambda: shashetgadwal("sabet"))
    sgl.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

    idafa2 = tk.Button(thwabtframe, text=" إتمام ", command=lambda: sqlsum("thwabt", thwabtframe, "sabet"))
    idafa2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    idafa3 = tk.Button(thwabtframe, text="إضافة ثابت", command=windowsabet)
    idafa3.grid(row=1, column=6, padx=5, pady=5, sticky="ew")

    idafa3 = tk.Button(thwabtframe, text="سجل", command=lambda: shashetgadwal("sglsabet"))
    idafa3.grid(row=1, column=7, padx=5, pady=5, sticky="ew")

    #-------------------------------------------------------------------------------------------------الجمعيات
    gameyaframe = tk.LabelFrame(restframe, text=" الجمعيات ", labelanchor="ne")
    gameyaframe.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

    gameyatableframe = tk.Frame(gameyaframe)
    gameyatableframe.grid(row=2, column=1, columnspan=3, sticky="nsew")
    gameyaorder = ("gameya", "monthsd", "months", "qima", "start", "name", "id")
    gameyacolumns = {"ج/ش": 60, "دُفع": 60, "مج شهر": 60, "القيمة": 60, "ابتدى": 70, "الاسم": 100, "#": 20}
    gameyatable = createtable(gameyatableframe, gameyaorder, gameyacolumns, "left", "e")
    createscroll(gameyatable, gameyatableframe, 0, 5, 0, 0, "right")

    kestgameya(gameyatable, "gameya")
    mofrdatg = [{"nass": "دفع شهر", "dalla": dafa3shahr}]
    kaymaD8taYmin(gameyatableframe, gameyatable, mofrdatg)

    sgl = tk.Button(gameyaframe, text=" سجل ", command=lambda: shashetgadwal("sglgameya"))
    sgl.grid(row=1, column=1, padx=(10, 5), pady=5, sticky="ew")

    idafagameya = tk.Button(gameyaframe, text=" إضافة جمعية ", command=lambda: kestgameyaidafa(gameyatable, "gameya"))
    idafagameya.grid(row=1, column=3, padx=(5, 20), pady=5, sticky="ew")
    #-------------------------------------------------------------------------------------------------الاقساط
    qestframe = tk.LabelFrame(restframe, text=" الأقساط ", labelanchor="ne")
    qestframe.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

    qesttableframe = tk.Frame(qestframe)
    qesttableframe.grid(row=2, column=1, columnspan=3, sticky="nsew")
    qestorder = ("kest", "monthsd", "months", "qima", "start", "pname", "name", "id")
    qestcolumns = {"ج/ش": 50, "دُفع": 50, "مج ش": 50, "الثمن": 50, "ابتدى": 70, "السلعة": 70, "العميل": 70, "#": 20}
    qesttable = createtable(qesttableframe, qestorder, qestcolumns, "left", "e")
    createscroll(qesttable, qesttableframe, 0, 5, 0, 0, "right")

    kestgameya(qesttable, "kest")
    mofrdatk = [{"nass": "دفع شهر", "dalla": dafa3shahr}]
    kaymaD8taYmin(qesttableframe, qesttable, mofrdatk)

    sgl = tk.Button(qestframe, text=" سجل ", command=lambda: shashetgadwal("sglkest"))
    sgl.grid(row=1, column=1, padx=(10, 5), pady=5, sticky="ew")

    idafaqest = tk.Button(qestframe, text=" إضافة قسط ", command=lambda: kestgameyaidafa(qesttable, "kest"))
    idafaqest.grid(row=1, column=3, padx=(5, 20), pady=5, sticky="ew")

#----------------------------------------------------------------------------------------------------دوال فودافون كاش

def E1L1window(esm, function, sqlcommand):
    newWindow = tk.Toplevel(base)
    newWindow.title("إضافة عميل")

    nameframe = tk.LabelFrame(newWindow, text=esm, labelanchor="ne")
    nameframe.grid(row=1, column=2, padx=20, pady=20)

    modhal = tk.Entry(nameframe, width=30)
    modhal.grid(row=1, column=1, padx=10, pady=10)

    zorar = tk.Button(nameframe, text=esm, command=lambda: function(sqlcommand, (modhal.get(),), newWindow), width=10)
    zorar.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
    return

def idafat(sqlcommand, qima, window=None):
    conn = sqlite3.connect("tasfeya.db")
    tasfeyadb = conn.cursor()
    if "INSERT INTO omala" in sqlcommand:
        if not halEsmMwgood(tasfeyadb, qima, "omala", "name"):
            tasfeyadb.execute(sqlcommand, qima)
            conn.commit()
            messagebox.showinfo("تم", "تمت إضافة العميل بنجاح", parent=window)
        else:
            messagebox.showerror("خطأ", "قد أدخلت اسما فارغا أو اسم العميل موجود بالفعل", parent=window)
    elif "INSERT INTO vodnum" in sqlcommand:
        try:
            int(qima[0])
        except ValueError:
            messagebox.showerror("خطأ", "القيمة المدخلة فيها حروف", parent=window)
            return
        if not halEsmMwgood(tasfeyadb, qima, "vodnum", "number"):
            tasfeyadb.execute(sqlcommand, qima)
            conn.commit()
            messagebox.showinfo("تم", "تمت إضافة الرقم بنجاح", parent=window)
        else:
            messagebox.showerror("خطأ", "قد أدخلت رقما فارغا أو الرقم موجود بالفعل", parent=window)
    else:
        tasfeyadb.execute(sqlcommand, qima)
        messagebox.showinfo("تم", "تمت إضافة المعاملة بنجاح", parent=window)
        conn.commit()
    tasfeyadb.close()

    if window:
        window.destroy()

    tahdisomalarkam()
    vodtablefill()
    return

def sglvod(vodcashqima, amill, rakamm, lihaleh):
    qima = (vodcashqima.get(),)
    amilll = amill.get()
    amil = (amilll,)
    rakam = (rakamm.get(),)
    try:
        rakamsql = arkamdict[rakam[0]][0]
    except KeyError:
        messagebox.showerror("خطأ", "أنت لم تختر رقما أو عميلا")
        return
    rakamsql = arkamdict[rakam[0]][0]
    rakamaleh = istehrag("SELECT aleh FROM vodnum WHERE number = ?", (rakamsql,))
    amilkey = 1
    try:
        amilll[0] == '{'
    except IndexError:
        amilkey = 0
        amil = ('إضافة خارجية',)
    else:
        #----------------------------------------------------لمعالجة حالة الاسم العربي
        if amilll[0] == '{':
            amillll = amilll[1:-1]
            amil = (amillll,)
            print(amil)

        #----------------------------------------------------جدول العملاء
        amillih = istehrag("SELECT lih FROM omala WHERE name=?", amil)
        amilaleh = istehrag("SELECT aleh FROM omala WHERE name=?", amil)

    try:
        int(qima[0])
    except ValueError:
        messagebox.showerror("خطأ", "الرقم المدخل فيه حروف أو فارغ")
        return
    #----------------------------------------------------------------------------------عند ضغط زر الاستقبال
    if lihaleh == "له":
        #----------------------------------------------------جدول الأرقام
        rakamgdid = rakamaleh[0][0] + int(qima[0])
        idafat("UPDATE vodnum SET aleh = ? WHERE number = ?", [rakamgdid, rakamsql])

        #----------------------------------------------------جدول العملاء
        if amilkey == 1:
            qimagdid = int(qima[0]) + amillih[0][0] - amilaleh[0][0]
            if qimagdid >= 0:
                idafat("UPDATE omala SET lih = ? WHERE name = ?", [qimagdid, amil[0]])
                idafat("UPDATE omala SET aleh = 0 WHERE name = ?", amil)
            elif qimagdid < 0:
                qimagdid = -qimagdid
                idafat("UPDATE omala SET aleh = ? WHERE name = ?", [qimagdid, amil[0]])
                idafat("UPDATE omala SET lih = 0 WHERE name = ?", amil)

        sql = "INSERT INTO sglvod (esmamil, qimalih, rakam, date, hour) VALUES (?, ?, ?, ?, ?);"
        idhalat = [str(amil[0]), int(qima[0]), str(rakamsql), nowtime("date"), nowtime("hour")]
        idafat(sql, idhalat)
    #----------------------------------------------------------------------------------عند ضغط زر الأرسال
    elif lihaleh == "عليه":
        #----------------------------------------------------جدول الأرقام
        rakamgdid = rakamaleh[0][0] - int(qima[0])
        if rakamgdid < 0:
            messagebox.showerror("خطأ", "القيمة المدخلة غير متاحة على الرقم المختار!")
            return
        else:
            idafat("UPDATE vodnum SET aleh = ? WHERE number = ?", [rakamgdid, rakamsql])

        #----------------------------------------------------جدول العملاء
            if amilkey == 1:
                qimagdid = int(qima[0]) + amilaleh[0][0] - amillih[0][0]
                if qimagdid >= 0:
                    idafat("UPDATE omala SET aleh = ? WHERE name = ?", [qimagdid, amil[0]])
                    idafat("UPDATE omala SET lih = 0 WHERE name = ?", amil)
                elif qimagdid < 0:
                    qimagdid = -qimagdid
                    idafat("UPDATE omala SET lih = ? WHERE name = ?", [qimagdid, amil[0]])
                    idafat("UPDATE omala SET aleh = 0 WHERE name = ?", amil)

    #----------------------------------------------------جدول سجلات فودافون
            sql = "INSERT INTO sglvod (esmamil, qimaaleh, rakam, date, hour) VALUES (?, ?, ?, ?, ?);"
            idhalat = [str(amil[0]), int(qima[0]), str(rakamsql), nowtime("date"), nowtime("hour")]
            idafat(sql, idhalat)

    vodtablefill()
    vodcashqima.delete('0', 'end')

    return

def vodtablefill():
    gadwalsgl = istehrag("SELECT hour, rakam, qimaaleh, qimalih, esmamil, id FROM sglvod WHERE shaghal = 'a';")
    ppltableinfo = istehrag("SELECT lih, aleh, name FROM omala ORDER BY aleh;")
    numtableinfo = istehrag("SELECT aleh, number FROM vodnum ORDER BY aleh;")
    tableupdate(gdwlSgl, gadwalsgl)
    tableupdate(ppltable, ppltableinfo, "vodomala")
    tableupdate(numtable, numtableinfo, "vodnum")
    return

def tahdisomalarkam(frame=None):
    global customers, last3nums, customersdict, arkamdict, amilmokhtarsend, amilmokhtarrec, rkammokhtarsend, rkammokhtarrec

    customers = istehrag("SELECT name FROM omala;")

    numbers = istehrag("SELECT number FROM vodnum;")
    last4nums = [str(number)[-7:-3] for number in numbers]
    arkamdict = dict(zip(last4nums, numbers))

    customermenu1, amilmokhtarsend = createcombobox(moamlatframe, "", customers)
    customermenu2, amilmokhtarrec = createcombobox(moamlatframe, "", customers)

    numbermenu1, rkammokhtarsend = createcombobox(moamlatframe, "", last4nums)
    numbermenu2, rkammokhtarrec = createcombobox(moamlatframe, "", last4nums)

    customermenu1.grid(row=1, column=6, padx=(20, 0), pady=5)
    customermenu2.grid(row=2, column=6, padx=(20, 0), pady=5)
    numbermenu1.grid(row=1, column=2, padx=(20, 0), pady=5)
    numbermenu2.grid(row=2, column=2, padx=(20, 0), pady=5)

    global tarihframe, tarihframe2

    if frame == "omala":
        global amilmokhtar, rkammokhtar
        customermenu11, amilmokhtar = createcombobox(tarihframe, "", customers)
        customermenu11.grid(row=1, column=3, padx=5, pady=5)
    elif frame == "arkam":
        numbermenu11, rkammokhtar = createcombobox(tarihframe2, "", last4nums)
        numbermenu11.grid(row=1, column=3, padx=5, pady=5)
    return

#----------------------------------------------------------------------------------------------------دوال المعاملات

def moamlatdf(name, value, moamlattable, sqltable):
    esm = name.get()
    qima = value.get()
    try:
        int(qima)
    except ValueError:
        messagebox.showerror("خطأ", "لقد أدخلت حروفا في خانة القيمة أو الحقل فارغ")
        return
    if (str(esm) == '') or (str(qima) == ''):
        messagebox.showerror("خطأ", "أحد الحقلين أو كلاهما فارغ!")
    else:
        idafat(f"INSERT INTO {sqltable} (name, qima, date, hour) VALUES (?, ?, ?, ?)", [str(esm), int(qima), nowtime('date'), nowtime('hour')])
        moamlattahdith(moamlattable, sqltable)
        name.delete('0', 'end')
        value.delete('0', 'end')
    return

def moamlattahdith(moamlattable, sqltable):
    info = istehrag(f"SELECT hour, qima, name, id FROM {sqltable} WHERE shaghal = 'a';")
    tableupdate(moamlattable, info)
    return

def izaletdyon(gdwl, itar):
    egaba = messagebox.askyesnocancel("تأكد", "أمتأكد أنك تريد إزالة هذا الدين؟", parent=itar)
    if egaba == True:
        wsl = sqlite3.connect("tasfeya.db")
        tasfeyadb = wsl.cursor()

        mo5tar = gdwl.selection()
        qimamo5tar = gdwl.item(mo5tar)
        id = qimamo5tar['values'][3]
        tasfeyadb.execute(f"UPDATE sgldyon SET shaghal='Nh' WHERE id={id}")

        wsl.commit()
        tasfeyadb.close()

        moamlattahdith(gdwl, "sgldyon")
        messagebox.showinfo("تم", "تمت الإزالة بنجاح", parent=itar)
    return
#----------------------------------------------------------------------------------------------------دالة إتمام التصفية النهائية

def eltamam():
    global Alam
    if 0 in Alam:
        messagebox.showerror("خطأ", "لم تتمم على كل عناصر التصفية")
        return
    check = messagebox.askyesnocancel("تأكد", "هل أنت متأكد من تصفية اليوم؟ لن تستطيع إضافة أي بيانات لهذا اليوم مرة أخرى.")
    if check == True:
        wsl = sqlite3.connect("tasfeya.db")
        tasfeyadb = wsl.cursor()

        kest = istehrag("SELECT id FROM sglkest ORDER BY id DESC LIMIT 1")
        try:
            kest[0][0]
        except IndexError:
            kestid = 0
        else:
            if kestid[0][0] is None:
                kestid = 0
            else:
                kestid = kest[0][0]

        kestQd = istehrag("SELECT kestid FROM sgltasfeya ORDER BY id DESC LIMIT 1")
        try:
            kestQd[0][0]
        except IndexError:
            kestQddid = 0
        else:
            if kestQd[0][0] is None:
                kestQddid = 0
            else:
                kestQddid = kestQd[0][0]

        if kestid != kestQddid:
            maggkest = istehrag(f"SELECT SUM(qima) FROM sglkest WHERE id > {kestQddid} AND id <= {kestid};")
            magkest = maggkest[0][0]
            if magkest is None:
                magkest = 0
        else:
            magkest = 0

        global rebh, tasfeyaQdm, mlkFtrd, mlkHqiq, zyada, zyadatrakom
        global da5elsum, mabiatsum, haregsum, makansum, omalamagmo3, rakammagmo3, dorgmag, thwabtsum, dyonsum

        if da5elsum[0][0] is None:
            da55elsum = 0
        else:
            da55elsum = da5elsum[0][0]
        if mabiatsum[0][0] is None:
            mabbiatsum = 0
        else:
            mabbiatsum = mabiatsum[0][0]
        if haregsum[0][0] is None:
            hareggsum = 0
        else:
            hareggsum = haregsum[0][0]
        if thwabtsum[0][0] is None:
            thwaabtsum = 0
        else:
            thwaabtsum = thwabtsum[0][0]
        if dyonsum[0][0] is None:
            dyonnsum = 0
        else:
            dyonnsum = dyonsum[0][0]
        if makansum is None:
            makansum = 0
        if omalamagmo3 is None:
            omalamagmo3 = 0
        if rakammagmo3 is None:
            rakammagmo3 = 0
        if dorgmag is None:
            dorgmag = 0

        rebh = da55elsum + mabbiatsum - hareggsum + magkest
        lina = makansum + omalamagmo3 + rakammagmo3 + dorgmag
        alena = thwaabtsum + dyonnsum

        tasfeyaQd = istehrag("SELECT tasfHqiq FROM sgltasfeya ORDER BY id DESC LIMIT 1")
        try:
            tasfeyaQd[0][0]
        except IndexError:
            tasfeyaQdm = 0
        else:
            if tasfeyaQd[0][0] is None:
                tasfeyaQdm = 0
            else:
                tasfeyaQdm = tasfeyaQd[0][0]

        mlkFtrd = tasfeyaQdm + rebh
        mlkHqiq = lina - alena
        zyada = mlkHqiq - mlkFtrd

        tarih = nowtime('date')
        saayom = nowtime('hour')
        yom = tarih[0:3]
        shahrfat = str(int(tarih[3:5]) - 1)
        sana = tarih[5:10]
        tarihshahrfat = yom + shahrfat + sana

        zyadatrakomm = istehrag(f"SELECT SUM(zyada) FROM sgltasfeya WHERE date='{tarihshahrfat}'")
        zyadatrakom = zyadatrakomm[0][0]
        if zyadatrakom is None:
            zyadatrakom = 0

        global molahzatframe, textfield
        if (textfield.get("1.0", tk.END)) == "\n":
            mohtawa = ''
        else:
            mohtawa = f"{nowtime('datehour')}" + "\n\n" + textfield.get("1.0", tk.END) + "-----------------------\n\n"
        tasfeyadb.execute(f"INSERT INTO sgltasfeya (date, hour, dorg, bedaa, rasidmkn, dahel, hareg, vodnum, omala, dyon, kestid, rebh, sabet, magkest, lina, alena, tasfHqiq, tasfFtrd, zyada, molahzat) VALUES ('{tarih}', '{saayom}', {dorgmag}, {mabbiatsum}, {makansum}, {da55elsum}, {hareggsum}, {rakammagmo3}, {omalamagmo3}, {dyonnsum}, {kestid}, {rebh}, {thwaabtsum}, {magkest}, {lina}, {alena}, {mlkHqiq}, {mlkFtrd}, {zyada}, '{mohtawa}')")

        tasfeyadb.execute(f"INSERT INTO sglomalacash (idAmil, amil, qima, date, hour) SELECT idAmil, name, aleh, '{tarih}', '{saayom}' FROM omala WHERE aleh != 0")
        tasfeyadb.execute(f"INSERT INTO sglomalacash (idAmil, amil, qima, date, hour) SELECT idAmil, name, aleh, '{tarih}', '{saayom}' FROM omala WHERE aleh != 0")
        tasfeyadb.execute(f"INSERT INTO sglarkamcash (elrakam, elrakamid, qima, date, hour) SELECT id, number, aleh, '{tarih}', '{saayom}' FROM vodnum WHERE aleh != 0")

        tasfeyadb.execute("UPDATE sglvod SET shaghal = 'Nh' WHERE shaghal = 'a'")
        tasfeyadb.execute("UPDATE sgldahel SET shaghal = 'Nh' WHERE shaghal = 'a'")
        tasfeyadb.execute("UPDATE sglhareg SET shaghal = 'Nh' WHERE shaghal = 'a'")
        tasfeyadb.execute("UPDATE sglbedaa SET shaghal = 'Nh' WHERE shaghal = 'a'")

        wsl.commit()
        tasfeyadb.close()

        messagebox.showinfo("تم", "أُنهيت تصفية اليوم بنجاح")

        Alam = [0] * len(Alam)
        textfield.delete("1.0", tk.END)

        global rakammag, omalamag, magmo3mabiat, magmo3thwabt, magmo3dyon, magmo35areg, magmo3da5el, magmo3dorg, magmo3makan
        rakammag.destroy()
        rakammag = ttk.Label(cashframe, text=0, style="BorderedLabel.TLabel", width=20)
        rakammag.grid(row=2, column=3, padx=10, pady=(0, 5), sticky="ew")

        omalamag.destroy()
        omalamag = ttk.Label(cashframe, text=0, style="BorderedLabel.TLabel", width=20)
        omalamag.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")

        magmo3mabiat.destroy()
        magmo3mabiat = ttk.Label(mabiatframe, text=0, style="BorderedLabel.TLabel", width=20)
        magmo3mabiat.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")

        magmo3thwabt.destroy()
        magmo3thwabt = ttk.Label(thwabtframe, text=0, style="BorderedLabel.TLabel", width=20)
        magmo3thwabt.grid(row=1, column=4, padx=10, pady=(0, 5), sticky="ew")

        magmo3dyon.destroy()
        magmo3dyon = ttk.Label(dyonframe, text=0, style="BorderedLabel.TLabel", width=20)
        magmo3dyon.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")

        magmo35areg.destroy()
        magmo35areg = ttk.Label(haregframe, text=0, style="BorderedLabel.TLabel", width=20)
        magmo35areg.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")

        magmo3da5el.destroy()
        magmo3da5el = ttk.Label(da5elframe, text=0, style="BorderedLabel.TLabel", width=20)
        magmo3da5el.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")

        magmo3dorg.destroy()
        magmo3dorg = ttk.Label(dorgframe, text=0, style="BorderedLabel.TLabel", width=20)
        magmo3dorg.grid(row=1, column=3, padx=(10, 10), pady=(0, 5), sticky="ew")

        magmo3makan.destroy()
        magmo3makan = ttk.Label(makanframe, text=0, style="BorderedLabel.TLabel")
        magmo3makan.grid(row=3, column=1, columnspan=2, padx=10, pady=(0, 5), sticky="ew")

        tasfeyakabllabel = ttk.Label(tasfeyakablframe, text=tasfeyaQdm, style="BorderedLabel.TLabel", width=20)
        tasfeyakabllabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        tasfeyakabllabel.configure(style='Colored.TLabel')

        maksablabel = ttk.Label(maksabframe, text=rebh, style="BorderedLabel.TLabel", width=20)
        maksablabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        maksablabel.configure(style='Colored.TLabel')

        tasfeyabaadlabel = ttk.Label(tasfeyabaadframe, text=mlkFtrd, style="BorderedLabel.TLabel", width=20)
        tasfeyabaadlabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        tasfeyabaadlabel.configure(style='Colored.TLabel')

        tasfeyahaqiqilabel = ttk.Label(tasfeyahaqiqiframe, text=mlkHqiq, style="BorderedLabel.TLabel", width=20)
        tasfeyahaqiqilabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        tasfeyahaqiqilabel.configure(style='Colored.TLabel')

        agzlabel = ttk.Label(agzframe, text=zyada, style="BorderedLabel.TLabel", width=20)
        agzlabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        if zyada < -100 or zyada > 100:
            agzlabel.configure(style='ColoredR.TLabel')
        else:
            agzlabel.configure(style='Colored.TLabel')

        agztrakomilabel = ttk.Label(agztrakomiframe, text=zyadatrakom, style="BorderedLabel.TLabel", width=20)
        agztrakomilabel.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        agztrakomilabel.configure(style='Colored.TLabel')

        global inputtable, mabiattable, outputtable
        vodtablefill()
        moamlattahdith(inputtable, "sgldahel")
        moamlattahdith(outputtable, "sglhareg")
        moamlattahdith(mabiattable, "sglbedaa")
    return

#----------------------------------------------------------------------------------------------------دوال سجل فودافون كاش

def sglVcashW():
    newWindowww = tk.Toplevel(base)
    newWindowww.title("سجل فودافون كاش")

    global tarihframe, tarihframe2
    tarihframe = tk.LabelFrame(newWindowww, text="تاريخ العملاء", labelanchor="ne")
    tarihframe.grid(row=1, column=1, sticky="ew")
    cal1 = DateEntry(tarihframe, date_pattern="dd/MM/yyyy")
    cal1.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    zorar1 = tk.Button(tarihframe, text="إتمام", command=lambda: sglVcashtahdith(omalatablee, "omala", windowdate(cal1)))
    zorar1.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    tahdisomalarkam(frame="omala")

    tarihframe2 = tk.LabelFrame(newWindowww, text="تاريخ الأرقام", labelanchor="ne")
    tarihframe2.grid(row=1, column=2, sticky="ew")
    cal2 = DateEntry(tarihframe2, date_pattern="dd/MM/yyyy")
    cal2.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    zorar2 = tk.Button(tarihframe2, text="إتمام", command=lambda: sglVcashtahdith(arkamtablee, "arkam", windowdate(cal2)))
    zorar2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    tahdisomalarkam(frame="arkam")

    omalaframe = tk.LabelFrame(newWindowww, text="جدول سجل تصفية العملاء", labelanchor="ne")
    omalaframe.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

    arkamframe = tk.LabelFrame(newWindowww, text="جدول سجل تصفية الأرقام", labelanchor="ne")
    arkamframe.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

    omalaorder = ["hour", "date", "value", "name", "id"]
    arkamorder = ["hour", "date", "value", "num", "id"]

    omalainfo = {"الساعة": 100, "التاريخ": 100, "القيمة": 100, "الاسم": 100, "#": 40}
    arkaminfo = {"الساعة": 100, "التاريخ": 100, "القيمة": 100, "الرقم": 100, "#": 40}

    omalatablee = createtable(omalaframe, omalaorder, omalainfo, "left", "e")
    arkamtablee = createtable(arkamframe, arkamorder, arkaminfo, "left", "e")
    createscroll(omalatablee, omalaframe, 0, 5, 5, 5, "right")
    createscroll(arkamtablee, arkamframe, 0, 5, 5, 5, "right")

    sglVcashtahdith(omalatablee, "omala")
    sglVcashtahdith(arkamtablee, "arkam")

    gridfillrow(tarihframe, 1)
    gridfillrow(tarihframe2, 1)
    return

def sglVcashtahdith(gdwl, key, date=None):
    global amilmokhtar, rkammokhtar
    amil = amilmokhtar.get()
    rakam = rkammokhtar.get()
    if key == "omala":
        if date is None:
            info = istehrag("SELECT hour, date, qima, amil, id FROM sglomalacash")
        elif date == f"{nowtime('date')}":
            if amil == "":
                info = istehrag(f"SELECT hour, date, qima, amil, id FROM sglomalacash WHERE date='{date}'")
            else:
                if amil[0] == '{':
                    amill = amil[1:-1]
                info = istehrag(f"SELECT hour, date, qima, amil, id FROM sglomalacash WHERE amil='{amill}'")
        else:
            if amil == "":
                info = istehrag(f"SELECT hour, date, qima, amil, id FROM sglomalacash WHERE date='{date}'")
            else:
                if amil[0] == '{':
                    amill = amil[1:-1]
                info = istehrag(f"SELECT hour, date, qima, amil, id FROM sglomalacash WHERE date='{date}' AND amil='{amill}'")
    elif key == "arkam":
        if date is None:
            if rakam == "":
                info = istehrag("SELECT hour, date, qima, elrakam, id FROM sglarkamcash")
            else:
                info = istehrag(f"SELECT hour, date, qima, elrakam, id FROM sglarkamcash WHERE elrakam='{rakam}'")
        else:
            if rakam == "":
                info = istehrag(f"SELECT hour, date, qima, elrakam, id FROM sglarkamcash WHERE date='{date}'")
            else:
                info = istehrag(f"SELECT hour, date, qima, elrakam, id FROM sglarkamcash WHERE date='{date}' AND elrakam='{rakam}'")
    tableupdate(gdwl, info)
    return

#----------------------------------------------------------------------------------------------------دوال السجلات

def segelltahdith(esmgadwl, tablename, datee=None, special=None):
    key = None
    if special == "الدرج":
        if datee is None:
            info = istehrag(f"SELECT date, hour, dorg, id FROM {esmgadwl}")
        else:
            info = istehrag(f"SELECT date, hour, dorg, id FROM {esmgadwl} WHERE date='{datee}'")
    elif special == "المكن":
        if datee is None:
            info = istehrag(f"SELECT date, hour, rasidmkn, id FROM {esmgadwl}")
        else:
            info = istehrag(f"SELECT date, hour, rasidmkn, id FROM {esmgadwl} WHERE date='{datee}'")
    elif esmgadwl == "sabet":
        info = istehrag(f"SELECT date, hour, qima, name, id FROM {esmgadwl} ORDER BY shaghal='a' ASC")
        key = "sabet"
    elif esmgadwl == "sglsabet":
        if datee is None:
            info = istehrag(f"SELECT hour, date, farq, no3, qima, sabetid, esmamil, id FROM {esmgadwl}")
        else:
            info = istehrag(f"SELECT hour, date, farq, no3, qima, sabetid, esmamil, id FROM {esmgadwl} WHERE date='{datee}'")
    elif esmgadwl == "sglkest":
        if datee is None:
            info = istehrag(f"SELECT hour, date, qima, kestid, esmamil, id FROM {esmgadwl}")
        else:
            info = istehrag(f"SELECT hour, date, qima, kestid, esmamil, id FROM {esmgadwl} WHERE date='{datee}'")
    elif esmgadwl == "sglgameya":
        if datee is None:
            info = istehrag(f"SELECT hour, date, qima, gameyaid, esmamil, id FROM {esmgadwl}")
        else:
            info = istehrag(f"SELECT hour, date, qima, gameyaid, esmamil, id FROM {esmgadwl} WHERE date='{datee}'")
    elif esmgadwl == "sgltasfeya":
        if datee is None:
            info = istehrag(f"SELECT zyada, tasfHqiq, tasfFtrd, rebh, omala, vodnum, magkest, kestid, sabet, hour, date, id FROM {esmgadwl}")
        else:
            info = istehrag(f"SELECT zyada, tasfHqiq, tasfFtrd, rebh, omala, vodnum, magkest, kestid, sabet, hour, date, id FROM {esmgadwl} WHERE date<='{datee}'")
            klamm = istehrag(f"SELECT molahzat FROM {esmgadwl} WHERE date <= '{datee}'")
            klam = ''
            for klma in klamm:
                if klma[0] == None:
                    continue
                else:
                    klam = klam + klma[0]

            global textx
            textx.configure(state="normal")
            textx.delete("1.0", tk.END)
            textx.insert(tk.END, klam)
            textx.configure(state="disabled")
    else:
        if datee is not None:
            info = istehrag(f"SELECT date, hour, qima, name, id FROM {esmgadwl} WHERE date='{datee}'")
        else:
            info = istehrag(f"SELECT date, hour, qima, name, id FROM {esmgadwl}")

    tableupdate(tablename, info, key)
    return

def shashetgadwal(table):
    newWindow = tk.Toplevel(base)
    newWindow.minsize(width=610, height=450)
    s = 0
    tableframe = tk.Frame(newWindow)
    tableframe.pack(side="bottom", fill="both", padx=5, pady=5, anchor="e", expand=True)

    global nameframe2
    nameframe2 = tk.Frame(newWindow)
    if table == "sgldahel":
        segel = "سجل الداخل"
        columnsorder = ["date", "hour", "value", "name", "id"]
        columnsinfo = {"التاريخ": 150, "الساعة": 150, "القيمة": 150, "الاسم": 150, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename)
    elif table == "sglhareg":
        segel = "سجل الخارج"
        columnsorder = ["date", "hour", "value", "name", "id"]
        columnsinfo = {"التاريخ": 150, "الساعة": 150, "القيمة": 150, "الاسم": 150, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename)
    elif table == "sglbedaa":
        segel = "سجل المبيعات"
        columnsorder = ["date", "hour", "value", "name", "id"]
        columnsinfo = {"التاريخ": 150, "الساعة": 150, "القيمة": 150, "الاسم": 150, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename)
    elif table == "sgldyon":
        segel = "سجل المديونية"
        columnsorder = ["date", "hour", "value", "name", "id"]
        columnsinfo = {"التاريخ": 150, "الساعة": 150, "القيمة": 150, "الاسم": 150, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename)
    elif table == "dorg":
        segel = "سجل الدرج"
        table = "sgltasfeya"
        columnsorder = ["date", "hour", "value", "id"]
        columnsinfo = {"التاريخ": 150, "الساعة": 150, "القيمة": 150, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename, special="الدرج")
    elif table == "makan":
        segel = "سجل المكن"
        table = "sgltasfeya"
        columnsorder = ["date", "hour", "value", "id"]
        columnsinfo = {"التاريخ": 150, "الساعة": 150, "القيمة": 150, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename, special="المكن")
    elif table == "sabet":
        segel = "قائمة الثوابت"
        columnsorder = ["date", "hour", "value", "name", "id"]
        columnsinfo = {"التاريخ": 150, "الساعة": 150, "القيمة": 150, "الاسم": 150, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename, special="thwabt")
        s = 1
        mofrdat = [{"nass": "زيادة القيمة", "dalla": zyadetsabet}, {"nass": "إنقاص القيمة", "dalla": inqassabet}, {"nass": "إزالة الثابت", "dalla": izaletsabet}]
        kaymaD8taYmin(tableframe, tablename, mofrdat)
    elif table == "sglsabet":
        segel = "سجل الثوابت"
        columnsorder = ["hour", "date", "farq", "no3", "qima", "sabetid", "esmamil", "id"]
        columnsinfo = {"الساعة": 80, "التاريخ": 80, "قيمة المعاملة": 80, "نوع المعاملة": 80, "المتاح": 80, "رقم الثابت": 50, "اسم العميل": 100, "#": 30}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename, special="sglsabet")
    elif table == "sglkest":
        segel = "سجل الأقساط"
        columnsorder = ["hour", "date", "qima", "kestrkm", "esmamil", "id"]
        columnsinfo = {"الساعة": 120, "التاريخ": 120, "القيمة": 120, "رقم القسط": 120, "الاسم": 120, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename, special="kest")
    elif table == "sglgameya":
        segel = "سجل الجمعيات"
        columnsorder = ["hour", "date", "qima", "kestrkm", "esmamil", "id"]
        columnsinfo = {"الساعة": 120, "التاريخ": 120, "القيمة": 120, "رقم القسط": 120, "الاسم": 120, "#": 40}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")
        segelltahdith(table, tablename, special="gameya")
    elif table == "sgltasfeya":
        segel = "سجل التصفيات"
        newWindow.minsize(width=1000, height=600)

        columnsorder = ["zyada", "tasfhqiq", "tafFtrd", "rebh", "omala", "vodnum", "magkest", "kestid", "sabet", "hour", "date", "id"]
        columnsinfo = {"الزيادة": 80, "تصف حقيقية": 80, "تصف افتراضية": 80, "الربح": 80, "مج عملاء المحافظ": 100, "مج المحافظ": 100, "الأقساط": 80, "آخر قسط": 80, "الثابت": 80, "الساعة": 80, "التاريخ": 80, "#": 30}
        tablename = createtable(tableframe, columnsorder, columnsinfo, "left", "e")

        itartext = tk.LabelFrame(nameframe2, text="الملاحظات", labelanchor="ne")
        itartext.grid(row=2, column=1, columnspan=2, sticky="nsew")

        nameframe2.pack(side="right", padx=5, pady=5, anchor="n")
        tableframe.pack(side="left", fill="both", padx=5, pady=5, anchor="e", expand=True)

        global textx
        textx = tk.Text(itartext, wrap="word", padx=5, pady=5, width=23, height=35)
        textx.grid(sticky="nsew")

        segelltahdith(table, tablename)

    newWindow.title(f"{segel}")

    createscroll(tablename, tableframe, 0, 5, 5, 5, "right")
    if s == 0:
        nameframe2.pack(side="top", padx=5, pady=5, anchor="e")

        cal = DateEntry(nameframe2, date_pattern="dd/MM/yyyy")
        cal.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        zorar = tk.Button(nameframe2, text="إتمام", command=lambda: segelltahdith(table, tablename, windowdate(cal)))
        zorar.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    return

#----------------------------------------------------------------------------------------------------دوال المجاميع

def izhar(button, qima1, qima2=None, qima3=None, qima4=None):
    global Alam
    qima = qima1.get()
    if button == "makan":
           fawry2 = qima2.get()
           opay = qima3.get()
           momken = qima4.get()

           try:
               int(qima)
               int(fawry2)
               int(opay)
               int(momken)
           except ValueError:
               messagebox.showerror("خطأ", "لقد أدخلت حروفا في خانة القيمة")
               return

           if qima != '' and fawry2 != '' and opay != '' and momken != '':
                global makansum
                makansum = int(qima) + int(fawry2) + int(opay) + int(momken)
                global magmo3makan
                magmo3makan.destroy()
                magmo3makan = ttk.Label(makanframe, text=makansum, style="BorderedLabel.TLabel")
                magmo3makan.grid(row=3, column=1, columnspan=2, padx=10, pady=(0, 5), sticky="ew")
                magmo3makan.configure(style='Colored.TLabel')
                Alam[5] = 1
                qima1.delete('0', 'end')
                qima2.delete('0', 'end')
                qima3.delete('0', 'end')
                qima4.delete('0', 'end')
           else:
               messagebox.showerror("خطأ", "هناك خانة أو أكثر غير مملوئة!")
    elif button == "dorg":
        try:
            int(qima)
        except ValueError:
            messagebox.showerror("خطأ", "لقد أدخلت قيما غير رقمية في الخانة.")
        else:
            if qima == '':
                messagebox.showerror("خطأ", "الخانة غير مملوئة!")
            else:
                global dorgmag
                dorgmag = int(qima)
                global magmo3dorg
                magmo3dorg.destroy()
                magmo3dorg = ttk.Label(dorgframe, text=dorgmag, style="BorderedLabel.TLabel", width=20)
                magmo3dorg.grid(row=1, column=3, padx=(10, 10), pady=(0, 5), sticky="ew")
                magmo3dorg.configure(style='Colored.TLabel')
                Alam[6] = 1
                qima1.delete('0', 'end')
    return

def sqlsum(type, itar, gadwalsql):
    global Alam
    magmo3 = istehrag(f"SELECT SUM(qima) FROM {gadwalsql} WHERE shaghal = 'a'")
    if magmo3[0][0] is None:
        magmo3 = [(0,)]
    if type == "da5el":
        global da5elsum
        da5elsum = magmo3
        global magmo3da5el
        magmo3da5el.destroy()
        magmo3da5el = ttk.Label(itar, text=da5elsum, style="BorderedLabel.TLabel", width=20)
        magmo3da5el.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")
        magmo3da5el.configure(style='Colored.TLabel')
        Alam[0] = 1
    elif type == "hareg":
        global haregsum
        haregsum = magmo3
        global magmo35areg
        magmo35areg.destroy()
        magmo35areg = ttk.Label(itar, text=haregsum, style="BorderedLabel.TLabel", width=20)
        magmo35areg.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")
        magmo35areg.configure(style='Colored.TLabel')
        Alam[1] = 1
    elif type == "dyon":
        global dyonsum
        global magmo3dyon
        dyonsum = magmo3
        magmo3dyon.destroy()
        magmo3dyon = ttk.Label(itar, text=dyonsum, style="BorderedLabel.TLabel", width=20)
        magmo3dyon.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")
        magmo3dyon.configure(style='Colored.TLabel')
        Alam[2] = 1
    elif type == "thwabt":
        global thwabtsum
        global magmo3thwabt
        thwabtsum = magmo3
        magmo3thwabt.destroy()
        magmo3thwabt = ttk.Label(itar, text=thwabtsum, style="BorderedLabel.TLabel", width=20)
        magmo3thwabt.grid(row=1, column=4, padx=10, pady=(0, 5), sticky="ew")
        magmo3thwabt.configure(style='Colored.TLabel')
        Alam[3] = 1
    elif type == "mabiat":
        global mabiatsum
        global magmo3mabiat
        mabiatsum = magmo3
        magmo3mabiat.destroy()
        magmo3mabiat = ttk.Label(itar, text=mabiatsum, style="BorderedLabel.TLabel", width=20)
        magmo3mabiat.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")
        magmo3mabiat.configure(style='Colored.TLabel')
        Alam[4] = 1
    return

def sqlsumvodcash(vodtable, omalatable, itar):
    global omalamagmo3, rakammagmo3, Alam
    omalamagmo3 = istehrag(f"SELECT SUM(aleh) FROM {omalatable}")[0][0]
    rakammagmo3 = istehrag(f"SELECT SUM(aleh) FROM {vodtable}")[0][0]
    if omalamagmo3 is None:
        omalamagmo3 = 0
    if rakammagmo3 is None:
        rakammagmo3 = 0
    check = istehrag(f"SELECT SUM(lih) FROM {omalatable}")
    if check[0][0] is not None:
        if check[0][0] > 0:
            messagebox.showerror("خطأ", "!هناك أموال لعميل(عملاء) في جدول فودافون كاش لم تلغى بعد\n !'أزلها ثم دونها في جدول 'الديون اليومية")
            return
    global omalamag
    omalamag.destroy()
    omalamag = ttk.Label(itar, text=omalamagmo3, style="BorderedLabel.TLabel", width=20)
    omalamag.grid(row=1, column=3, padx=10, pady=(0, 5), sticky="ew")
    omalamag.configure(style='Colored.TLabel')

    global rakammag
    rakammag.destroy()
    rakammag = ttk.Label(itar, text=rakammagmo3, style="BorderedLabel.TLabel", width=20)
    rakammag.grid(row=2, column=3, padx=10, pady=(0, 5), sticky="ew")
    rakammag.configure(style='Colored.TLabel')
    Alam[7] = 1
    return

#----------------------------------------------------------------------------------------------------دوال الثوابت

def zyadetsabet(gdwl, itar, key=None):
    mo5tar = gdwl.selection()
    qimamo5tar = gdwl.item(mo5tar)

    id = qimamo5tar['values'][4]
    esmamil = qimamo5tar['values'][3]
    shashettaadil = tk.Toplevel(itar)
    taadilLsq = tk.Label(shashettaadil, text="")
    taadild5l = tk.Entry(shashettaadil)
    taadilzr = tk.Button(shashettaadil, text="إتمام", command=lambda: tahdithsabet(taadild5l.get(), id, shashettaadil, itar, gdwl, key, esmamil))

    taadilLsq.grid(row=1, column=2, padx=10, pady=5)
    taadild5l.grid(row=1, column=1, padx=10, pady=5)
    taadilzr.grid(row=2, column=1, columnspan=2, pady=5)
    return

def inqassabet(gdwl, itar):
    zyadetsabet(gdwl, itar, "naqs")

def tahdithsabet(qimaa, id, window, itar, gdwl, key, esmamil):
    try:
        qima = int(qimaa)
    except ValueError:
        messagebox.showerror("خطأ", "القيمة المدخلة ليست رقما أو فارغة", parent=itar)
        if window:
            window.destroy()
    else:
        qima = int(qimaa)
        wsl = sqlite3.connect("tasfeya.db")
        tasfeyadb = wsl.cursor()
        if key == "naqs":
            qimaAd = istehrag(f"SELECT qima FROM sabet WHERE id={id}")
            qimaGd = qimaAd[0][0] - qima
            if qimaGd <= 0:
                if window:
                    window.destroy()
                tasfeyadb.close()
                izaletsabet(gdwl, itar, esmamil, id)
                return
            else:
                tasfeyadb.execute(f"UPDATE sabet SET qima={qimaGd} WHERE id={id}")
                tasfeyadb.execute(f"INSERT INTO sglsabet (esmamil, date, hour, sabetid, qima, farq, no3) VALUES ('{esmamil}', '{nowtime('date')}', '{nowtime('hour')}', {id}, {qimaGd}, {qima}, 'سحب')")
        else:
            qimaAd = istehrag(f"SELECT qima FROM sabet WHERE id={id}")
            qimaGd = qimaAd[0][0] + qima
            tasfeyadb.execute(f"UPDATE sabet SET qima={qimaGd} WHERE id={id}")
            tasfeyadb.execute(f"INSERT INTO sglsabet (esmamil, date, hour, sabetid, qima, farq, no3) VALUES ('{esmamil}', '{nowtime('date')}', '{nowtime('hour')}', {id}, {qimaGd}, {qima}, 'إضافة')")
        messagebox.showinfo("تم", "تم التعديل بنجاح", parent=itar)
        wsl.commit()
        if window:
            itar.focus_force()
            window.destroy()
        segelltahdith("sabet", gdwl, None, "thwabt")
        tasfeyadb.close()
    return

def izaletsabet(gdwl, itar, esmamil=None, id=None):
    egaba = messagebox.askyesnocancel("تأكد", "أمتأكد أنك تريد إزالة هذا الثابت؟", parent=itar)
    if egaba == True:
        wsl = sqlite3.connect("tasfeya.db")
        tasfeyadb = wsl.cursor()
        if id is None:
            mo5tar = gdwl.selection()
            qimamo5tar = gdwl.item(mo5tar)
            id = qimamo5tar['values'][4]
            esmamil = qimamo5tar['values'][3]
        qimaAd = istehrag(f"SELECT qima FROM sabet WHERE id={id}")
        tasfeyadb.execute(f"INSERT INTO sglsabet (esmamil, date, hour, sabetid, qima, farq, no3) VALUES ('{esmamil}', '{nowtime('date')}', '{nowtime('hour')}', {id}, 0, {qimaAd[0][0]}, 'إزالة')")
        tasfeyadb.execute(f"UPDATE sabet SET shaghal='Nh', qima=0 WHERE id={id}")
        wsl.commit()
        segelltahdith("sabet", gdwl, None, "thwabt")
        messagebox.showinfo("تم", "تمت الإزالة بنجاح", parent=itar)
        tasfeyadb.close()
    return

def windowsabet():
    sabetwindow = tk.Toplevel(base)
    esmamil = tk.Entry(sabetwindow)
    qima = tk.Entry(sabetwindow)
    esmamilL = tk.Label(sabetwindow, text="اسم العميل")
    qimaL = tk.Label(sabetwindow, text="المبلغ")
    zrIdafa = tk.Button(sabetwindow, text="إتمام", command=lambda: idafetsabet(esmamil.get(), qima.get(), sabetwindow))

    esmamil.grid(row=1, column=1, padx=10, pady=5)
    qima.grid(row=2, column=1, padx=10, pady=5)
    esmamilL.grid(row=1, column=2, padx=10, pady=5)
    qimaL.grid(row=2, column=2, padx=10, pady=5)
    zrIdafa.grid(row=3, column=1, columnspan=2)
    return

def idafetsabet(amil, qimaa, window):
    try:
        int(qimaa)
    except ValueError:
        messagebox.showerror("خطأ", "القيمة المدخلة ليست رقما أو فارغة", parent=window)
    else:
        if amil == '':
            messagebox.showerror("خطأ", "يجب إدخال اسم للعميل", parent=window)
        else:
            qima = int(qimaa)
            wsl = sqlite3.connect("tasfeya.db")
            tasfeyadb = wsl.cursor()

            tasfeyadb.execute(f"INSERT INTO sabet (name, qima, hour, date) VALUES ('{amil}', {qima}, '{nowtime('hour')}', '{nowtime('date')}')")
            wsl.commit()
            messagebox.showinfo("تم", "تمت إضافة الثابت بنجاح", parent=window)
            if window:
                window.destroy()
            tasfeyadb.close()
    return

#----------------------------------------------------------------------------------------------------دوال الأقساط والجمعيات

def dafa3shahr(gdwl, itar):
    mo5tar = gdwl.selection()
    qimamo5tar = gdwl.item(mo5tar)

    tarih = nowtime("date")
    sa3aa = nowtime("hour")
    sa3a = str(sa3aa)

    try:
        id = qimamo5tar['values'][7]
    except IndexError:
        id = qimamo5tar['values'][6]
        esmamil = qimamo5tar['values'][5]
        qima = qimamo5tar['values'][0]

        wsl = sqlite3.connect("tasfeya.db")
        tasfeyadb = wsl.cursor()
        tasfeyadb.execute(f"UPDATE gameya SET kamshahrE = kamshahrE + 1 WHERE id={id}")
        tasfeyadb.execute(f"INSERT INTO sglgameya (esmamil, qima, date, hour, gameyaid) VALUES ('{esmamil}', {qima}, '{tarih}', '{sa3a}', {id})")
        messagebox.showinfo("تم", "تمت إضافة الشهر بنجاح")
        wsl.commit()

        gameyashahrE = istehrag(f"SELECT kamshahrE, kamshahr FROM gameya WHERE id={id}")
        if gameyashahrE[0][0] == gameyashahrE[0][1]:
            messagebox.showinfo("تم", "تم الانتهاء من هذه الجمعية")
            tasfeyadb.execute(f"UPDATE gameya SET shaghal='Nh' WHERE id={id}")
            wsl.commit()

        kestgameya(gdwl, "gameya")
    else:
        id = qimamo5tar['values'][7]
        esmamil = qimamo5tar['values'][6]
        qima = qimamo5tar['values'][0]

        wsl = sqlite3.connect("tasfeya.db")
        tasfeyadb = wsl.cursor()
        tasfeyadb.execute(f"UPDATE kest SET kamshahrE = kamshahrE + 1 WHERE id={id}")
        tasfeyadb.execute(f"INSERT INTO sglkest (esmamil, qima, date, hour, kestid) VALUES ('{esmamil}', {qima}, '{tarih}', '{sa3a}', {id})")
        messagebox.showinfo("تم", "تمت إضافة الشهر بنجاح")
        wsl.commit()

        kestshahrE = istehrag(f"SELECT kamshahrE, kamshahr FROM kest WHERE id={id}")
        if kestshahrE[0][0] == kestshahrE[0][1]:
            messagebox.showinfo("تم", "تم الانتهاء من هذا القسط")
            tasfeyadb.execute(f"UPDATE kest SET shaghal='Nh' WHERE id={id}")
            wsl.commit()
        kestgameya(gdwl, "kest")

    tasfeyadb.close()
    return

def kestgameya(gdwl, key):
    if key == "kest":
        info = istehrag("SELECT qimashahr, kamshahrE, kamshahr, qima, bedaya, esmelmobile, esmamil, id FROM kest ORDER BY shaghal='a' ASC")
    elif key == "gameya":
        info = istehrag("SELECT qimashahr, kamshahrE, kamshahr, qima, bedaya, esmamil, id FROM gameya ORDER BY shaghal='a' ASC")
    tableupdate(gdwl, info, key)
    return

def kestgameyaidafa(table, key=None):
    kestgameyawindow = tk.Toplevel(base)
    esmamil = tk.Entry(kestgameyawindow)
    shohor = tk.Entry(kestgameyawindow)
    gnehfelshahr = tk.Entry(kestgameyawindow)
    text3 = "عدد الشهور"
    text4 = "جنيه/الشهر"
    text1= "العميل"

    if key == "kest":
        enwan = "سجل الأقساط"
        text2 = "السلعة"
        selaa = tk.Entry(kestgameyawindow)
        label2 = tk.Label(kestgameyawindow, text=text2)
        zrr = tk.Button(kestgameyawindow, text="إتمام", command=lambda: idragkestgam(key, esmamil.get(), shohor.get(), gnehfelshahr.get(), table, kestgameyawindow, selaa.get()))
        selaa.grid(row=2, column=1)
        label2.grid(row=2, column=2)
    elif key == "gameya":
        enwan = "سجل الجمعيات"
        zrr = tk.Button(kestgameyawindow, text="إتمام", command=lambda: idragkestgam(key, esmamil.get(), shohor.get(), gnehfelshahr.get(), table, kestgameyawindow))

    kestgameyawindow.title(f"{enwan}")

    label1 = tk.Label(kestgameyawindow, text=text1)
    label3 = tk.Label(kestgameyawindow, text=text3)
    label4 = tk.Label(kestgameyawindow, text=text4)

    esmamil.grid(row=1, column=1, padx=10, pady=5)
    shohor.grid(row=3, column=1, padx=10, pady=5)
    gnehfelshahr.grid(row=4, column=1, padx=10, pady=5)
    label1.grid(row=1, column=2, padx=10, pady=5)
    label3.grid(row=3, column=2, padx=10, pady=5)
    label4.grid(row=4, column=2, padx=10, pady=5)
    zrr.grid(row=5, column=1, columnspan=2, padx=10, pady=5)
    return

def idragkestgam(key, esmamil, shohor, gnehfelshahr, table, window, selaa=None):
    try:
        int(shohor)
    except ValueError:
        messagebox.showerror("خطأ", "المدخل فارغ أو فيه رموز غير رقمية", parent=window)
        if window:
            window.destroy()
        return
    else:
        shohorr = int(shohor)

    try:
        int(gnehfelshahr)
    except ValueError:
        messagebox.showerror("خطأ", "المدخل فارغ أو فيه رموز غير رقمية", parent=window)
        if window:
            window.destroy()
        return
    else:
        gnehfelshahrr = int(gnehfelshahr)

    if gnehfelshahr == '' or shohorr == '' or esmamil == '':
        messagebox.showerror("خطأ", "حقل مدخل أو أكثر فارغ")
        if window:
            window.destroy()
            return

        if key == "kest" and selaa == '':
            messagebox.showerror("خطأ", "حقل مدخل أو أكثر فارغ")
            if window:
                window.destroy()
                return


    qima = gnehfelshahrr * shohorr

    conn = sqlite3.connect("tasfeya.db")
    tasfeyadb = conn.cursor()
    if key == "kest":
        tasfeyadb.execute(f"INSERT INTO kest (qima, kamshahr, qimashahr, esmelmobile, esmamil, bedaya) VALUES ({qima}, {shohorr}, {gnehfelshahrr}, '{selaa}', '{esmamil}', '{nowtime('date')}')")
        conn.commit()
        tasfeyadb.close()
        kestgameya(table, "kest")
    elif key == "gameya":
        tasfeyadb.execute(f"INSERT INTO gameya (qima, kamshahr, qimashahr, esmamil, bedaya) VALUES ({qima}, {shohorr}, {gnehfelshahrr}, '{esmamil}', '{nowtime('date')}')")
        conn.commit()
        tasfeyadb.close()
        kestgameya(table, "gameya")

    conn.commit()
    tasfeyadb.close()
    messagebox.showinfo("تم", "تمت العملية بنجاح", parent=window)
    if window is not None:
        window.destroy()
    return

#----------------------------------------------------------------------------------------------------دوال عامة للتيكنتر

def halEsmMwgood(tasfeyadb, name, your_table, input):
    tasfeyadb.execute(f"SELECT COUNT(*) FROM {your_table} WHERE {input} = ?", name)
    count = tasfeyadb.fetchone()[0]
    return count > 0

def istehrag(sqlcommand, qima=None):
    conn = sqlite3.connect("tasfeya.db")
    tasfeyadb = conn.cursor()
    if qima is None:
        qeyam = tasfeyadb.execute(sqlcommand)
    else:
        qeyam = tasfeyadb.execute(sqlcommand, qima)

    qeyam = qeyam.fetchall()
    tasfeyadb.close()
    return qeyam

def tableupdate(table, info, shart=None):
    table.tag_configure('highlightG', background='grey')
    table.tag_configure('highlightR', background='#FF0000')

    for item in table.get_children():
        table.delete(item)

    for item in info:
        if shart == "kest" or shart == "gameya":
            if item[1] == item[2]:
                table.insert('', '0', values=item, tags='highlightG')
                continue
        if shart == "sabet":
            if item[2] == 0:
                table.insert('', '0', values=item, tags='highlightG')
                continue
        if shart == "vodomala":
            if item[1] == 0:
                table.insert('', '0', values=item, tags='highlightG')
                continue
        if shart == "vodnum":
            if item[0] == 0:
                table.insert('', '0', values=item, tags='highlightG')
                continue
        table.insert('', '0', values=item)

    for col in table['columns']:
        table.column(col, anchor='e')

    return

def windowdate(cal):
    cal.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    dateraw = cal.get_date()
    date = dateraw.strftime("%d/%m/%Y")
    return str(date)

def da8taYmin(hadath, kayma, gdwl):
    mofrada = gdwl.identify_row(hadath.y)
    tags = gdwl.item(mofrada, 'tags')
    if mofrada and ('highlightG' not in tags) and ('highlightR' not in tags):
        gdwl.selection_set(mofrada)
        kayma.post(hadath.x_root, hadath.y_root)

def kaymaD8taYmin(itar, gdwl, mofrdat):
    kayma = tk.Menu(itar, tearoff=0)
    for mofrada in mofrdat:
        kayma.add_command(label=mofrada["nass"], command=lambda m=mofrada: m["dalla"](gdwl, itar))
    gdwl.bind("<Button-3>", lambda hadath: da8taYmin(hadath, kayma, gdwl))

    return

def gridfillrow(framename, rownum):
    for i in range(rownum):
        framename.rowconfigure(i, weight=1)

def gridfillcolumn(framename, columnnum):
    for i in range(columnnum):
        framename.columnconfigure(i, weight=1)

#values: قيم القائمة
#defaultchoice: الاختيار الافتراضي
def createcombobox(framename, defaultchoice, values):
    selection = tk.StringVar(framename)
    selection.set(defaultchoice)
    menu = ttk.Combobox(framename, textvariable=selection, values=values, state="readonly")

    return menu, selection

#columnsorder: كود عناوين الحقول وتعبر عن الترتيب
#columnsinfo: قاموس فيه المفتاح عنوان الحقل، والقيمة هي عرض الحقل
#columnanchor: مكان عنوان الحقل في خانته
def createtable(tableframe, columnsorder, columnsinfo, side, columnanchor, height=None):
    tablename = ttk.Treeview(tableframe, columns=columnsorder, show="headings", height=height)
    tablename.pack(side=side, anchor="center", fill="both", expand=True)
    columnsnames = list(columnsinfo.keys())
    columnswidths = list(columnsinfo.values())

    for i in range(len(columnsorder)):
        tablename.heading(columnsorder[i], text=columnsnames[i], anchor=columnanchor)
        tablename.column(columnsorder[i], width=columnswidths[i], stretch="YES")

    return tablename

#side: يعبر عن ناحية البكرة يمين أم يسار
def createscroll(tablename, tableframe, padxl, padxr, padyl, padyr, side):
    scroll = ttk.Scrollbar(tableframe, orient="vertical", command=tablename.yview)
    tablename.configure(yscrollcommand=scroll.set)
    scroll.pack(padx=(padxl, padxr), pady=(padyl, padyr), side=side, fill="y")

#ادخل فيها
#date أو hour أو datehour
# على حسب أتريد التاريخ أم الساعة أم كليهما
def nowtime(datehour):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    hour = now.strftime("%H:%M:%S")
    datehourr = now.strftime("%d/%m/%Y || %H:%M:%S")
    formattime = {"hour": hour, "date": date, "datehour": datehourr}
    return formattime[datehour]

#----------------------------------------------------------------------------------------------------البرنامج

def createtab(tabname):
    global frame
    frame = ttk.Frame(notebook)
    frame.pack(fill="both", expand=True)
    notebook.add(frame, text=tabname)

    if tabname == moamlatstr:
        moamlat()
    elif tabname == vodcashname:
        vodcash()
    elif tabname == tasfeyastr:
        tasfeya()

base = tk.Tk()
base.title(" محل الباشمهندس ")
base.minsize(width=1000, height=600)

Alam = [0] * 8
style = ttk.Style()
style.configure("BorderedLabel.TLabel", borderwidth=1, relief="solid")
style.configure('Colored.TLabel', background='lightgreen')
style.configure('ColoredR.TLabel', background='#FF0000')
style.configure("Treeview.Heading", anchor="e")
style.configure("Treeview", anchor="e")

notebook = ttk.Notebook(base)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

vodcashname = "                                                        فودافون كاش                                                        "
tasfeyastr = "                                                        تصفية                                                        "
moamlatstr = "                                                        معاملات                                                        "

createtab(tasfeyastr)
createtab(moamlatstr)
createtab(vodcashname)

notebook.select(2)

base.mainloop()
