import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

from weather_utils import get_weather 

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Weather App')
        self.setGeometry(300, 300, 800, 500) 

        self.setStyleSheet('background-color: #222222; color: #e67e22;')
        self.setWindowOpacity(0.8)

        font_consolas = QFont("Consolas", 12)

        self.location_label = QLabel('Enter Location:')
        self.location_label.setFont(font_consolas)

        self.location_input = QLineEdit()
        self.location_input.setFont(font_consolas)

        self.search_button = QPushButton('Search')
        self.search_button.setStyleSheet('background-color: #333333; color: #e67e22;')
        self.search_button.clicked.connect(self.get_weather_info)
        self.search_button.setFont(font_consolas)

        self.result_label = QLabel(' ')
        self.result_label.setFont(font_consolas)

        self.weather_icon_label = QLabel()
        self.weather_icon_label.setFont(font_consolas)


        result_layout = QGridLayout()
        result_layout.addWidget(self.result_label, 0, 0, 1, 4)
        result_layout.addWidget(self.weather_icon_label, 0, 4, 1, 1, alignment=Qt.AlignRight)

        layout = QGridLayout()  
        layout.addWidget(self.location_label, 1, 0, 1, 2)  
        layout.addWidget(self.location_input, 1, 2, 1, 4)  
        layout.addWidget(self.search_button, 2, 4, 1, 1, alignment=Qt.AlignRight) 
        layout.addLayout(result_layout, 3, 0, 1, 5)  

        layout.setAlignment(self.location_label, Qt.AlignHCenter)
        layout.setAlignment(self.location_input, Qt.AlignHCenter)
        layout.setAlignment(self.search_button, Qt.AlignLeft)

        self.setLayout(layout)


    def get_weather_info(self):
        location = self.location_input.text()
        if location:
            try:
                weather_data = get_weather(location)
                self.display_weather_info(weather_data)
            except Exception as e:
                self.result_label.setText(f"Error fetching weather: {str(e)}")
        else:
            self.result_label.setText('Please enter a location.')

    def display_weather_info(self, weather_data):

        current_conditions = weather_data['currentConditions']
        datetime = current_conditions.get('datetime', 'N/A')
        temp = current_conditions.get('temp', 'N/A')
        feelslike = current_conditions.get('feelslike', 'N/A')
        humidity = current_conditions.get('humidity', 'N/A')
        precip = current_conditions.get('precip', 'N/A')
        precipprob = current_conditions.get('precipprob', 'N/A')
        snow = current_conditions.get('snow', 'N/A')
        windspeed = current_conditions.get('windspeed', 'N/A')
        winddir = current_conditions.get('winddir', 'N/A')
        pressure = current_conditions.get('pressure', 'N/A')
        visibility = current_conditions.get('visibility', 'N/A')
        cloudcover = current_conditions.get('cloudcover', 'N/A')
        conditions = current_conditions.get('conditions', 'N/A')
        icon = current_conditions.get('icon', 'N/A')

        result_text = f"<span style='color: #e67e22'>Current Conditions as of {datetime}:</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Temperature:</span></b> <span style='color: #3498db'>{temp}°C</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Feels Like:</span></b> <span style='color: #3498db'>{feelslike}°C</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Humidity:</span></b> <span style='color: #3498db'>{humidity}%</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Precipitation:</span></b> <span style='color: #3498db'>{precip} mm</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Precipitation Probability:</span></b> <span style='color: #3498db'>{precipprob}%</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Snow:</span></b> <span style='color: #3498db'>{snow} mm</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Wind Speed:</span></b> <span style='color: #3498db'>{windspeed} m/s</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Wind Direction:</span></b> <span style='color: #3498db'>{winddir}°</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Pressure:</span></b> <span style='color: #3498db'>{pressure} hPa</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Visibility:</span></b> <span style='color: #3498db'>{visibility} km</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Cloud Cover:</span></b> <span style='color: #3498db'>{cloudcover}%</span><br>"
        result_text += f"<b><span style='color: #e67e22'>Conditions:</span></b> <span style='color: #3498db'>{conditions}</span>"

        self.result_label.setText(result_text)

        icon_path = f'icons/cloudy.png' if cloudcover > 60 else 'icons/sunny.png' 
        pixmap = QPixmap(icon_path)
        self.weather_icon_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

