from website import create_app, db
from flask import render_template

def create_all():
    """ Create all db tables. Meant to be called from command line."""
    with app.app_context():
        db.create_all()

app = create_app()
create_all()


if __name__ == '__main__':
    app.run(debug=True)
