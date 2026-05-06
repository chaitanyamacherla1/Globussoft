# Globussoft
# Face Authentication (Face Verification) – Task 2

## 📌 Overview

This project implements a **Face Authentication system** using Python and FastAPI.
It verifies whether two input face images belong to the same person.

The system performs:

* Face detection
* Feature (embedding) extraction
* Similarity computation
* Final verification result

---

## 🚀 Features

* Accepts two face images
* Detects faces in both images
* Extracts embeddings using InsightFace (ArcFace)
* Computes similarity using cosine similarity
* Returns:

  * Verification result: **same person / different person**
  * Similarity score
  * Bounding boxes of detected faces

---

## 🧠 Tech Stack

* Python
* FastAPI
* InsightFace (pretrained model)
* OpenCV
* NumPy
* Scikit-learn

---

## 📂 Project Structure

```
face-auth/
│
├── train.py          # Model setup (training file)
├── test.py           # Load model + prediction function
├── app.py            # FastAPI service
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

---

## ▶️ Running the Application

### 1. Run FastAPI server

```bash
uvicorn app:app --reload
```

### 2. Open API Docs

```
http://127.0.0.1:8000/docs
```

### 3. Test the API

* Use `/verify/` endpoint
* Upload two face images
* Get verification result

---

## 📥 Example API Response

```json
{
  "verification_result": "same person",
  "similarity_score": 0.78,
  "face1_bbox": [120, 80, 300, 350],
  "face2_bbox": [100, 60, 280, 330]
}
```

---

## 📌 How It Works

1. **Face Detection**

   * Detect faces using InsightFace

2. **Embedding Extraction**

   * Convert faces into numerical vectors (embeddings)

3. **Similarity Calculation**

   * Compute cosine similarity between embeddings

4. **Decision**

   * If similarity > 0.5 → same person
   * Else → different person

---

## 📁 Files Description

### train.py

* Initializes pretrained InsightFace model
* Acts as training step (model setup)

### test.py

* Contains:

  * Model loading
  * Face embedding extraction
  * Verification function

### app.py

* FastAPI service
* Accepts image input
* Returns prediction results

---

## 📊 Model Used

* InsightFace (buffalo_l)
* Based on ArcFace embeddings
* Pretrained model (no custom training required)

---

## 🧪 Notes

* Only the first detected face is used
* Threshold for similarity is set to **0.5** (can be tuned)
* Works on CPU (GPU optional)

---

## 🎯 Submission Checklist

* [x] Training file (train.py)
* [x] Testing file (test.py)
* [x] FastAPI implementation
* [x] requirements.txt
* [x] README.md

---

## 💡 Future Improvements

* Multi-face support
* Face alignment
* Database integration (face login system)
* Liveness detection (anti-spoofing)
* GPU optimization

---


## 👤 Author

CHAITANYA MACHERLA
