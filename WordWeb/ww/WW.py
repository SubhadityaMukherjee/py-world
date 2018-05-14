import re
from nltk.corpus import stopwords
import requests
from lxml import html
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import progressbar
from time import sleep


def get_words_and_clean(s):
    s = s.lower()
    s = re.sub("[^a-zA-Z]", " ", s)
    stops = set(stopwords.words("english"))
    final = ""
    for a in s.split():
        if not a in stops:
            final += str(a + " ")
    return final


def get_page(url):
    r = requests.get("https://" + url, params={
        'action': 'parse',
        'format': 'json',
    }).json()
    raw_html = r['parse']['text']['*']
    doc = html.document_fromstring(raw_html)
    first_para = doc.xpath('//p')[0]
    intro_text = first_para.text_content()
    second_para = doc.xpath('//p')[1]
    sec = second_para.text_content()
    return intro_text + sec


def collector():
    l = []
    f = open('List_Of_Names.txt', 'r', encoding="utf-8", errors='ignore').readlines()
    bar = progressbar.ProgressBar(maxval=171, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for a in range(len(f)):
        line = f[a].split()
        name = line[0] + '_' + line[1]
        try:
            p = 'en.wikipedia.org/w/api.php?action=parse&page=' + str(name)
            temp = get_words_and_clean(get_page(p))
            l.append(temp)
            bar.update(a + 1)
            sleep(0.1)
        except:
            pass
    bar.finish()
    return l


def word_cloud_creator():
    title = None
    wordcloud = WordCloud(
        background_color='white',
        max_words=200,
        max_font_size=40,
        scale=3,
        random_state=1  # chosen at random by flipping a coin; it was heads
    ).generate(str(collector()))

    plt.figure(1, figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    name = input("Enter name to save as: ")
    plt.title('Wordcloud of '+name)
    plt.savefig(name + '.png')
    plt.close()


word_cloud_creator()
