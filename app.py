from flask import Flask,render_template,request
import csv,os


app = Flask(__name__)


#Home Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add-students.html')


#Add Students
@app.route('/add_details',methods=['POST'])
def add_details():
    if request.method == 'POST':
        flag=False
        student_id = request.form['stud_id']
        student_name = request.form['name']
        gender = request.form['optradio']
        date = request.form['date']
        city = request.form['city']
        state = request.form['state']
        email = request.form['email']
        degree = request.form['degree']
        stream = request.form['stream']

        file_exists = os.path.isfile('sample.csv')

        with open('sample.csv','a',newline='') as f:
            
            fieldnames = ['Student_ID','Student_Name','Gender','Date','City','State','Email','Qualification','Stream']
            writetofile = csv.DictWriter(f,fieldnames=fieldnames)
            if not file_exists:
                writetofile.writeheader()   
            
            writetofile.writerow({'Student_ID':student_id,'Student_Name':student_name,
                                    'Gender':gender,'Date':date,'City':city,
                                    'State':state,'Email':email,'Qualification':degree,
                                    'Stream':stream
                                })
            
            flag=True
    if (flag):
        return render_template('add-students.html',student_status="Success")

    return render_template('add-students.html',student_status='Error')


#Search Details
@app.route('/find')
def find():
    return render_template('search.html')



@app.route('/search',methods=['POST'])
def search():
    if request.method == 'POST':
        results=[]
        student_id = request.form['stud_id']
        with open('sample.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if student_id == row[0]:
                    results.append({
                        "Student_ID": row[0],
                        "Student_Name": row[1],
                        "Gender": row[2],
                        "Date":row[3],
                        "City":row[4],
                        "State":row[5],
                        "Email":row[6],
                        "Qualification":row[7],
                        "Stream":row[8]

                        })

    return render_template("search.html", results=results)




#Display Details
@app.route('/show')
def show():
    return render_template('display.html')


@app.route('/display',methods=['POST'])
def display():
    if request.method == 'POST':
        results=[]
        rows=[]
        file_exists = os.path.exists('../sample.csv')
        if(file_exists):
            with open('sample.csv', 'r') as f:
                reader = csv.reader(f, delimiter=',')
                fields = next(reader)
                for row in reader: 
                    rows.append(row) 
                for row in rows:
                        results.append({
                            "Student_ID": row[0],
                            "Student_Name": row[1],
                            "Gender": row[2],
                            "Date":row[3],
                            "City":row[4],
                            "State":row[5],
                            "Email":row[6],
                            "Qualification":row[7],
                            "Stream":row[8]
                            })
        else:
            results.append({
                            "Student_ID": "No",
                            "Student_Name": "-",
                            "Gender": "-",
                            "Date":"Data",
                            "City":"/",
                            "State":"Record",
                            "Email":"-",
                            "Qualification":"-",
                            "Stream":"Found"
                            })


    return render_template("display.html", results=results)
    


if __name__ == "__main__":
    app.run(debug=True)
