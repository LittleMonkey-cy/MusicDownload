import requests
from bs4 import BeautifulSoup
import threading,time,os,json
#创建界面
from tkinter import*
<<<<<<< HEAD

from tkinter.filedialog import askdirectory#打开文件夹
=======
<<<<<<< HEAD

from tkinter.filedialog import askdirectory#打开文件夹
=======
#打开文件夹
from tkinter.filedialog import askdirectory
>>>>>>> 7a7b224 (new commit)
>>>>>>> 9a8bf82 (kugou music download)

headers = {"user-agent":
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11"
}
#存储歌曲信息
data = []
def getHtml(url,headers = headers):
    try:
<<<<<<< HEAD
        response =  requests.get(url,headers=headers,timeout=30)
=======
<<<<<<< HEAD
        response =  requests.get(url,headers=headers,timeout=30)
=======
        response = requests.get(url,headers=headers,timeout=30)
>>>>>>> 7a7b224 (new commit)
>>>>>>> 9a8bf82 (kugou music download)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return ""
#在新线程中获取TOP500歌曲列表
def downloadSongInToop500():
#删除原列表和存储数据中的内容
    listbox.delete(0,listbox.size())
    data.clear()
#生成Toop500首歌曲的url地址
    urls = ["https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(i) for i in range(1, 24)]
    #遍历toop500的url
    i = 1
    for url in urls:
        content = getHtml(url)
        time.sleep(3)
        #对页面进行解析找到所有歌名
        soup = BeautifulSoup(content,"html.parser")
        if soup == None:
            v1.set('下载失败')
        titles = soup.select("div.pc_temp_songlist > ul > li >a")
#遍历歌名获取TOOP500的每个歌名及歌曲的信息
        for title in titles:
            singer=""
            name = title.get_text()#得到歌名的信息
            url = title.get("href")#得到歌曲播放地址信息
            listbox.insert(END,name)#将歌曲名字插入到歌曲列表显示区当中
            data.append({"name":name,"singer":singer,"hash":"no","url":url})#先将这些数据存储到数据列表中
#当歌曲正在获取时提示
        v1.set("正在获取第{}页的歌曲".format(i))
#当歌曲列表全部获取成功后提示
        i+=1
    v1.set("歌曲列表获取完成！")
def downloadSongInDJ():
    # 删除原列表和存储数据中的内容
    listbox.delete(0, listbox.size())
    data.clear()
    # 生成DJ的url地址
    url1 = ['https://www.kugou.com/yy/rank/home/{}-24971.html?from=rank'.format(i) for i in range(1, 6)]
    # 遍历DJ的url
    i = 1
    for url in url1:
        content = getHtml(url)
        time.sleep(3)
        # 对页面进行解析找到所有歌名
        soup = BeautifulSoup(content, "html.parser")
        if soup == None:
            v1.set('下载失败')
        titles1 = soup.select("div.pc_temp_songlist > ul > li >a")
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
        # print(titles1)
>>>>>>> 7a7b224 (new commit)
>>>>>>> 9a8bf82 (kugou music download)
        # 遍历歌名获取DJ的每个歌名及歌曲的信息
        for title in titles1:
            singer = ""
            name = title.get_text()  # 得到歌名的信息
            url = title.get("href")  # 得到歌曲播放地址信息
            listbox.insert(END, name)  # 将歌曲名字插入到歌曲列表显示区当中
            data.append({"name": name, "singer": singer, "hash": "no", "url": url})  # 先将这些数据存储到数据列表中
        # 当歌曲正在获取时提示
        v1.set("正在获取第{}页的歌曲".format(i))
        # 当歌曲列表全部获取成功后提示
        i += 1
<<<<<<< HEAD
        v1.set("歌曲列表获取完成！")
=======
<<<<<<< HEAD
        v1.set("歌曲列表获取完成！")
=======
    v1.set("歌曲列表获取完成！")
>>>>>>> 7a7b224 (new commit)
>>>>>>> 9a8bf82 (kugou music download)
def downloadSongInUp():
#删除原列表和存储数据中的内容
    listbox.delete(0,listbox.size())
    data.clear()
#生成飙升榜歌曲的url地址
    url2 = ['https://www.kugou.com/yy/rank/home/{}-6666.html?from=rank'.format(i) for i in range(1, 11)]
    #遍历飙升榜的url
    i = 1
    for url in url2:
        content = getHtml(url)
        time.sleep(3)
        #对页面进行解析找到所有歌名
        soup = BeautifulSoup(content,"html.parser")
        if soup == None:
            v1.set('下载失败')
        titles = soup.select("div.pc_temp_songlist > ul > li >a")
#遍历歌名获取TOOP500的每个歌名及歌曲的信息
        for title in titles:
            singer=""
            name = title.get_text()#得到歌名的信息
            url = title.get("href")#得到歌曲播放地址信息
            listbox.insert(END,name)#将歌曲名字插入到歌曲列表显示区当中
            data.append({"name":name,"singer":singer,"hash":"no","url":url})#先将这些数据存储到数据列表中
#当歌曲正在获取时提示
        v1.set("正在获取第{}页的歌曲".format(i))
#当歌曲列表全部获取成功后提示
        i+=1
    v1.set("歌曲列表获取完成！")
def downloadSongInHot():
#删除原列表和存储数据中的内容
    listbox.delete(0,listbox.size())
    data.clear()
#生成红歌榜歌曲的url地址
    url2 = ['https://www.kugou.com/yy/rank/home/{}-23784.html?from=rank'.format(i) for i in range(1, 6)]
    #遍历飙升榜的url
    i = 1
    for url in url2:
        content = getHtml(url)
        time.sleep(3)
        #对页面进行解析找到所有歌名
        soup = BeautifulSoup(content,"html.parser")
        if soup == None:
            v1.set('下载失败')
        titles = soup.select("div.pc_temp_songlist > ul > li >a")
#遍历歌名获取红歌榜的每个歌名及歌曲的信息
        for title in titles:
            singer=""
            name = title.get_text()#得到歌名的信息
            url = title.get("href")#得到歌曲播放地址信息
            listbox.insert(END,name)#将歌曲名字插入到歌曲列表显示区当中
            data.append({"name":name,"singer":singer,"hash":"no","url":url})#先将这些数据存储到数据列表中
#当歌曲正在获取时提示
        v1.set("正在获取第{}页的歌曲".format(i))
#当歌曲列表全部获取成功后提示
        i+=1
    v1.set("歌曲列表获取完成！")
#多线程获取Top500歌曲列表
def getTop500List(event):
    #创建新线程并启动
    t = threading.Thread(target=downloadSongInToop500)
    t.setDaemon(True)
    t.start()
#多线程获取DJ歌曲列表
def getDJList(event):
    #创建新线程并启动
    t1 = threading.Thread(target=downloadSongInDJ)
    t1.setDaemon(True)
    t1.start()
#多线程获取飙升榜歌曲列表
def getUpList(event):
    #创建新线程并启动
    t1 = threading.Thread(target=downloadSongInUp)
    t1.setDaemon(True)
    t1.start()
def getHotList(event):
    #创建新线程并启动
    t1 = threading.Thread(target=downloadSongInHot)
    t1.setDaemon(True)
    t1.start()
#搜索歌曲
def searchSong(event):
    v1.set("正在搜索歌曲列表")#提示
    #清除掉原有列表和数据中的信息
    listbox.delete(0,listbox.size())
    data.clear()
    #歌曲搜索链接地址
    url = "http://songsearch.kugou.com/song_search_v2?callback=jQuery191034642999175022426_1489023388639&keyword={}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641"
    content = getHtml(url.format(inp.get()))#将获得的数据进行格式化输出
    jsonText = content.replace("jQuery191034642999175022426_1489023388639(","").replace(")","")#去除搜索后显示的源代码中不需要的数据，只是获取到json中的需要的信息。
    views = json.loads(jsonText)#将json字符串转换为字典格式
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9a8bf82 (kugou music download)
    #循环遍历提取信息
    for view in views["data"]["lists"]:
        song_name = view["SongName"].replace("<em>","").replace("</em>","")#获取到歌曲名称。（去除无用的<em>加粗信息,即将其替换为空字符串）
        singer_name = view["SingerName"].replace("<em>","").replace("</em>","")#获取到歌手名称。（去除无用的<em>加粗信息,即将其替换为空字符串）
#获取歌曲的hash值
        file_hash = view["FileHash"]
        #将获取到的三个信息存储到搜索列表中。
        listbox.insert(END,song_name+"---"+singer_name)
        #将数据保存到data中
        data.append({"name":song_name,"singer":singer_name,"hash":file_hash,"url":"no"})
<<<<<<< HEAD
=======
=======
    # print(views)
    #循环遍历提取信息
    for view in views["data"]["lists"]:
        song_name = view["SongName"].replace("<em>","").replace("</em>","")#获取到歌曲名称。（去除无用的<em>加粗信息,即将其替换为空字符串）
        # print(song_name)
        singer_name = view["SingerName"].replace("<em>","").replace("</em>","")#获取到歌手名称。（去除无用的<em>加粗信息,即将其替换为空字符串）
        # print(singer_name)
#获取搜索歌曲的hash值
        file_hash = view["FileHash"]
        # print(file_hash)
        # 获取单个歌曲的AlbumID值
        file_AlbumID = view["AlbumID"]
        # print(file_AlbumID)
        #将获取到的三个信息存储到搜索列表中。
        listbox.insert(END,song_name+"---"+singer_name)
        #将数据保存到data中
        data.append({"name":song_name,"singer":singer_name,"hash":file_hash,"album_id":file_AlbumID,"url":"no"})
>>>>>>> 7a7b224 (new commit)
>>>>>>> 9a8bf82 (kugou music download)
        v1.set("获取列表完成！")
#获取歌曲的hash码
def getHash(url):
    html = getHtml(url)
    reg = '"hash":"(\w+)",'
    music_hash = re.search(reg,html)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9a8bf82 (kugou music download)
    return music_hash.group(1)
def getSongJson(hash):
#获取url时url的地址随时会发生改变,(Network>index>Headers>url),每次都需重新获取。获取时将url中的hash=的值换为hash='+hash+’；&album_id= 的值 换为&album_id=0
    url = r'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19106837612618244941_1597910870830&hash='+hash+'&album_id=0&dfid=3dlJiw3FpIBD0z7kn73HCx8T&mid=85800640056c217ee916fa13020833a2&platid=4&_=1597910870831'
<<<<<<< HEAD
=======
=======
    # print("music_hash="+str(music_hash))
    return music_hash.group(1)
# 获取歌曲的真实id值
def getalbum(url):
    html = getHtml(url)
    # print(html)
    reg = '"album_id":(.*?)}'
    album_id = re.search(reg,html)
    # print("album_id="+str(album_id))
    return album_id.group(1)
def getSongJson(hash,album_id):
#获取url时url的地址随时会发生改变,(Network>index>Headers>url),每次都需重新获取。获取时将url中的hash=的值换为hash='+hash+’；&album_id= 的值可以动态获取
    url = r'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery191006233373959735955_1609918117953&hash='+hash+'&dfid=4E5xfm0IbDqJ139Umr2XQ8Yu&mid=716b73d92ea48953a062f3847a161802&platid=4&album_id='+album_id+'&_=1609918117955'
>>>>>>> 7a7b224 (new commit)
>>>>>>> 9a8bf82 (kugou music download)
    mp3_file = getHtml(url,headers=headers)
    return mp3_file
#下载歌曲
#在新线程中下载歌曲
def download_song():

    print(listbox.curselection())
    for i in listbox.curselection():
        if data[i]["hash"] == "no":
            data[i]["hash"] = getHash(data[i]["url"])
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9a8bf82 (kugou music download)
            name1 = data[i]["name"] + " - " + data[i]["singer"]
        else:
            name1 = data[i]["name"] + " - " + data[i]["singer"]
        mp3_json = getSongJson(data[i]["hash"])
        reg = '"play_backup_url":"(.*?.mp3)"'
        rezult = re.search(reg, mp3_json)
        url2 = rezult.group(1).replace("\\", "")
        v1.set("正在下载{}".format(name1))
        print(url2)
<<<<<<< HEAD
=======
=======
            # 循环遍历找到每个歌曲的唯一id值
            data[i]["album_id"] = getalbum(data[i]["url"])
            name1 = data[i]["name"] + " - " + data[i]["singer"]
        else:
            name1 = data[i]["name"] + " - " + data[i]["singer"]
        mp3_json = getSongJson(data[i]["hash"],data[i]["album_id"])
        # print("mp3-json="+mp3_json)
        reg = '"play_backup_url":"(.*?)"'
        result = re.search(reg, mp3_json)
        url2 = result.group(1).replace("\\", "")
        print(url2)
        v1.set("正在下载{}".format(name1))
>>>>>>> 7a7b224 (new commit)
>>>>>>> 9a8bf82 (kugou music download)
        path = pathInp.get()
        if not os.path.exists(path):
            os.makedirs(path)
        response1 = requests.get(url2, headers=headers,timeout=30)
        with open(path + "\\" + name1 + "--" + ".mp3", "wb") as  f:
            f.write(response1.content)
            time.sleep(3)
        v1.set("{}下载完成".format(name1))
def download_song1():
    #创建一个新的下载线程并启动
    t1 = threading.Thread(target=download_song)
    t1.setDaemon(True)
    t1.start()
#全选事件
def changeAll():
    if allV.get()==0:
        listbox.select_clear(0,listbox.size())
    else:
        listbox.select_set(0,listbox.size())
#反选事件
def fanchangeAll():
    for i in range(0,listbox.size()): #将listbox中所有歌曲遍历给i
        if i in listbox.curselection(): #如果i这首歌被选中的了
            listbox.select_clear(i) #清除选中这首歌
        else:
            listbox.select_set(i) #如果没被选中，选中这首歌
def dzz():
    path_=askdirectory()
    pathInp.delete(0,END)
    pathInp.insert(END,path_)
# 创建界面
root = Tk()
#窗口标题
root.title("酷狗音乐下载器----陈钰")
#窗口界面大小
root.geometry("1000x700")
root.resizable(0,0) #防止用户调整尺寸
# 添加背景图片
im = PhotoImage(file="bg.png")
bj = Label(root, image=im)
bj.pack()
#创建界面上的控件
lb1 = Label(root,text = '酷狗音乐',fg = "red",bg = "black",font = ("楷体",30))
lb1.place(x=340,y=35,width=200,height=45)
lb2 = Label(root,text = "请输入需要下载的歌曲或歌手")
lb2.place(x=400,y=80,width=250,height=25)
#创建搜索框
inp = Entry(root)
inp.place(x=680,y=80,width=200,height=25)
#搜索按钮
btn = Button(root,text='搜索')
btn.place(x=900,y=80,width=100,height=25)
# toop500按钮
btn1 = Button(root,text='toop500',bg="red")
btn1.place(x=580,y=400,width=100,height=25)
# 飙升榜
btn2 = Button(root,text='DJ热歌榜',bg="red")
btn2.place(x=580,y=450,width=100,height=25)
# DJ热歌榜
btn3 = Button(root,text='飙升榜',bg="red")
btn3.place(x=580,y=500,width=100,height=25)
# 红歌榜
btn4 = Button(root,text='酷狗红歌榜',bg="red")
btn4.place(x=580,y=550,width=100,height=25)
#下载按钮
btn5 = Button(root,text='开始下载',command=download_song1)
btn5.place(x=420,y=650,width=100,height=25)
# #退出按钮
# btn6 = Button(root,text='退出程序',command=quit)
# btn6.place(x=900,y=650,width=100,height=25)
#歌曲列表显示区
listbox = Listbox(root,selectmode=MULTIPLE)
listbox.place(x=20,y=125,width=500,height=500)
#添加滚动条
scroly = Scrollbar(listbox,command=listbox.yview)
scroly.pack(sid=RIGHT,fill=Y)
listbox.config(yscrollcommand=scroly.set)
# 全选框，选择全部歌曲root
allV = IntVar()
all = Checkbutton(root,text="全选",variable=allV,command=changeAll)
all.place(x=20,y=90,width=80,height=25)
#反选
allV1=IntVar()
fan=Checkbutton(text='反选',variable=allV1,command=fanchangeAll)
fan.place(x=100,y=90,width=80,height=25)
#下载框`
lb3=Label(root,text='下载地址')
lb3.place(x=25,y=650,width=70,height=25)
pathInp = Entry(root)#下载路径输入框
pathInp.place(x=100,y=650,width=210,height=25)
pathInp.insert(END,"c:\\mymp3")
#地址按钮
dz = Button(root,text="选择文件夹",command=dzz)
dz.place(x=300,y=650,width=100,height=25)
#提示文字绑定变量
v1 = StringVar()
v1.set("无下载")
ts = Label(root,textvariable=v1)
ts.place(x=540,y=650,width=450,height=25)
# 励志文字
lb4 = Label(root,text = "只要你肯努力去奋斗\r\n生活中永远充满精彩\r\n坚持到底\r\n蜗牛它照样可以攀登珠峰！",fg="red",bg="black",font=("华文行楷",20))
lb4.place(x=600,y=120)
lb5 = Label(root,text = "警告：本软件仅限个人娱乐使用，严禁用于商业用途！",fg="red",bg="black",font=("宋体",20))
lb5.place(x=0,y=0,width=1000)
lb6 = Label(root,text = "尽情享受音乐\n\t带给你的快乐吧！！！",fg="red",bg="black",font=("华文行楷",20))
lb6.place(x=700,y=420,width=280,height=70)
#绑定事件
btn.bind("<Button-1>",searchSong)#为搜索框增加事件，敲击搜索按钮时会自动进行搜索。
btn1.bind("<Button-1>",getTop500List)#为toop500按钮添加事件，当点击该按钮时会自动显示歌曲列表。
btn2.bind("<Button-1>",getDJList)#为DJ榜按钮添加事件，当点击该按钮时会自动显示歌曲列表。
btn3.bind("<Button-1>",getUpList)#为飙升榜按钮添加事件，当点击该按钮时会自动显示歌曲列表。
btn4.bind("<Button-1>",getHotList)#为红歌榜按钮添加事件，当点击该按钮时会自动显示歌曲列表。
root.mainloop()
<<<<<<< HEAD
input()
=======
<<<<<<< HEAD
input()
=======
# input()
>>>>>>> 7a7b224 (new commit)
>>>>>>> 9a8bf82 (kugou music download)
