"""Expose the FastAPI app instance.

This is done like this so that uvicorn can find the app instance.

Provides:
- app: The FastAPI app instance.
"""

from api.router import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
