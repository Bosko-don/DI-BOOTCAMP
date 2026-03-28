#!/usr/bin/env python3
"""
Weather App - Complete Single File Solution
Features:
- Current weather data
- Wind information
- Sunrise/sunset times
- 5-day forecast with humidity
- Air pollution data
- GUI bar chart for humidity forecast (Bonus)
"""

import sys
import random
from datetime import datetime, timedelta

# Try to import optional modules
try:
    import pytz
    PYTZ_AVAILABLE = True
except ImportError:
    PYTZ_AVAILABLE = False
    print("Note: pytz not installed. Using basic timezone handling.")

try:
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Note: matplotlib not installed. GUI features will be disabled.")

try:
    import tkinter as tk
    from tkinter import ttk, messagebox
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    print("Note: tkinter not available. GUI mode will be disabled.")

try:
    from pyowm import OWM
    from pyowm.utils import timestamps
    PYOWM_AVAILABLE = True
except ImportError:
    PYOWM_AVAILABLE = False
    print("Note: pyowm not installed. Running in MOCK DATA mode.")


class MockWeatherData:
    """Mock weather data for testing without API key."""

    def __init__(self):
        self.cities = {
            "paris": {"id": 2988507, "lat": 48.8566, "lon": 2.3522, "country": "FR"},
            "london": {"id": 2643743, "lat": 51.5074, "lon": -0.1278, "country": "GB"},
            "new york": {"id": 5128581, "lat": 40.7128, "lon": -74.0060, "country": "US"},
            "tokyo": {"id": 1850147, "lat": 35.6762, "lon": 139.6503, "country": "JP"},
            "sydney": {"id": 2147714, "lat": -33.8688, "lon": 151.2093, "country": "AU"},
            "los angeles": {"id": 5368361, "lat": 34.0522, "lon": -118.2437, "country": "US"},
        }

    def get_weather_at_place(self, city):
        """Generate mock current weather data."""
        city_key = city.lower().split(',')[0].strip()
        if city_key not in self.cities:
            temp = random.randint(5, 35)
            humidity = random.randint(30, 90)
            wind_speed = random.randint(1, 20)
        else:
            base_temps = {"paris": 15, "london": 12, "new york": 18, "tokyo": 22, "sydney": 25, "los angeles": 24}
            temp = base_temps.get(city_key, 20) + random.randint(-5, 5)
            humidity = random.randint(40, 80)
            wind_speed = random.randint(2, 15)

        return {
            "temperature": temp,
            "humidity": humidity,
            "status": random.choice(["Clear", "Clouds", "Rain", "Sunny"]),
            "detailed_status": random.choice(["clear sky", "few clouds", "light rain", "scattered clouds"]),
            "wind_speed": wind_speed,
            "wind_direction": random.randint(0, 360),
            "pressure": random.randint(1000, 1030),
            "clouds": random.randint(0, 100),
            "rain": {"1h": random.randint(0, 5)} if random.random() > 0.7 else {},
            "snow": {}
        }

    def get_sunrise_sunset(self, city):
        """Generate mock sunrise/sunset times."""
        now = datetime.now()
        sunrise = now.replace(hour=6, minute=30, second=0) + timedelta(minutes=random.randint(-30, 30))
        sunset = now.replace(hour=19, minute=45, second=0) + timedelta(minutes=random.randint(-30, 30))
        return {"sunrise": sunrise, "sunset": sunset}

    def get_forecast(self, city):
        """Generate mock 5-day forecast data."""
        forecast = []
        now = datetime.now()
        base_temps = {"paris": 15, "london": 12, "new york": 18, "tokyo": 22, "sydney": 25, "los angeles": 24}
        city_key = city.lower().split(',')[0].strip()
        base_temp = base_temps.get(city_key, 20)

        for i in range(5):
            date = now + timedelta(days=i)
            forecast.append({
                "date": date,
                "temp_max": base_temp + random.randint(0, 5),
                "temp_min": base_temp - random.randint(3, 8),
                "humidity": random.randint(40, 85),
                "status": random.choice(["Clear", "Clouds", "Rain", "Sunny", "Partly cloudy"]),
                "wind_speed": random.randint(2, 20)
            })
        return forecast

    def get_air_pollution(self, city):
        """Generate mock air pollution data."""
        return {
            "aqi": random.randint(1, 5),
            "co": random.uniform(200, 500),
            "no": random.uniform(0, 50),
            "no2": random.uniform(10, 100),
            "o3": random.uniform(20, 150),
            "so2": random.uniform(1, 50),
            "pm2_5": random.uniform(5, 50),
            "pm10": random.uniform(10, 80),
            "nh3": random.uniform(0, 20)
        }

    def get_city_id(self, city_name):
        """Get city ID from name."""
        city_key = city_name.lower().strip()
        if city_key in self.cities:
            return self.cities[city_key]["id"]
        return random.randint(1000000, 9999999)


class WeatherApp:
    """Main Weather Application class."""

    def __init__(self, api_key=None):
        """Initialize the Weather App."""
        self.api_key = api_key
        self.use_mock = not PYOWM_AVAILABLE or not api_key

        if self.use_mock:
            self.mock_data = MockWeatherData()
            print("Running in MOCK DATA mode (no API key required).")
        else:
            try:
                self.owm = OWM(api_key)
                self.weather_mgr = self.owm.weather_manager()
                print("Connected to OpenWeatherMap API.")
            except Exception as e:
                print(f"Error connecting to API: {e}")
                print("Falling back to MOCK DATA mode.")
                self.use_mock = True
                self.mock_data = MockWeatherData()

    def get_current_weather(self, location):
        """Get current weather for a location."""
        if self.use_mock:
            return self.mock_data.get_weather_at_place(location)
        else:
            try:
                observation = self.weather_mgr.weather_at_place(location)
                weather = observation.weather
                return {
                    "temperature": weather.temperature("celsius")["temp"],
                    "humidity": weather.humidity,
                    "status": weather.status,
                    "detailed_status": weather.detailed_status,
                    "wind_speed": weather.wind()["speed"] if weather.wind() else 0,
                    "wind_direction": weather.wind().get("deg", 0) if weather.wind() else 0,
                    "pressure": weather.pressure["press"] if weather.pressure else 1013,
                    "clouds": weather.clouds,
                    "rain": weather.rain,
                    "snow": weather.snow
                }
            except Exception as e:
                print(f"Error fetching weather: {e}")
                return None

    def get_wind_info(self, location):
        """Get detailed wind information."""
        weather = self.get_current_weather(location)
        if weather:
            return {
                "speed": weather["wind_speed"],
                "direction": weather["wind_direction"],
                "gust": weather.get("wind_gust", 0)
            }
        return None

    def get_sun_times(self, location):
        """Get sunrise and sunset times."""
        if self.use_mock:
            return self.mock_data.get_sunrise_sunset(location)
        else:
            try:
                observation = self.weather_mgr.weather_at_place(location)
                weather = observation.weather
                sunrise = datetime.fromtimestamp(weather.sunrise_time())
                sunset = datetime.fromtimestamp(weather.sunset_time())
                return {"sunrise": sunrise, "sunset": sunset}
            except Exception as e:
                print(f"Error fetching sun times: {e}")
                return None

    def get_city_id(self, location):
        """Get city ID for a location."""
        if self.use_mock:
            return self.mock_data.get_city_id(location)
        else:
            try:
                geo_mgr = self.owm.geocoding_manager()
                locations = geo_mgr.geocode(location, limit=1)
                if locations:
                    return locations[0].id
                return None
            except Exception as e:
                print(f"Error fetching city ID: {e}")
                return None

    def get_forecast(self, location, interval='3h'):
        """Get weather forecast."""
        if self.use_mock:
            return self.mock_data.get_forecast(location)
        else:
            try:
                forecast = self.weather_mgr.forecast_at_place(location, interval)
                weathers = forecast.forecast.weathers
                result = []
                for weather in weathers[:5]:
                    result.append({
                        "date": datetime.fromtimestamp(weather.reference_time()),
                        "temp_max": weather.temperature("celsius")["temp_max"],
                        "temp_min": weather.temperature("celsius")["temp_min"],
                        "humidity": weather.humidity,
                        "status": weather.status,
                        "wind_speed": weather.wind()["speed"] if weather.wind() else 0
                    })
                return result
            except Exception as e:
                print(f"Error fetching forecast: {e}")
                return None

    def get_air_pollution(self, location):
        """Get air pollution data."""
        if self.use_mock:
            return self.mock_data.get_air_pollution(location)
        else:
            try:
                geo_mgr = self.owm.geocoding_manager()
                locations = geo_mgr.geocode(location, limit=1)
                if not locations:
                    return None
                lat = locations[0].lat
                lon = locations[0].lon
                pollution_mgr = self.owm.airpollution_manager()
                air_status = pollution_mgr.air_quality_at_coords(lat, lon)
                return {
                    "aqi": air_status.aqi,
                    "co": air_status.co,
                    "no": air_status.no,
                    "no2": air_status.no2,
                    "o3": air_status.o3,
                    "so2": air_status.so2,
                    "pm2_5": air_status.pm2_5,
                    "pm10": air_status.pm10,
                    "nh3": air_status.nh3
                }
            except Exception as e:
                print(f"Error fetching air pollution: {e}")
                return None

    def display_weather(self, location):
        """Display current weather in user-friendly format."""
        print("\n" + "=" * 50)
        print(f"WEATHER REPORT FOR: {location.upper()}")
        print("=" * 50)
        
        weather = self.get_current_weather(location)
        if weather:
            print(f"\nCurrent Conditions:")
            print(f"  Temperature: {weather['temperature']:.1f}C")
            print(f"  Feels like: {weather['status']}")
            print(f"  Description: {weather['detailed_status']}")
            print(f"  Humidity: {weather['humidity']}%")
            print(f"  Cloud cover: {weather['clouds']}%")
            print(f"  Pressure: {weather['pressure']} hPa")
            if weather['rain']:
                print(f"  Rain (1h): {weather['rain'].get('1h', 0)} mm")
        
        wind = self.get_wind_info(location)
        if wind:
            print(f"\nWind Information:")
            print(f"  Speed: {wind['speed']} m/s")
            print(f"  Direction: {wind['direction']} degrees")
        
        sun_times = self.get_sun_times(location)
        if sun_times:
            print(f"\nSun Times:")
            print(f"  Sunrise: {sun_times['sunrise'].strftime('%H:%M')}")
            print(f"  Sunset: {sun_times['sunset'].strftime('%H:%M')}")
        
        city_id = self.get_city_id(location)
        if city_id:
            print(f"\nCity ID: {city_id}")
        
        print("=" * 50)

    def display_forecast(self, location):
        """Display 5-day forecast."""
        print("\n" + "=" * 50)
        print(f"5-DAY FORECAST FOR: {location.upper()}")
        print("=" * 50)
        
        forecast = self.get_forecast(location)
        if forecast:
            for day in forecast:
                date_str = day['date'].strftime('%A, %B %d')
                print(f"\n{date_str}:")
                print(f"  Max: {day['temp_max']:.1f}C | Min: {day['temp_min']:.1f}C")
                print(f"  Humidity: {day['humidity']}%")
                print(f"  Conditions: {day['status']}")
                print(f"  Wind: {day['wind_speed']} m/s")
        else:
            print("Unable to retrieve forecast data.")
        
        print("=" * 50)

    def display_air_pollution(self, location):
        """Display air pollution data."""
        print("\n" + "=" * 50)
        print(f"AIR QUALITY FOR: {location.upper()}")
        print("=" * 50)
        
        pollution = self.get_air_pollution(location)
        if pollution:
            aqi_labels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}
            aqi = pollution['aqi']
            print(f"\nAir Quality Index: {aqi} ({aqi_labels.get(aqi, 'Unknown')})")
            print(f"\nPollutant Levels:")
            print(f"  CO: {pollution['co']:.2f} ug/m3")
            print(f"  NO: {pollution['no']:.2f} ug/m3")
            print(f"  NO2: {pollution['no2']:.2f} ug/m3")
            print(f"  O3: {pollution['o3']:.2f} ug/m3")
            print(f"  SO2: {pollution['so2']:.2f} ug/m3")
            print(f"  PM2.5: {pollution['pm2_5']:.2f} ug/m3")
            print(f"  PM10: {pollution['pm10']:.2f} ug/m3")
            print(f"  NH3: {pollution['nh3']:.2f} ug/m3")
        else:
            print("Unable to retrieve air pollution data.")
        
        print("=" * 50)


class WeatherGUI:
    """GUI for displaying humidity forecast bar chart."""

    def __init__(self, weather_app):
        self.weather_app = weather_app
        self.root = None
        self.fig = None
        self.ax = None

    def init_plot(self, ax):
        """Initialize the plot with labels and title."""
        ax.set_ylabel('Humidity (%)')
        ax.set_title('3-Day Humidity Forecast')
        ax.set_ylim(0, 100)

    def plot_temperatures(self, ax, dates, humidities):
        """Create the bar chart."""
        colors = ['#3498db', '#2ecc71', '#f39c12']
        bars = ax.bar(dates, humidities, color=colors, edgecolor='black', linewidth=1.2)
        return bars

    def write_humidity_on_bar_chart(self, ax, bars, humidities):
        """Display humidity percentage on each bar."""
        for bar, humidity in zip(bars, humidities):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{humidity}%',
                   ha='center', va='bottom', fontsize=12, fontweight='bold')

    def style_chart(self, ax):
        """Style the bar chart."""
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    def create_humidity_chart(self, location):
        """Create and display the humidity forecast chart."""
        if not MATPLOTLIB_AVAILABLE:
            print("Matplotlib not available. Cannot display chart.")
            return
        
        forecast = self.weather_app.get_forecast(location)
        if not forecast:
            print("No forecast data available.")
            return
        
        forecast = forecast[:3]
        dates = [day['date'].strftime('%a\n%m/%d') for day in forecast]
        humidities = [day['humidity'] for day in forecast]
        
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.init_plot(self.ax)
        bars = self.plot_temperatures(self.ax, dates, humidities)
        self.write_humidity_on_bar_chart(self.ax, bars, humidities)
        self.style_chart(self.ax)
        
        plt.suptitle(f'Humidity Forecast for {location.title()}', 
                    fontsize=14, fontweight='bold', y=0.98)
        plt.tight_layout()
        
        if TKINTER_AVAILABLE:
            self.show_in_tkinter(location)
        else:
            plt.show()

    def show_in_tkinter(self, location):
        """Display the chart in a tkinter window."""
        self.root = tk.Tk()
        self.root.title(f"Weather Forecast - {location.title()}")
        self.root.geometry("900x700")
        
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        close_btn = ttk.Button(self.root, text="Close", command=self.root.destroy)
        close_btn.pack(pady=10)
        
        self.root.mainloop()


def get_user_location():
    """Get and validate user input for location."""
    while True:
        location = input("\nEnter city name (or 'quit' to exit): ").strip()
        
        if location.lower() == 'quit':
            return None
        
        if location:
            return location
        
        print("Please enter a valid city name.")


def display_menu():
    """Display main menu options."""
    print("\n" + "=" * 50)
    print("WEATHER APP MENU")
    print("=" * 50)
    print("1. Get current weather")
    print("2. Get 5-day forecast")
    print("3. Get air pollution data")
    print("4. Show humidity forecast chart (GUI)")
    print("5. Get city ID")
    print("6. Get all information")
    print("7. Change location")
    print("8. Quit")
    print("=" * 50)


def main():
    """Main function to run the Weather App."""
    print("=" * 60)
    print("           WEATHER APP")
    print("=" * 60)
    print("\nNOTE: This app works in MOCK DATA mode by default.")
    print("To use real weather data:")
    print("1. Get a free API key from: https://openweathermap.org/api")
    print("2. Install pyowm: pip install pyowm")
    print("3. Run: python weather_app.py YOUR_API_KEY")
    print("=" * 60)
    
    api_key = None
    if len(sys.argv) > 1:
        api_key = sys.argv[1]
    
    app = WeatherApp(api_key)
    gui = WeatherGUI(app)
    
    location = get_user_location()
    if not location:
        print("\nGoodbye!")
        return
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            app.display_weather(location)
        
        elif choice == "2":
            app.display_forecast(location)
        
        elif choice == "3":
            app.display_air_pollution(location)
        
        elif choice == "4":
            if MATPLOTLIB_AVAILABLE:
                print(f"\nOpening humidity chart for {location}...")
                gui.create_humidity_chart(location)
            else:
                print("\nGUI features not available. Please install matplotlib:")
                print("  pip install matplotlib")
        
        elif choice == "5":
            city_id = app.get_city_id(location)
            if city_id:
                print(f"\nCity ID for {location}: {city_id}")
            else:
                print("\nUnable to retrieve city ID.")
        
        elif choice == "6":
            app.display_weather(location)
            app.display_forecast(location)
            app.display_air_pollution(location)
        
        elif choice == "7":
            new_location = get_user_location()
            if new_location:
                location = new_location
                print(f"\nLocation changed to: {location}")
            else:
                print("\nLocation unchanged.")
        
        elif choice == "8" or choice.lower() == "quit":
            print("\nThank you for using Weather App. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()