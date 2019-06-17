from faust_app.app import app
from .hooks import hook
from .mpesa import mpesa_blueprint as mpesa

app.web.blueprints.add('/hook/', hook)
app.web.blueprints.add('/mpesa/', mpesa)
