#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

typedef struct UL {
    char lexeme[50];
    int code;
    int ligne;
    struct UL* suivant;
} UL;

#define ID 260
#define NUM 261
#define PO 266
#define PF 267
#define AFF 268
#define PV 269
#define FIN 999
#define PLUS 262
#define MINUS 263
#define MUL 264
#define DIV 265
#define ERR -9

UL* ajouter(UL* tete, char* lex, int code, int ligne) {
    UL* e = (UL*)malloc(sizeof(UL));
    strcpy(e->lexeme, lex);
    e->code = code;
    e->ligne = ligne;
    e->suivant = NULL;

    if (tete == NULL) return e;

    UL* tmp = tete;
    while (tmp->suivant != NULL)
        tmp = tmp->suivant;

    tmp->suivant = e;
    return tete;
}

UL* analyser(FILE* f ) {
    UL* liste = NULL;
    char c;
    int ligne = 1;

    while ((c = fgetc(f)) != EOF) {

        if (c == ' ' || c == '\t')
            continue;
        if (c == '\n') {
            ligne++;
            continue;
        }

        if (isalpha(c)) {
            char mot[20];
            int i = 0;
            while (isalnum(c) || c == '_') {
                mot[i++] = c;
                c = fgetc(f);
            }
            mot[i] = '\0';
            ungetc(c, f);

            liste = ajouter(liste, mot, ID, ligne);
        }

        else if (isdigit(c)) {
            char num[20];
            int i = 0;

            while (isdigit(c)) {
                num[i++] = c;
                c = fgetc(f);
            }
            num[i] = '\0';
            ungetc(c, f);

            liste = ajouter(liste, num, NUM, ligne);
        }

        else {
            char lex[] = {c, '\0'};

            switch (c) {
                case '(': liste = ajouter(liste, lex, PO, ligne); break;
                case ')': liste = ajouter(liste, lex, PF, ligne); break;
                case '=': liste = ajouter(liste, lex, AFF, ligne); break;
                case ';': liste = ajouter(liste, lex, PV, ligne); break;
                case '+': liste = ajouter(liste, lex, PLUS, ligne); break;
                case '-': liste = ajouter(liste, lex, MINUS, ligne); break;
                case '*': liste = ajouter(liste, lex, MUL, ligne); break;
                case '/': liste = ajouter(liste, lex, DIV, ligne); break;

                default:
                    liste = ajouter(liste,lex, ERR , ligne);
                    return liste;
            }
        }
    }

    liste = ajouter(liste, "#", FIN, ligne);
    return liste;
}

void afficher(UL* liste) {
    printf("ANALYSE LEXICALE REUSSITE - LISTE DES ULs :\n\n");
    for (int i = 0 ;i < 44 ; i++) printf("=");
    printf("\n");
    while (liste != NULL) {
        printf(" Lexeme [%s] , Code : [%d] , Ligne [ligne] %d \n",liste->lexeme, liste->code, liste->ligne);
        liste = liste->suivant;
    }
    for (int i = 0 ;i < 44 ; i++) printf("=");

}


void main() {
    FILE* f = fopen("source.txt", "r");
    if (!f) {
        printf("\n*** Erreur Lors de l'Ouverture du fichier ***\n\n");
        return ;
    }

    printf("\nCODE A ANALYSER :     ");
    char c;
    while ((c = fgetc(f)) != EOF) putchar(c);
    printf("\n\n");
    rewind(f);
    
    UL* analyse = analyser(f);
    if (analyse) afficher(analyse);

    fclose(f);
}