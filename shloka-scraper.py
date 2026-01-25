import httpx
import json
import asyncio

from pathlib import Path
from bs4 import BeautifulSoup


class TaskQueue(asyncio.TaskGroup):
    def __init__(self, /, maxsize):
        self._semaphore = asyncio.Semaphore(maxsize)
        super().__init__()

    def create_task(self, coro, **kwargs):
        async def wrapper_coro():
            await self._semaphore.acquire()
            try:
                await coro
            finally:
                self._semaphore.release()
        return super().create_task(wrapper_coro(), **kwargs)


headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
root = Path('data')
root.mkdir(exist_ok=True)


async def run():
    async with httpx.AsyncClient(headers=headers) as client:
        page = await client.get('https://shlokam.org/bhagavad-gita/index/',
                                 headers={'Accept': 'text/html'})

        async with TaskQueue(maxsize=15) as tg: 
            for i in range(1, 18+1):
                chapter = BeautifulSoup(page, 'lxml').find('div', id=f'index-c{i}')
                chapter_dir = root / f'{i-1}'
                chapter_dir.mkdir(exist_ok=True)

                async def download(index, url):
                    page = await client.get(url)
                    shloka = BeautifulSoup(page, 'lxml')

                    def extract_string(tag):
                        return '\n'.join(tag.stripped_strings)
                
                    payload = {
                           'sanskrit': extract_string(shloka.find('div', class_='FontSanskrit24')),
                               'iast': extract_string(shloka.find('div', class_='Font20A')),
                        'translation': extract_string(shloka.find('div', class_='Font19I'))
                    }

                    with open(chapter_dir / f'{index}.json', 'w') as file:
                        # `ensure_ascii=False` ensures the Devnagri script is directly written.
                        json.dump(payload, file, ensure_ascii=False)

                for index, link in enumerate(chapter.find_all('a')):
                    tg.create_task(download(index, link['href']))

asyncio.run(run())

