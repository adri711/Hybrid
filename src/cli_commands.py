from src import application,db

@application.cli.command("setup_db")
def setupdb():
    # Deleting the database if it exists then recreating it
	db.drop_all()
	db.create_all()
	
	print("The database has been initialized.")