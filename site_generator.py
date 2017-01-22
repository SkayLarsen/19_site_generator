import argparse
import jinja2
import json
import markdown
import os
import sys

ARTICLES_DIR = 'articles'
INDEX_TEMPLATE = 'templates/index.html'
ARTICLE_TEMPLATE = 'templates/article.html'
OUTPUT_DIR = 'static'


def load_config(path):
    if not os.path.exists(path):
        return None
    with open(path) as config_file:
        return json.load(config_file)


def load_markdown(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as md_file:
        return md_file.read()


def html_from_markdown(md_content):
    if md_content:
        return markdown.markdown(md_content, extensions=['codehilite', 'fenced_code'])


def save_page(config, path, template):
    with open(path, 'w', encoding='utf-8') as out_page:
        out_page.write(template.render(info=config))


def make_dirs():
    try:
        os.makedirs(OUTPUT_DIR)
    except OSError:
        pass
    for entry in os.scandir(ARTICLES_DIR):
        try:
            os.makedirs(os.path.join(OUTPUT_DIR, entry.name))
        except OSError:
            continue


def make_index(config):
    with open(INDEX_TEMPLATE, encoding='utf-8') as template_file:
        template = jinja2.Template(template_file.read())
        for article in config['articles']:
            article['html_source'] = os.path.join(OUTPUT_DIR, article['source']).replace('.md', '.html')
        index_path = os.path.join(OUTPUT_DIR, 'index.html')
        save_page(config, index_path, template)


def make_articles(config):
    with open(ARTICLE_TEMPLATE, encoding='utf-8') as template_file:
        template = jinja2.Template(template_file.read())
        for article in config['articles']:
            article_md_path = os.path.join(ARTICLES_DIR, article['source'])
            article['text'] = html_from_markdown(load_markdown(article_md_path))
            save_page(article, article['html_source'], template)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Создание сайта из набора статей формата markdown')
    argparser.add_argument('configpath', help='Путь к файлу конфигурации')
    args = argparser.parse_args()
    config = load_config(args.configpath)
    if not config:
        sys.exit(1)
    else:
        make_dirs()
        make_index(config)
        make_articles(config)
