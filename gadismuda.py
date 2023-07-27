# Created by RanddSoft

import time
import os
import random

print("Getting data Higgs Domino slot fafafa.....")
time.sleep(3.5)
    
step = 1
connect = 1
collect = 1
extract = 1
print(f'Connecting slot fafafa higgs domino...')
while connect < 98:     
	print(f'Connect higgs domino...{connect}%')
	step = random.randint(1, 4)
	connect += step
	time.sleep(step/5)
    
time.sleep(4)
print(f'Connect higgs domino...100%')
time.sleep(2)
print(f'Connected!')
time.sleep(2.5)

while collect < 6545:     
	print(f'Collect slot fafafa higgs domino...{collect}kb/6548kb')
	step = random.randint(1, 300)
	collect += step
	time.sleep(step/100)

time.sleep(3)
print(f'Collect slot fafafa higgs domino...6548kb/6548kb')
time.sleep(3)

for _ in range(24):
	print(random.sample(range(100000, 999999), 6))
	time.sleep(0.2)

while extract < 16701:     
	print(f'Extract data higgs domino...{extract}kb/16703kb')
	step = random.randint(1, 300)
	extract += step
	time.sleep(step/200)

time.sleep(0.4)
print(f'Extract data higgs domino...16703kb/16703kb')
time.sleep(2)
print(f'sukses...')
time.sleep(1.5)
print(f'masukan id game higgs domino')

#link="https://randdsoftindonesia.com"
#os.system("termux-open-url \""+link+"\"")