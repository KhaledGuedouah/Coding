#include "img_reconstruct.h"

double** reconstructionImg (char * filename,unsigned int dim_x,unsigned int  dim_y )
{
    unsigned int  x,y,p,q;
    double** mat;
    Moments mom;
    mom=lireMomentsTxt(filename);
    double ** co = matCoefficientLegendre(mom.n);
    mat= creerMatrice(dim_x,dim_y);

    for ( x = 0; x < dim_x; x++)
    {

        for ( y = 0; y < dim_y; y++)
        {
            for (p=0 ; p<= mom.n ; p++ )
            {
                for (q=0 ; q<= mom.n-p ; q++)
                {
                    mat[x][y] += mom.leg[p][q]*polyLegendre((2*(double)x/dim_x-1),p,co)*polyLegendre((2*(double)y/dim_y-1),q,co);
                }
            }
        }
    }
    freeMatrice(&co, mom.n + 1);
    FreeMoments(&mom);
    return mat ;
}

void reconstructionBmp (char* filemom, char* imgName,unsigned int dim_x, unsigned int dim_y)
{
    printf("\n Reconstruction en cours ... \n" );

    double ** mat=reconstructionImg ( filemom,dim_x,dim_y );

    BmpImg img=createBmpImg("Result",dim_x,dim_y) ;


    unsigned int i,j;

    for ( i = 0 ; i<dim_x; i++)
    {
        for ( j =0 ; j<dim_y; j++)
        {
            if (mat[i][j]< 0 )
            {
                mat[i][j]=0;
            }
            else
            {
                if ((mat[i][j])>1 )
                {
                    mat[i][j]=1;
                }
            }
            setPixel(img,(int)(255*mat[i][j]),i,j);

        }
    }
    writeBmpImage(imgName,&img);
    freeMatrice(&mat,dim_x);
    freeBmpImg(&img);
    printf("\n Image reconstruite avec Succes ! \n" );
}
