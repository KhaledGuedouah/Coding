#include "tools.h"
#include "moment_geometrique.h"
#include "legendre.h"

double ** creerMatrice (unsigned int dim_x, unsigned int dim_y)
{
    double **mat = malloc(dim_x*sizeof(double*));
    unsigned int i;
    for (i=0; i<dim_x; i++)
    {
        mat[i]=calloc(dim_y,sizeof(double));
    }
    return mat;
}
double ** matVandermonde (unsigned int dim,unsigned int pow_max,double moy)
{
    double ** van_m = creerMatrice (dim,pow_max+1);
    unsigned int i, j;
    for (i=0; i<dim; i++)
    {
        for (j=0; j<=pow_max; j++)
        {
            van_m[i][j] = pow(i-moy,j);
        }
    }
    return van_m;
}

double ** creerMatAntiDiagonal (unsigned int dim)
{
    double **mat = malloc(dim*sizeof(double*));
    unsigned int i;
    for (i=0; i<dim; i++)
    {
        mat[i]=calloc(dim-i,sizeof(double));
    }
    return mat;
}

double ** creerMatDiagonale (unsigned int dim)
{
    double **mat = malloc(dim*sizeof(double*));
    unsigned int i;
    for ( i=0; i<dim; i++)
    {
        mat[i]=calloc(i+1,sizeof(double));
    }
    return mat;

}


void freeMatrice(double ***mat,unsigned int dim_x)
{
    if (mat == NULL || *mat == NULL)
    {
        return;
    }
    unsigned int i;
    for ( i = 0; i< dim_x; i++)
    {
        free((*mat)[i]);
    }
    free(*mat);
    *mat = NULL;
    //  if ((*mat)==NULL) printf( "Functions succesfully Freed \n");
}




Moments creerMoments(unsigned int n )
{
    Moments mom ;
    mom.n = n ;
    mom.centres_norm= creerMatAntiDiagonal(n+1) ;
    mom.leg= creerMatAntiDiagonal(n+1) ;
    mom.label[0] = '\0';
    return mom ;
}

void FreeMoments (Moments *mom )
{

    freeMatrice (&(mom->centres_norm),mom->n+1);
    freeMatrice(&(mom->leg),mom->n+1);
    mom->n=0 ;
    mom->label[0] = '\0';
}

void setMomentsLabel (Moments *mom, const char *label)
{
    if (mom == NULL)
    {
        return;
    }
    if (label == NULL)
    {
        mom->label[0] = '\0';
        return;
    }
    strncpy(mom->label, label, MAX_LABEL_LEN - 1);
    mom->label[MAX_LABEL_LEN - 1] = '\0';
}

Moments getMoment(BmpImg img,unsigned int  n)
{
    Moments mom = creerMoments(n) ;

    mom.centres_norm = matMomentsCentreNorme(img,n);

    mom.leg = matMomentsDeLegendre(img,n,mom.centres_norm);

    return mom;

}

double distanceEuclidienne (double ** mat1, double **mat2, unsigned int  n )
{

    unsigned int  p,q;
    double res = 0.00 ;
    for (p=0 ; p<=n ; p++ )
    {
        for (q=0 ; q<=n-p; q++)
        {
            res+= pow(mat1[p][q]-mat2[p][q],2);
        }
    }
    res = sqrt (res);

    return res;
}

void ecrireMomentTxt (char * filename, Moments mom  )
{
    unsigned int  i, j;
    FILE * fichier = fopen (filename,"w");
    if ( fichier != NULL )
    {
        fprintf(fichier, "%d \n", mom.n);
        fprintf(fichier, "%s \n", mom.label);
        fprintf(fichier, "Moments geometrique centres, normes : \n");
        for (i=0 ; i<= mom.n  ; i++ )
        {
            for (j=0 ; j<= mom.n-i ; j++)
            {
                fprintf(fichier, "%lf ", mom.centres_norm[i][j]);
            }
            fprintf(fichier, "\n");
        }
        fprintf(fichier, "Moments de Legendre : \n");
        for (i=0 ; i<= mom.n ; i++ )
        {
            for (j=0 ; j<=mom.n-i ; j++)
            {
                fprintf(fichier, "%lf ", mom.leg[i][j]);
            }
            fprintf(fichier, "\n");
        }
    }
    else
    {
        printf("Error Opening File Please Fix the problem and retry \n");
    }
//if( fclose (fichier)== 0) {printf("\nsuccessfully close \n");}
    fclose (fichier) ;
}

Moments lireMomentsTxt (char * filename )
{
    unsigned int  i, j;
    unsigned int  n ;
    Moments mom = creerMoments(0);
    FILE * fichier = fopen (filename,"r");
    if ( fichier != NULL )
    {
        fscanf(fichier, "%d \n", &n);
        mom = creerMoments(n);
        fscanf(fichier, LABEL_SCANF_FMT " \n", mom.label);
        fscanf(fichier, "Moments geometrique centres, normes : \n");
        for (i=0 ; i<= n ; i++ )
        {
            for (j=0 ; j<=n-i ; j++)
            {
                fscanf(fichier, "%lf", &mom.centres_norm[i][j]);
            }
            fscanf(fichier, "\n");
        }
        fscanf(fichier, "Moments de Legendre : \n");
        for (i=0 ; i<= n ; i++ )
        {
            for (j=0 ; j<= n-i ; j++)
            {
                fscanf(fichier, "%lf", &mom.leg[i][j]);
            }
            fscanf(fichier, "\n");
        }
    }
    else
    {
        printf("Error Opening File Please Fix the problem and retry \n");
    }
    //if( fclose (fichier)== 0) {printf("\nsuccessfully close \n");}
    fclose (fichier);
    return mom  ;
}
void afficherMoments (Moments mom, int legAndOrCenNor )
{
    unsigned int i,j;
    if ( legAndOrCenNor == 1|| legAndOrCenNor == 0)
    {
        printf("Moments geometrique centres, normes de %s sont : \n",mom.label);
        for ( i = 0 ; i<= mom.n ; i++ )
        {
            for ( j =0; j<= mom.n-i ; j++)
            {
                printf("%lf ",mom.centres_norm[i][j]);
            }
            printf("\n");
        }
    }
    if ( legAndOrCenNor == 2 || legAndOrCenNor == 0 )
    {
        printf("Moments de Legendre de %s sont: \n", mom.label);
        for ( i = 0 ; i<=mom.n ; i++ )
        {
            for ( j =0; j<=mom.n-i ; j++)
            {
                printf("%lf ",mom.leg[i][j]);
            }
            printf("\n");
        }

    }
}
