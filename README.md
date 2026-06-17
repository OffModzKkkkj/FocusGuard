# FocusGuard: Real-time Cognitive Distraction Detection System

## Overview

FocusGuard is a computer vision-based Artificial Intelligence system designed to detect cognitive distraction in real-time using a standard webcam. By monitoring facial expressions, gaze direction, and head posture, FocusGuard aims to help users maintain focus during work or study sessions, proactively identifying when their attention wanes.

## Problem Statement

Maintaining sustained focus is a significant challenge in modern work and study environments, often leading to decreased productivity and increased errors. Traditional methods of tracking focus rely on self-reporting or intrusive monitoring software. FocusGuard offers a non-intrusive, privacy-preserving solution that analyzes subtle physical cues to infer cognitive state.

## Solution

FocusGuard utilizes a Machine Learning model to analyze visual data captured by a webcam. The system extracts key features related to the user's physical state and uses them to predict whether the user is focused or distracted.

1.  **Monitor Physical Cues**: Analyze facial expressions, gaze direction, and head posture.
2.  **Detect Distraction**: Identify patterns indicative of cognitive distraction.
3.  **Provide Real-time Alerts**: Notify the user when their focus drops below a certain threshold.
4.  **Preserve Privacy**: Process all visual data locally, ensuring that no images or videos are transmitted or stored.

## Technical Approach & AI Model

### Data Collection (Simulated)

For this proof-of-concept, visual data is simulated using `data_simulator.py`. This script generates synthetic datasets that mimic the physical cues associated with focused and distracted states. Key features simulated include:

*   **Facial Expression**: e.g., neutral, slight smile (focused) vs. frown, bored, looking away (distracted).
*   **Gaze Direction**: e.g., center, slight left/right (focused) vs. left, right, up, down (distracted).
*   **Head Pose**: e.g., straight, slight tilt (focused) vs. tilted left/right, forward, back (distracted).
*   **Attention Score**: A simulated metric representing the overall level of attention.

### Feature Engineering

The simulated categorical features (expression, gaze, head pose) are encoded into numerical values using Label Encoding. The numerical feature (attention score) is standardized using StandardScaler to ensure that all features contribute equally to the model.

### Machine Learning Model

The core of FocusGuard is a **Random Forest Classifier**. Random Forests are robust, versatile, and handle both categorical and numerical data well, making them suitable for this classification task.

*   **Input**: Encoded and standardized features representing physical cues.
*   **Model**: An ensemble of decision trees that vote on the final classification.
*   **Output**: A prediction of the user's state: "focused" or "distracted".

## Installation and Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/OffModzKkkkj/FocusGuard.git
    cd FocusGuard
    ```
2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Generate Simulated Data

Run the `data_simulator.py` script to create a synthetic dataset for training and testing:

```bash
python data_simulator.py
```

This will generate a `face_data.csv` file in the project directory.

### 2. Train and Evaluate the Model

Run the `main.py` script to load the simulated data, train the Random Forest model, evaluate its performance, and make sample predictions:

```bash
python main.py
```

## Future Enhancements

*   **Real-time Webcam Integration**: Implement OpenCV to capture and process live video feeds.
*   **Advanced Computer Vision Models**: Utilize deep learning models (e.g., CNNs) for more accurate feature extraction from images.
*   **Personalized Thresholds**: Allow users to customize the sensitivity of the distraction detection.
*   **Integration with Productivity Tools**: Connect with applications to automatically pause notifications or suggest breaks when distraction is detected.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

[1] Simulated Visual Data: Generated via `data_simulator.py`
[2] Random Forest Classifier: [Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5-32.](https://link.springer.com/article/10.1023/A:1010933404324)
