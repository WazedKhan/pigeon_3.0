from pydantic import BaseModel


class TODO(BaseModel):
    name: str
    description: str
    complete: bool
