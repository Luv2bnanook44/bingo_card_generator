from flask import Flask, send_from_directory, render_template, request, redirect, url_for 
from waitress import serve
import os
from itertools import product 
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
def generate_cards():    
    """ Use provided images to generate different bingo cards from matplotlib saved in pdf form """

    board_title = request.form.get('word')
    folder = request.form.get('image_folder')
    destination_path = request.form.get('destination_path')
    path = os.listdir(folder)
    coordinates = list(product(range(5), range(5)))
    num_cards = request.form.get('num_cards')
    plt.switch_backend('Agg') 

    for i in range(int(num_cards)):
        fig, ax = plt.subplots(ncols=5, nrows=5, figsize=(15,15)) # may need to adjust plot size
        perm = coordinates
        np.random.shuffle(perm)
        print(i)
        
        for j, pair in enumerate(perm):
            # resize images to fit in template
            
            img_file = Image.open(folder+'/'+path[j])
            print(path[i])
            img_file = img_file.resize((400,400)) # placeholder size for now
            # place images in bingo template
            ax[pair[0]][pair[1]].imshow(img_file)
            
            ax[pair[0]][pair[1]].set_xticks([])
            ax[pair[0]][pair[1]].set_yticks([])
            ax[pair[0]][pair[1]].set_xticklabels([])
            ax[pair[0]][pair[1]].set_yticklabels([])

        fig.suptitle(board_title.upper(), size=100)
        fig.tight_layout()
        
        fig.savefig(destination_path+f'/board{i}', format='pdf')

    return redirect(url_for("confirmation", destination_path=destination_path))

@app.route("/confirmation")
def confirmation():    
    """ Confirm that Bingo Cards were created. """        
    destination_path = request.args.get('destination_path')
    # Return the results page    
    return render_template("confirmation.html", destination_path=destination_path)
    
if __name__ == "__main__":    
    serve(app, host='0.0.0.0', port=5000)