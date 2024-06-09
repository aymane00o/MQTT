import paho.mqtt.client as mqtt
# Define the MQTT broker address and port
broker_address = "192.168.0.184"
broker_port = 1883

# Define the MQTT topic
topic = "home/distance"

# Define the MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)
#########
 # Draw bounding boxes for detected objects
    #for i in range(len(boxes)):
        #if i in indexes:
            #x, y, w, h = boxes[i]
            #label = str(classes[class_ids[i]])
            #color = colors[class_ids[i]]
            #if label == "stop sign":
                client.publish(topic, "Stop") # publishing data to the recepter 
                #cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                #cv2.putText(frame, "stop_sign", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    # Detect speed limit signs
    #frame = detect_speed_limit_signs(frame)

    # Display the annotated image
    #cv2.imshow("Frame", frame)

    # Exit the loop if the 'q' key is pressed
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break
