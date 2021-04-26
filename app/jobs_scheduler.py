from config import Config
from app.json_construct import construct
import datetime
import schedule

dirpath = Config().PATH_TO_CONTENT


def main():

    def job():
        construct(dirpath)

    schedule.every(30).seconds.do(job)

    while True:
        schedule.run_pending()
