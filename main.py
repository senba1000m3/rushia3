def on_forever():
    if mooncar.ultrasonic_sensor() <= 5:
        mooncar.moon_car_go(mooncar.Direction.DIRECT4, 30)
        basic.pause(500)
        mooncar.moon_car_go(mooncar.Direction.DIRECT4, 0)
        if mooncar.ultrasonic_sensor() <= 5:
            mooncar.moon_car_go(mooncar.Direction.DIRECT3, 30)
            basic.pause(800)
            mooncar.moon_car_go(mooncar.Direction.DIRECT3, 0)
        else:
            if mooncar.ultrasonic_sensor() <= 5:
                mooncar.moon_car_go(mooncar.Direction.DIRECT3, 30)
                basic.pause(300)
                mooncar.moon_car_go(mooncar.Direction.DIRECT3, 0)
                basic.pause(100)
            else:
                mooncar.moon_car_lr(10, 10)
basic.forever(on_forever)
