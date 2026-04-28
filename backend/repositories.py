class MockRepository:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self._categories = [
            {"id": 1, "name": "Robotics"},
            {"id": 2, "name": "3D Prints"},
            {"id": 3, "name": "Drones"},
            {"id": 4, "name": "Electronics"}
        ]
        self._products = [
            {"id": 101, "name": "Robot Arm v1", "price": 12500.0, "desc": "6-DOF manipulator for small payloads"},
            {"id": 102, "name": "Custom Gear Set", "price": 45.0, "desc": "High-torque ASA printed gears"},
            {"id": 103, "name": "Micro Servo", "price": 15.0, "desc": "9g micro servo motor"},
            {"id": 104, "name": "Stepper Motor NEMA 17", "price": 25.0, "desc": "High precision stepper motor"},
            {"id": 105, "name": "PLA Filament 1kg", "price": 20.0, "desc": "1.75mm PLA filament, black"},
            {"id": 106, "name": "PETG Filament 1kg", "price": 25.0, "desc": "1.75mm PETG filament, white"},
            {"id": 107, "name": "Quadcopter Frame", "price": 50.0, "desc": "Carbon fiber 5 inch drone frame"},
            {"id": 108, "name": "Brushless Motor 2207", "price": 18.0, "desc": "2400KV brushless motor"},
            {"id": 109, "name": "Flight Controller F4", "price": 45.0, "desc": "F4 flight controller with OSD"},
            {"id": 110, "name": "Arduino Uno R3", "price": 25.0, "desc": "ATmega328P microcontroller board"},
            {"id": 111, "name": "Raspberry Pi 4", "price": 75.0, "desc": "4GB RAM single board computer"},
            {"id": 112, "name": "Breadboard Power Supply", "price": 5.0, "desc": "3.3V/5V power supply module"},
            {"id": 113, "name": "Jumper Wires", "price": 8.0, "desc": "120pcs dupont wire set"},
            {"id": 114, "name": "Resistor Kit", "price": 12.0, "desc": "600pcs 1/4W metal film resistors"},
            {"id": 115, "name": "Soldering Iron", "price": 35.0, "desc": "60W adjustable temperature soldering iron"},
            {"id": 116, "name": "Lipo Battery 3S", "price": 25.0, "desc": "1500mAh 3S lipo battery"},
            {"id": 117, "name": "Lipo Battery 4S", "price": 35.0, "desc": "1500mAh 4S lipo battery"},
            {"id": 118, "name": "Lipo Battery 6S", "price": 45.0, "desc": "1300mAh 6S lipo battery"},
            {"id": 119, "name": "Propellers 5 inch", "price": 5.0, "desc": "5045 tri-blade propellers"},
            {"id": 120, "name": "Propellers 7 inch", "price": 8.0, "desc": "7040 bi-blade propellers"},
            {"id": 121, "name": "FPV Camera", "price": 35.0, "desc": "1200TVL FPV camera"},
            {"id": 122, "name": "VTX 5.8GHz", "price": 25.0, "desc": "800mW video transmitter"},
            {"id": 123, "name": "Receiver 2.4GHz", "price": 15.0, "desc": "ELRS 2.4G nano receiver"},
            {"id": 124, "name": "Radio Transmitter", "price": 100.0, "desc": "2.4GHz radio controller"},
            {"id": 125, "name": "FPV Goggles", "price": 250.0, "desc": "5.8GHz analog FPV goggles"},
            {"id": 126, "name": "ABS Filament 1kg", "price": 22.0, "desc": "1.75mm ABS filament, black"},
            {"id": 127, "name": "TPU Filament 1kg", "price": 28.0, "desc": "1.75mm flexible TPU filament"},
            {"id": 128, "name": "3D Printer Nozzle 0.4mm", "price": 5.0, "desc": "Brass nozzle for MK8"},
            {"id": 129, "name": "Hotend Assembly", "price": 40.0, "desc": "All-metal hotend"},
            {"id": 130, "name": "Heated Bed 235x235", "price": 30.0, "desc": "24V heated bed"},
            {"id": 131, "name": "Mainboard 32-bit", "price": 50.0, "desc": "Silent stepper mainboard"},
            {"id": 132, "name": "Limit Switch", "price": 2.0, "desc": "Mechanical endstop"},
            {"id": 133, "name": "Timing Belt GT2", "price": 5.0, "desc": "2m GT2 timing belt"},
            {"id": 134, "name": "Pulley GT2 20T", "price": 3.0, "desc": "Aluminum pulley"},
            {"id": 135, "name": "Linear Bearing LM8UU", "price": 8.0, "desc": "10pcs linear bearings"},
            {"id": 136, "name": "DC Motor 12V", "price": 10.0, "desc": "High torque DC motor"},
            {"id": 137, "name": "Motor Driver L298N", "price": 4.0, "desc": "Dual H-bridge motor driver"},
            {"id": 138, "name": "Ultrasonic Sensor HC-SR04", "price": 3.0, "desc": "Distance measuring sensor"},
            {"id": 139, "name": "Servo Motor MG996R", "price": 12.0, "desc": "High torque metal gear servo"},
            {"id": 140, "name": "Gyro Sensor MPU6050", "price": 5.0, "desc": "6-axis accelerometer and gyro"},
            {"id": 141, "name": "IR Sensor Module", "price": 2.0, "desc": "Infrared obstacle avoidance sensor"},
            {"id": 142, "name": "Relay Module 5V", "price": 3.0, "desc": "1-channel relay module"},
            {"id": 143, "name": "LCD Display 16x2", "price": 6.0, "desc": "I2C character LCD display"},
            {"id": 144, "name": "LED Assortment Kit", "price": 8.0, "desc": "300pcs 5mm LEDs"},
            {"id": 145, "name": "Capacitor Kit", "price": 15.0, "desc": "Electrolytic capacitor assortment"}
        ]
        self._junction = [
            {"p_id": 101, "c_id": 1}, {"p_id": 102, "c_id": 2},
            {"p_id": 103, "c_id": 1}, {"p_id": 104, "c_id": 1},
            {"p_id": 105, "c_id": 2}, {"p_id": 106, "c_id": 2},
            {"p_id": 107, "c_id": 3}, {"p_id": 108, "c_id": 3},
            {"p_id": 109, "c_id": 3}, {"p_id": 110, "c_id": 4},
            {"p_id": 111, "c_id": 4}, {"p_id": 112, "c_id": 4},
            {"p_id": 113, "c_id": 4}, {"p_id": 114, "c_id": 4},
            {"p_id": 115, "c_id": 4},
            {"p_id": 116, "c_id": 3}, {"p_id": 117, "c_id": 3},
            {"p_id": 118, "c_id": 3}, {"p_id": 119, "c_id": 3},
            {"p_id": 120, "c_id": 3}, {"p_id": 121, "c_id": 3},
            {"p_id": 122, "c_id": 3}, {"p_id": 123, "c_id": 3},
            {"p_id": 124, "c_id": 3}, {"p_id": 125, "c_id": 3},
            {"p_id": 126, "c_id": 2}, {"p_id": 127, "c_id": 2},
            {"p_id": 128, "c_id": 2}, {"p_id": 129, "c_id": 2},
            {"p_id": 130, "c_id": 2}, {"p_id": 131, "c_id": 2},
            {"p_id": 132, "c_id": 2}, {"p_id": 133, "c_id": 2},
            {"p_id": 134, "c_id": 2}, {"p_id": 135, "c_id": 2},
            {"p_id": 136, "c_id": 1}, {"p_id": 137, "c_id": 1},
            {"p_id": 138, "c_id": 1}, {"p_id": 139, "c_id": 1},
            {"p_id": 140, "c_id": 1}, {"p_id": 141, "c_id": 4},
            {"p_id": 142, "c_id": 4}, {"p_id": 143, "c_id": 4},
            {"p_id": 144, "c_id": 4}, {"p_id": 145, "c_id": 4}
        ]
        self._media = [
            {"product_id": 101, "filename": "robot_arm.jpg", "is_primary": True},
            {"product_id": 102, "filename": "gears.png", "is_primary": True},
            {"product_id": 103, "filename": "servo.jpg", "is_primary": True},
            {"product_id": 104, "filename": "stepper.jpg", "is_primary": True},
            {"product_id": 105, "filename": "pla.jpg", "is_primary": True},
            {"product_id": 106, "filename": "petg.jpg", "is_primary": True},
            {"product_id": 107, "filename": "frame.jpg", "is_primary": True},
            {"product_id": 108, "filename": "motor.jpg", "is_primary": True},
            {"product_id": 109, "filename": "fc.jpg", "is_primary": True},
            {"product_id": 110, "filename": "arduino.jpg", "is_primary": True},
            {"product_id": 111, "filename": "rpi.jpg", "is_primary": True},
            {"product_id": 112, "filename": "breadboard_ps.jpg", "is_primary": True},
            {"product_id": 113, "filename": "jumper.jpg", "is_primary": True},
            {"product_id": 114, "filename": "resistors.jpg", "is_primary": True},
            {"product_id": 115, "filename": "soldering_iron.jpg", "is_primary": True},
            {"product_id": 116, "filename": "lipo_3s.jpg", "is_primary": True},
            {"product_id": 117, "filename": "lipo_4s.jpg", "is_primary": True},
            {"product_id": 118, "filename": "lipo_6s.jpg", "is_primary": True},
            {"product_id": 119, "filename": "props_5.jpg", "is_primary": True},
            {"product_id": 120, "filename": "props_7.jpg", "is_primary": True},
            {"product_id": 121, "filename": "fpv_cam.jpg", "is_primary": True},
            {"product_id": 122, "filename": "vtx.jpg", "is_primary": True},
            {"product_id": 123, "filename": "rx.jpg", "is_primary": True},
            {"product_id": 124, "filename": "radio.jpg", "is_primary": True},
            {"product_id": 125, "filename": "goggles.jpg", "is_primary": True},
            {"product_id": 126, "filename": "abs.jpg", "is_primary": True},
            {"product_id": 127, "filename": "tpu.jpg", "is_primary": True},
            {"product_id": 128, "filename": "nozzle.jpg", "is_primary": True},
            {"product_id": 129, "filename": "hotend.jpg", "is_primary": True},
            {"product_id": 130, "filename": "bed.jpg", "is_primary": True},
            {"product_id": 131, "filename": "board.jpg", "is_primary": True},
            {"product_id": 132, "filename": "endstop.jpg", "is_primary": True},
            {"product_id": 133, "filename": "belt.jpg", "is_primary": True},
            {"product_id": 134, "filename": "pulley.jpg", "is_primary": True},
            {"product_id": 135, "filename": "bearing.jpg", "is_primary": True},
            {"product_id": 136, "filename": "dc_motor.jpg", "is_primary": True},
            {"product_id": 137, "filename": "l298n.jpg", "is_primary": True},
            {"product_id": 138, "filename": "hc_sr04.jpg", "is_primary": True},
            {"product_id": 139, "filename": "mg996r.jpg", "is_primary": True},
            {"product_id": 140, "filename": "mpu6050.jpg", "is_primary": True},
            {"product_id": 141, "filename": "ir_sensor.jpg", "is_primary": True},
            {"product_id": 142, "filename": "relay.jpg", "is_primary": True},
            {"product_id": 143, "filename": "lcd.jpg", "is_primary": True},
            {"product_id": 144, "filename": "leds.jpg", "is_primary": True},
            {"product_id": 145, "filename": "capacitors.jpg", "is_primary": True}
        ]

    def get_categories(self):
        return self._categories

    def get_products(self, category_id: int = None):
        results = []
        for p in self._products:
            c_ids = [j["c_id"] for j in self._junction if j["p_id"] == p["id"]]
            if category_id and int(category_id) not in c_ids:
                continue
            
            cat_names = [c["name"] for c in self._categories if c["id"] in c_ids]
            p_media = [{"media_url": f"{self.base_url}/{m['filename']}", "is_primary": m['is_primary'], "position": 1} 
                       for m in self._media if m["product_id"] == p["id"]]
            
            primary = next((m["media_url"] for m in p_media if m["is_primary"]), None)

            results.append({
                **p, "categories": cat_names, "media": p_media, "primary_image": primary, "description": p.get("desc")
            })
        return results

class SQLRepository:
    def __init__(self, db_path: str, base_url: str):
        self.db_path = db_path
        self.base_url = base_url