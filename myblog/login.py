'''*********************用-户-登-录-注-册********************'''
from time import sleep
dic = {}
def Register():   #注册函数
    name = input("请输入您要注册的用户名：")
    if dic.__contains__(name):
        print("用户名已存在，请重新注册！")
        Register()
    elif len(name) < 8 or len(name)> 18:    #用户名长度检测
        print("用户名最少8位，最多18位")
        Register()
    else:
        pass1 = input("请输入密码：")
        pass2 = input("请再次确认密码：")
        if pass1 == pass2 and len(pass1) >=8 and len(pass1)<=18:
        #进行密码检测，判断2次密码是否输入一致
            print("注册成功，请登录！\n")
            o = open(r'C:\Users\xionl\Desktop\user.txt', 'a', encoding='utf-8')
            #创建一个对象o，用来打开文件
            #这里的r'C:\Users\Lenovo\Desktop\user.txt'是txt文件的的地址，可以根据自己的情况，导入文件的绝对路径就可以了，前面的r一定要加上
            o.write('\n'+name+':'+pass1)
            #写入用户名和密码    用户名和密码的存储格式是：user:password
            o.close()
            Login()               #注册完用户名后，调用登录函数
        else:
            print("两次密码输入不一致，请重新注册！\n")
            Register()            # 密码输入不一致，重新调用注册函数，进行注册

def Login():                      #登录函数
    o = open(r'C:\Users\xionl\Desktop\user.txt', 'r', encoding='utf-8')
                                  #创建一个对象o，用来打开txt文档
    all = o.read()                #创建对象all用来读取文档内容
    a = all.replace('\n',' ')     #用空格' '来替换文档中的换行符
    b = a.split(' ')              #按照空格进行切割
    user_name = input("请输入您的用户名：")
    for i in b:                   #对数据库中的用户信息进行遍历
        c = i.split(':')
        dic[c[0]] = c[1]
        if dic.__contains__(user_name):        #检查输入的用户名是否存在数据库中
            user_pass = input("请输入密码：")    #如果存在就输入对应的密码
            if user_pass == dic[user_name]:
                print("登录成功！")
                break
            else:
                print("密码错误，已退出登录！")
                break
        if b.index(i) == len(b)-1:
            #判断是否已经遍历完所有的用户信息，如果遍历完了，没有找到输入的对应用户信息，说明用户不存在
            print("您输入的用户不存在！")
            YN = input("是否需要注册用户 （如果注册请输入：1  退出输入：0）: ")
            #这里只是一个提示信息，只有在输入1时才会调用注册函数，输入其他的都会直接退出
            if YN == '1':
                Register()
            else:
                print("3s后自动退出...")
                sleep(3)
                break
                ''''''
'''主函数就一行调用登录的代码'''
Login()   #程序从这里开始运行
