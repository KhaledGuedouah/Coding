#include"constructeurBDD.h"


DataBase creerBDD()
{
    DataBase bdd;
    bdd.images = creerListe(sizeof(Moments));
    return bdd;
}

void freeBDD(DataBase *bdd)
{
    freeListe(bdd->images);
}
void afficherBdd (DataBase* bdd)
{
    afficherListe(bdd->images);
}
void imgTotxt()
{
    printf("Creation de la base de donnees en cours ... \n");
    Moments momImg ;
    BmpImg img;
    FILE *DB = fopen(sourceDB,"r");
    FILE *txtDB = fopen(sourcetxtDB,"w");
    int img_count = 0;
    if (DB != NULL && txtDB != NULL)
    {
        fscanf(DB,"%d",&img_count);
        fprintf(txtDB,"%d\n",img_count);
        for (int i = 0 ; i<img_count; i++)
        {
            char DBdest[MAX_PATH_LEN];
            char imgName[MAX_LABEL_LEN];
            char imgPath[MAX_PATH_LEN];
            snprintf(DBdest, sizeof(DBdest), "%s", destDB);
            fscanf(DB, PATH_SCANF_FMT " " LABEL_SCANF_FMT, imgPath, imgName);
            img = readBmpImage(imgPath);
            if (img.img == NULL)
            {
                printf("Erreur: impossible de lire %s\n", imgPath);
                continue;
            }
            //   printf("%s" ,imgPath);
            momImg = getMoment(img,N);
            setMomentsLabel(&momImg, imgName);
            strcat(DBdest,imgName);
            strcat(DBdest,".txt");
            fprintf(txtDB,"%s\n",DBdest);

            ecrireMomentTxt(DBdest,momImg);
            // printf("%s\n",imgName);
            //   printf("image %s uploaded \n", imgName);
            FreeMoments(&momImg);
            freeBmpImg(&img);

        }
        // printf("\nBDD Text files succesfully created ! ;) \n");
        fclose(DB);
        fclose(txtDB);
    }
    else
        printf("ERROR DB FILE MISSING OR DAMMAGED");
    printf(" base de donnees creer avec succes \n");

}

DataBase chainageListeBDD(char* sourcetxt)
{

    int i ;
    DataBase data_base = creerBDD();
    Moments momImg;
    unsigned int fileCount = 0;
    const char *txtPath = (sourcetxt != NULL) ? sourcetxt : sourcetxtDB;
    FILE *txtDB = fopen(txtPath,"r");
    if (txtDB != NULL)
    {
        fscanf (txtDB,"%d\n",&fileCount);
        for ( i=1; i<=fileCount; i++)
        {
            //  printf("filepath of file %d aquired thus ",i);
            char filePath[MAX_PATH_LEN];
            fscanf(txtDB, PATH_SCANF_FMT "\n", filePath);

            momImg = lireMomentsTxt(filePath);

            ajout(data_base.images,&momImg,2);

            //printf("%s added to liste\n",((Moments*)data_base.images->current->data)->label);

        }
    }
    else
    {
        printf("ERROR DB FILE MISSING OR DAMMAGED\n");
    }
    fclose(txtDB);
    return data_base;
}
