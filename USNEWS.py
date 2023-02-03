from bs4 import BeautifulSoup
import requests

def main():
	
    #Loading the USNews website
    headers = {'User-Agent':'Mozilla/5.0'}
    url2= "https://www.usnews.com/"
    page2 = requests.get(url2, headers=headers)
    soup2 = BeautifulSoup(page2.text, 'lxml')
    #our goal is to get the top second story
    #all stories url and text are undeer <h3> text
    #Accessing all the <a> tags nested directly under <h3> tags
    #contains all the stories url and text
    content_usn = soup2.select("h3>a[href]")

    ### Save the url into a variable that is under the second element of the content_usn array
    url_top_story = content_usn[1]['href']
    
    ###Printing the URL
    print("URL of the second Top Story:")
    print(url_top_story)
	
    ### Load the url that we saved under a variable, that leads to the second top story
    headers = {'User-Agent':'Mozilla/5.0'}
    page3 = requests.get(url_top_story, headers=headers)
    soup3 = BeautifulSoup(page3.text, 'lxml')

    ### Access the header using necessary tags
    #accessing tag h1 class Heading-sc-1w5xk2o-0.iQhOvV for the header, there is only one header for this class
    content_usn2 = soup3.select("h1.Heading-sc-1w5xk2o-0.iQhOvV")

    ### Printing the header
    print("Header of the Second Top Story:")
    print(content_usn2[0].text)

    
    ### Access the paragraph part of the article nested under the relevant tag
    #accessing div tag class Raw-slyvem-0.bCYKCn and then all the text for that story. Contains all the sentences.
    content_usn3 = soup3.select("div.Raw-slyvem-0.bCYKCn>p")

    ### Create an empty string where we will store the whole paragraph
    p = ""
    for i in content_usn3:
        p = p + " " + str(i.text)
        
    #p will have all the paragraphs separated by space
    ### Split the string paragraph by ". " separator
    p_split = p.split(". ")
    #p_split contains sentences separately

    ### Print the first 3 sentences of the article
    for i in range(3):
        print("Sentence " + str(i+1))
        print(p_split[i])


if __name__ == '__main__':
	main()
