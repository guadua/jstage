# -*- coding:utf8 -*-
import os
import re
from lxml import html, etree
#import pandas as pd
import requests
import zipfile
import io # for python 2.7 import StringIO
import MeCab # NEED TO DO 'export LD_LIBRARY_PATH=/usr/local/lib'
import pdb

JST_API = 'http://api.jstage.jst.go.jp/searchapi/do'
JST_ATOM = {'atom': 'http://www.w3.org/2005/Atom'}

def get_volume_list(cdjournal):
    payload = {'service': 2, 'cdjournal': cdjournal}
    r = requests.get(JST_API, params=payload)
    tree = etree.fromstring(r.content)
    entries = tree.findall('./atom:entry', JST_ATOM)

    df = pd.DataFrame()
    i = 0
    for entry in entries:
        # pubyear = entry.find('./atom:pubyear', JST_ATOM)
        # link = entry.find('./atom:id', JST_ATOM)
        for el in entry.getchildren():
            df.loc[i, el.tag] = el.text
        i = i + 1
    return df

def get_ris_files(href):
    r = requests.get(href)
    tree = html.fromstring(r.content)
    # 'https://www.jstage.jst.go.jp/AF05S010ShoshJkuDld?sryCd=mez&noVol=1&noIssue=1&kijicd=1_KJ00003266760%2F1_KJ00003266761%2F1_KJ00003266762%2F1_KJ00003266763%2F1_KJ00003266764%2F1_KJ00003266765%2F1_KJ00003266766%2F1_KJ00003266767%2F1_KJ00003266768%2F1_KJ00003266769%2F1_KJ00003266770%2F1_KJ00003266771%2F1_KJ00003266772%2F1_KJ00003266773%2F1_KJ00003266774%2F1_KJ00003266775%2F1_KJ00003266776%2F1_KJ00003266777%2F1_KJ00003266778%2F1_KJ00003266779%2F1_KJ00003266780%2F1_KJ00003266781%2F1_KJ00003266782&cdjournals=mez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez%2Fmez&btnaction=JT0052&request_locale=JA'

    script = tree.xpath('//script')[0].text
    start = script.find('https')
    stop = script.find('JA') + len('JA')
    ris_url = script[start:stop]
    r1 = requests.get(ris_url, stream=True)
    z = zipfile.ZipFile(io.StringIO(r1.content))
    z.extractall()
    print('extracted %s files' % len(z.filelist))

    # items = tree.xpath('//ul[@class="search-resultslisting"]/li')

    # df = pd.DataFrame()
    # i = 0
    # for item in items:
    #     df.loc[i, 'doc'] = item.findall('./div/a')[0].attrib['href']
    #     df.loc[i, 'doi'] = item.findall('./div/a')[1].attrib['href']
    #     df.loc[i, 'pdf'] = item.find('./div/div/span/a').attrib['href']
    #     i = i + 1
    # pdb.set_trace()

def get_ris_list(cdjournal):
    ris_files = os.listdir(cdjournal)
    ris_files = [os.path.join(cdjournal, ris) for ris in ris_files]
    return ris_files

def parse_ris(ris):
    with open(ris, 'r') as f:
        lines = f.readlines()
        m = MeCab.Tagger()
        print(m.parse(lines[4][5:]))


def main():
    volumes = get_volume_list(cdjournal = 'mez')
    for index, row in volumes.iterrows():
        url = row['{http://www.w3.org/2005/Atom}id']
        print(url)
        get_ris_files(url)

if __name__ == '__main__':
    # main()
    ris_files = get_ris_list('mez')
    for ris in ris_files:
        parse_ris(ris)
        print('%s/%s' % (ris_files.index(ris), len(ris_files)))