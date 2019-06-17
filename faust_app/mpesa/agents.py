from faust_app.app import app
from faust_app.mpesa.models import Transaction

mpesa = app.topic("mpesa", value_type=Transaction)


@app.agent(mpesa)
async def mpesa_agent(transactions):
    async for transaction in transactions:
        print(transaction.id)

