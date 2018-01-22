import time
from ftplib import FTP



##############################################APERTURA FILE INI IMPOSTAZIONI###############################################################
file = open("setting.ini", "r") 
for riga in file:
	if riga.find("|")!=-1: #SOLO LE RIGHE DELLE IMPOSTAZIONI CHE CONTENGONO IL | VENGONO CONSIDERATE, GLI ALTRI SONO COMMENTI
		riga=riga.replace(" ","") #TOGLO GLI SPAZI BIANCHI
		impostazione,valore=riga.split("|"); #PRENDE IMPOSTAZIONE E VALORE IMPOSTAZIONE USANDO COME SEPARATORE I :
		if impostazione=='ftpserver':
			ftpserver=valore
			ftpserver=ftpserver.replace("\n","")
		if impostazione=='ftpuser':
			ftpuser=valore
			ftpuser=ftpuser.replace("\n","")
		if impostazione=='ftppassword':
			ftppassword=valore
			ftppassword=ftppassword.replace("\n","")
		if impostazione=='ftpfat':
			ftpfat=valore
			ftpfat=ftpfat.replace("\n","")
		if impostazione=='nopostel':
			nopostel=valore
			nopostel=nopostel.replace("\n","")
		if impostazione=='postel':
			postel=valore
			postel=postel.replace("\n","")
		if impostazione=='destinazione':
			destinazione=valore
			destinazione=destinazione.replace("\n","")
##############################################FINE FILE INI IMPOSAZIONI###################################################################


########################################################################################################
####################################################FTP#################################################
########################################################################################################
def retr_file():
	ftp = FTP(ftpserver)
	ftp.login(ftpuser,ftppassword) 
	#######NOPOSTEL
	file_nopostel = open(nopostel,'wb') #FILE LOCALE
	ftp.cwd(ftpfat)
#	ftp.retrlines('LIST') 
	try:
		ftp.retrbinary("RETR "+nopostel,file_nopostel.write)
	except:
		print("IMPOSSIBILE RECUPERARE NOPOSTEL")
	file_nopostel.close()
	#######POSTEL
	file_postel = open(postel,'wb') #FILE LOCALE
	try:
		ftp.retrbinary("RETR "+postel,file_postel.write)
	except:
		print("IMPOSSIBILE RECUPERARE POSTEL")
	file_postel.close()

########################################################################################################
####################################################FINE FTP############################################
########################################################################################################

def creazione_nopostel():
	file = open(nopostel, "r") 
	contariga=1
	aperto=0
	nome_precedente=""
	
	for riga in file:
		if contariga==1:
			controllo_riga=riga[66:74]
			nome_file=riga[66:74]+".txt"
			
			#print (contariga)
			
			#if len(nome_file)>3 and nome_file.find(" ")!=-1:
				#CONTROLLO FATTURE CON PIU PAGINE
			if nome_precedente==nome_file or nome_file.find(" ")!=-1:#NUOVA
				print ("appendi")
				out=open(destinazione+nome_precedente.replace("\n",""),"a")
			else:#CONTINUA LA PRECEDENTE
				out=open(destinazione+nome_file.replace("\n",""),"w")
			aperto=1
		contariga=contariga+1
		if aperto==1:
			inserisci=riga
			inserisci=inserisci.replace("2A          T","")
			inserisci=inserisci.replace("2A          C","")
			inserisci=inserisci.replace("2A          S","")
			inserisci=inserisci.replace("2A          F","")
			inserisci=inserisci.replace("21          T","")
			inserisci=inserisci.replace("21          C","")
			inserisci=inserisci.replace("21          S","")
			inserisci=inserisci.replace("21          F","")
			inserisci=inserisci.replace("22          T","")
			inserisci=inserisci.replace("22          C","")
			inserisci=inserisci.replace("22          S","")
			inserisci=inserisci.replace("22          F","")
			inserisci=inserisci.replace("31          T","")
			inserisci=inserisci.replace("31          C","")
			inserisci=inserisci.replace("31          S","")
			inserisci=inserisci.replace("31          F","")
			inserisci=inserisci.replace("4M          T","")
			inserisci=inserisci.replace("4M          C","")
			inserisci=inserisci.replace("4M          S","")
			inserisci=inserisci.replace("4M          F","")
			inserisci=inserisci.strip()
			inserisci=inserisci+"\n"
			out.write(inserisci)
		if riga.find("FCBUNIX FATTURE-MELCHIONI")==1:
			contariga=1
			aperto=0
			nome_precedente=nome_file
			#nome_file.close()


retr_file()
creazione_nopostel()

