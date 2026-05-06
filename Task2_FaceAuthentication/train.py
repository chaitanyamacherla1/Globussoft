# train.py

from insightface.app import FaceAnalysis

def train_model():
    model = FaceAnalysis(name='buffalo_l')
    model.prepare(ctx_id=0)
    print("✅ Model ready (pretrained InsightFace)")

if __name__ == "__main__":
    train_model()