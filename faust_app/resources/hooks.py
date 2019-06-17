from typing import Any
from faust.web import View, Blueprint, Request, Response
from faust_app.mifos import agent, MifosEvent


hook = Blueprint('hook')


@hook.route('/mifos/')
class Hooks(View):
    count: int = 0

    async def get(self, request: Request, **kwargs: Any) -> Response:
        return self.json({'count': self.count})

    async def post(self, request: Request, **kwargs: Any) -> Response:
        payload = await request.json()
        headers = request.headers
        entity = headers['X-FINERACT-ENTITY']
        action = headers['X-FINERACT-ACTION']

        event = MifosEvent(id=payload['resourceId'], entity=entity, action=action, payload=payload)
        await agent.send(value=event)
        return self.json({'status': 'success'})









