from flask import Flask, send_from_directory, render_template, request, redirect, url_for 
from waitress import serve
import os
from itertools import permutations 
from PIL import Image
import numpy as np

# https://wireframe.cc/pro/pp/558eb12f1461834 

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():    
    """Return the main page."""    
    return send_from_directory("static", "images.html")

@app.route("/generator", methods=["POST"])
def generate_cards(num_cards):    
    """ Use the ML model to make a prediction using the form inputs. """

    path = os.listdir(folder)
    bingo_spaces = range(0,25)
    perms = permutations(bingo_spaces)
    sel_perms = np.random.choice(perms, num_cards)
    labeled_imgs = {}
    img_paths = []

    for img in path:
        img_paths.append(img)

    for perm in sel_perms:
        labeled_imgs.keys() = perm

        for i in range(len(sel_perms)):
            # resize images to fit in template
            img_file = Image.open(path/img)
            img_file = img_file.resize((400,400)) # placeholder size for now
            # label images
            labeled_imgs[i] = img_file
            # place images in bingo template


    # Tell the browser to fetch the results page, passing along the prediction    
    return redirect(url_for("show_results", prediction=prediction, prob0=prob0, prob1=prob1))

@app.route("/confirmation")
def show_results():    
    """ Display the results page with the provided prediction """        

    
    # Return the results pge    
    return render_template("confirmation.html")
    
if __name__ == "__main__":    
    serve(app, host='0.0.0.0', port=5000)
