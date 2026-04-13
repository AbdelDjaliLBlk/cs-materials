import ftplib
# ouverture d'une connexion au serveur FTP
connexionftp=ftplib.FTP("ftp.nluug.nl")
print('\n######### Fin instruction [connexionftp=ftplib.FTP("ftp.vim.org")]\n')
# commande login anonyme
connexionftp.login()

print( '\n######### Fin instruction [connexionftp.login()]\n')
# commande NLST
print( '\n'.join(connexionftp.nlst()))

print( '\n######### Fin instruction [connexionftp.nlst()]\n')

print(connexionftp.cwd("pub"))
print(connexionftp.cwd("ImageMagick"))
print('\n######### Fin instruction CD pub\ImageMagick')
# telechargement du fichier welcome.msg 
connexionftp.retrbinary('RETR ImageMagick-6.9.11-29.7z', open('ImageMagick-6.9.11-29.7z', 'wb').write)

