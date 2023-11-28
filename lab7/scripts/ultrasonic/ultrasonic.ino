#include <ros.h>
#include <std_msgs/Float64.h>

// ROS node initialization
ros::NodeHandle nh;

// Define a message of type Float64 to store distance data
std_msgs::Float64 Distance;

// Define a ROS publisher named "chatter" for Float64 messages
ros::Publisher chatter("chatter", &Distance);

// Define the trigger and echo pins for the ultrasonic sensor
const int trigPin = 9;   // Trigger pin for the ultrasonic sensor
const int echoPin = 10;  // Echo pin for the ultrasonic sensor

// Variables to store the duration of the pulse and calculated distance
long duration;
float distance;

void setup() {
  // Initialize the ROS node
  nh.initNode();

  // Advertise the publisher
  nh.advertise(chatter);

  // Set the trigPin as an output and echoPin as an input
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Start serial communication for debugging
  Serial.begin(57600);
}

void loop() {
  // Clear the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Set the trigPin on HIGH state for 10 microseconds to trigger the ultrasonic sensor
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echoPin, which returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance based on the travel time
  distance = duration * 0.034 / 2;

  // Update the Distance message with the calculated distance
  Distance.data = distance;

  // Publish the updated distance data to the ROS topic named "chatter"
  chatter.publish(&Distance);

  // Allow ROS to process any pending communication
  nh.spinOnce();

  // Print the distance on the Serial Monitor for debugging
  // Serial.print("Distance: ");
  // Serial.println(distance);

  // Delay to control the update rate
  delay(100);
}
