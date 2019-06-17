import faust

app: faust.App = faust.App(
    id="farmdrive",
    version=1,
    autodiscover=True,
    origin='faust_app',
    store='rocksdb://',
    # value_serializer='raw',
)


def main() -> None:
    app.main()
