from flask import Flask, send_from_directory, render_template, request, redirect, url_for 
import os
# from waitress import serve
from itertools import product 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# https://wireframe.cc/pro/pp/558eb12f1461834 

app = Flask(__name__)

@app.route("/")
def index():    
    """Return the main page."""    
    return render_template("images.html")

@app.route("/generator", methods=["POST"])
def generate_cards():    
    """ Use provided images to generate different bingo cards from matplotlib saved in pdf form """
    ncols = int(request.form.get('ncols'))
    nrows = int(request.form.get('nrows'))
    board_title = request.form.get('word')
    folder = request.form.get('image_folder')
    destination_path = request.form.get('destination_path')
    path = os.listdir(folder)
    coordinates = list(product(range(ncols), range(nrows)))
    num_cards = request.form.get('num_cards')
    plt.switch_backend('Agg') 

# check if there are the correct number of images in the directory
    if len(path) < (nrows*ncols):
        message = f"According to our records, you have {len(path)} images in your folder, but you \
                    need {nrows*ncols} images to make a {nrows} by {ncols} bingo board."

        return redirect(url_for("confirmation", message=message))

    else:
        message = f"Your cards should be saved in {destination_path}!"

        for i in range(int(num_cards)):

            fig, ax = plt.subplots(ncols=ncols, nrows=nrows, figsize=(15,15)) # may need to adjust plot size
            perm = coordinates
            np.random.shuffle(perm)
            
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

            fig.suptitle(board_title.upper(), size=130)
            fig.tight_layout()
            
            fig.savefig(destination_path+f'/board{i}', format='pdf')

        return redirect(url_for("confirmation", message=message))

@app.route("/confirmation")
def confirmation():    
    """ Confirm that Bingo Cards were created. """  
    message = request.args.get('message')
    # Return the results page    
    return render_template("confirmation.html", message=message)
    
# if __name__ == "__main__":    
#     serve(app, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # serve(app, host='0.0.0.0', port=5000)
    app.run(debug=True)