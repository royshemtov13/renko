from pydantic import BaseModel


class RenkoBar(BaseModel):
    timestamp: float
    open: float
    high: float
    low: float
    close: float
    trend: int
