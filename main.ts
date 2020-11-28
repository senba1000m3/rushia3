basic.forever(function () {
    if (mooncar.UltrasonicSensor() <= 7) {
        mooncar.MoonCarGo(mooncar.Direction.direct4, 10)
    } else {
        mooncar.MoonCarGo(mooncar.Direction.direct1, 10)
    }
})
