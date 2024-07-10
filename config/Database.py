from pymongo import MongoClient
from datetime import datetime
from pygooglenews import GoogleNews
from newspaper import Article

def get_text(generator):
    article = Article(generator['link'])
    article.download()
    article.html
    article.parse()
    return article.text


gn = GoogleNews(lang = 'en', country = 'IN')
s = gn.search('NEET',helper = True)
#
#
# # DB_PASSWORD = dotenv_values(".env").get("DB_PASSWORD")
#
client = MongoClient(f"mongodb://localhost:27017")
db=client["News_DB"]
collection=db["Tecnology"]
for i in range(5):
    insert_these={
        "_id":i,
        "Title":s['entries'][i]['title'],
        "link":s['entries'][i]['link'],
        "published":datetime.strptime(s['entries'][i]['published'], '%a, %d %b %Y %H:%M:%S %Z'),
        "source":s['entries'][i]['source']

     }
    collection.insert_one(insert_these)
    p=collection.find({"_id":i})
    k=next(p)

    collection.update_one(
       {"_id":i},
       { '$set': { "text":get_text(k)} }
    )


