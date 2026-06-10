from flask_frozen import Freezer
from app import app

# Configure Freezer
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'dist'

freezer = Freezer(app)

if __name__ == '__main__':
    print("Freezing application...")
    freezer.freeze()
    print("Static website successfully compiled to 'dist/' directory!")
