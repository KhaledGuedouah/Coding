#include "legendre.h"

double coefficientLegendre (unsigned int  x, unsigned int  i)  
{
    if (x==0 && i==0)
    {
        return 1;
    }
    else
    {
        if (x==1 && i==0)
        {
            return 0 ;
        }
        else
        {
            if (x!=1 && i==0)
            {
                return ((-((double)x-1)/(double)x)*coefficientLegendre(x-2,0));
            }
            else
            {
                if (i>= x-1)
                {
                    return (((2*((double)x-1)+1)/(double)x)* coefficientLegendre(x-1,i-1));
                }
                else
                {
                    return (((2*((double)x-1)+1)/x)* coefficientLegendre(x-1,i-1)+(-((double)x-1)/(double)x)*coefficientLegendre(x-2,i));
                }
            }
        }
    }
}

double ** matCoefficientLegendre (unsigned int n ) 
{
    double ** a = creerMatDiagonale(n+1);
    unsigned int  x,i;
    a[0][0] = 1.00;
    a[1][0]= 0.00 ;
    a[1][1]=1.00;
    for (x=2; x<=n; x++ )
    {
        for (i=0; i<=x; i++)
        {
            if (i==0)
            {
                a[x][i]=-((double)x-1)/((double)x) *a[x-2][0];
            }
            else
            {
                if (i>= x-1)
                {
                    a[x][i]=((2*((double)x-1)+1)/(double)x)* a[x-1][i-1];
                }
                else
                {
                    a[x][i]=((2*((double)x-1)+1)/x)* a[x-1][i-1] +(-((double)x-1)/(double)x)*a[x-2][i];
                }
            }
        }
    }
    return a;
}

double polyLegendre(double x,unsigned int  n, double ** co )
{
    unsigned int i ;
    double poly =0.00;

    for (i=0; i<=n; i++)
    {
        poly+= co[n][i]*pow(x,i);
    }
    return poly;
}

double** constantsDeNormalisation(unsigned int  n)
{
    double** C=creerMatAntiDiagonal(n+1);
    unsigned int p,q;
    for (p=0 ; p<=n ; p++ )
    {
        for (q=0 ; q<=n-p; q++)
        {

            C[p][q]=(2*p + 1)*(2*q + 1)/(4.);

        }
    }
    return C;
}

double momentDeLegendre (BmpImg img,unsigned int  p,unsigned int  q, unsigned int  n, double ** co, double ** momg, double ** Cpq)
{
    unsigned int  i,j;
    double res=0.00;


    for (i=0 ; i<= p ; i++)
    {
        for (j=0 ; j<= q; j++ )
        {

            res += co[p][i]*co[q][j] * momg[i][j]   ;

        }
    }
    res*=Cpq[p][q];

    return res ;
}
double ** matMomentsDeLegendre (BmpImg img, unsigned int  n, double ** momg )
{
    double ** mat = creerMatAntiDiagonal(n+1);
    double ** co= matCoefficientLegendre(n);
    double ** Cpq=constantsDeNormalisation(n);
    unsigned int  p,q;

    for (p=0 ; p<=n ; p++ )
    {
        for (q=0 ; q<=n-p; q++)
        {

            mat[p][q]=momentDeLegendre (img, p,q,n,co,momg,Cpq);

        }
    }
    freeMatrice(&co, n + 1);
    freeMatrice(&Cpq, n + 1);
    return mat ;
}

