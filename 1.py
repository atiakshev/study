from time import sleep

class TrafficLight:
    _colors = ['red', 'yellow', 'green']

    def running(self):
        i=0
        while i<3:
            print(f'TrafficLight - ',f'{TrafficLight._colors[i]}')
            if i == 0:
                sleep(7)
            elif i ==1:
                sleep(5)
            elif i == 2:
                sleep(7)
            i  += 1
TrafficLight = TrafficLight()
TrafficLight.running()

