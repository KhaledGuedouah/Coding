#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tools.h"
#include "constructeurBDD.h"

static const unsigned int kReconDimX = 32;
static const unsigned int kReconDimY = 32;
static const char *kTestListFile = "InputImg/TestImg.txt";
static const char *kTestDir = "InputImg/";

static int read_yes_no(const char *prompt)
{
    int value = -1;
    while (value != 0 && value != 1)
    {
        printf("%s", prompt);
        if (scanf("%d", &value) != 1)
        {
            int ch;
            while ((ch = getchar()) != '\n' && ch != EOF)
            {
            }
            value = -1;
        }
    }
    return value;
}

static void print_test_list(void)
{
    char tmp[MAX_PATH_LEN];
    FILE *fichier = fopen(kTestListFile, "r");
    if (fichier == NULL)
    {
        printf("Impossible d'ouvrir %s\n", kTestListFile);
        return;
    }

    while (fscanf(fichier, PATH_SCANF_FMT " \n", tmp) == 1)
    {
        printf("\t | %s \n", tmp);
    }
    fclose(fichier);
}

int main(void)
{
    int a;
    char tmp[MAX_PATH_LEN];
    char input_path[MAX_PATH_LEN];
    char moment_path[MAX_PATH_LEN];
    double min_dist;
    const char *output_label = NULL;

    a = read_yes_no(" Voulez-vous creer une nouvelle base de donnee ? [1/0] \n");
    if (a == 1)
    {
        imgTotxt();
    }

    a = read_yes_no("Voulez-vous faire une reconnaissance de forme ?[1/0]\n");
    if (a == 0)
    {
        return 0;
    }

    printf(" Veuillez choisir un nom d'image a reconnaitre de la liste suivante :\n");
    printf("**IMPORTANT** LES IMAGES XX_d.BMP SONT DES IMAGES DECALEES\n\n");
    print_test_list();
    printf("\n Sinon, sauvegardez une image dans InputImg et indiquez son nom : \n");
    scanf(PATH_SCANF_FMT, tmp);
    snprintf(input_path, sizeof(input_path), "%s%s", kTestDir, tmp);

    printf("\n Calcule en cours ... \n");

    DataBase bdd = chainageListeBDD(sourcetxtDB);
    BmpImg input_img = readBmpImage(input_path);
    if (input_img.img == NULL)
    {
        printf("Erreur: impossible de lire %s\n", input_path);
        freeBDD(&bdd);
        return 1;
    }
    Moments input_mom = getMoment(input_img, N);
    setMomentsLabel(&input_mom, "InputImg");

    if (bdd.images == NULL || bdd.images->root == NULL)
    {
        printf("Base de donnees vide ou introuvable.\n");
        FreeMoments(&input_mom);
        freeBmpImg(&input_img);
        freeBDD(&bdd);
        return 1;
    }

    min_dist = distanceEuclidienne(input_mom.leg, ((Moments*)bdd.images->root->data)->leg, N);
    output_label = ((Moments*)bdd.images->root->data)->label;

    for (bdd.images->current = bdd.images->root; hasNext(bdd.images); getNext(bdd.images))
    {
        double current_dist = distanceEuclidienne(input_mom.leg, ((Moments*)bdd.images->current->data)->leg, N);
        if (min_dist > current_dist)
        {
            min_dist = current_dist;
            output_label = ((Moments*)bdd.images->current->data)->label;
        }
    }

    printf("\n La forme la plus proche de l'image %s est : %s \n", input_path, output_label);
    printf("\n La distance euclidienne entre leurs moments de Legendre est : %lf\n", min_dist);

    a = read_yes_no("\n Voulez-vous faire une reconstruction de l'image entree ? [1/0] \n");
    if (a == 1)
    {
        snprintf(moment_path, sizeof(moment_path), "%s%s.txt", destDB, output_label);
        reconstructionBmp(moment_path, "ImgRec.bmp", kReconDimX, kReconDimY);
    }

    FreeMoments(&input_mom);
    freeBmpImg(&input_img);
    freeBDD(&bdd);

    return 0;
}
