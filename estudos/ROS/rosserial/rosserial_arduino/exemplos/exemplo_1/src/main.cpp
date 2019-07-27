/*
* rosserial Publisher Example
* Prints "hello world!"
*/

#include <Wire.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

#define USE_USBCON
#include <ros.h>
#include <std_msgs/String.h>
ros::NodeHandle  nh;
std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

char hello[13] = "hello world!";

void setup()
{
    lcd.begin(16, 2);
    // LCD FRAME ====================================
    // --------------------------"0123456789abcdef"--
    lcd.setCursor(0,0);lcd.print("                ");
    lcd.setCursor(0,1);lcd.print("                ");
    delay(250);
    // --------------------------"0123456789abcdef"--
    lcd.setCursor(0,0);lcd.print("                ");
    lcd.setCursor(0,1);lcd.print(".               ");
    delay(250);
    // --------------------------"0123456789abcdef"--
    lcd.setCursor(0,0);lcd.print("                ");
    lcd.setCursor(0,1);lcd.print("..              ");
    delay(250);
    // --------------------------"0123456789abcdef"--
    lcd.setCursor(0,0);lcd.print("                ");
    lcd.setCursor(0,1);lcd.print("...             ");
    delay(500);

    // INIT ROS NODE  ================================
    nh.initNode();
    nh.advertise(chatter);
}

void loop()
{
    str_msg.data = hello;
    chatter.publish( &str_msg );
    nh.spinOnce();

    // --------------------------"0123456789abcdef"--
    lcd.setCursor(0,0);lcd.print("                ");
    lcd.setCursor(0,1);lcd.print("       :)       ");
    delay(1000);
}
