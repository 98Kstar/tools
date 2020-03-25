# -*- coding: utf-8 -*-

import os
import requests


class run():
    def __init__(self):
        self.url = '''http://en.shincheonji.kr/index.php?ch=adminMemberView&memberNumber=%s'''

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Cookie': "__utmz=106803543.1582694423.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmz=223618521.1582694897.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.784134724.1582694897; __utma=223618521.784134724.1582694897.1582978125.1582988823.9; __utma=106803543.1628985062.1582694423.1582821944.1582988929.7; _gid=GA1.2.1764988619.1582989145; __utmt=1; __utmt=1; __utmb=223618521.15.10.1582988823; PHPSESSID=lu1lp8634mtqthltiobhrojoe0; __utmc=106803543; __utmb=106803543.24.10.1582988929",
            'X-Forwarded-For': '172.31.41.90'
        }

    def run(self,i):
        request = requests.get((self.url % i), headers=self.headers)
        request.encoding = 'utf-8'
        data = request.content
        return  data

    def saveToFile(self,file_name, data):
        cwd = os.getcwd()
        file_path = cwd + '/data/' + str(file_name) + '.html'
        print(str(file_path))
        file = open(file_path, 'wb+')
        file.write(data)
        file.close()


if __name__ == '__main__':
    classObject = run()
    for i in range(115527, 115735):
        data = classObject.run(i)
        classObject.saveToFile(i,data)
        print(i)
