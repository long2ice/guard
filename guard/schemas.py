from pydantic import BaseModel


class CreateLogReq(BaseModel):
    project_id: int
    content: str
