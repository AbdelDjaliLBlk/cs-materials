#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int check_login_pw(char * login , char * pw){
    // Login Commence Par Une Majuscule
    if(!isalpha(login[0])) return 0;
    // Login Doit etre AlphaNumérique
    int e = 0;
    for (int i = 0; i <strlen(login);i++)
        if (!isalnum(login[i]))
         e--;
    if (e < 0) return 0;
    // Mot de Passe Contient Majuscule
    e = 0;
    for (int i = 0; i <strlen(pw);i++)
        if (isupper(pw[i])) 
            e--;
    // Mot de Passe Supérieur à 10
    if (e == 0 || strlen(pw) <= 10) return 0;
    // Login != Mot de Passe
    if (!strcmp(login,pw)) return 0;
    // Login/Mot de Passe Valide
    return 1;

}
void toString(int x) {
    printf("    ---Verifier---\n");
    if(x)  
        printf("Login/MotDePasse Valide.\n");
    else
        printf("Login/MotDePasse Non Valide.\n");
    printf("    --------------");
    }

void main(){
    toString(check_login_pw("med","mDsktkp2019"));
}