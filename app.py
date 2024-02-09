from flask import Flask,request,render_template
import pickle as pkl

app = Flask(__name__)

ohe = pkl.load(open("ohe.pkl","rb"))
locations = ohe.transformers_[0][1].categories_[0]

model = pkl.load(open("model.pkl","rb"))

global predicted
predicted = ""

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        loc = request.form.get("location")
        bath = request.form.get("bath")
        bed = request.form.get("bed")
        area = request.form.get("area")
        pre = r"Rs : " +str(model.predict([
            [loc,bath,bed,area]
        ])[0]*100000)
        return render_template("index.html",locations=sorted(locations),predict=pre)
    return render_template("index.html",locations=sorted(locations),
                           predict=predicted)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__=='__main__':
    app.run(debug=True)