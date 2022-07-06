from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512")
movies_web_page = response.text
soup = BeautifulSoup(movies_web_page, "html.parser")
movies = soup.find_all(name="h1", class_="list-item__title")
list = [movie.getText() for movie in movies]

new_list= list[::-1]

with open("100-days-of-code/day 45/movie list.txt", mode="w") as file:
    for i in new_list:
        file.write(f"{i}\n")














# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")

# #print(soup.title)

# articles = soup.find_all(name="a", class_="storylink")
# article_texts = []
# article_links = []
# for article in articles:
#     link = article.get("href")
#     article_links.append(link)
#     text = article.getText()
#     article_texts.append(text)
# article_upvote = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

# # print(article_links)
# # print(article_texts)
# highest_upvotes = article_upvote.index(max(article_upvote))
# print(f"{article_texts[highest_upvotes]}, {article_links[highest_upvotes]}")



# # with open("100-days-of-code/day 45/website.html") as website:
# #     contents = website.read()

# # soup = BeautifulSoup(contents, 'html.parser')
# # # print(soup.title)
# # # print(soup.title.string)
# # # print(soup.prettify())

# # # all_anchor_tags = soup.find_all(name="a")
# # # for tag in all_anchor_tags:
# # #     print(tag.getText())
# # #     print(tag.get("href"))

# # heading = soup.find(name='h1', id="name")
# # print(heading)

# # section_heading = soup.find(name='h3', class_="heading")
# # print(section_heading.get("class"))
# # company_url = soup.select_one(selector="p strong")
# # print(company_url)

