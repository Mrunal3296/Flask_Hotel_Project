from flask import *

import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "hotelmrunal"
    )

cursor = db.cursor()

app =Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    name = ""
    
    mylist = ['']
    

    return render_template("About.html",username=name,mylist=mylist)

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/price")
def price():
    return render_template("price.html")


@app.route("/allusers")
def allusers():
    cursor.execute("select * from hotel")
    data = cursor.fetchall()
    return render_template("allusers.html",userdata=data)

@app.route("/create",methods=["POST"])
def create():
    name = request.form.get('name')
    contact =request.form.get('contact')
    address=request.form.get('address')
    insq = "insert into hotel(name,contact,address) values('{}','{}','{}')".format(name,contact,address)
    
    try : 
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in Query"
    
@app.route("/edit")
def edit():
    id = request.args.get('id')
    
    selq = "select * from hotel where id = {}".format(id)
    cursor.execute(selq)
    data = cursor.fetchone()
    return render_template("edit.html",row=data)

@app.route("/update",methods = ["POST"])
def update():
    name = request.form.get('name')
    contact = request.form.get('contact')
    address = request.form.get('address')
    uid = request.form.get('uid')
    insq = "update hotel set name ='{}',contact='{}',address='{}'where id={}".format(name,contact,address,uid)
    
    try: 
         cursor.execute(insq)
         db.commit()
         return redirect(url_for("allusers")) 
    except:
         db.rollback()
         return "Error in Query" 
       
@app.route("/delete")
def delete():
    
    id = request.args.get('id')
    
    delq = "delete from hotel where id = {}".format(id)
    try: 
         cursor.execute(delq)
         db.commit()
         return redirect(url_for("allusers")) 
    except:
         db.rollback()
         return "Error in Query"
     
@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/getdata",methods=["POST"])
def getdata():
    id = request.form.get('id')
    selq = "select * from hotel where id = {}".format(id)
    
    cursor.execute(selq)
    data = cursor.fetchone()
    return render_template("search.html",row=data)


if __name__=='__main__':
    app.run(debug=True)
    