articles = [
    {
        "id": 1,
        "title": "Article 1",
        "img_url": None,
        "content": "Voici  le contenu de l'article 1",
    },
    {
        "id": 2,
        "title": "Macky le ...",
        "img_url": "https://information.tv5monde.com/sites/info.tv5monde.com/files/styles/medium_article_list/public/assets/images/AP_16263541625779.jpg?itok=kGmjgtrc",
        "content": "Voici  le contenu de l'article sur Macky Sall",
    },
    {
        "id": 3,
        "title": "Article 3",
        "img_url": None,
        "content": "Voici  le contenu de l'article 3",
    },
]


def getAllArticles():
    return articles


def findArticleById(id_article):
    for a in articles:
        if a["id"] == id_article:
            return a
    return None
