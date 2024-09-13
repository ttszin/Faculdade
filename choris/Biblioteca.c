#include<stdio.h>
#include<math.h>
#include<string.h>

double Distancia(double x,double y,double z,double h){
    double dist,l,m;
    l = x-y;
    m = z-h;
    dist = sqrt(pow(l,2) + pow(m,2));

    return dist;
}