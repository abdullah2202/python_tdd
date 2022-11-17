from ast import List
from blog.models import Article
from blog.queries import ListArticlesQuery, GetArticleByIDQuery

def test_list_articles():
   """
   GIVEN 
   WHEN 
   THEN 
   """

   Article(
      author="jon@doe.com",
      title="New Article",
      content="Super new awesome content"
   ).save()
   Article(
      author="jon@doe.com",
      title="Another Article",
      content="More Super new awesome content"
   ).save()

   query = ListArticlesQuery()

   assert len(query.execute()) == 2

def test_get_article_by_id():
   article = Article(
      author="jane@doe.com",
      title="New Article",
      content="Super extra awesome article"
   ).save()

   query = GetArticleByIDQuery(
      id = article.id
   )

   assert query.execute().id == article.id
