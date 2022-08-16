import asyncio
import httpx

async def download (query, current_page):
    heder = {'Authorization':'563492ad6f9170000100000137633c8197de4954961882a473fd6525'}
    params = {'query':query, 'per_page':1, 'page':current_page}
    url = "https://api.pexels.com/v1/search"

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers = heder, params = params)
        if r.status_code == 200:
            _r = r.json()
            for item in _r.get('photos'):
                print(item.get('src').get('original'))
        else:
            print(r.status_code)
    print(f'{query} = {current_page}')

async def main():
    queue = asyncio.Queue()
    query = input('Что ищем? ')
    page_count = int(input('кол-во картинок '))

    current_page = 0
    tasks_list = []
    while current_page< page_count:
        current_page+=1
        task = asyncio.create_task(download(query, current_page))
        tasks_list.append(task)

    await queue.join()
    await asyncio.gather(*tasks_list, return_exceptions=True)

asyncio.run(main())