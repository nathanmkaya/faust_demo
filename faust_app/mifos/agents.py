from faust_app.app import app
from .models import MifosEvent
from .clients import client_creation_agent

mifos_event = app.topic("mifos_event", value_type=MifosEvent)


@app.agent(mifos_event)
async def mifos_agent(events):
    async for event in events:
        event: MifosEvent = event
        print(event.payload)
        if event.entity == 'CLIENT':
            await client_creation_agent.send(value=event)
        else:
            yield event
