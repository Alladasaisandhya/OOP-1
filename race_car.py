import math
class Car:
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
        self._color=color
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        self._is_engine_started=False
        self._current_speed=0
        if self._max_speed<0:
            raise ValueError("Invalid value for max_speed")
        if self._acceleration<0:
            raise ValueError("Invalid value for acceleration")
        if self._tyre_friction<0:
            raise ValueError("Invalid value for tyre_friction")
    @property
    def color(self):
        return self._color
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def current_speed(self):
        return self._current_speed
        
    def accelerate(self):
        if self._is_engine_started==True:
            if self._current_speed+self._acceleration<=self._max_speed:
                self._current_speed+=self._acceleration
            else: 
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
            
    def start_engine(self):
        self._is_engine_started=True
    def apply_brakes(self):
        if self._current_speed>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
        else:
            self._current_speed=0
            
    def sound_horn(self):
        if self._is_engine_started==False:
            print("Start the engine to sound_horn")
        else:
            print("Beep Beep")
            
    def stop_engine(self):
        self._is_engine_started=False
class RaceCar(Car):
    def __init__(self,color=None, max_speed=0,acceleration=0,tyre_friction=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro=0
    @property
    def nitro(self):
        return self._nitro
    
    def accelerate(self):
        s = 0
        if self._is_engine_started==True:
            if self._nitro>0:
                s=math.ceil(self._acceleration*30/100)
                self._nitro-=10 
            if self._current_speed+self._acceleration+s<=self._max_speed:
                self._current_speed+=self._acceleration+s
            else: 
                self._current_speed = self._max_speed
        else:
           print("Start the engine to accelerate")
          
    def apply_brakes(self):
        if self._current_speed>=self._max_speed//2:
            self._nitro+=10
        if self._current_speed>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
        else:
            self._current_speed=0
    def sound_horn(self):
        if self._is_engine_started:
            print("Peep Peep\nBeep Beep")
        else:
            print("Start the engine to sound_horn")

            
