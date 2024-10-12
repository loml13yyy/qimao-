import requests
from bs4 import  BeautifulSoup

def downloadPage(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    title = soup.find("h2",class_="chapter-title").get_text()
    page1 = title + '.txt'
    print(page1)
    list_conn = soup.find_all('div',class_='article')
    for e in list_conn:
        with open(page1,'w+') as f:
            print(f'【*】当前正在下载{page1}')
            f.write(str(e.text))


def startwith():
    logo = """"
░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓█▓▒░        
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 



"""
    print(logo)
    print("writen by loml13yyy".center(60,'*'))
    print("七猫小说爬虫工具")


if __name__ == '__main__':
    startwith()
page_Num = int(input('你想下载多少章小说：'))
for i in range(317270,317271+page_Num-1):
    if i == 317270:
        url = "https://www.qimao.com/shuku/149774-316193/"
        downloadPage(url)
    else:
        url = "https://www.qimao.com/shuku/149774-"+str(i)+"/"
        downloadPage(url)