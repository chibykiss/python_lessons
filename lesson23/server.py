from flask import Flask, render_template, request
from weather import get_weather 
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('location')
    # Check for empty input or whitespace
    if not bool(city.strip()):
        city = 'Lagos'
        # print('You must enter a valid city name.')
        # exit()
    weather_data = get_weather(city)

    # Check if the API returned an error
    if not weather_data['cod'] == 200:
        return render_template('not_found.html')
    
    return render_template(
        'weather.html', 
         title=weather_data['name'],
         status = weather_data['weather'][0]['description'].capitalize(),
         temperature = f"{weather_data['main']['temp']:.1f}",
         feels_like = f"{weather_data['main']['feels_like']:.1f}"
        )

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=7070)