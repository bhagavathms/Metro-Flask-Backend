from flask import Flask,jsonify,request
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with
from flas_sqlalchemy import SQLAlchemy
import csv
import route

app = Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://database.db'
db=SQLAlchemy(app)

#For Creating Database and tables
class AllStationEntry(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Line1=db.Column(db.String(20),nullable=False)
    Line2=db.Column(db.String(20),nullable=True)
    Line2=db.Column(db.String(20),nullable=True)

class YellowLine(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Inter1=db.Column(db.String(20),nullable=True)
    Inter2=db.Column(db.String(20),nullable=True)

class RedLine(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Inter1=db.Column(db.String(20),nullable=True)
    Inter2=db.Column(db.String(20),nullable=True)

class VioletLine(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Inter1=db.Column(db.String(20),nullable=True)
    Inter2=db.Column(db.String(20),nullable=True)

class BlueLine(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Inter=db.Column(db.String(20),nullable=True)

class GreenLine(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Inter=db.Column(db.String(20),nullable=True)

class PinkLine(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Inter=db.Column(db.String(20),nullable=True)

class MagentaLine(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Inter=db.Column(db.String(20),nullable=True)

class OrangeLine(db.Model):
    SId=db.Column(db.Integer,primary_key=True)
    Sname=db.Column(db.String(50),nullable=False)
    Inter=db.Column(db.String(20),nullable=True)

class CostOfTravel(db.Model):
    minst=db.Column(db.Integer,nullable=False)
    maxst=db.Column(db.Integer,nullable=False)
    cost=db.Column(db.Integer,nullable=False)

#def __repe__(self):
#   return f"route(name={Sname},Line={Line1})"

db.create_all()

#Error Handling 
def not_found(name):
    if name not in db:
        abort(404,message="Station Not Found")

#Getting Request from extenal source
class route(Resource):
    def get(self,source,destination):
        not_found(source)
        not_found(destination)
        out=route.find_short(source,destiantion)
        return out
        

    #Creating Database in SQLAlchemy
    #As Database is already created so this function is commented
    '''
    def post(self):
        #All Stations
        with open('/Project Metro/Data entries/All_Stations.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=AllStationEntry(SId=args[Sno],Sname=args[Name],Line1=args[Line1],Line2=args[Line2],Line3=args[Line3])
            db.session.add(inp)
            file.close();

        #Yellow Line
        with open('/Project Metro/Data entries/Yellow Line.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=YellowLine(SId=args[Sno],Sname=args[Name],Inter1=args[Interchange1],Inter2=args[Interchange2])
            db.session.add(inp)
            file.close();

        #Blue Line
        with open('/Project Metro/Data entries/Blue Line.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=BlueLine(SId=args[Sno],Sname=args[Name],Inter=args[Interchange])
            db.session.add(inp)
            file.close();

        #RedLine
        with open('/Project Metro/Data entries/Red Line.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=RedLine(SId=args[Sno],Sname=args[Name],Inter1=args[Interchange1],Inter2=args[Interchange2])
            db.session.add(inp)
            file.close();

        #Green Line
        with open('/Project Metro/Data entries/Green Line.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=BlueLine(SId=args[Sno],Sname=args[Name],Inter=args[Interchange])
            db.session.add(inp)
            file.close();

        #Violet Line
        with open('/Project Metro/Data entries/Voilet Line.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=VoiletLine(SId=args[Sno],Sname=args[Name],Inter1=args[Interchange1],Inter2=args[Interchange2])
            db.session.add(inp)
            file.close();

        #Pink Line
        with open('/Project Metro/Data entries/Pink Line.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=PinkLine(SId=args[Sno],Sname=args[Name],Inter=args[Interchange])
            db.session.add(inp)
            file.close();

        #Magenta Line
        with open('/Project Metro/Data entries/Magenta Line.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=MagentaLine(SId=args[Sno],Sname=args[Name],Inter=args[Interchange])
            db.session.add(inp)
            file.close();

        #Orange Line
        with open('/Project Metro/Data entries/Orange Line.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=OrangeLine(SId=args[Sno],Sname=args[Name],Inter=args[Interchange])
            db.session.add(inp)
            file.close(); 

        #cost
        with open('/Project Metro/Data entries/cost.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            args=route_put_args.parse_args()
            inp=CostOfTravel(minst=args[minstation],maxst=args[maxstation],cost=args[fare])
            db.session.add(inp)
            file.close();

        db.commit()
        return 201
        '''


api.add_resource(route,"/route/<string:source><String:destination>")

if __name__=="__main__":
    app.run(debug=True )


