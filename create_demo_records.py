#!/usr/bin/env python

'''
create some records for demo database
'''

from minicms.wsgi import *
from news.models import Column, Article

def main():
    column_urls = [
        ("How about anvil today", "anvil"),
        ("How about today's review build", "build"),
        ("Remote build Status", "remote"),
    ]

    for column_name, url in column_urls:
        c = Column.objects.get_or_create(name=column_name, slug=url)[0]

        for i in range(1, 11):
            article = Article.objects.get_or_create(
                title = '{}_{}'.format(column_name, i),
                slug = 'article_{}'.format(i),
                content = 'Detail: {} {}'.format(column_name, i)
            )[0]

            article.column.add(c)

if __name__ == '__main__':
    main()
    print("Done!")