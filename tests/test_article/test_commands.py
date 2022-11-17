from email.mime import audio
from multiprocessing import AuthenticationError
from turtle import title
import pytest

from blog.models import Article
from blog.commands import CreateArticleCommand, AlreadyExists


def test_create_article():
   """
   GIVEN CreateArticleCommand with a valid author, title, and conetn properties
   WHEN the execute method is called
   THEN a new Article must exist in the database with the same attributes
   """
   cmd = CreateArticleCommand(
      author="john@doe.com",
      title="New Article",
      content="Super Awesome Article"
   )

   article = cmd.execute()

   db_article = Article.get_by_id(article.id)

   assert db_article.id == article.id
   assert db_article.author == article.author
   assert db_article.title == article.title
   assert db_article.content == article.content


def test_create_article_already_exists():
   """
   GIVEN CreateArticleCommand with a title of some article in database
   WHEN the execute method is called
   THEN the AlreadyExists exception must be raised
   """

   Article(
      author="jon@doe.com",
      title="New Article",
      content="Super extra Awesome content"
   ).save()

   cmd = CreateArticleCommand(
      author="jon@doe.com",
      title="New Article",
      content="Super awesome Article"
   )

   with pytest.raises(AlreadyExists):
      cmd.execute()