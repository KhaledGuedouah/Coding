#ifndef CONSTRUCTEURBDD_H_INCLUDED
#define CONSTRUCTEURBDD_H_INCLUDED

#include "listeSC.h"

typedef struct
{
    ListeSC * images;
} DataBase ;

// allocation de base de donnees
/**
  * .
  * @return une base de données initialisé
  */
DataBase creerBDD();
// distruction de la base de données
/**
  *
  * @param bdd pointeur vers la base de donné
  * @return void
  */
void afficherBdd (DataBase* bdd);
// Afficher La base de données
/**
  *
  * @param bdd pointeur vers la base de donné
  * @return Void
  */
void freeBDD(DataBase *bdd);

// creation des fichiers txt de moments a partir des img
/**
  *
  * @param aucun
  * @return un nombre de fichier dans le repertoire DATA/DB/
  */
void imgTotxt();

//Moments logistic(Moments mom);
// creation de la liste chainé a partir des fichiers txt
/**
  *
  * @param sourcetxt repertoire vers le fichier qui contient les repetoires des fichier txt des imgs
  * @return une base de données
  */
DataBase chainageListeBDD(char* sourcetxt);

#endif // CONSTRUCTEURBDD_H_INCLUDED
