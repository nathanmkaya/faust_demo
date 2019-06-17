from faust_app.app import app
from faust_app.mifos.models import MifosEvent

client_creation = app.topic("client_creation", value_type=MifosEvent)


@app.agent(client_creation)
async def client_creation_agent(clients):
    async for client in clients:
        print(client.payload)
        yield client
