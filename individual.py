from pyrosim import PYROSIM

from robot import ROBOT

import random, math

class INDIVIDUAL:

        def __init__(self):

		self.genome = random.random() * 2 - 1

		self.fitness = 0

	def Evaluate(self, pb):

        	sim = PYROSIM( playPaused=False, playBlind=pb, evalTime=200 )

        	robot = ROBOT( sim , self.genome )

        	sim.Start()

        	sim.Wait_To_Finish()

        	sensorData = sim.Get_Sensor_Data(sensorID = 4 , s = 1)

        	self.fitness = sensorData[199]

	def Mutate(self):

                #self.genome = random.random() * 2 - 1

		self.genome = random.gauss( self.genome , math.fabs(self.genome) )

