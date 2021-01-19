#!/usr/bin/env python

print("How G. Wiz Spent Their Lottery Money")

# Set up initial conditions

winnings = 1000
tax_rate = .09

print("Initial amount: " + str(winnings))

# Reduce winnings by tax rate
winnings -= winnings * tax_rate

print("Taxes paid: " + str(winnings * tax_rate))

# Buy some cookies
croc_scout = 10.00 * 5
winnings -= croc_scout

print("CrocScout cookies: " + str(croc_scout))

# Gossip rag
clawparazzi = 5.00
clawparazzi += clawparazzi * tax_rate
winnings -= clawparazzi

print("Clawparazzi: " + str(clawparazzi))

# Friends come a-knockin'
shares = winnings / 4
winnings -= shares * 3

print("Owed to friends: " + str(shares * 3))

print("Total remaining: " + str(winnings))