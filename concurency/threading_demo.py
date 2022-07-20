from queue import Queue
from threading import Thread
import requests

NUM_THREADS = 5
q = Queue()

images = [
    'https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7',
    'https://images.unsplash.com/photo-1587620962725-abab7fe55159',
    'https://images.unsplash.com/photo-1493119508027-2b584f234d6c',
    'https://images.unsplash.com/photo-1482062364825-616fd23b8fc1',
    'https://images.unsplash.com/photo-1521185496955-15097b20c5fe',
    'https://images.unsplash.com/photo-1510915228340-29c85a43dcfe',
]


def download_img():
    """
    Download image from img_url in current directory
    """
    global q

    while True:
        img_url = q.get()

        res = requests.get(img_url, stream=True)
        filename = f"{img_url.split('/')[-1]}.jpg"

        with open(filename, 'wb') as f:
            for block in res.iter_content(1024):
                f.write(block)
        q.task_done()


def main():
    for img_url in images * 5:
        q.put(img_url)

    for t in range(NUM_THREADS):
        worker = Thread(target=download_img)
        worker.daemon = True
        worker.start()

    q.join()


if __name__ == '__main__':
    main()
