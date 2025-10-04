
## Human Emotion Recognition 🎭  

This project is a **Human Emotion Recognition** application built with [Streamlit](https://streamlit.io/) and [DeepFace](https://github.com/serengil/deepface).  
It allows users to upload **images** or **videos**, and the app will detect and display the **dominant emotion** of detected faces in real time.  

---

## 🚀 Features  
- Upload an **image** (JPG, PNG, JPEG) and detect emotions.  
- Upload a **video** (MP4, MOV, AVI) and detect emotions frame by frame.  
- Uses **DeepFace** for emotion analysis.  
- Simple and interactive **Streamlit** web app interface.  

---

## 📂 Project Structure  

```

.
├── Human_Emotion_Recognition.py   # Main Streamlit app
├── README.md                      # Documentation

````

---

## 🛠 Installation  

Make sure you have **Python 3.8+** installed.  

1. Clone the repository:  
```bash
git clone https://github.com/your-username/Human-Emotion-Recognition.git
cd Human-Emotion-Recognition
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, here are the main dependencies:

```txt
streamlit
numpy
opencv-python
deepface
pillow
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run Human_Emotion_Recognition.py
```

Then open your browser at **[http://localhost:8501/](http://localhost:8501/)**.

---

## 📸 Example

* **Image Upload:**
  Detects the most dominant emotion in the uploaded image.

* **Video Upload:**
  Processes video frames and overlays detected emotions on faces.

---

## 🙌 Acknowledgements

* [DeepFace](https://github.com/serengil/deepface) for facial analysis.
* [Streamlit](https://streamlit.io/) for easy web app deployment.

---


