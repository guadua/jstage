import requests
import pandas as pd
from lxml import etree
from pdb import set_trace
API2 = pd.read_csv('response_2.csv', header=None)
API3 = pd.read_csv('response_3.csv', header=None)

API_URL = 'http://api.jstage.jst.go.jp/searchapi/do'
NS = {'a': 'http://www.w3.org/2005/Atom'}
payload = {'service': 2, 
        'material': '日本土壌肥料学雑誌',
        # 'material': '日本',
        # 'article': 'キュウリ',
        # 'cdjournal': 'jjshs',
        # 'text': 'Cucumis sativus 肥',
        # 'text': '肥料',
        'start': 1,
        'count': 1000}
# payload = {'service': 3}
req = requests.get(API_URL, params=payload)
parser = etree.XMLParser()
tree = etree.fromstring(req.content, parser=parser)
df = pd.DataFrame(tree.xpath('//a:entry', namespaces=NS))
set_trace()
