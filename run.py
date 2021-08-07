from app.main import app
import multiprocessing
from app import main 

if __name__ == "__main__":
    app.run(debug=True)

plot_graph = multiprocessing.Process(target=main.generate_cards,args=())
plot_graph.start()
