import flask, flask_login, os, pandas
from main.models import Tours
import main

def delete_tours():
    Tours.query.delete()
    main.db.session.commit()
    
def render_tour():
    delete_tours()
    global username
    username = "none"
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.name
    
    excel_path = os.path.abspath(__file__ + "/../../instance/tours.xlsx")
    excel_read = pandas.read_excel(
        io = excel_path,
        header = None,
        names = ["title", "date", "country", "price", "description"]  
        )

    if Tours.query.count() == 0:
        for tour in excel_read.iterrows():
            row_data = tour[1]
            tour = Tours(
                title = row_data["title"],
                date = row_data["date"],
                country = row_data["country"],
                price = row_data["price"],
                description = row_data["description"]
            )
            print(Tours.query.all())
            main.db.session.add(tour)
        main.db.session.commit()
        print(Tours.query.all())


    return flask.render_template(template_name_or_list= "tour.html", username = username, tours = Tours.query.all())