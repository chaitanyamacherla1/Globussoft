# app.py

from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
from test import load_model
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

model = load_model()


def read_image(file):
    img_bytes = file.file.read()
    np_arr = np.frombuffer(img_bytes, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)


def get_embedding(image):
    faces = model.get(image)

    if len(faces) == 0:
        return None, None

    face = faces[0]
    return face.embedding, face.bbox.tolist()


@app.post("/verify/")
async def verify(image1: UploadFile = File(...), image2: UploadFile = File(...)):

    img1 = read_image(image1)
    img2 = read_image(image2)

    emb1, bbox1 = get_embedding(img1)
    emb2, bbox2 = get_embedding(img2)

    if emb1 is None or emb2 is None:
        return {"error": "Face not detected"}

    similarity = cosine_similarity([emb1], [emb2])[0][0]

    result = "same person" if similarity > 0.5 else "different person"

    return {
        "verification_result": result,
        "similarity_score": float(similarity),
        "face1_bbox": bbox1,
        "face2_bbox": bbox2
    }