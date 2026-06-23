# 🖼️ MobileNetV2 Image Classifier with Streamlit

An interactive Web Application built with **Streamlit**, **TensorFlow/Keras**, and **OpenCV** that uses a pre-trained **MobileNetV2** model to classify uploaded images in real-time.

---

## 🚀 Features
* **Instant Classification:** Upload any image (JPEG, PNG, JPG) and get top predictions instantly.
* **Pre-trained Deep Learning:** Built using Google's MobileNetV2 architecture, trained on the ImageNet dataset (recognizes 1,000 distinct object classes).
* **OpenCV Image Processing:** Utilizes OpenCV and PIL for quick image handling and resizing.
* **Modern UI:** Clean and responsive interface powered completely by Streamlit.

---

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Deep Learning Framework:** [TensorFlow / Keras](https://www.tensorflow.org/)
* **Computer Vision:** [OpenCV (cv2)](https://opencv.org/) & [PIL (Pillow)](https://pillow.readthedocs.io/)
* **Package Manager:** [uv](https://github.com/astral-sh/uv) (or standard pip)

---

## 📦 Installation & Setup

Ensure you have Python 3.10 to 3.13 installed (Note: TensorFlow does not officially support Python 3.14 stable yet).

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

project structure : 
├── .venv/               # Virtual environment
├── main.py              # Main Streamlit application source code
├── pyproject.toml       # Project configuration and metadata (if using uv)
└── README.md            # Project documentation