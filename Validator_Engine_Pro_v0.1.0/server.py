import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from validator_engine import ValidatorEngine

# Initialize the server application and your core engine asset
app = FastAPI(title="Validator-Engine-Pro API")
engine = ValidatorEngine()

# Establish the incoming data rule parameter structure
class PayloadRequest(BaseModel):
    raw_stream: str

@app.post("/validate")
async def process_payload(request: PayloadRequest):
    """
    Live production API gate. Intercepts incoming network payloads,
    executes your real-time repairs, and returns structured data.
    """
    try:
        result = engine.repair_and_validate(request.raw_stream)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

if __name__ == "__main__":
    # Boots the server locally on Port 8000 using your hardware
    uvicorn.run(app, host="127.0.0.1", port=8000)
