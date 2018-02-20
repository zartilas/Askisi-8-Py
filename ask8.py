# -*- coding: utf-8 -*-
#Άσκηση 8

import random
#for x in range(30):
  #print random.randint(-30,30)

#number = range(-30,31)
#print(number)
number = []
for i in range(-30,31): number.append(i)
print(number)
i = 60
j = 60
k = 60
for i in range(i):
 for j in range(j):
  for k in range(k):
   if(number[i] + number[j] + number[k] == 0):
       print number[i] , number[j] , number[k] ,"ισούνται με 0"
   else:
       print number[i] , number[j] , number[k] ,"δεν ισούνται με 0"



#for (int i = 0; i < N; i++) {
 #for (int j = i + 1; j < N; j++) {
 #for (int k = j + 1; k < N; k++) {
 #if(numbers[i] + numbers[j] + numbers[k] == 0) {
 #x++;
