#! /usr/bin/python
n= int (raw_input ("Dame el numero de subintervalos para aproximar pi"))
sum=0
if (n>0):
 for i in range (1,n):
   a= float(i-1)/n
   b=float (i)/n
   xi=float (i-0.5)/n
   fxi=float (4.0/(1.0 + xi*xi))
   print '%f' % a
   print '%f' % b
   print '%f' % xi
   print '%f' % fxi
   sum+=fxi 
Pi= float (sum/n)
print("El valor de pi aproximado es:",Pi)
