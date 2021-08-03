from fastapi import APIRouter, Header, HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from guard.models import Log, Project
from guard.schemas import CreateLogReq

router = APIRouter()


@router.post("")
async def add_log(req: CreateLogReq, x_secret: str = Header(...)):
    project_id = req.project_id
    content = req.content
    project = await Project.get(pk=project_id)
    if project.secret != x_secret:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    return await Log.create(project=project, content=content)
