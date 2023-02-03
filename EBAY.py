
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
#question 1 
def q1():
       
                  headers = {'User-Agent':'Mozilla/5.0'}

                   url= "https://www.ebay.com/sch/i.html?_from=R40&_nkw=amazon+gift+card&_sacat=0&LH_Sold=1&rt=nc"

                   page = requests.get(url, headers=headers)

                   soup = BeautifulSoup(page.text, "html.parser")

                   for i in range(10):
                            filename = f"amazon_gift_card_{str(i+1).zfill(2)}.htm"
                            headers = {'User-Agent':'Mozilla/5.0'}
                            page = requests.get(url, headers=headers)
                            with open(filename, "w") as f:
                                f.write(page.text)
                                print(f'Product page {i+1} is downloaded to {filename}')
                                time.sleep(10) # a 10 second pause
                     #downloading first 10 result pages and giving them a file name

                     face_value = []

                     for i in range(10):
                          filename = f"amazon_gift_card_{str(i+1).zfill(2)}.htm"
                          with open(filename, 'r') as file:
                              soup = BeautifulSoup(file, 'html.parser')
                              title = soup.select("div.s-item__title > span")
                              for x in range(1,len(title)):
                                  print("Title: ", title[x].text)#printing all the titles of all 10 pages
                                  face_value.append(re.findall("\$([0-9]+)", title[x].text))


                     pricevalue=[]


                     for i in range(10):
                            filename = f"amazon_gift_card_{str(i+1).zfill(2)}.htm"
                            with open(filename, 'r') as file:
                                soup = BeautifulSoup(file, 'html.parser')
                                price = soup.find_all('span', {'class': 's-item__price'})
                                for x in range(1,len(price)):
                                    print("Price: ", price[x].text) #printing all item's prices from all 10 pages
                                    pricevalue.append(re.findall("\$([0-9]+.[0-9]+)",price[x].text)




                     shippingvalue = []


                     for i in range(10):
                            filename = f"amazon_gift_card_{str(i+1).zfill(2)}.htm"
                            with open(filename, 'r') as file:
                                soup = BeautifulSoup(file, 'html.parser')
                                shipping_price = soup.find_all('span', {'class': 's-item__shipping s-item__logisticsCost'})
                                for x in range(1,len(shipping_price)):
                                    print(shipping_price[x].text)#printing shipping price of all items from all 10 pages
                                    shippingvalue.append(re.findall("\$([0-9]+.[0-9]+)",shipping_price[x].text


                     f = pd.DataFrame(
                         {'face_value': face_value,
                          'pricevalue': pricevalue,
                          'shippingvalue': shippingvalue
                         })


q1()



#question 2 



from bs4 import BeautifulSoup
import requests
import time
   
def fy():
        
        URL = "https://www.fctables.com/user/login/"
        page1 = requests.get(URL)
        doc1 = BeautifulSoup(page1.content, 'html.parser')
        
                      
        time.sleep(5) # 5s

        #An open session carries the cookies and allows you to make post requests
        session_requests = requests.session()

        res = session_requests.post(URL,  data = {'login_username': 'jorn_thebest',
                                                  'login_password': 'jornthebest',
                                                  'user_remeber': '1',
                                                  'login_action': '1'})
                               
        # This will get us the Cookies. 
        cookies = session_requests.cookies.get_dict()
        # And this is the easiest way to remain in session.

        page2 = session_requests.get('https://www.fctables.com/tipster/my_bets/',  
                                      cookies=cookies)
        
        doc2 = BeautifulSoup(page2.content, 'html.parser')
        #print(doc2) # your username here
 

        print(bool(doc2.findAll(text = "Wolfsburg 0-0 vs Bayern Munich")))


fy()






