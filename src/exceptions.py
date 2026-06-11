"""Custom exception hierarchy for the security-questionnaire-sync package."""

class ApiError(Exception):
    """Raised when the remote API returns a non‑2xx status code."""

    def __init__(self, status_code: int, message: str, response_text: str | None = None):
        self.status_code = status_code
        self.message = message
        self.response_text = response_text
        super().__init__(f"[{status_code}] {message}")

    def __repr__(self):
        return f"<ApiError status={self.status_code} message={self.message!r}>"