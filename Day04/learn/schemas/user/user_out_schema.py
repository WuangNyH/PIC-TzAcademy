from learn.schemas.common.base_out_schema import BaseOutSchema


class UserOut(BaseOutSchema):
    name: str
    age: int
