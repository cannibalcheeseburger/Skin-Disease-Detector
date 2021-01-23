from bs4 import BeautifulSoup as soup
from urllib.request import Request,urlopen
import os
import wget
import sys

working_dir = os.getcwd()
os.mkdir(os.path.join(working_dir,'Dataset'))

def bar_progress(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()

url = "http://www.dermnet.com/dermatology-pictures-skin-disease-pictures/"
req = Request(url)
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
page_soup = soup(webpage,"html.parser")
table = page_soup.find_all('table')
diseases  =  list()
for i in range(1,644):
    diseases.append(table[1].find_all('a')[i].text.replace(' ','-'))

url = "http://www.dermnet.com/images/{dis}/photos/"

for disease in diseases:
    print("\n"+disease+ " downloading .....")

    os.mkdir(os.path.join(os.path.join(working_dir,'Dataset'),disease))
    for i in range(1,2): #change
        print("Page "+ str(i))
        req = Request(url.format(dis = disease)+str(i))
        web_byte = urlopen(req).read()
        webpage = web_byte.decode('utf-8')
        page_soup = soup(webpage,"html.parser")
        if str(i) != page_soup.find_all('div',class_ ="breadcrumbs")[0].text.strip()[-3:-1].strip():
            break 
        img_cont =  page_soup.find_all('div', class_="thumbnails")
        for container in img_cont:
            wget.download(container.find_all('img')[0]['src'],out='Dataset/'+disease,bar = bar_progress)