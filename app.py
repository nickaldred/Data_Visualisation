from flask import Flask, render_template, redirect
import csv
import itertools
from operator import itemgetter
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/basic')
def display_data():
        with open('static/data/Kaggle_TwitterUSAirlineSentiment.csv', encoding='utf-8-sig') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            first_line = True
            tweetData = []

            for row in itertools.islice(data, 41):
                if not first_line:
                    tweetData.append({
                        "id": row[0],
                        "airline_sentiment": row[1],
                        "airline_sentiment_confidence": row[2],
                        "negative_reason": row[3],
                        "airline": row[4],
                        "name": row[5],
                        "text": row[6],
                        "tweet_created": row[7],
                        "tweet_location": row[8]
                    })

                else:
                    first_line = False


        tweetData.sort(key = itemgetter('airline_sentiment_confidence'))

        return render_template("basic.html", tweetData=tweetData)



@app.route('/advanced')
def display_data_d3():
    return render_template("advanced.html")


@app.route('/creative')
def visualise_data_d3():
    return render_template("creative2.html")

@app.route('/portfolio')
def portfolio():
    return redirect("https://www.nickaldred.com/")


#app.run(debug=True, host='0.0.0.0', port=81)
