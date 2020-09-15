from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pymongo

App = Flask(__name__) ## initializing the Flask app

@App.route('/',methods=['POST','GET'])

def func():
    if request.method == 'POST' : ## request-> When someone is trying to hit the data
        search_string=request.form['content'].replace("","")
        try:
            DB=pymongo.MongoClient("mongodb://localhost:27017/") ## connecting to the mongo db server
            db=DB['ReviewsData'] ## creating a new Database or using existing one
            reviews=db[search_string].find({})  ## Searching for thr review in the database
            if reviews.count>0:     ## if review is present in the database
                return render_template('results.html',reviews=reviews)
            else:
                flipkart_url = "https://www.flipkart.com/search?q=" + search_string  # preparing the URL to search the product on flipkart
                uClient = uReq(flipkart_url)  # requesting the webpage from the internet
                flipkartPage = uClient.read()  # reading the webpage
                uClient.close()  # closing the connection to the web server
                flipkart_html = bs(flipkartPage, "html.parser")  # parsing the webpage as HTML
                bigboxes = flipkart_html.findAll("div", {"class": "bhgxx2 col-12-12"})  # seacrhing for appropriate tag to redirect to the product link
                del bigboxes[0:3]  # the first 3 members of the list do not contain relevant information, hence deleting them.
                box = bigboxes[0]  # taking the first iteration (for demo)
                productLink = "https://www.flipkart.com" + box.div.div.div.a['href']  # extracting the actual product link
                prodRes = requests.get(productLink)  # getting the product page from server
                prod_html = bs(prodRes.text, "html.parser")  # parsing the product page as HTML
                commentboxes = prod_html.find_all('div', {'class': "_3nrCtb"})  # finding the HTML section containing the customer comments

                table = db[search_string]
                reviews = []  # initializing an empty list for reviews
                #  iterating over the comment section to get the details of customer and their comments
                for commentbox in commentboxes:
                    try:
                        name = commentbox.div.div.find_all('p', {'class': '_3LYOAd _3sxSiS'})[0].text

                    except:
                        name = 'No Name'

                    try:
                        rating = commentbox.div.div.div.div.text

                    except:
                        rating = 'No Rating'

                    try:
                        commentHead = commentbox.div.div.div.p.text
                    except:
                        commentHead = 'No Comment Heading'
                    try:
                        comtag = commentbox.div.div.find_all('div', {'class': ''})
                        custComment = comtag[0].div.text
                    except:
                        custComment = 'No Customer Comment'
                    # fw.write(searchString+","+name.replace(",", ":")+","+rating + "," + commentHead.replace(",", ":") + "," + custComment.replace(",", ":") + "\n")
                    mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                              "Comment": custComment}  # saving that detail to a dictionary
                    x = table.insert_one(
                        mydict)  # insertig the dictionary containing the rview comments to the collection
                    reviews.append(mydict)  # appending the comments to the review list
                return render_template('results.html', reviews=reviews)  # showing the review to the user
        except:
            return 'something is wrong'
            # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    App.run(port=8000, debug=True)  # running the app on the local machine on port 8000








