#ifndef IMG_RECONSTRUCT_H_INCLUDED
#define IMG_RECONSTRUCT_H_INCLUDED

#include "tools.h"



// reconstruction de l'image eq.5.4
/**
  * @param filename le nom du fichiers qui comporte les moments
  * @param dim_x dimension X
  * @param dim_y dimension Y
  * @return Matrice de l'image reconstruite
  */
double** reconstructionImg (char * filename,unsigned int  dim_x,unsigned int  dim_y );

//
/**
  * @param filemom moment structure geom
  * @param imgName le nom de l'image
 * @param dim_x dimension X
  * @param dim_y dimension Y
  * @return Nae
  */
void reconstructionBmp (char* filemom, char* imgName,unsigned int dim_x, unsigned int dim_y);

#endif // IMG_RECONSTRUCT_H_INCLUDED
