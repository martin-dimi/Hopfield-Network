#for the submission uncomment the submission statements
#so submission.README

from utilities import seven_segment
from math import *
from Network import Network

from submission import *

# Init the submittion latex
submission=Submission("Martin_Dimitrov")
submission.header("Martin")

# The patterns to be remembered
six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)
seven_segment(one)

print("######################################")

# Init the network and update the latex
net = Network(len(six), submission)
submission.section("Weight matrix")
submission.matrix_print("W", net.weights)

# Teach the network the patterns
net.learn([six, three, one])

# Do the first test
print("test1")
submission.section("Test 1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]
test = net.predict(test)

# submission.seven_segment(test)
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step

print("######################################")

# Do the second test
print("test2")
submission.section("Test 2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
test = net.predict(test)

# submission.seven_segment(test)
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step

submission.bottomer()



