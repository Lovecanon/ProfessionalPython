import requests
import re
import asyncio
import time

RANK_PATTERN = '</span>\n(\d+)\n</span>'
AMAZON = 'https://www.amazon.cn/dp/'
headers = {
    'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25',
}
ASIN = {
    'B01FQAS0KK': 'Python核心编程',
    'B00WKR1OKG': 'Python Cookbook(第3版)(中文版)',
    'B004TUJ7A6': 'Python学习手册',
    'B00GHGZLWS': '利用Python进行数据分析',
    'B01KTX2AF0': '用Python写网络爬虫',
    'B01MTY3ZAL': 'Python机器学习:预测分析核心算法'
}

@asyncio.coroutine
def get_rank(asin):
    resp = requests.get('%s%s' % (AMAZON, asin), headers=headers)
    return re.findall(RANK_PATTERN, resp.text)[0]

async def get_rank1(asin):
    resp = requests.get('%s%s' % (AMAZON, asin), headers=headers)
    return re.findall(RANK_PATTERN, resp.text)[0]


@asyncio.coroutine
def num_sum(*nums):
    sum = 0
    print(nums)
    for num in nums:
        sum += num
    return sum


if __name__ == '__main__':
    start = time.time()
    # for asin, name in ASIN.items():
    #     print(name, ':', get_rank(asin))

    # TODO 为什么yield from 不能和requests.get
    coro = asyncio.wait([get_rank(asin) for asin in ASIN.keys()])
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(coro)
    print([future.result() for future in results[0]])
    print('Total time:', time.time() - start)
