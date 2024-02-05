# Smart-Garden-Automated-Plant-Watering-System-Using-Machine-Learning-and-IoT

## Steps for Completing the Project
## 1. Hardware Setup
- Assemble the Arduino Mega board with the soil humidity, temperature, and light sensors.
- Connect the LCD screen via I2C to the Arduino for displaying real-time sensor data.
- Integrate the nRF24L01 module with both the Arduino and Raspberry Pi for wireless communication.

## 2. Software Development on Arduino
- Write the Arduino sketch to read data from the sensors.
- Implement code to send sensor data to the Raspberry Pi using the nRF24L01 module.
- Display the current sensor readings on the LCD screen.

## 3. Data Reception and Storage on Raspberry Pi
- Develop a Python script on the Raspberry Pi to receive data from the Arduino via nRF24L01.
- Store the received data into an SQLite database, ensuring you have a schema that includes timestamps and sensor values.

## 4. Data Visualization
- Create a local web server on the Raspberry Pi using Flask or Django.
- Implement endpoints to fetch sensor data from the SQLite database.
- Use libraries like Matplotlib or Plotly in your web application to plot the sensor data over time.

## 5. Machine Learning Implementation
- Choose supervised learning algorithms suitable for time-series forecasting or classification (e.g., decision trees, SVM, or neural networks).
- Extract features and labels from your stored data for training. The features could be time, sensor readings, and any derived statistics; labels could be binary (water/no water) or categorical (low/medium/high water need).
- Train your model on historical data and evaluate its performance using suitable metrics.
- Implement a mechanism to periodically retrain the model with new data.

## 6. Automated Decision Making
Based on the output of your machine learning model, send commands back to the Arduino to control the watering system (e.g., through actuators or relays connected to a water pump).


## Hardware Components Needed:
-	Arduino Mega: Chosen for its ample number of GPIO pins and compatibility with multiple sensors and modules.
-	Soil Humidity Sensor: To measure the moisture level in the soil.
-	Temperature Sensor: To monitor the environmental temperature affecting the plant.
-	Light Sensor: To assess the amount of sunlight or ambient light available for the plant.
-	LCD Screen with I2C Communication: To display sensor readings and status messages.
-	nRF24L01 Wireless Transceiver Modules: Two modules, one for the Arduino Mega and one for the Raspberry Pi, to enable wireless data transmission.
-	Raspberry Pi: Acts as the central unit for receiving sensor data, processing it, and making decisions. Any model with GPIO pins (such as Raspberry Pi 3 or 4) will work.
-	Breadboard and Jumper Wires: For prototyping the connections without soldering.
-	Power Sources: For both Arduino and Raspberry Pi, plus any additional components like the water pump for the actual watering mechanism.

