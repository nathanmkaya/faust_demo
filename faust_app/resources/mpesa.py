from typing import Any
from faust.web import View, Blueprint, Request, Response
from faust_app.mpesa import agent, Transaction


mpesa_blueprint = Blueprint('mpesa')


@mpesa_blueprint.route('/callback/')
class M_Pesa(View):

    async def post(self, request: Request, **kwargs: Any) -> Response:
        payload = await request.json()

        transaction = Transaction(id=payload['id'])
        await agent.send(key=transaction.id, value=transaction)
        return self.json({'status': 'success'})


