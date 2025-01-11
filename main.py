from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from helper import predict

app = FastAPI()

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        prediction_label = predict(BytesIO(contents))
        return JSONResponse(content={"prediction": prediction_label}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)