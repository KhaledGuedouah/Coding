#include "moment_geometrique.h"

static const double kBeta = 2.0;

double MomentGeometrique (BmpImg img, unsigned int p,unsigned int q, unsigned int n)
{
    unsigned int x,y;
    double res=0;
    double ** vanx=matVandermonde(img.dimX,n,0);
    double ** vany=matVandermonde(img.dimY,n,0);
    for (x=0; x<img.dimX; x++)
    {
        for (y=0; y<img.dimY; y++)
        {
            if (getPixel( img, x, y )!=0)
            {
                res+=vanx[x][p]*vany[y][q] ;
            }
        }
    }
    freeMatrice(&vanx, img.dimX);
    freeMatrice(&vany, img.dimY);
    return res;
}

double momentGeoCentreNorme (BmpImg img,unsigned int p, unsigned int q, unsigned int n)
{
    double res=0.00;
    double omega = MomentGeometrique(img,0,0,n);
    double x_bar = MomentGeometrique(img,1,0,n)/omega;
    double y_bar = MomentGeometrique(img,0,1,n)/omega;
    unsigned int x,y;
    // centralisation des cordonne
    double ** vanx_centre=matVandermonde(img.dimX,n,x_bar);
    double ** vany_centre=matVandermonde(img.dimY,n,y_bar);
    for (x=0; x<img.dimX; x++)
    {
        for (y=0; y<img.dimY; y++)
        {
            if (getPixel( img, x, y )!=0)
            {
                res+=vanx_centre[x][p]*vany_centre[y][q]/pow(kBeta*omega,(p+q+2)/2.) ;
            }
        }
    }
    freeMatrice(&vanx_centre, img.dimX);
    freeMatrice(&vany_centre, img.dimY);
    return res;
}

double ** matMomentsCentreNorme(BmpImg img,unsigned int n)
{

    double ** mat_mom = creerMatAntiDiagonal (n+1);
    unsigned int p,q;

    for ( p=0; p<=n; p++)
    {
        for (q=0; q<=n-p; q++)
        {

            mat_mom[p][q]=momentGeoCentreNorme (img,p,q,n);

        }
    }
    return mat_mom;
}
