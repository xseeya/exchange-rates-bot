from api import Api

import time
formatted_time = time.strftime("%H:%M:%S")

from db import Session, Exchange

client = Api()

async def job():
    with Session() as db:
        rates = db.query(Exchange).filter().first()
        rates.usd_to_rub = f'{client.usd()}'
        rates.eur_to_rub = f'{client.eur()}'
        rates.cny_to_rub = f'{client.cny()}'
        rates.time = formatted_time
        db.commit()
        





