# test.py

import cv2
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity


def load_model():
    model = FaceAnalysis(name='buffalo_l')
    model.prepare(ctx_id=0)
    return model


def get_embedding(model, image_path):
    img = cv2.imread(image_path)
    faces = model.get(img)

    if len(faces) == 0:
        return None, None

    face = faces[0]
    return face.embedding, face.bbox.tolist()


def verify_faces(image1_path, image2_path, threshold=0.5):
    model = load_model()

    emb1, bbox1 = get_embedding(model, image1_path)
    emb2, bbox2 = get_embedding(model, image2_path)

    if emb1 is None or emb2 is None:
        return {"error": "Face not detected"}

    similarity = cosine_similarity([emb1], [emb2])[0][0]

    result = "same person" if similarity > threshold else "different person"

    return {
        "verification_result": result,
        "similarity_score": float(similarity),
        "face1_bbox": bbox1,
        "face2_bbox": bbox2
    }