# -*- coding: utf-8 -*-
import json
import os
import sys
from urllib import request

from bs4 import BeautifulSoup
from flask import Flask, render_template, Response


class Entry:
    hot = 0
    value = ''

    def __init__(self, hot, value) -> None:
        super().__init__()
        self.hot = hot
        self.value = value


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def start():
    with request.urlopen('https://s.weibo.com/top/summary') as f:
        data = f.read().decode('utf-8')
        soup = BeautifulSoup(data, features='html.parser')
        json_list = []
        for element in soup.find_all(attrs={'class': 'td-02'}):
            tag = element.find('span')
            if tag is not None:
                text = element.find('a').text
                # print(
                #     "热度: " + tag.text + "\t\t"
                #     + text
                #     + " https://s.weibo.com" + element.find('a').attrs['href']
                # )
                entry = Entry(hot=int(tag.text), value=text)
                json_list.append(entry)
        return json.dumps([ob.__dict__ for ob in json_list])


app = Flask(__name__, template_folder=resource_path('templates'), static_folder=resource_path('static'))


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/get', methods=['GET'])
def get():
    return Response(start(), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
