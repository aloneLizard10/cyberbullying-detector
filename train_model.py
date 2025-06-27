import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# --- Load and Combine Data ---
aggressive_df = pd.read_csv("3. Aggressive_All.csv")
non_aggressive_df = pd.read_csv("4. Non_Aggressive_All.csv")
cb_labels_df = pd.read_csv("6. CB_Labels.csv")

aggressive_df['aggressive'] = 1
non_aggressive_df['aggressive'] = 0
df = pd.concat([aggressive_df, non_aggressive_df], ignore_index=True)

# Merge with CB_Labels on ID (if available)
if 'ID' in cb_labels_df.columns and 'ID' in df.columns:
    df = pd.merge(df, cb_labels_df, on='ID', how='left')
    df['CB_Label'] = df['CB_Label'].fillna('cyberbullying')
else:
    df['CB_Label'] = df['aggressive'].apply(lambda x: 'cyberbullying' if x == 1 else 'non-cyberbullying')

# --- Text Column Setup ---
text_column = 'Message'  # Make sure this is the correct column name
df[text_column] = df[text_column].astype(str)

# Define X and y
X = df[text_column]
y = df['CB_Label']  # We use multi-class label (not just 0/1)

# --- TF-IDF and Classifier Pipeline ---
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

# --- Save the model and vectorizer ---
joblib.dump(model, "cyberbullying_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model and vectorizer saved successfully!")
