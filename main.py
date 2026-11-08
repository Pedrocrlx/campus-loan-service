from fastapi import FastAPI

app = FastAPI(title="Campus Loan Service")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
