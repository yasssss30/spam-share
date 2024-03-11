import asyncio
import aiohttp
import json
import re
from colorama import init, Fore, Style
import random
import time
init()
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
config = {
  'cookies': '',
  'id': ''
}
texx="""
╔═╗╦   ╦╔═╗╦═╗╔═╗      ╦      ╦╦╔═╗
╚═╗╠═╣╠═╣╠╦╝║╣ ───╚╗╔╝║╠═╝
╚═╝╩   ╩╩   ╩╩╚═╚═╝         ╚╝   ╩╩  
-- Canhcutkhongbay --
suocre code share boost 1 cookie
contact me: fb.me/canhcutkhongbay.sieudeptrai
"""
def banner(texx):
  for char in texx:
    random_color = random.choice(colors)
    print(random_color + char, end='')
banner(texx)
config['cookies'] = input("cookie facebook: ")
config['id'] = input("id post: ")
share_count = int(input("share_count: "))
import os
os.system("clear")
banner(texx)
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': "Windows",
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1'
}
class Share:
  async def get_token(self, session):
    headers['cookie'] = config['cookies']
    async with session.get('https://business.facebook.com/content_management', headers=headers) as response:
      data = await response.text()
      access_token = 'EAAG' + re.search('EAAG(.*?)","', data).group(1)
      return access_token, headers['cookie']
  async def share(self, session, token, cookie):
    headers['cookie']
    headers['sec-fetch-dest']
    headers['sec-fetch-mode']
    headers['sec-fetch-site']
    headers['sec-fetch-user']
    headers['upgrade-insecure-requests']
    headers['accept-encoding'] = 'gzip, deflate'
    headers['host'] = 'graph.facebook.com'
    headers['cookie'] = cookie
    count = 1
    while count < share_count:
      async with session.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{config["id"]}&published=0&access_token={token}', headers=headers) as response:
        time.sleep(0.2)
        data = await response.json()
        # print(f'[ {count + 1} ] - {data["id"]}')
        # count += 1
        if 'id' in data:
          print(f"[ {count}/{share_count} ] - {Fore.GREEN}{data['id']} - booster share{Style.RESET_ALL}",end="\r")
          count += 1
        else:
          # print(data)
          print(f"[ BLOCK ]: {Fore.RED}cookie is blocked, ctrl c to exit !!!!{Style.RESET_ALL}")
          print(f"End: {count} ok?")
          break
async def main(num_tasks): 
  async with aiohttp.ClientSession() as session:
    share = Share()
    token, cookie = await share.get_token(session)
    tasks = []
    for i in range(num_tasks):
      task = asyncio.create_task(share.share(session, token, cookie))
      tasks.append(task)
    await asyncio.gather(*tasks)

##=================##
##===== [ main ] =====##
asyncio.run(main(1)) #=#
##==== [ thread ] ====##
