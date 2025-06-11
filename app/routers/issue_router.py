from fastapi import APIRouter
from pydantic import BaseModel
from app.llm_logic import predict_issue_reason

router = APIRouter()

class IssueRequest(BaseModel):
    issue: str

class IssueResponse(BaseModel):
    reason: str

@router.post("/reason", response_model=IssueResponse)
def get_reason(data: IssueRequest):
    reason = predict_issue_reason(data.issue)
    return IssueResponse(reason=reason)