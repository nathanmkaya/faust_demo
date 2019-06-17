from faust import Record


class MifosEvent(Record):
    entity: str
    action: str
    id: int
    payload: dict


