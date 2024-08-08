'''Напишите приложение, которое скачивает картинки заданного альбома и сохраняет в директории
photos. Все шаги должны логироваться: от старта приложения до вывода текущего состояния и информации о
завершении приложения и общем количестве скачанных картинок.'''
import requests
import logging
from  requests import HTTPError,ConnectionError

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger()

url = 'https://jsonplaceholder.typicode.com/photos'

def get_images(album_id,limited = 100):

    logger.info('Starting app...')
    try:
        response = requests.get(url)
        counter = 1
        logger.info('Downloading album 1 images...')

        for i in response.json():
            if i.get('albumId') == album_id:
                image_url = i.get('url')
                image_data = requests.get(image_url)
                logger.info(f"Saving image {counter} to photos/{album_id}-{counter}.jpg")
                with open(f"../photos/{album_id}-{counter}.jpg",'wb') as f:
                    f.write(image_data.content)
                counter += 1
                if counter > limited:
                    logger.info(f'Finished downloading images. Total images downloaded: {counter-1}')
                    # {counter -1} т.к. кол-во записи лога > чем кол-во фотографий
                    break
    except ConnectionError:
        logger.error("error connect")
    except HTTPError:
        logger.error("Wrong hhtp. Check him.")




if __name__ == "__main__":
    get_images(1,4)





