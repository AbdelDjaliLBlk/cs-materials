#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Liste Chainée
typedef struct Mot_De_La_Phrase { 
char Mon_mot[20]; 
struct Mot_De_La_Phrase *  Adresse_Mot_suivant; 
} Mot; 

// Inserer a la Fin
Mot* Inserer_a_la_fin(Mot* les_mots_de_laphrase, char* mot){ 
    if(les_mots_de_laphrase==NULL){ 
        les_mots_de_laphrase=malloc(sizeof(Mot)); 
        les_mots_de_laphrase->Adresse_Mot_suivant=NULL; 
        strcpy(les_mots_de_laphrase->Mon_mot,mot); 
        return les_mots_de_laphrase;
    } 
    Mot* dernier_mot=les_mots_de_laphrase; 
    while(dernier_mot->Adresse_Mot_suivant!=NULL){ 
        dernier_mot=dernier_mot->Adresse_Mot_suivant; } 
        dernier_mot->Adresse_Mot_suivant=malloc(sizeof(Mot)); 
        strcpy(dernier_mot->Adresse_Mot_suivant->Mon_mot,mot); 
        dernier_mot->Adresse_Mot_suivant->Adresse_Mot_suivant=NULL; 
        return les_mots_de_laphrase; 
        } 

Mot* Inserer_au_debut(Mot* les_mots_de_laphrase,char* mot){ 
    Mot* premier_mot=malloc(sizeof(Mot)); 
    strcpy(premier_mot->Mon_mot,mot); 
    premier_mot->Adresse_Mot_suivant=les_mots_de_laphrase; 
    return premier_mot;
 } 

Mot* Decouper_phrase(char * phrase){
    int n = strlen(phrase) ,s=1, j=0 , i=0, h=1;
    char mot[20] ;
    Mot * mots = (Mot*)malloc(sizeof(Mot));  
    mots->Adresse_Mot_suivant = NULL;
    mots->Mon_mot[0] = '\0';
    for(i = 0; i <= n ;i++){
        if (phrase[i] == ' ' || phrase[i] == '.' || phrase[i] == ',' || phrase[i] == ';' 
            || phrase[i] == '?' || phrase[i] == '!' || phrase[i] == '\0' || phrase[i] == '\n'){
            mot[j] = '\0';
            Inserer_a_la_fin(mots,mot);
            * mot = '\0';
            j = 0;
        }
        else {
          mot[j] = phrase[i];
            j++;
        }
        }
    return mots;
}
void Afficher_Liste(Mot * list){
    while(list){
        printf("-%s\n",list->Mon_mot);
        list = list->Adresse_Mot_suivant;
    }
}

// ---Main---
void main(){
// --- Exo1 ---
char phrase [100];
    printf("Entrez une phrase : ");
    fgets(phrase , 100 , stdin);    
Mot * mots = Decouper_phrase(phrase);
Afficher_Liste(mots->Adresse_Mot_suivant);
}