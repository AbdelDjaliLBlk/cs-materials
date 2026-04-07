#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define Q0  0
#define Q1  1
#define Q2  2
#define Q3  3 

int AEF_Multiple_5(char* nbr){
    int i, n=strlen(nbr);
    int etat_automate=0, etat_finale=1;
    // parcourir la chaine de caractères
    for(i=0; (i<n) && (nbr[i]!='\0'); i++) 
        switch(etat_automate){
        // si le chiffre courant == 0 ou 5 le nombre devient multiple de 5
        case Q0:
          if(nbr[i]=='0'||nbr[i]=='5') 
             etat_automate=1;
        // sinon le nombre n'est pas un multiple de 5 (a cet étape)
            else if(isdigit(nbr[i]))
                etat_automate= 0;
        // si le caractère n'est pas un chiffre, ce n'est pas un nombre et ce n'est pas multiple de 5
        else 
            return 0;
        break;
        // si le chiffre courant == 0 ou 5 le nombre reste multiple de 5
        case Q1:
          if(nbr[i]=='0'||nbr[i]=='5')
            etat_automate=1;
        // sinon le nombre n'est pas un multiple de 5
            else if(isdigit(nbr[i]))
                etat_automate= 0;
        // si le caractère n'est pas un chiffre, ce n'est pas un nombre et ce n'est pas multiple de 5 (a cet étape)
        else 
            return 0;
        break;
    		}
    // teste si l'état courant après le parcours de la chaine de caractère est un état final (Q1 est l'état final)
    return (etat_automate==Q1);
}
// ---Language 1---
int AEF_Multiple_110(char* nbr){
    int i, n =strlen(nbr);
    int etat_automate=0;
    // parcourir la chaine de caractères
    for(i=0; (i<n) && (nbr[i]!='\0'); i++) 
        switch(etat_automate){
        case Q0:
            if(nbr[i]=='1') 
                etat_automate=1;
            else if(nbr[i]== '0')
                etat_automate= 0;
            else 
                return 0;
        break;
        case Q1:
            if(nbr[i] == '0')
              etat_automate=0;
            else if(nbr[i] == '1')
                etat_automate= 2;
            else 
                return 0;
        break;
        case Q2:
            if(nbr[i] == '0')
                etat_automate=3;
            else if(nbr[i] == '1')
                etat_automate= 2;
            else 
                return 0;
        break;
    		}
    // Teste si l'état courant après le parcours de la chaine de caractère est un état final (Q3 est l'état final)
    return (etat_automate==Q3);
}
// ---Language 2---
int AEF_Multiple_abc(char* nbr){
    int i, n =strlen(nbr);
    int etat_automate=0;
    // parcourir la chaine de caractères
    for(i=0; (i<n) && (nbr[i]!='\0'); i++) 
        switch(etat_automate){
        case Q0:
            if(nbr[i]=='<') 
                etat_automate = 1;
            else 
                return 0;
        break;
        case Q1:
            if(nbr[i] == '/')
              etat_automate = 2;
            else if(isalpha(nbr[i]))
                etat_automate = 1;
            else if(nbr[i] == '>' && isalpha(nbr[i-1]))
                etat_automate = 3;
            else 
                return 0;
        break;
        case Q2:
            if(isalpha(nbr[i]))
                etat_automate = 2;
            else if(nbr[i] == '>')
                etat_automate = 3;
            else 
                return 0;
        break;
    		}
    // Teste si l'état courant après le parcours de la chaine de caractère est un état final (Q3 est l'état final)
    return (etat_automate==Q3);
}
// ---Language 3---
int AEF_Multiple_abc(char* nbr){
    int i, n =strlen(nbr);
    int etat_automate=0;
    // parcourir la chaine de caractères
    for(i=0; (i<n) && (nbr[i]!='\0'); i++) 
        switch(etat_automate){
        case Q0:
            if(nbr[i]=='<') 
                etat_automate = 1;
            else 
                return 0;
        break;
        case Q1:
            if(nbr[i] == '/')
              etat_automate = 2;
            else if(isalpha(nbr[i]))
                etat_automate = 1;
            else if(nbr[i] == '>' && isalpha(nbr[i-1]))
                etat_automate = 3;
            else 
                return 0;
        break;
        case Q2:
            if(isalpha(nbr[i]))
                etat_automate = 2;
            else if(nbr[i] == '>')
                etat_automate = 3;
            else 
                return 0;
        break;
    		}
    // Teste si l'état courant après le parcours de la chaine de caractère est un état final (Q3 est l'état final)
    return (etat_automate==Q3);
}

void main(){
    char * s = "</a>";
    if(AEF_Multiple_abc(s))
        printf("True.\n");
    else
        printf("False.\n");
}