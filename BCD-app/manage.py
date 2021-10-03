import argparse


# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("comand", help="pass comand to take action")

# Read arguments from command line
args = parser.parse_args()

if args.comand:
    if args.comand == "runserver":
        try:
            import os
            os.system('python app.py')
        except:
            print("flask app stopped successfully")
    elif args.comand == "migrate":
        from app import db
        db.create_all()
