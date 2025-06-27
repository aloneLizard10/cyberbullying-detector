# 🛡️ Cyberbullying Detector for Social Media

This project is a **Machine Learning-based Cyberbullying Detector** that classifies social media text into different types of bullying — helping make the internet a safer place.

## 🚀 Features

- ✅ Detects **Cyberbullying** in social media posts
- ✅ Identifies type (e.g., religion, ethnicity, other)
- ✅ 📤 Upload and scan multiple tweets from CSV
- ✅ 📊 Visualization of model performance
- ✅ 📝 Feedback form for user input
- ✅ 🧠 Trained using a labeled dataset from IEEE Mendeley

---

## 🧪 Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas
- nltk
- seaborn & matplotlib
- joblib

---

## 📁 Project Structure

cyberbullying-detector/
│
├── app.py # Streamlit frontend app
├── train_model.py # Model training script
├── cyberbullying_model.pkl # Trained ML model
├── vectorizer.pkl # Trained TF-IDF vectorizer
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── data/ # Contains input datasets
└── assets/ # Optional: logos, plots, etc.

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/cyberbullying-detector.git
   cd cyberbullying-detector
2. Create & activate virtual environment:
    python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

3. Install dependencies:
    pip install -r requirements.txt

4. Train the model:
    python train_model.py

5. Run the app:
    streamlit run app.py

✍️ Feedback
Feel free to use the feedback form inside the app to help improve it!

📌 Dataset
This project uses a labeled dataset from the Comprehensive Cyberbullying Dataset (Mendeley, Jan 2024) containing aggressive and non-aggressive tweets with user data and labels.

🤝 Contributions
PRs are welcome. Feel free to suggest improvements, add more labels, or even expand this to multilingual content!

📜 License
This project is open-source under the MIT License.
