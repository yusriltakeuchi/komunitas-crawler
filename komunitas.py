from bs4 import BeautifulSoup
import requests
import requests_cache
import time
import json
import sys
import subprocess as proses
import platform
from json2mysql import Json2Mysql

#-------------------------------------------
# KOMUNITAS CRAWLER
# CREATED BY YUSRIL RAPSANJANI
# SCRIPT VERSION V1.0
# facebook: www.facebook.com/yuranitakeuchi
#-------------------------------------------

class Komunitas():
    url = "https://komunita.id"
    komunitas_data = []
    komunitas_gained = 0

    #Color script
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    GREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'

    def clearScreen(self):
        system_os = platform.system()
        if 'Linux' in system_os:
            proses.call('clear', shell=True)
        elif "Windows" in system_os:
            proses.call('cls', shell=True)

    def headers(self):
        self.clearScreen()
        print("              {}╭╮╭━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮".format(self.WARNING))
        print("              ┃┃┃╭╯╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮")
        print("              ┃╰╯╯╭━━┳╮╭┳╮╭┳━╮┣╮╭╋━━┳━━╮")
        print("              ┃╭╮┃┃╭╮┃╰╯┃┃┃┃╭╮╋┫┃┃╭╮┃━━┫")
        print("              ┃┃┃╰┫╰╯┃┃┃┃╰╯┃┃┃┃┃╰┫╭╮┣━━┃")
        print("              ╰╯╰━┻━━┻┻┻┻━━┻╯╰┻┻━┻╯╰┻━━╯")

        print("")
        print("         {}[{}━{}]    {}Crawling Data Komunitas  {}[{}━{}]".format(self.WARNING, self.OKBLUE, self.WARNING, self.OKBLUE, self.WARNING, self.OKBLUE, self.WARNING))
        print("         {}[{}━{}]  {}made by: {}Yusril Rapsanjani {}[{}━{}]".format(self.WARNING, self.OKBLUE, self.WARNING, self.OKBLUE, self.HEADER, self.WARNING, self.OKBLUE, self.WARNING))
        print("         {}[{}━{}]         {}Version: {}1.0        {}[{}━{}]".format(self.WARNING, self.OKBLUE, self.WARNING, self.OKBLUE, self.HEADER, self.WARNING, self.OKBLUE, self.WARNING))
        print("         {}[{}━{}]       {}Codename: {}yurani      {}[{}━{}]".format(self.WARNING, self.OKBLUE, self.WARNING, self.OKBLUE, self.HEADER, self.WARNING, self.OKBLUE, self.WARNING))
        print("         {}[{}━{}]     {}Sites: {}www.yurani.me    {}[{}━{}]".format(self.WARNING, self.OKBLUE, self.WARNING, self.OKBLUE, self.HEADER, self.WARNING, self.OKBLUE, self.WARNING))
        print("         {}[{}━{}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[{}━{}]".format(self.WARNING, self.OKBLUE, self.WARNING, self.OKBLUE, self.WARNING))
        print("")

    def __init__(self):
        category_list = self.getCategoryList()
        category_list.append("exit")
        self.komunitas_gained = 0
        self.komunitas_data.clear()

        self.headers()
        #Showing category
        print("        {}===---------- KATEGORI ----------===".format(self.WARNING))

        #Looping category
        for x in range(0, len(category_list)):
            print("        {}{}.){} {}".format(self.OKBLUE, str(x+1), self.WARNING,category_list[x]))
        
        print("        {}------------------------------------".format(self.WARNING))
        select = input("        [?] Kategori mana yang ingin kamu crawling? [1-{}]: ".format(str(len(category_list))))

        if int(select) <= len(category_list)-1 and int(select) > 0:
            #Start crawling
            print("        [INFO] Mempersiapkan Yurani Spider untuk menjelajah...")
            time.sleep(1)
            print("        [INFO] Yurani Spider mulai menjelajah kategori...")
            time.sleep(1)

            selectedCategory = category_list[int(select)-1]
            self.startCrawling(selectedCategory)
        else:
            sys.exit()

    def getCategoryList(self):
        requests_cache.install_cache("komunitas")
        r = requests.get(self.url)

        #Create a scraping object
        soup = BeautifulSoup(r.content, 'html.parser')
        #Parsing by element
        category_element = soup.findAll("span", class_="link_text")
        
        #Looping element and store to list
        category_list = []
        for x in range(3, len(category_element)-10):
            category_list.append(category_element[x].get_text().replace("\n", "").replace("\t", ""))

        return category_list

    def ParsingLink(self, category):
        return self.url + "/listing-category/" + category.lower().replace("&", "").replace("  ", "-").replace(" ", "-")


    def convertToJson(self, data, name):
        interval = 0
        print("\n        [INFO] Berhasil mendapatkan {} data komunitas".format(str(self.komunitas_gained)))
        answer = input("        [?] Anda yakin ingin mengeluarkan output sebagai json file?[] [y/n]: ")
        if answer.lower() == "y":
            with open('{}.json'.format(name), "w") as outfile:
                json.dump(data, outfile)
                print("        [*] Create file {}.json successfully".format(name))

        if self.komunitas_gained < 100:
            interval = 2
        elif self.komunitas_gained > 100 and self.komunitas_gained < 500:
            interval = 5
        elif self.komunitas_gained > 500:
            interval = 7

        time.sleep(interval)
        print("        [*] Proses crawling sukses.")
        answer = input("        [?] Anda yakin ingin untuk sync ke database? [y/n]: ")

        if answer.lower() == "y":
            #komunitas = Komunitas()
            json2mysql = Json2Mysql('{}.json'.format(name))
            data = json2mysql.readData()

            for dat in data['komunitas']:
                try:
                    #Insert category
                    #print(dat['category'])
                    json2mysql.insertChildField('category', 'name', dat['category'])

                    #Insert social media
                    json2mysql.insertChildField('social_media', 'url', dat['social_media'])
                    
                    #Insert tag
                    json2mysql.insertChildField('tag', 'name', dat['tag'])

                    #Insert details
                    json2mysql.insertDetails(dat)

                    #Get table category id
                    category_id = json2mysql.getDataDB("id", "category", "name", dat['category'])

                    #Get table social media id
                    id_social = json2mysql.getDataDB("id", "social_media", "url", dat['social_media'])

                    #Get table tag id
                    id_tag = json2mysql.getDataDB("id", "tag", "name", dat['tag'])

                    #Get table details
                    id_details = json2mysql.getDetailID(dat['title'])

                    dict_details = {}
                    dict_details['category_id'] = category_id
                    dict_details['social_id'] = id_social
                    dict_details['tag_id'] = id_tag
                    dict_details['details_id'] = id_details

                    if dict_details['details_id'] != None:
                        json2mysql.inserts(dict_details)
                except:
                    continue

        answer = input("        [?] Anda yakin ingin kembali ke menu utama? [y/n]: ")

        if answer.lower() == "y": 
            komunitas = Komunitas()
        else:
            sys.exit()

    def decryptEmail(self, code):
        split = code.split("#")
        encoded_bytes = bytes.fromhex(split[1])
        encoded = bytes(byte ^ encoded_bytes[0] for byte in encoded_bytes[1:])
        return encoded.decode('utf-8')

    def travelData(self, url):
        #Get Web Element
        requests_cache.install_cache("komunitas")
        r = requests.get(url)

        #Creating a scraping object
        soup = BeautifulSoup(r.content, 'html.parser')

        #Installing attributes
        title = soup.find("span", class_="single-listing-title").get_text()
        print("        [*] Mendapatkan data komunitas {}{}{}".format(self.OKBLUE, title, self.WARNING))

        #Get Category list
        main_div = soup.find("div", class_="listing-content col-md-8")
        cat_list = []
        #Parsing div and div
        div = main_div.findAll("div")

        try:
            cat_a = div[1].findAll("a", href=True)
            for a in cat_a:
                if a.text != "":
                    cat_list.append(a.text.strip().replace("\r\n", "").strip())
                else:
                    break
        except:
            cat_list.append("")

        #Get Address komunitas
        try:
            address = soup.find("span", itemprop="streetAddress").get_text().strip()
        except:
            address = ""

        #Get City komunitas
        try:
            city = soup.find("span", itemprop="addressLocality").get_text().strip()
        except:
            city = ""

        #Get Region komunitas
        try:
            region = soup.find("span", itemprop="addressRegion").get_text().strip()
        except:
            region = ""

        #Get Postal Code
        try:
            postal_code = soup.find("span", itemprop="postalCode").get_text().strip()
        except:
            postal_code = ""

        #Get Phone number
        try:
            phone = ""
            div_listing = soup.find("div", class_="listing-content col-md-8")
            for div in div_listing.findAll("a", class_="single-listing-meta"):
                result_div = div.get_text().strip()
                if result_div != "Website":
                    phone = result_div
        except:
            phone = ""

        #Get social media
        social_media = []
        try:
            div_social = soup.find("div", class_="listing-content col-md-8")
            #Parse any link on div social
            link_social = div_social.findAll("a", href=True)
            for link in link_social:
                if 'facebook.com' in link['href'] or 'twitter.com' in link['href'] or 'instagram.com' in link['href']:
                    social_media.append(link['href'])
        except:
            social_media.append("")

        #Get Description komunitas
        try:
            description = soup.find("span", itemprop="description").get_text().strip()
        except:
            description = ""

        #Get Tag
        div_tag = soup.find("div", class_="single-text")
        tag_list = []
        try:
            #Parse any link on div tag
            link_tag = div_tag.findAll("a", href=True)
            for link in link_tag:
                tag_list.append(link.text.strip())
        except:
            tag_list.append("")

        #Get Website
        try:
            web = ""
            div_listing = soup.find("div", class_="listing-content col-md-8")
            for div in div_listing.findAll("a", class_="single-listing-meta"):
                result_div = div.get_text().strip()
                if result_div == "Website":
                    web = div['href']
        except:
            web = ""

        #Get Email
        try:
            email = ""
            div_listing = soup.find("div", class_="listing-content col-md-8")
            mail_link = div_listing.findAll("a", href=True)
            for mail in mail_link:
                if 'email-protection' in mail['href']:
                    email = self.decryptEmail(mail['href'])
        except:
            email = ""

        #Set data to dictionary
        data = {}
        data['title'] = title
        data['category'] = cat_list
        data['address'] = address
        data['city'] = city
        data['region'] = region
        data['postal_code'] = postal_code
        data['phone'] = phone
        data['social_media'] = social_media
        data['description'] = description
        data['website'] = web
        data['email'] = email
        data['tag'] = tag_list

        self.komunitas_gained += 1
        self.komunitas_data.append(dict(data))


    def startCrawling(self, category):
        content_link = self.ParsingLink(category)

        #Get Maximum Page
        requests_cache.install_cache("komunitas")
        r = requests.get(content_link)
        soup = BeautifulSoup(r.content, 'html.parser')

        page_list = soup.findAll("a", class_="page-numbers")
        split = page_list[1]['href'].split("/")

        max_page = split[len(split)-1]
        
        for x in range(1, int(max_page)+1):
            try:
                #Get Web Element
                requests_cache.install_cache("komunitas")
                r = requests.get("{}/page/{}/".format(content_link, x))

                #Create a scraping object
                soup = BeautifulSoup(r.content, 'html.parser')
                raw_link = soup.findAll("h4", class_="entry-title")

                #Traveling to komunitas data
                print("\n        [*] Mendapat {}{}{} komunitas dalam page {}{}/{}{}...".format(self.OKBLUE, str(len(raw_link)), self.WARNING, self.OKBLUE, str(x), str(max_page), self.WARNING))
                
                print("        [*] Memulai penjelajahan data komunitas...")
                
                #Looping raw link
                for raw in raw_link:
                    link = raw.findAll("a", href=True)

                    for res_link in link:
                        self.travelData(res_link['href'])
            except:
                continue

        #Convert to json
        big_data = {}
        big_data['komunitas'] = self.komunitas_data
        self.convertToJson(big_data, category)

def main():
    komunitas = Komunitas()


if __name__ == '__main__':
    main()