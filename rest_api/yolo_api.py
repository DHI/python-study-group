import io
from typing import List
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import uvicorn
import numpy as np
from enum import Enum
from datetime import datetime
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI(title='Deploying a ML Model with FastAPI')

class Model(str, Enum):
    yolov3tiny = "yolov3-tiny"
    yolov3 = "yolov3"


class ModelMetaData(BaseModel):

    version : int
    name : str
    trainable: bool
    last_updated: datetime
    tags: List[str] = []


@app.get("/")
def home():
    return "Now head over to http://localhost:8000/docs."

@app.get("/metadata")
def metadata() -> ModelMetaData:

    return ModelMetaData(name="yolov3", version=2, trainable=False, last_updated=datetime(2021,1,1), tags=["AI","Skynet"])


@app.post("/predict") 
def prediction(model: Model, file: UploadFile = File(...)):

    filename = file.filename
    fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")
    
    
    image_stream = io.BytesIO(file.file.read())
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    bbox, label, conf = cv.detect_common_objects(image, model=model)
    output_image = draw_bbox(image, bbox, label, conf)

    cv2.imwrite(f'images_uploaded/{filename}', output_image)
    
    file_image = open(f'images_uploaded/{filename}', mode="rb")
    
    return StreamingResponse(file_image, media_type="image/jpeg")


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)