Web Scraping(Text)
1. Introduction:
Web scraping is a technique using which the webpages from the internet are fetched and parsed to understand and extract specific information similar to a human being. Web scrapping
  consists of two parts:
• Web Crawling→ Accessing the webpages over the internet and pulling data from
  them.
• HTML Parsing→ Parsing the HTML content of the webpages obtained through webcrawling and then extracting specific information from it.
   Hence, web scrappers are applications/bots, which automatically send requests to websites andthen extract the desired information from the website output.
 Let’s take an example:
how do we buy a phone online?
1. We first look for a phone with good reviews
2. We see on which website it’s available at the lowest price
3. We check whether it’s delivered in our area or not
4. If everything looks good, then we buy the phone.
What if there is a computer program that can do all of these for us? That’s what web scrappers
necessarily do. They try to understand the webpage content as a human would do.
Other examples of the applications of web scrapping are:
• Competitive pricing.
• Manufacturers monitor the market, whether the retailer is maintaining a minimum price
or not.
• Sentiment analysis of the consumers, whether they are happy with the services and
products or not.
• To aggregate news articles.
• To aggregate Marketing data.
• To gain financial insights from the market.
• To gather data for research.
• To generate marketing leads.
4 | P a g e
• To collect trending topics by media houses.
And, the list goes on.
In this document, we’ll take the example of buying a phone online further and try to scrap the
reviews from the website about the phone that we are planning to buy.
For example, if we open filpkart.com and search for ‘iPhone’, the search result will be as
follows:
Then if we click on a product link, it will take us to to the following page:
  If we scroll down on this page, we’ll get to see the comments posted by the customers:
  Our end goal is to build a web scraper that collects the reviews of a product from the internet.
2. Prerequisites:
The things needed before we start building a python based web scraper are:
• Python installed.
• A Python IDE (Integrated Development Environment): like PyCharm, Spyder, or any
other IDE of choice (Explained Later)
• Flask Installed. (A simple command: pip install flask)
• MongoDB installed .
• Basic understanding of Python and HTML.
• Basic understanding of Git (download Git CLI from https://gitforwindows.org/ )
