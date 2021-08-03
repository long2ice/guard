from fastapi import APIRouter

from .log import router as log
from .project import router as project

router = APIRouter()
router.include_router(project, prefix="/project")
router.include_router(log, prefix="/log")
