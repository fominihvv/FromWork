import aiohttp
import asyncio
import os
import aiofiles
from bs4 import BeautifulSoup
import time


def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


async def download_img(url: str, download_folder: str, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore):
    async with semaphore:
        async with session.get(url) as response:
            if response.status == 200:
                filename = url.rsplit('/', 1)[1]
                async with aiofiles.open(f'{download_folder}\\{filename}', 'wb') as file:
                    await file.write(await response.read())


async def main():
    start_page = 'https://asyncio.ru/zadachi/4/index.html'
    download_folder = 'c:\\temp\\downloads'
    semaphore = asyncio.Semaphore(100)

    async with aiohttp.ClientSession() as session:
        if not os.path.exists(download_folder):
            os.mkdir(download_folder)

        async with session.get(start_page) as response:
            response_text = await response.text()

        soup = BeautifulSoup(response_text, 'html.parser')
        links = soup.find_all('img')
        url_list = [link.get('src') for link in links]
        base_url = start_page.rsplit('/', 1)[0] + '/'

        tasks = [download_img(base_url + url, download_folder, session, semaphore) for url in url_list]
        await asyncio.gather(*tasks)

    print(get_folder_size(download_folder))


start = time.time()
asyncio.run(main())
print(time.time() - start)
