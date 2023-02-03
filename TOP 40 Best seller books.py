from bs4 import BeautifulSoup
import requests
import time

def main():
    # Question 1
	# Load the B&N Top 100 website 
    headers = {'User-Agent':'Mozilla/5.0'}
    url= "https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8?Nrpp=40&page=1"
    page = requests.get(url, headers=headers)


    # Creating a beautifulsoup object 
    soup = BeautifulSoup(page.text, 'lxml')
	
    ## get the titles of 40 items
    title_contents = soup.select("div.product-shelf-title a")
    for title in title_contents:
        print(title.text)

    ## get the URLs of 40 items
    url_cont = soup.select("div.product-shelf-title > h3.product-info-title > a")
    for i in url_cont:
        partial_profuct = i['href']
        full_product = "https://www.barnesandnoble.com" + partial_profuct
        print(full_product)

    # 2
    #get the URLs of 40 items
    url_cont = soup.select("div.product-shelf-title > h3.product-info-title > a")
    urllist = []
    for i in url_cont:
        partial_profuct= i['href']
        full_product = "https://www.barnesandnoble.com" + partial_profuct
        urllist = urllist + [full_product]

    ## length of the list
    listlength = len(urllist)
    print(f"The length of the product page URLs is {listlength}.")

    ## the whole list of urls
    print(urllist)

    # Q 3
    for i in range(40):
        filename = f"bn_top100_{str(i+1).zfill(2)}.htm"
        headers = {'User-Agent':'Mozilla/5.0'}
        each_url = urllist[i]
        page = requests.get(each_url, headers=headers)
        with open(filename, "w") as f:
            f.write(page.text)
            print(f'Product page {i+1} is downloaded to {filename}')
            time.sleep(5)   # using sleep() to make each request followed by at least a 5 second pause



    # 4
    for i in range(40):
        filename = f"bn_top100_{str(i+1).zfill(2)}.htm"
        with open(filename, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')
            overview_section = soup.select("div.overview-cntnt")
            for j in overview_section:
                print(filename + "\n" + j.text[1:101])

if __name__ == '__main__':
	main()