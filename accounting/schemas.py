from pydantic.typing import Optional

from ninja import Schema


class FourOFourOut(Schema):
    detail: str


class AccountOut(Schema):
    parent: 'AccountOut' = None
    name: str
    type: str
    code: str
    full_code: str


AccountOut.update_forward_refs()
