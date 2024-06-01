from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    reaction_level = 5  # Default rating
    show_image = False  # Initially don't show image
    message = ""

    if request.method == 'POST':
        reaction_level = int(request.form.get('reaction_level', 5))
        
        if reaction_level == 10:
            confirm_best = request.form.get('confirm_best')
            if confirm_best == 'on':  # Checkbox is checked
                show_image = True
                message = "💯 Alright, alright! We get it, Raghu's your hero! 🥳"
            else:
                message = "🤔 Maybe dial it back a notch? 😉"
        elif reaction_level >= 5:
            message = "👍 Raghu's got some moves, but can he moonwalk? 🤔"
        else:
            message = "😂 Did Raghu trip over his shoelaces again? 🤪"

    # Load and rotate image (only if needed)
    img_data = None
    if show_image:
        img = Image.open("static/raghu.jpg")
        img = img.rotate(250, expand=True)
        img_data = img

    return render_template('index.html', reaction_level=reaction_level, show_image=show_image, message=message, img_data=img_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)  # For Docker
