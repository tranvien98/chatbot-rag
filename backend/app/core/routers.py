from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/healthchecker")
async def health(request: Request):
    client_host = request.client.host
    x_real_ip = request.headers.get("X-Real-IP")
    x_forwarded_for = request.headers.get("X-Forwarded-For")

    return {
        "client_host": client_host,
        "X-Real-IP": x_real_ip,
        "X-Forwarded-For": x_forwarded_for,
    }
