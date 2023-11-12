import os
import sys
import urllib.request
import datetime
import time
import json

client_id = 'kc_ifqp2lwp0JjjqmfMj'
client_secret = 'V4VTaNAMal'


# [CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    # parameter 값을 naver openAPI 에서 지정하는 값으로 바꿔서 넣어줌
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    # print(node)

    # node 다른애로 보이는데,,, 값은 제대로 들어가있음
    url = base + node + parameters
    # url = base + json_node + parameters
    responseDecode = getRequestUrl(url)  # [CODE 1] 위에서 선언한 함수 호출

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)


def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    print(post)

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append(
        {'cnt': cnt,
         'title': title,
         'description': description,
         'org_link': org_link,
         'link': link,
         'pDate': pDate}
    )
    return


def main():
    # 이거 바꾸면,,, 다른 주제로 검색 가능함!!
    node = 'news'  # 크롤링 할 대상
    srcText = input("검색어를 입력하세요 \n")
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)  # [CODE 2]
    total = jsonResponse['total']

    def isResponseValid(jsonResponse):
        return (jsonResponse != None) and (jsonResponse['display'] != 0)

    while (isResponseValid(jsonResponse)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)  # [CODE 3]

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start - 1, 100)  # [CODE 2]

    print(f'전체검색 : {total} 건')

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='UTF-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(jsonFile)

    print("가져온 데이터 : %d 건" % (cnt))
    print(f"{srcText}_naver_{node}.json SAVED")


if __name__ == '__main__':
    main()
