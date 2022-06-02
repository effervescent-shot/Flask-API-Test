from application import create_app
import os

# run server
if __name__ == '__main__':

    app = create_app()
    app.run(debug=True)
   



