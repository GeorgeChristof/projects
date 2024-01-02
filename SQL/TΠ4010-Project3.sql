drop database asfalistikh;
create database asfalistikh;
use asfalistikh;

create table ypallhlous(	atyp int,
							onoma varchar(15),
                            epwnumo varchar(20),
                            thlef varchar(15),
                            dieuth varchar(30),
                            misthos float,
                            hmerprosl date,
                            arithmostmhm int,
                            primary key(atyp));
	
create table dioikit(	atyp int UNIQUE,
						titlosptux varchar(30),
                        etoskthshs date,
                        constraint foreign key(atyp) references ypallhlous(atyp));
                        
create table empeirognwm(	atyp int UNIQUE,
							ethproup int,
							constraint foreign key(atyp) references ypallhlous(atyp));
                        
                            
create table ypokatasthmata( 	arithmos int,
								onoma varchar(15),
                                thlefwna varchar(22),
                                odos varchar(15),
                                arithms int,
                                polh varchar(15),
                                atdieuth int,
                                primary key(arithmos),
                                constraint foreign key (atdieuth) references ypallhlous(atyp));
                                
create table pelates(	AT int,
						onoma varchar(15),
                        epwnumo varchar(20),
                        odos varchar(15),
                        arithmos int,
                        polh varchar(15),
                        ardiplwm int,
                        hmgen date,
                        primary key(AT));
                        
create table autokinhta(	arkuklofor int,
							ergtimh float,
                            eidos varchar(10),
                            kubika int,
                            atpelath int,
							primary key(arkuklofor),
                            constraint foreign key(atpelath) references pelates(AT));
                            
create table prostateuomena(	atypal int,
								onoma varchar(15),
                                fulo char(1),
                                hlikia int,
                                constraint foreign key(atypal) references ypallhlous(atyp));
                                
create table atuxhmata(	arithmos int,
						hmer date,
                        topos varchar(30),
						primary key(arithmos));
                        
create table asfalisthrio(	arasf int,
							enarksh date,
                            lhksh date,
                            aksiaapoz float,
                            timh float,
                            arkuklauto int,
                            atpelath int,
                            arithmosypok int,
                            primary key(arasf),
                            constraint foreign key(arkuklauto) references autokinhta(arkuklofor),
                            constraint foreign key(atpelath) references pelates(AT),
                            constraint foreign key(arithmosypok) references ypokatasthmata(arithmos));
                            
create table pelathsypokat(	arithmosyp int,
							atpelath int,
                            constraint foreign key(arithmosyp) references ypokatasthmata(arithmos),
                            constraint foreign key(atpelath) references pelates(AT));
                            
create table AtAuPelYpal(	arithmosat int,
							arkuklof int,
                            atpelath int,
                            atypal int,
                            kostoszhm float,
                            constraint foreign key(arithmosat) references atuxhmata(arithmos),
                            constraint foreign key(arkuklof) references autokinhta(arkuklofor),
                            constraint foreign key(atpelath) references pelates(AT),
                            constraint foreign key(atypal) references ypallhlous(atyp));
                            
insert into ypallhlous values	(1,'Kwstas','Pappous','6930295031','alikarnasou 75',591.5,'2008-03-01',5),
								(2,'Maria','Lamprou','6992048602','Porou 52',722.8,'2013-09-30',5),
                                (3,'Panagiwths','Paradeigmas','2103849021','athitaki 340',1290.0,'1998-05-21',2);
                                
insert into ypokatasthmata values	(2,'Interamer','2105534291/2109582017','Papamixalh',49,'Athina',3),
									(5,'master','2810496029','Averof',125,'hrakleio',1),
                                    (6,'ion','2110395840/6999999999','Vlasthra',352,'Igoumenitsa',2);

INSERT INTO pelates VALUES ('1', 'Kwsths', 'Kwstakis', 'Plastira', '94', 'Hrakleio', '1', '1990-08-09'); 

insert into autokinhta values(	1,15403.1,'Van',1798,1);

insert into asfalisthrio values	(2,'2013-06-23','2014-02-13',201.3,49.9,1,1,2),
								(3,'2014-09-03','2015-11-19',395.3,89.9,1,1,5),
                                (4,'2016-10-30','2017-03-04',148.3,38.6,1,1,6);

update ypallhlous
set misthos = 0.1 * misthos + misthos
where (year(NOW()) - year(ypallhlous.hmerprosl)) >= 20;

delete from asfalisthrio
where year(NOW()) - year(asfalisthrio.lhksh) >= 5