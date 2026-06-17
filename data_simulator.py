
import numpy as np
import pandas as pd
import random

def simulate_face_data(num_samples=1000, states=["focused", "distracted"]):
    data = []
    for _ in range(num_samples):
        state = random.choice(states)
        
        # Simulate facial expression (e.g., 'neutral', 'frown', 'smile')
        if state == "focused":
            expression = random.choice(["neutral", "slight_smile"])
        else:
            expression = random.choice(["frown", "bored", "looking_away"])

        # Simulate gaze direction (e.g., 'center', 'left', 'right', 'up', 'down')
        if state == "focused":
            gaze_direction = random.choice(["center", "slight_left", "slight_right"])
        else:
            gaze_direction = random.choice(["left", "right", "up", "down", "center"])

        # Simulate head pose (e.g., 'straight', 'tilted_left', 'tilted_right', 'forward', 'back')
        if state == "focused":
            head_pose = random.choice(["straight", "slight_tilt"])
        else:
            head_pose = random.choice(["tilted_left", "tilted_right", "forward", "back"])

        # Simulate attention score (0-100)
        if state == "focused":
            attention_score = random.gauss(85, 10) # High attention
        else:
            attention_score = random.gauss(30, 15) # Low attention
        attention_score = max(0, min(100, attention_score))

        data.append({
            "expression": expression,
            "gaze_direction": gaze_direction,
            "head_pose": head_pose,
            "attention_score": attention_score,
            "state": state
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = simulate_face_data(num_samples=2000)
    df.to_csv("face_data.csv", index=False)
    print("Simulated face_data.csv created with 2000 samples.")
    print(df.head())
