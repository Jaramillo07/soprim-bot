from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SOPRIM BOT is alive"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Mensaje recibido:", data)

    # Respuesta simulada
    return JSONResponse(content={"reply": "Hola desde SOPRIM BOT 🚀"})
