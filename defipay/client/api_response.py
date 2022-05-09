from dataclasses import dataclass
from typing import Optional

from defipay.error.api_error import ApiError


@dataclass
class ApiResponse:
    success: bool
    result: Optional[dict]
    exception: Optional[ApiError]
