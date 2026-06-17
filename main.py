
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Placeholder for data loading and preprocessing
def load_and_preprocess_data(filepath="face_data.csv"):
    df = pd.read_csv(filepath)
    
    # Encode categorical features
    for col in ["expression", "gaze_direction", "head_pose"]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    
    # Features (X) and Target (y)
    X = df[["expression", "gaze_direction", "head_pose", "attention_score"]].values
    y = df["state"].values
    
    # Encode target variable
    label_encoder_state = LabelEncoder()
    y_encoded = label_encoder_state.fit_transform(y)
    
    # Standardize numerical features
    scaler = StandardScaler()
    X[:, -1] = scaler.fit_transform(X[:, -1].reshape(-1, 1)).flatten()
    
    return X, y_encoded, label_encoder_state, scaler

# Placeholder for model training
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    print("FocusGuard: Cognitive Distraction Detection System")
    print("--------------------------------------------------")
    print("1. Simulating data...")
    try:
        from data_simulator import simulate_face_data
        simulate_face_data(num_samples=2000).to_csv("face_data.csv", index=False)
        print("Simulated data generated: face_data.csv")
    except FileNotFoundError:
        print("Error: face_data.csv not found. Please run data_simulator.py first.")
        exit()
    except Exception as e:
        print(f"Could not simulate data: {e}. Attempting to load existing data.")

    print("2. Loading and preprocessing data...")
    X, y_encoded, label_encoder_state, scaler = load_and_preprocess_data()
    print(f"Data loaded. X shape: {X.shape}, y shape: {y_encoded.shape}")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    print(f"Data split. Train samples: {len(X_train)}, Test samples: {len(X_test)}")

    print("3. Training model...")
    model = train_model(X_train, y_train)

    print("4. Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {accuracy*100:.2f}%")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=label_encoder_state.classes_))

    print("5. Making a sample prediction...")
    # Example: focused-like data (expression: neutral, gaze: center, head: straight, attention: 90)
    sample_data_focused = np.array([[1, 0, 1, 90]]) 
    # Example: distracted-like data (expression: frown, gaze: left, head: tilted_left, attention: 20)
    sample_data_distracted = np.array([[0, 1, 2, 20]])

    # Scale attention score for sample data
    sample_data_focused[:, -1] = scaler.transform(sample_data_focused[:, -1].reshape(-1, 1)).flatten()
    sample_data_distracted[:, -1] = scaler.transform(sample_data_distracted[:, -1].reshape(-1, 1)).flatten()

    prediction_focused = model.predict(sample_data_focused)
    predicted_state_focused = label_encoder_state.inverse_transform(prediction_focused)[0]
    print(f"Sample focused data: {sample_data_focused[0]}")
    print(f"Predicted state: {predicted_state_focused}")

    prediction_distracted = model.predict(sample_data_distracted)
    predicted_state_distracted = label_encoder_state.inverse_transform(prediction_distracted)[0]
    print(f"Sample distracted data: {sample_data_distracted[0]}")
    print(f"Predicted state: {predicted_state_distracted}")

    print("FocusGuard project setup complete. Further development is required for real-time webcam integration and advanced features.")
