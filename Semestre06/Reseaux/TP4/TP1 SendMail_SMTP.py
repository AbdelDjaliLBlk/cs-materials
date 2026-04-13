import smtplib
from email.mime.text import MIMEText
from email.header    import Header
# nom domaine du serveur SMTP pour le quel ont souhaite transmettre un mail
smtp_host = 'smtp.gmail.com'

# donnees d'authentification du transmetteur (adresse mail et mot de passe)
AdresseMailExpediteur="MasterInfo.tlemcen.MAIL@gmail.com"
MotDePasse="CodingMonk?L7*5"

# adresse mail recepteur
AdresseMailRecepteur="VOTRE.ADRESSE.EMAIL.SVP@gmail.com"

# Mail formate avec le format RFC822 ( voir le cours SMTP)
# contenu text
Mail_FormatRFC822 = MIMEText('Testing, Testing Hello! Are you there? k', 'plain', 'utf-8')
# entete Subject:
Mail_FormatRFC822['Subject'] ='Sujet == THIS IS A MAIL'
# entete From:
Mail_FormatRFC822['From'] = AdresseMailExpediteur
# entete To:
Mail_FormatRFC822['To'] = AdresseMailRecepteur

# etablissement de la connexion avec le serveur SMTP smtp.gmail.com
Objet_de_connexion_avec_ServeurSMTP = smtplib.SMTP(smtp_host, 587, timeout=10)
# activation de l'affichage des commandes reponses echangees avec le serveur
Objet_de_connexion_avec_ServeurSMTP.set_debuglevel(1)
try:
    # envoie de la commande STARTTLS (connection securisee)
    Objet_de_connexion_avec_ServeurSMTP.starttls()
    # envoie des informations d'authentification de l'expediteur (AdresseMailExpediteur,MotDePasse )
    Objet_de_connexion_avec_ServeurSMTP.login(AdresseMailExpediteur,MotDePasse )
    # envoie du mail
    Objet_de_connexion_avec_ServeurSMTP.sendmail("MasterInfo.tlemcen.MAIL@gmail.com", AdresseMailRecepteur , Mail_FormatRFC822.as_string())
finally:
    #envoie de la commande QUIT
    Objet_de_connexion_avec_ServeurSMTP.quit()
