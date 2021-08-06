from flask import Flask, send_from_directory, render_template, request, redirect, url_for 
from waitress import serve
import os
from itertools import permutations, product 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# https://wireframe.cc/pro/pp/558eb12f1461834 

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():    
    """Return the main page."""    
    return send_from_directory("static", "images.html")

@app.route("/generator", methods=["POST"])
def generate_cards(num_cards, word="BINGO"):    
    """ Use provided images to generate different bingo cards from matplotlib saved in pdf form """

    path = os.listdir(folder)
    coordinates = list(product('01234', '01234'))
    sel_perms = np.random.choice(coordinates, num_cards)
    labeled_imgs = {}
    img_paths = []

    for img in path:
        img_paths.append(img)

    for perm in sel_perms:
        board_num = 0
        labeled_imgs.keys() = coordinates
        fig, ax = plt.subplots(ncols=5, nrows=5) # may need to adjust plot size

        for pair in coordinates:
            # resize images to fit in template
            img_file = Image.open(path/img)
            img_file = img_file.resize((400,400)) # placeholder size for now
            # label images
            labeled_imgs[pair] = img_file
            # place images in bingo template
            ax[pair[0]][pair[1]].imshow(img_file)

        ax.set_title(word, size=50)
        
        plt.savefig(f'board{board_num}', format='pdf')
        board_num += 1
        


    # Tell the browser to fetch the results page, passing along the prediction    
    return redirect(url_for("show_results", prediction=prediction, prob0=prob0, prob1=prob1))

@app.route("/confirmation")
def show_results():    
    """ Display the results page with the provided prediction """        

    
    # Return the results pge    
    return render_template("confirmation.html")
    
if __name__ == "__main__":    
    serve(app, host='0.0.0.0', port=5000)
