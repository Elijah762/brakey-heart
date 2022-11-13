from mpu6050 import mpu6050
import time
import numpy as np
import pandas as pd

mpu = mpu6050(0x68)
t = 0

labels = {'Acc X': [], 'Acc Y': [], 'Acc Z': []}

while True:
  while True:
    accel_data = mpu.get_accel_data()
    x = accel_data['x']
    y = accel_data['y']
    z = accel_data['z']
    print('Acc X: {x}', format(x=x))
    print('Acc Y: {y}', format(y=y))
    print('Acc Z: {z}', format(z=z))
  
    labels['Acc X'].append(x)
    labels['Acc Y'].append(y)
    labels['Acc Z'].append(z)
  
    print('-'*24)
    print()
  
    t += 1
    time.sleep(1)
    if(t == 15):
      break

  df.pd.DataFrame(labels)
  df.to_csv('data.csv')

  avg_x = df[['Acc X']].mean(axis=0)
  avg_y = df[['Acc Y']].mean(axis=0)
  avg_z = df[['Acc Z']].mean(axis=0)
  
  print('============ Last 15 Seconds ===========')
  print(float(avg_x), float(avg_y), float(avg_z))
  print('========================================')
  time.sleep(5)
  
