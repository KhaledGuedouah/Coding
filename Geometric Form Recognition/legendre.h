#ifndef LEGENDRE_H_INCLUDED
#define LEGENDRE_H_INCLUDED

#include "tools.h"

// calculateur du coef de legendre  eq. 5.3
/**
  * @param x la valeur du coeff_legendre et sa position de ligne
  * @param i l'ordre et la position dans la colonne de la matrice
  * @return le coeff de legendre
  */
double coefficientLegendre (unsigned int  x, unsigned int  i);

// Mat du coef de legendre
/**
  * @param n la dimension de la matrice de legendre
  * @return une matrice de coeff de legendre
  */
double ** matCoefficientLegendre (unsigned int  n);

// calculateur de polynome de legendre
/**
  * @param x une entree
  * @param n l'ordre
  * @param co coeficient
  * @return la valeur de legendre en x a l'ordre n
  */
double polyLegendre(double x,unsigned int  n, double ** co );


/**
  * @param n l'ordre de la matrice.
  * @return matrice de constant de normalisation.
  */
double** constantsDeNormalisation(unsigned int  n);

/** moment de legendre
  * @param BmpImg string of char.
  * @param p
  * @param q
  * @param n l'ordre du moment
  * @param co mat de coeficient de legendre
  * @param momg mat des moment geometrique
  * @param Cpq mat constants De Normalisation
  * @return un moment de legendre.
  */
double momentDeLegendre (BmpImg img,unsigned int  p,unsigned int  q, unsigned int  n, double ** co, double ** momg, double ** Cpq);

/**
  * @param BmpImg image a convertir
  * @param n l'ordre des moments
  * @param momg matrice moment geomtique centres normes
  * @return matrice de moment de legendre
  */
double ** matMomentsDeLegendre (BmpImg img, unsigned int  n,double ** momg );


#endif // LEGENDRE_H_INCLUDED
