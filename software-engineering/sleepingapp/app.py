from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


df_data = pd.DataFrame(columns=['date', 'hours'])


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sleep', methods=['GET', 'POST'])
def sleep():
    if request.method == 'POST':
        date = request.form['date']
        hours = request.form['hours']
        df_data.loc[len(df_data)] = [date, hours]
        return redirect('/sleep')
    return render_template('sleep.html', sleep_data=df_data)

@app.route('/chart')
def chart():
    plt.plot(df_data['date'], df_data['hours'])
    plt.xlabel('Date')
    plt.ylabel('Hours of Sleep')
    plt.title('Sleep Tracker')
    plt.xticks(rotation=45)
    plt.tight_layout()
    chart = plt.gcf()
    return chart

