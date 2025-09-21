import time
import random

def fetch_page(url):
    print(f"Start fetching {url}")
    yield f"Fetching {url}..."   
    time.sleep(random.randint(1, 3))
    yield f"Finished {url}"

urls = ["page1.com", "page2.com", "page3.com"]

tasks = [fetch_page(url) for url in urls]

while tasks:
    for task in tasks[:]:
        try:
            print(next(task))
        except StopIteration:
            tasks.remove(task)
