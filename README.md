# k8-workshop

A simple and fun Streamlit web application for rating "Raghu's Awesomeness" with Docker support.

## Overview

This is a clean and simple Streamlit web application that displays Raghu's image and allows users to rate his awesomeness on a scale of 0-10. The app provides funny and encouraging messages based on the rating submitted.

## Features

- **Image Display**: Shows Raghu's image from the static folder
- **Interactive Rating**: Slider-based rating from 0-10
- **Funny Messages**: Different humorous responses based on rating levels
- **Visual Feedback**: Star ratings and special effects (balloons for perfect 10!)
- **Responsive Design**: Clean Streamlit interface
- **Containerized**: Ready-to-deploy Docker container

## Project Structure

```
k8-workshop/
├── app.py              # Main Streamlit application
├── Dockerfile          # Docker container configuration
├── requirements.txt    # Python dependencies (just streamlit)
└── static/
    └── raghu.jpg      # Image file for display
```

## Technology Stack

- **Framework**: Streamlit (Python web framework)
- **Frontend**: Streamlit's built-in components
- **Containerization**: Docker

## Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd k8-workshop
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t k8-workshop .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 k8-workshop
   ```

3. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

### DockerHub Deployment

1. **Build and tag the image**
   ```bash
   docker build --platform linux/amd64 -t learnwithraghu/k8-workshop:latest .
   ```

2. **Login to DockerHub**
   ```bash
   docker login
   ```

3. **Push to DockerHub**
   ```bash
   docker push learnwithraghu/k8-workshop:latest
   ```

4. **Run from DockerHub (on any machine)**
   ```bash
   docker run -p 8501:8501 learnwithraghu/k8-workshop:latest
   ```

5. **Optional: Create additional tags**
   ```bash
   # Tag with version
   docker tag learnwithraghu/k8-workshop:latest learnwithraghu/k8-workshop:v1.0
   docker push learnwithraghu/k8-workshop:v1.0
   ```

### GitHub Codespaces / Cross-Platform Notes

If you encounter "exec format error" when running in GitHub Codespaces or other x86_64 environments:

```bash
# Always build with platform specification for compatibility
docker build --platform linux/amd64 -t learnwithraghu/k8-workshop:latest .

# Or build multi-platform image
docker buildx build --platform linux/amd64,linux/arm64 -t learnwithraghu/k8-workshop:latest --push .
```

## How It Works

1. **Image Display**: The app automatically displays `raghu.jpg` from the static folder
2. **Rating Interface**: Users interact with a slider to select a rating from 0-10
3. **Submit & Response**: Click the submit button to get a funny message based on the rating:
   - **Rating 10**: "🎉 Wow thanks a lot! Raghu is absolutely amazing! 🌟" (with balloons!)
   - **Rating 0**: "🤔 Hey what can Raghu do better? Everyone starts somewhere! 🌱"
   - **Other ratings**: Various encouraging and humorous messages
4. **Visual Feedback**: Star display showing the current rating

## Rating Messages

- **10**: Wow thanks a lot! + balloons animation
- **9**: Almost perfect! Raghu is fantastic!
- **8**: Great job Raghu! You're doing awesome!
- **7**: Pretty good! Raghu's got some solid skills!
- **6**: Not bad at all! Raghu's on the right track!
- **5**: Right in the middle! Raghu's got potential!
- **4**: Room for improvement! Keep going Raghu!
- **3**: Could be better! What can Raghu work on?
- **2**: Ouch! Raghu might need some practice!
- **1**: Yikes! Time for Raghu to level up!
- **0**: Hey what can Raghu do better? Everyone starts somewhere!

## Configuration

- **Port**: Application runs on port 8501 (Streamlit default)
- **Image Path**: `static/raghu.jpg` (automatically detected)
- **Rating Range**: 0-10 with default value of 5

## Dependencies

- `streamlit`: The only dependency needed!

## Troubleshooting

### Image Not Displaying
If the image doesn't show up:
1. Ensure `raghu.jpg` exists in the `static/` directory
2. Check that the image file is a valid image format (JPG, PNG, etc.)
3. Verify the image file permissions are readable
4. The app will show an error message if the image is not found

### Common Issues
- **Port conflicts**: If port 8501 is in use, Streamlit will automatically try the next available port
- **Missing dependencies**: Run `pip install streamlit` if you get import errors
- **Docker build issues**: Ensure Docker is running and you have sufficient disk space

### DockerHub Issues
- **Login problems**: Make sure you have a DockerHub account and are logged in with `docker login`
- **Push permission denied**: Ensure you're using the correct DockerHub username `learnwithraghu` in the image tag
- **Image not found**: Verify the image name `learnwithraghu/k8-workshop:latest` is correct when pulling
- **Large image size**: The image should be relatively small (~200-300MB) due to Python slim base
- **Architecture errors**: Use `--platform linux/amd64` when building for GitHub Codespaces compatibility

## Development Notes

- Streamlit automatically handles the web interface - no HTML/CSS needed
- The app uses Streamlit's built-in components for a clean, responsive design
- Images are served directly by Streamlit from the static folder
- The app includes fun visual effects like balloons for perfect ratings
- All styling and interactions are handled by Streamlit's framework

## Future Enhancements

- Add user authentication
- Implement rating persistence/database
- Add more visual effects and animations
- Include multiple images or image carousel
- Add comment system alongside ratings
- Export ratings to CSV or other formats
- Add admin dashboard for viewing all ratings