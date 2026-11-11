from fastapi import FastAPI, UploadFile, File
from image_service import ImageService

app = FastAPI(title="Image Prediction API")

image_service = ImageService()


@app.post("/predict-image")
async def predict_image_endpoint(file: UploadFile = File(...)):
    # 1. هنا الـ API بيستدعي الفانكشن
    
    # 2. الفانكشن بدورها بتستدعي السيرفس (preprocess ثم predict)
    processed_image = image_service.preprocess(file)
    result = image_service.predict(processed_image)
    
    return {
        "filename": file.filename,
        "result": result
    }