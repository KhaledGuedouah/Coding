#ifndef MOMENT_GEOMETRIQUE_H_INCLUDED
#define MOMENT_GEOMETRIQUE_H_INCLUDED
#include "tools.h"

// Moment geometrique eq 5.1
/**
  * @param img image binaire
  * @param p l'ordre de x
  * @param q l'ordre de y
  * @return un moment geometrique
  */
double MomentGeometrique (BmpImg img, unsigned int p, unsigned int q, unsigned int n );

// Moment geometrique centre norme eq.5.2
/**
  * @param img image binaire
  * @param p l'ordre de x
  * @param q l'ordre de y
  * @return un moment geometrique centre et norme
  */
double momentGeoCentreNorme (BmpImg img,unsigned int p, unsigned int q, unsigned int n);

// Matrice des Moments geometriques centres (vandermonde) et normes equation (6)
/**
  * @param img image binaire
  * @param n la dimension de la matrice
  * @return une matrice anti diagonale superieur des moments geometriques centres et normes
  */
double ** matMomentsCentreNorme(BmpImg img,unsigned int n);


#endif // MOMENT_GEOMETRIQUE_H_INCLUDED
