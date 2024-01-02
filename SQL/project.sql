create database metaforiki;
use metaforiki

create table ypallhlos(
				AT int,
				Fname varchar(20),
                Lname varchar(20),
                thlefwno int,
                odos varchar(20),
                arithmos_odou int,
                polh varchar(15),
                misthos float,
                eidikothta varchar(20),
                hm.proslipsis date,
                hm.genisis date,
                hlikia int,
                primary key(AT));
                
create table prostateuomena_melh(
				ATpm int,
                onomapm varchar(20),
                fulo char,
                hlikiapm int,
                atupall int,
                primary key(ATpm),
                foreign key(atupall) references ypallhlos(AT));
                
create table grafeia(
				arithmos int,
                onomagr varchar(15),
                thlefwna int,
                odosgr varchar(20),
                arithmosgr int,
                polhgr varchar(15),
                primary key(arithmos));
                
create table pelates(
				afm int,
                odospel varchar(20),
                arithmospel int,
                tkpel int,
                polhpel varchar(15),
                thlefwnapel int,
                primary key(afm));
                
create table fusika_proswpa(
				ATpel int,
                onomapel varchar(20),
                epwnumopel varchar(20),
                afmpel int,
                primary key(ATpel),
                foreign key(afmpel) references pelates(afm));
                
create table etairies(
				atetair int,
                epwnumia varchar(20),
                afmetair int,
                primary key(atetair),
                foreign key(afmetair) references pelates(afm));
                
create table diadromes(
				arithmosdiad int,
                afetiria varchar(20),
                proorismos varchar(20),
                kostos float,
                timh float,
                hmerom.enar date,
                diarkeia float,
                primary key(arithmosdiad));
                
create table pwlhseis(
				arithmospwl int,
                hmerpwl date,
                hmerdiekp date,
                primary key(arithmospwl));
                
create table autokinita(
				arithmosautok int,
                hmkuklof date,
                kuvika int,
                primary key(arithmosautok));
                
create table forthga(
				arithmosfort int,
                xwrhtik float,
                arithmosaut int,
                primary key(arithmosfort),
                foreign key(arithmosaut) references autokinita(arithmosautok));
		
create table epivatika(
				arithmosepiv int,
                theseis int,
                arithmosau int,
                primary key(arithmosepiv),
                foreign key(arithmosau) references autokinita(arithmosautok));
			
create table diadromesforthga(
				arithdf int,
                kostosdf float,
                arithd int,
                arithf int,
                primary key(arithdf),
                foreign key(arithd) references diadromes(arithmosdiad),
                foreign key(arithf) references forthga(arithmosfort));
			
create table pelpwlypal(
				arithppy int,
                paralaviparadwsh varchar(10),
                afmppy int,
                arithpwlpy int,
                atypp int,
                primary key(arithppy),
                foreign key(afmppy) references pelates(afm),
                foreign key(arithpwlpy) references pwlhseis(arithmospwl),
                foreign key(atypp) references ypallhlos(at));
                
UPDATE ypallhlos
set misthos = misthos + 0.1 * misthos
where hm.proslipsis > 1999-01-01 and at=atupall;

delete from pwlhseis
where hmerdiekp > 2017-01-01