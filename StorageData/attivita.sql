CREATE TABLE nearyou.activity(
  activity_uuid UUID,
  name String,
  longitude Float64,
  latitude Float64,
  address String,
  type String,
  description String,
  PRIMARY KEY(activity_uuid)
) ENGINE = MergeTree()
ORDER BY activity_uuid;


INSERT INTO nearyou.activity (activity_uuid, name, longitude, latitude, address, type, description) VALUES
(generateUUIDv4(), 'Vergerio, Nugnes e Giannelli SPA', 11.8605112, 45.4078018, 'Piazza Lucia, Civitella Di Romagna, Guidomandri, Reggio Calabria, 20049, Italia', 'Teatro', 'Scuola di recitazione'),
(generateUUIDv4(), 'Roncalli e figli', 11.8708361, 45.40904, 'Borgo Renzi, Roccantica, St. Moritz Ulten, Oristano, 20861, Italia', 'Cultura', 'Cinema'),
(generateUUIDv4(), 'Matteotti, Spadafora e Montalti Group', 11.9044239, 45.3876686, 'Incrocio Bonomo, Cremnago, Festiona, Crotone, 14012, Italia', 'Fotografia', 'Negozio di fotografia'),
(generateUUIDv4(), 'Trombetta SPA', 11.8586484, 45.3987484, 'Viale Angelo, Sticciano, Castagnole Monferrato, Agrigento, 21053, Italia', 'Musica', 'Sala concerti'),
(generateUUIDv4(), 'Ravaglioli, Abba e Chigi Group', 11.8881579, 45.4258293, 'Incrocio Giulietta, Pinzano Al Tagliamento, Pavignano, Napoli, 43029, Italia', 'Fitness', 'Centro di danza'),
(generateUUIDv4(), 'Paltrinieri-Agostinelli Group', 11.8789116, 45.3919339, 'Via Zaira, Escolca, Novalesa, Reggio Calabria, 98158, Italia', 'Tecnologia', 'Centro riparazioni'),
(generateUUIDv4(), 'Gregorio, Casellati e Liverotti SPA', 11.8864676, 45.4225168, 'Strada Battaglia, Conche Di Codevigo, Moerna, Lucca, 26028, Italia', 'Moda', 'Negozio di abbigliamento'),
(generateUUIDv4(), 'Sanguineti, Tuzzolino e Boccaccio Group', 11.9070736, 45.3606999, 'Contrada Sante, Miglianico, La California, Potenza, 14013, Italia', 'Musica', 'Scuola di musica'),
(generateUUIDv4(), 'Errani, Comeriato e Modigliani Group', 11.8908411, 45.3882005, 'Vicolo Pompeo, Cannalonga, Renate, Catanzaro, 23886, Italia', 'Fotografia', 'Studio fotografico'),
(generateUUIDv4(), 'Bulzoni, Mogherini e Caffarelli SPA', 11.9001283, 45.3996491, 'Stretto Rosmini, Boscone, Rocchetta A Volturno, Vibo Valentia, 31056, Italia', 'Sport', 'Piscina'),
(generateUUIDv4(), 'Opizzi, Segni e Mercalli s.r.l.', 11.8283311, 45.4029588, 'Vicolo Adriano, Casalbordino Stazione, Bressanone, Lecce, 84065, Italia', 'Fitness', 'Studio di pilates'),
(generateUUIDv4(), 'Sansoni e figli', 11.8673015, 45.3832271, 'Via Elmo, Ghibullo, Spercenigo, Bologna, 83044, Italia', 'Viaggi', 'Agenzia di viaggi'),
(generateUUIDv4(), 'Armani e figli', 11.8833322, 45.3823949, 'Piazza Zito, Denice, Cosio Stazione, Palermo, 09084, Italia', 'Educazione', 'Scuola di lingue'),
(generateUUIDv4(), 'Fusani-Detti s.r.l.', 11.8566444, 45.3993852, 'Viale Marta, Safforze, Villa San Vincenzo, Mantova, 31011, Italia', 'Teatro', 'Teatro di prosa'),
(generateUUIDv4(), 'Abatantuono, Stefanelli e Bignardi Group', 11.8804919, 45.4270868, 'Piazza Mattia, Geromina, Barberino Di Mugello, Forl-Cesena, 00038, Italia', 'Cultura', 'Biblioteca'),
(generateUUIDv4(), 'Bianchi-Palmisano s.r.l.', 11.8406898, 45.3567559, 'Viale Ungaretti, Sanarica, Arcugnano, Treviso, 44011, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Vitturi-Omma e figli', 11.9073475, 45.4155147, 'Borgo Ornella, Bardi, Masi Di Cavalese, Potenza, 00037, Italia', 'Natura', 'Giardino botanico'),
(generateUUIDv4(), 'Valmarana-Fracci Group', 11.8290105, 45.3992935, 'Via Fantozzi, Carrabba, Beinasco, Forli Cesena, 84049, Italia', 'Natura', 'Vivaio'),
(generateUUIDv4(), 'Zecchini Group', 11.867189, 45.3855723, 'Incrocio Malatesta, Acciaroli, Monte Cremasco, Ancona, 87075, Italia', 'Ristorazione', 'Caffetteria'),
(generateUUIDv4(), 'Abatantuono e figli', 11.8617144, 45.3880958, 'Strada Sagese, Viu, Rossana, Padova, 33016, Italia', 'Fitness', 'Studio di pilates'),
(generateUUIDv4(), 'Verga-Berengario SPA', 11.8544977, 45.4254872, 'Rotonda Salvo, San Rocco Al Porto, Petrosino, Aosta, 20025, Italia', 'Fitness', 'Centro di danza'),
(generateUUIDv4(), 'Mancini s.r.l.', 11.8408297, 45.3967739, 'Strada Randazzo, Zinasco Nuovo, Libertinia, Novara, 27035, Italia', 'Sport', 'Piscina'),
(generateUUIDv4(), 'Smirnoff', 11.873857, 45.4151801, 'Contrada Giulia, Cavagnolo, San Martino Di San Prospero, Brindisi, 25028, Italia', 'Natura', 'Giardino botanico'),
(generateUUIDv4(), 'Zanzi, Castelli e Fornaciari s.r.l.', 11.9195254, 45.3698032, 'Stretto Versace, Montalcino, Barasso, Enna, 23874, Italia', 'Sport', 'Campo da tennis'),
(generateUUIDv4(), 'Iannucci SPA', 11.8818499, 45.4157205, 'Viale Annalisa, Oberboze, Pozzolatico, Medio Campidano, 60026, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Vianello, Adinolfi e Troisi Group', 11.8876605, 45.4042787, 'Contrada Folliero, San Vittore, Cuccaro Monferrato, L''Aquila, 02049, Italia', 'Musica', 'Scuola di musica'),
(generateUUIDv4(), 'Cherubini, Ponti e Gentileschi SPA', 11.861848, 45.3986583, 'Viale Veneziano, Castana, Trigolo, Verbano-Cusio-Ossola, 38031, Italia', 'Teatro', 'Scuola di recitazione'),
(generateUUIDv4(), 'Cipolla-Franzese SPA', 11.8710421, 45.3845914, 'Via Pizziol, Borno, Rodeneck, Ancona, 34148, Italia', 'Cultura', 'Museo'),
(generateUUIDv4(), 'Turati SPA', 11.9027805, 45.4139638, 'Viale Cattaneo, Moggio Di Sotto, San Marco Dei Cavoti, Pesaro e Urbino, 26044, Italia', 'Cultura', 'Biblioteca'),
(generateUUIDv4(), 'Coppola SPA', 11.8996191, 45.3783412, 'Contrada Giosu, Olivola, Borgo Hermada, Cosenza, 41100, Italia', 'Educazione', 'Scuola di lingue'),
(generateUUIDv4(), 'Argurio-Belletini s.r.l.', 11.8700493, 45.4061813, 'Canale Carolina, Piova'' Massaia, Ciavolotto, Asti, 37043, Italia', 'Moda', 'Sartoria'),
(generateUUIDv4(), 'Einaudi-Turati e figli', 11.841922, 45.4096135, 'Canale Luxardo, Prato All''Isarco, Palombaio, Bolzano, 30031, Italia', 'Teatro', 'Teatro sperimentale'),
(generateUUIDv4(), 'Monduzzi, Bellocchio e Mazzanti e figli', 11.8717753, 45.3887319, 'Piazza Bianca, Cerlongo, Vitolini, Pisa, 71023, Italia', 'Sport', 'Palestra'),
(generateUUIDv4(), 'Sandi e figli', 11.8680394, 45.378989, 'Incrocio Margherita, Moehlen In Taufer, Casa Castalda, Roma, 06046, Italia', 'Arte', 'Scuola d''arte'),
(generateUUIDv4(), 'Ferrabosco-Antonetti SPA', 11.8500318, 45.3745312, 'Strada Ivan, Rocca Massima, Missian, Pesaro e Urbino, 32040, Italia', 'Viaggi', 'Ufficio turistico'),
(generateUUIDv4(), 'Camicione e figli', 11.8056397, 45.3785496, 'Strada Germano, Piansano, Tivolille, Como, 36030, Italia', 'Cinema', 'Cinema multisala'),
(generateUUIDv4(), 'Esposito-Giunti e figli', 11.8883294, 45.4153767, 'Viale Galuppi, Casciago, Pastena Di Salerno, Verbano-Cusio-Ossola, 43052, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Bianchi, Capone e Natta Group', 11.8835593, 45.3878128, 'Rotonda Francesca, Bondone, Torcino, Macerata, 10060, Italia', 'Ristorazione', 'Pub'),
(generateUUIDv4(), 'Carducci-Gargallo e figli', 11.8758195, 45.3909722, 'Via Virgilio, Valgatara, Ravello, Siena, 61038, Italia', 'Arte', 'Scuola d''arte'),
(generateUUIDv4(), 'Ruggieri, Canova e Babbo e figli', 11.8529968, 45.378389, 'Canale Serafina, Cursi, Villa Basilica, Avellino, 02049, Italia', 'Fotografia', 'Negozio di fotografia'),
(generateUUIDv4(), 'Piovani-Tognazzi Group', 11.8764582, 45.4165255, 'Piazza Querini, Padiglione, Ripe San Ginesio, Arezzo, 81037, Italia', 'Fotografia', 'Studio fotografico'),
(generateUUIDv4(), 'Bosio, Scaduto e Pignatti Group', 11.9021978, 45.3802045, 'Viale Roth, Castroreale Terme, Paullo, Caserta, 37026, Italia', 'Cultura', 'Cinema'),
(generateUUIDv4(), 'Tamborini, Balbi e Ruggieri e figli', 11.9073694, 45.4056971, 'Via Galiazzo, Vico Equense, Orbetello Stazione, Lecco, 07013, Italia', 'Cultura', 'Museo'),
(generateUUIDv4(), 'Marini-Pepe SPA', 11.8780171, 45.4008459, 'Viale Parisi, Caronte, Montegemoli, Novara, 93017, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Angiolello s.r.l.', 11.838113, 45.3979555, 'Vicolo Martino, Cortenova, Corio, Verbano-Cusio-Ossola, 41030, Italia', 'Musica', 'Club musicale'),
(generateUUIDv4(), 'Errani, Micca e Delle e figli', 11.9010922, 45.3972262, 'Contrada Vento, Sigillo Di Posta, Alzano Scrivia, Verbano-Cusio-Ossola, 63848, Italia', 'Giochi', 'Negozio di giochi'),
(generateUUIDv4(), 'Tasca, Bosurgi e Blasi Group', 11.8407789, 45.3968849, 'Canale Antonella, Airali, Fobello, Siena, 98021, Italia', 'Ristorazione', 'Pub'),
(generateUUIDv4(), 'Pisano-Petrassi e figli', 11.8913139, 45.4244568, 'Vicolo Natalia, San Pietro In Guarano, Semestene, Isernia, 13821, Italia', 'Giochi', 'Negozio di giochi'),
(generateUUIDv4(), 'Tarantino Group', 11.8295413, 45.3967857, 'Contrada Sophia, Mandriola, Montesano Salentino, Messina, 72017, Italia', 'Fitness', 'Centro benessere'),
(generateUUIDv4(), 'Nicolucci s.r.l.', 11.8888459, 45.3987381, 'Piazza Gargallo, Fasani, Colleferro Stazione, Agrigento, 98047, Italia', 'Arte', 'Studio privato'),
(generateUUIDv4(), 'Mazzacurati-Antelami s.r.l.', 11.8408433, 45.3626564, 'Canale Michelotto, Vasia, Gassano, Oristano, 63847, Italia', 'Viaggi', 'Agenzia di viaggi'),
(generateUUIDv4(), 'Antonini, Galiazzo e Segni Group', 11.902397, 45.4159014, 'Piazza Evangelista, Castelguidone, Plesio, Forl-Cesena, 85040, Italia', 'Tecnologia', 'Centro riparazioni'),
(generateUUIDv4(), 'Gussoni, Perini e Pigafetta Group', 11.8632592, 45.3601502, 'Rotonda Vincentio, Vazia, Ceriale, Gorizia, 95122, Italia', 'Musica', 'Scuola di musica'),
(generateUUIDv4(), 'Lamborghini, Battaglia e Germano SPA', 11.8538728, 45.3831108, 'Stretto Eugenia, San Valentino Torio, Castelnuovo Vomano, Messina, 43036, Italia', 'Educazione', 'Scuola di lingue'),
(generateUUIDv4(), 'Mantegna e figli', 11.8774879, 45.4256942, 'Rotonda Matilda, Vittorio Veneto, Faggeto Lario, Oristano, 98028, Italia', 'Tecnologia', 'Centro riparazioni'),
(generateUUIDv4(), 'Maggioli, Carducci e Toselli s.r.l.', 11.8582018, 45.372988, 'Stretto Angiolello, Sant''Oreste, Pescocanale, Oristano, 52021, Italia', 'Cinema', 'Cineclub'),
(generateUUIDv4(), 'Bembo s.r.l.', 11.8790312, 45.4219143, 'Incrocio Castioni, Maclodio, Nusenna, La Spezia, 02047, Italia', 'Teatro', 'Teatro di prosa'),
(generateUUIDv4(), 'Olivetti, Ceravolo e Franceschi Group', 11.8852733, 45.412886, 'Rotonda Fiorenzo, Coiano, Santa Mama, Lucca, 08019, Italia', 'Cultura', 'Cinema'),
(generateUUIDv4(), 'Liverotti, Faugno e Caracciolo e figli', 11.8760918, 45.3778601, 'Via Calbo, Pozzillo, Cellore, Arezzo, 10126, Italia', 'Sport', 'Piscina'),
(generateUUIDv4(), 'Greco SPA', 11.9196542, 45.3830894, 'Canale Mercalli, Novalesa, Cazzano Di Tramigna, Como, 81032, Italia', 'Teatro', 'Teatro di prosa'),
(generateUUIDv4(), 'Antonucci s.r.l.', 11.8580744, 45.3844441, 'Viale Fo, Castelgomberto, Spicchio, Padova, 20055, Italia', 'Ristorazione', 'Caffetteria'),
(generateUUIDv4(), 'Ferrucci SPA', 11.9035973, 45.3831502, 'Vicolo Patrizia, St. Nikolaus i. Eggen, Preore, Messina, 29010, Italia', 'Cultura', 'Museo'),
(generateUUIDv4(), 'Galeati e figli', 11.8936754, 45.3970109, 'Viale Gemma, Posta Fibreno, Porto Corsini, Catanzaro, 74012, Italia', 'Ristorazione', 'Pizzeria'),
(generateUUIDv4(), 'Peano SPA', 11.8839675, 45.3810282, 'Piazza Onisto, Montorio Nei Frentani, Rossa, Piacenza, 10051, Italia', 'Musica', 'Negozio di dischi'),
(generateUUIDv4(), 'Persico SPA', 11.874109, 45.4154039, 'Borgo Scaramucci, Bruzzano Zeffirio, Albenga, Monza e della Brianza, 13888, Italia', 'Viaggi', 'Ufficio turistico'),
(generateUUIDv4(), 'Bosurgi-Lombardo s.r.l.', 11.8001384, 45.3963634, 'Borgo Gritti, Selva Di Sora, Quattropani, Reggio Calabria, 33098, Italia', 'Fitness', 'Studio di pilates'),
(generateUUIDv4(), 'Emanuelli e figli', 11.8553569, 45.3714311, 'Contrada Bompiani, Ala Di Stura, Sant''Angelo Lodigiano, Vibo Valentia, 14020, Italia', 'Teatro', 'Scuola di recitazione'),
(generateUUIDv4(), 'Ferraris-Prada s.r.l.', 11.8583073, 45.3934969, 'Stretto Liberto, Zapponeta, Fiumara Di Piraino, Livorno, 31034, Italia', 'Fotografia', 'Negozio di fotografia'),
(generateUUIDv4(), 'Zito, Toldo e Andreozzi SPA', 11.9042004, 45.3942655, 'Canale Bernardi, Cadola, Zoldo Alto, Pistoia, 00023, Italia', 'Sport', 'Centro fitness'),
(generateUUIDv4(), 'Giacometti-Nosiglia Group', 11.8922338, 45.3856211, 'Canale Lara, Campobello Di Mazara, Acri, Siena, 31027, Italia', 'Musica', 'Scuola di musica'),
(generateUUIDv4(), 'Panatta-Tarchetti Group', 11.8276183, 45.3737407, 'Viale Peranda, Mezzate, Santa Sofia D''Epiro, Oristano, 45100, Italia', 'Giochi', 'Parco divertimenti'),
(generateUUIDv4(), 'Tuzzolino s.r.l.', 11.8698897, 45.3664452, 'Via Calbo, Talsano, Valcasotto, Bolzano, 88045, Italia', 'Fotografia', 'Studio fotografico'),
(generateUUIDv4(), 'Lopresti-Scandone Group', 11.8731491, 45.3786695, 'Incrocio Ezio, Fornace, Cologna Spiaggia, Brescia, 20031, Italia', 'Arte', 'Studio privato'),
(generateUUIDv4(), 'Argan s.r.l.', 11.8588035, 45.3967487, 'Via Lancisi, Taccone, San Filippo Di Contigliano, Pesaro e Urbino, 66045, Italia', 'Giochi', 'Sala giochi'),
(generateUUIDv4(), 'Greco-Lerner SPA', 11.8855847, 45.37931, 'Vicolo Fiorenzo, Stilves, Raffaellina, Medio Campidano, 86077, Italia', 'Arte', 'Galleria d''arte'),
(generateUUIDv4(), 'Petruzzi Group', 11.8846705, 45.4191338, 'Borgo Tamburini, Frattura, Cugnoli, Lodi, 07043, Italia', 'Sport', 'Campo da tennis'),
(generateUUIDv4(), 'Pederiva e figli', 11.8429047, 45.368439, 'Piazza Taliani, Redondesco, Acquavena, Pisa, 21057, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Scalera-Monteverdi s.r.l.', 11.892979, 45.4214253, 'Incrocio Vincenzo, Oleggio Castello, Campocroce, Novara, 12011, Italia', 'Educazione', 'Scuola di cucina'),
(generateUUIDv4(), 'Caccianemico-Turrini SPA', 11.8616775, 45.4132193, 'Vicolo Ferdinando, Rocca Pietore, Specchia, Perugia, 98152, Italia', 'Cultura', 'Teatro'),
(generateUUIDv4(), 'Rienzo s.r.l.', 11.8678682, 45.3755066, 'Rotonda Cainero, Puntaldia, Ama, Rieti, 39017, Italia', 'Giochi', 'Parco divertimenti'),
(generateUUIDv4(), 'Castellitto-Palmisano e figli', 11.9004825, 45.3803578, 'Rotonda Carullo, San Pietro Vara, Aielli Stazione, Cagliari, 86012, Italia', 'Ristorazione', 'Pizzeria'),
(generateUUIDv4(), 'Galvani Group', 11.9145756, 45.3687886, 'Viale Dallara, Serbariu, San Germano Vercellese, Reggio Calabria, 06064, Italia', 'Fotografia', 'Studio fotografico'),
(generateUUIDv4(), 'Lussu-Buscetta Group', 11.8702904, 45.3772778, 'Rotonda Borsiere, Morre, Cagno'', Asti, 06036, Italia', 'Giochi', 'Sala giochi'),
(generateUUIDv4(), 'Bajardi-Filippini', 11.846173, 45.3757247, 'Via Procacci, Caselle, Casaliggio, Grosseto, 22041, Italia', 'Arte', 'Galleria d''arte'),
(generateUUIDv4(), 'Caccioppoli e figli', 11.893254, 45.4177274, 'Stretto Borrani, Velate, Piediripa, Bari, 85053, Italia', 'Educazione', 'Scuola di cucina'),
(generateUUIDv4(), 'Mennea, Schicchi e Pepe e figli', 11.8635829, 45.3876242, 'Contrada Mastroianni, Massignano, Binanuova, Ascoli Piceno, 65010, Italia', 'Arte', 'Studio privato'),
(generateUUIDv4(), 'Caetani s.r.l.', 11.8699868, 45.3753402, 'Stretto Contrafatto, La Santona, Poianella, Monza e della Brianza, 95010, Italia', 'Musica', 'Club musicale'),
(generateUUIDv4(), 'Contarini, Scaramucci e Morandi Group', 11.8588268, 45.3993889, 'Via Tonino, Altivole, Coltaro, Teramo, 46042, Italia', 'Sport', 'Centro fitness'),
(generateUUIDv4(), 'Castiglione s.r.l.', 11.9063091, 45.3893723, 'Borgo Carla, Elmo, Piane Di Montegiorgio, Ferrara, 10026, Italia', 'Teatro', 'Scuola di recitazione'),
(generateUUIDv4(), 'Iacobucci Group', 11.8690006, 45.3818063, 'Contrada Granatelli, Borghetto Di Vara, San Vito Dei Lombardi, Ravenna, 06083, Italia', 'Tecnologia', 'Centro riparazioni'),
(generateUUIDv4(), 'Gianinazzi-Schicchi e figli', 11.8664613, 45.3842651, 'Canale Venditti, Madonna Dei Fornelli, Ulmi, Parma, 87011, Italia', 'Fotografia', 'Negozio di fotografia'),
(generateUUIDv4(), 'Antonucci s.r.l.', 11.8611661, 45.4197661, 'Contrada Ranieri, Carratiello, San Gillio, Foggia, 84073, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Tirabassi-Vidoni SPA', 11.8997456, 45.3751394, 'Vicolo Palumbo, Mongiuffi Melia, Bozzolo, Nuoro, 23030, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Vasari SPA', 11.897897, 45.4075731, 'Borgo Basadonna, Pianezza, Cupa, Avellino, 00069, Italia', 'Teatro', 'Teatro di prosa'),
(generateUUIDv4(), 'Mengolo, Tartini e Andreozzi Group', 11.8921311, 45.3606911, 'Strada Gaggini, Mathi, Arzerello, Trieste, 84048, Italia', 'Giochi', 'Sala giochi'),
(generateUUIDv4(), 'Naccari, Martinelli e Balbo Group', 11.9047421, 45.408984, 'Rotonda Barzini, Montemezzo, Tignale, Venezia, 20083, Italia', 'Cultura', 'Teatro'),
(generateUUIDv4(), 'Rosselli-Forza s.r.l.', 11.8617775, 45.4133193, 'Incrocio Anita, Tursi, Lupara, Oristano, 26042, Italia', 'Sport', 'Centro fitness'),
(generateUUIDv4(), 'Casalodi, Grimani e Golgi Group', 11.8660622, 45.3962381, 'Borgo Leoncavallo, Montebello Vicentino, Serravalle Pistoiese, Milano, 47035, Italia', 'Natura', 'Parco'),
(generateUUIDv4(), 'Guglielmi-Priuli SPA', 11.9033247, 45.3977318, 'Piazza Leone, San Giovanni Di Ceppaloni, Parmezzana Calzana, Modena, 00026, Italia', 'Ristorazione', 'Bar'),
(generateUUIDv4(), 'Tarantini-Bernardi Group', 11.8703442, 45.3791337, 'Via Alessia, Pontelungo, Sinic, Reggio Calabria, 43013, Italia', 'Ristorazione', 'Pizzeria'),
(generateUUIDv4(), 'Pisano-Bacosi s.r.l.', 11.9116637, 45.4027454, 'Piazza Coluccio, Exilles, Graun Vinschg., Brescia, 85040, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Chindamo s.r.l.', 11.8728204, 45.3900959, 'Incrocio Gualandi, Ponte Della Priula, Polizzello, Napoli, 40065, Italia', 'Natura', 'Parco'),
(generateUUIDv4(), 'Gasperi, Almagi e Lollobrigida SPA', 11.8444214, 45.3785957, 'Contrada Altera, Montegallo, Bellamonte, Grosseto, 51021, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Pellico SPA', 11.8237032, 45.4087505, 'Strada Leblanc, Magaro, Faver, Livorno, 10071, Italia', 'Educazione', 'Scuola di lingue'),
(generateUUIDv4(), 'Venditti SPA', 11.9101723, 45.3950259, 'Strada Almagi, Cascina Buon Gesu'', Rovere Di Rocca Di Mezzo, Palermo, 20032, Italia', 'Giochi', 'Parco divertimenti'),
(generateUUIDv4(), 'Morricone-Mastroianni s.r.l.', 11.8959561, 45.3725496, 'Rotonda Milena, Leverano, Grontardo, L''Aquila, 89843, Italia', 'Ristorazione', 'Pizzeria'),
(generateUUIDv4(), 'Necci-Valentino SPA', 11.8442214, 45.3985957, 'Borgo Gemma, Amato Di Taurianova, Gottolengo, Savona, 17043, Italia', 'Tecnologia', 'Centro riparazioni'),
(generateUUIDv4(), 'Iannotti Group', 11.8551602, 45.4067037, 'Piazza Rossellini, Padula Scalo, Selvena, Bergamo, 26016, Italia', 'Sport', 'Campo sportivo'),
(generateUUIDv4(), 'Tedesco SPA', 11.884212, 45.4177472, 'Viale Alessandra, Squille, La Forma, Massa-Carrara, 67044, Italia', 'Viaggi', 'Agenzia di viaggi'),
(generateUUIDv4(), 'Marenzio, Goldstein e Armani', 11.867438, 45.3978667, 'Piazza Guidone, Paiane, Scarmagno, Belluno, 27024, Italia', 'Ristorazione', 'Bar'),
(generateUUIDv4(), 'Agostini-Greco SPA', 11.8976961, 45.3887001, 'Stretto Giacomo, Recoleta, Acri, Ogliastra, 84096, Italia', 'Natura', 'Vivaio'),
(generateUUIDv4(), 'Trentini Group', 11.8698451, 45.3797184, 'Piazza Veronica, Collelungo, Pescocanale Di Capistrello, Isernia, 26022, Italia', 'Moda', 'Negozio di scarpe'),
(generateUUIDv4(), 'Zoppetti-Anguillara SPA', 11.9056397, 45.3785496, 'Viale Bragadin, Ottati, Castel Dell''Alpi, Gorizia, 26824, Italia', 'Moda', 'Negozio di scarpe'),
(generateUUIDv4(), 'Nitto, Ferrucci e Loredan Group', 11.8851643, 45.3794324, 'Incrocio Pisano, Quinto Di Treviso, Calopezzati, Livorno, 26044, Italia', 'Moda', 'Negozio di scarpe'),
(generateUUIDv4(), 'Vergassola-Palumbo s.r.l.', 11.8716374, 45.3685308, 'Viale Ricciotti, San Giacomo Di Teglio, Solbiate, Sondrio, 95012, Italia', 'Arte', 'Galleria d''arte'),
(generateUUIDv4(), 'Interiano, Paolucci e Taliercio Group', 11.8738186, 45.4242305, 'Piazza Gori, Maissana, Zagarise, Caserta, 00042, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Montesano-Vendetti s.r.l.', 11.8886669, 45.3895841, 'Incrocio Morandini, Sant''Agata Di Puglia, Macchie, Piacenza, 07014, Italia', 'Fitness', 'Centro benessere'),
(generateUUIDv4(), 'Babbo, Boito e Impastato Group', 11.8531805, 45.3615191, 'Vicolo Eugenia, Felline, Albano Sant''Alessandro, Venezia, 28823, Italia', 'Sport', 'Piscina'),
(generateUUIDv4(), 'Gregori Group', 11.9115966, 45.4033204, 'Piazza Viridiana, Centro Urbano, Acconia, Messina, 88068, Italia', 'Musica', 'Scuola di musica'),
(generateUUIDv4(), 'Cicilia-Brambilla Group', 11.8688206, 45.3762965, 'Piazza Gastone, Torre Del Mangano, Chieti Stazione, Perugia, 00043, Italia', 'Fitness', 'Centro benessere'),
(generateUUIDv4(), 'Romagnoli s.r.l.', 11.8654443, 45.3860058, 'Borgo Vezzali, Cavazzoli, Ardenza, Barletta-Andria-Trani, 00184, Italia', 'Ristorazione', 'Caffetteria'),
(generateUUIDv4(), 'Tartini, Cilea e Majewski SPA', 11.8489247, 45.3603691, 'Via Annamaria, Opera, Istrago, Como, 55014, Italia', 'Arte', 'Galleria d''arte'),
(generateUUIDv4(), 'Paolini SPA', 11.8466256, 45.3638929, 'Piazza Dario, Tufariello, Stiava, Treviso, 14013, Italia', 'Fotografia', 'Studio fotografico'),
(generateUUIDv4(), 'Gioberti-Abba e figli', 11.8880759, 45.3966485, 'Stretto Flavio, Pentone, Cerfignano, Monza e della Brianza, 91012, Italia', 'Fotografia', 'Studio fotografico'),
(generateUUIDv4(), 'Balotelli-Giannetti SPA', 11.9066765, 45.3897053, 'Contrada Rocco, Massascusa, Santa Maria Di Bobbio, Taranto, 11013, Italia', 'Tecnologia', 'Negozio di elettronica'),
(generateUUIDv4(), 'Mogherini, Castioni e Stoppani Group', 11.8880943, 45.3984251, 'Vicolo Ignazio, Sarno, Mili San Marco, Arezzo, 07038, Italia', 'Moda', 'Negozio di scarpe'),
(generateUUIDv4(), 'Bignami-Caetani e figli', 11.8694846, 45.3555671, 'Vicolo Francesca, Portula, Filighera, Gorizia, 80025, Italia', 'Musica', 'Sala concerti'),
(generateUUIDv4(), 'Petruzzi, Eco e Perini Group', 11.9187357, 45.3652284, 'Incrocio Ivo, Bisaccia, Cilavegna, Como, 34070, Italia', 'Musica', 'Sala concerti'),
(generateUUIDv4(), 'Lucciano-Mondaini SPA', 11.8911524, 45.405137, 'Contrada Barracco, Borgo Vodice, San Giorgio A Liri, Sondrio, 57031, Italia', 'Moda', 'Boutique'),
(generateUUIDv4(), 'Florio e figli', 11.8639896, 45.3610941, 'Vicolo Perini, Cannara, Sillavengo, Milano, 83020, Italia', 'Cultura', 'Cinema'),
(generateUUIDv4(), 'Andreozzi, Balbo e Storladi e figli', 11.8880985, 45.3909255, 'Piazza Amedeo, Argentiera, Sambiase, Siracusa, 82016, Italia', 'Fotografia', 'Studio fotografico'),
(generateUUIDv4(), 'Tarchetti e figli', 11.9010405, 45.381743, 'Stretto Ippazio, Pollena Trocchia, Fontanile, Siracusa, 84038, Italia', 'Arte', 'Scuola d''arte'),
(generateUUIDv4(), 'Spadafora, Bruno e Fornaciari Group', 11.840367, 45.4116723, 'Viale Achille, Faida, Montecompatri, Cagliari, 08013, Italia', 'Moda', 'Boutique'),
(generateUUIDv4(), 'Morosini, Vigorelli e Toldo SPA', 11.85284, 45.414547, 'Viale Caetani, San Martino Stella, Pineta Di Pescara, Como, 90144, Italia', 'Natura', 'Parco'),
(generateUUIDv4(), 'Manolesso Bellini e figli', 11.8645464, 45.4043881, 'Incrocio Maura, San Giorgio A Cremano, Vico Nel Lazio, Pistoia, 46039, Italia', 'Musica', 'Negozio di dischi'),
(generateUUIDv4(), 'Borrani, Spallanzani e Pedroni s.r.l.', 11.844402, 45.3650009, 'Incrocio Piermaria, Vigo Lomaso, Trecroci, Torino, 26020, Italia', 'Musica', 'Negozio di dischi'),
(generateUUIDv4(), 'Camicione s.r.l.', 11.8531968, 45.378189, 'Canale Sermonti, Calle, Borgo Di Montoro Inferiore, Barletta-Andria-Trani, 97011, Italia', 'Educazione', 'Centro di formazione'),
(generateUUIDv4(), 'Amaldi-Modiano s.r.l.', 11.8388517, 45.4055912, 'Canale Giovanna, Postalesio, Cordignano, Ragusa, 28064, Italia', 'Viaggi', 'Agenzia di viaggi'),
(generateUUIDv4(), 'Pavarotti-Raurica s.r.l.', 11.8681365, 45.4031481, 'Borgo Gianmarco, Sant''Antonino, Mendatica, Macerata, 84027, Italia', 'Natura', 'Vivaio'),
(generateUUIDv4(), 'Catenazzi-Iacovelli e figli', 11.8948866, 45.4010441, 'Incrocio Duse, Cevoli, Villanova Mondovi'', Roma, 28825, Italia', 'Ristorazione', 'Pub'),
(generateUUIDv4(), 'Cuzzocrea SPA', 11.914868, 45.4140207, 'Via Piermaria, Casateia, Verza, Verbano-Cusio-Ossola, 26821, Italia', 'Giochi', 'Escape room'),
(generateUUIDv4(), 'Benussi-Odescalchi e figli', 11.8899032, 45.3681973, 'Stretto Mattia, Villa Basilica, Cogne, Ancona, 25124, Italia', 'Moda', 'Negozio di abbigliamento'),
(generateUUIDv4(), 'Martinelli-Renault e figli', 11.8732368, 45.4132057, 'Vicolo Filippo, Agriano, Orbetello, Agrigento, 12041, Italia', 'Musica', 'Sala concerti'),
(generateUUIDv4(), 'Speri s.r.l.', 11.912532, 45.3944938, 'Borgo Irma, Teglia, Massarella, Arezzo, 09100, Italia', 'Fitness', 'Centro di arti marziali'),
(generateUUIDv4(), 'Ritacca, Cuzzocrea e Carli SPA', 11.8473864, 45.3641571, 'Rotonda Milena, Nuvolera, Crocette, Frosinone, 12053, Italia', 'Sport', 'Campo da calcio'),
(generateUUIDv4(), 'Borzomini-Detti SPA', 11.8852646, 45.4178088, 'Via Cundari, Meduna Di Livenza, Pescarolo, Nuoro, 61010, Italia', 'Ristorazione', 'Ristorante italiano'),
(generateUUIDv4(), 'Bataglia, Curatoli e Praga s.r.l.', 11.9010581, 45.4214312, 'Contrada Antonio, Verceia, Gorzone, Carbonia-Iglesias, 13891, Italia', 'Viaggi', 'Ufficio turistico'),
(generateUUIDv4(), 'Majorana SPA', 11.8630034, 45.410567, 'Vicolo Moschino, Rivarolo Canavese, San Lorenzo Pioppa, Perugia, 15050, Italia', 'Natura', 'Vivaio'),
(generateUUIDv4(), 'Fallaci SPA', 11.8888256, 45.4184393, 'Vicolo Federica, San Martino Spino, Lagaro, Novara, 15030, Italia', 'Musica', 'Club musicale'),
(generateUUIDv4(), 'Fantozzi e figli', 11.8779451, 45.4187849, 'Incrocio Garozzo, Padria, Tiarno Di Sopra, Vercelli, 84036, Italia', 'Fotografia', 'Negozio di fotografia'),
(generateUUIDv4(), 'Sanguineti, Zoppetto e Chechi Group', 11.8852078, 45.4129074, 'Canale Carlo, Specchia Tarantina, Lozio, Pesaro e Urbino, 00033, Italia', 'Fitness', 'Centro di arti marziali'),
(generateUUIDv4(), 'Ponti SPA', 11.8677794, 45.4093941, 'Piazza Paolini, Tereglio, Montecatini Terme, Salerno, 86033, Italia', 'Ristorazione', 'Pub'),
(generateUUIDv4(), 'Mondadori, Tedesco e Scotto SPA', 11.8504962, 45.3763895, 'Strada Stucchi, Montisola, Coreggia, Monza e della Brianza, 95042, Italia', 'Sport', 'Campo da calcio'),
(generateUUIDv4(), 'Ciampi, Juvara e Guarana s.r.l.', 11.8952267, 45.3932784, 'Borgo Passalacqua, Nugola, Cristo, Modena, 50145, Italia', 'Fotografia', 'Negozio di fotografia'),
(generateUUIDv4(), 'Sollima-Romano e figli', 11.9056173, 45.3768703, 'Piazza Nicolucci, Prata, Gaiba, Teramo, 33051, Italia', 'Cinema', 'Cineclub'),
(generateUUIDv4(), 'Impastato, Nicolucci e Sismondi s.r.l.', 11.888367, 45.4184598, 'Incrocio Giacomo, Costacciaro, Cassinelle, Venezia, 13033, Italia', 'Cultura', 'Galleria'),
(generateUUIDv4(), 'Tencalla, Bembo e Antonelli SPA', 11.8997974, 45.3971448, 'Via Grossi, Cerreto Sannita, Centa San Nicolo'', Caltanissetta, 71035, Italia', 'Arte', 'Scuola d''arte'),
(generateUUIDv4(), 'Caboto, Pascarella e Filippini s.r.l.', 11.8501384, 45.3663634, 'Via Pontecorvo, Lariano, Castanea Delle Furie, Ferrara, 43041, Italia', 'Natura', 'Vivaio'),
(generateUUIDv4(), 'Fermi-Vezzali s.r.l.', 11.901482, 45.4090896, 'Via Elena, Solofra, Fossato Di Vico, Piacenza, 07021, Italia', 'Giochi', 'Sala giochi'),
(generateUUIDv4(), 'Oliboni-Ossola SPA', 11.8965564, 45.3693024, 'Strada Mazzocchi, Ville Di Fano, Lucca, Bergamo, 67061, Italia', 'Natura', 'Giardino botanico'),
(generateUUIDv4(), 'Salandra, Abatantuono e Bernardini s.r.l.', 11.8415572, 45.3627742, 'Viale Fernanda, San Pietro Di Milazzo, Santa Paolina, Reggio Emilia, 46047, Italia', 'Giochi', 'Parco divertimenti'),
(generateUUIDv4(), 'Fagiani-Villadicani e figli', 11.917381, 45.3720366, 'Rotonda Aria, Gussago, Accadia, Cagliari, 12049, Italia', 'Fitness', 'Studio di pilates'),
(generateUUIDv4(), 'Ferrabosco-Procacci s.r.l.', 11.9184863, 45.4107009, 'Rotonda Raffaele, Piova'' Massaia, Spilamberto, Lecce, 27058, Italia', 'Teatro', 'Teatro sperimentale'),
(generateUUIDv4(), 'Morricone-Tiepolo s.r.l.', 11.8663643, 45.3817636, 'Strada Atenulf, Anitrella, Gairo, Savona, 03036, Italia', 'Arte', 'Galleria d''arte'),
(generateUUIDv4(), 'Manacorda-Chigi SPA', 11.8441273, 45.3902424, 'Vicolo Arnaldo, La Manna, Castel Raniero, Venezia, 56017, Italia', 'Natura', 'Parco'),
(generateUUIDv4(), 'Peano s.r.l.', 11.8988222, 45.3822188, 'Contrada Ranieri, Rodallo, Piano Maglio, Avellino, 67039, Italia', 'Teatro', 'Scuola di recitazione'),
(generateUUIDv4(), 'Tencalla e figli', 11.8689168, 45.3984143, 'Borgo Fiorino, Nocera Terinese, Castellafiume, Savona, 74022, Italia', 'Ristorazione', 'Pub'),
(generateUUIDv4(), 'Bartoli SPA', 11.8602492, 45.4192816, 'Viale Nicola, Torretta, Sticciano Scalo, Olbia-Tempio, 85040, Italia', 'Moda', 'Sartoria'),
(generateUUIDv4(), 'Folliero-Pedersoli e figli', 11.8488361, 45.3809152, 'Vicolo Giampaolo, Pecorile, Casalbellotto, Piacenza, 47855, Italia', 'Sport', 'Piscina'),
(generateUUIDv4(), 'Mannoia s.r.l.', 11.8874427, 45.4142212, 'Vicolo Veneziano, Giungano, Porto Cervo, Fermo, 87014, Italia', 'Cinema', 'Cinema multisala'),
(generateUUIDv4(), 'Boezio-Cossiga SPA', 11.8743256, 45.4154034, 'Vicolo Jacopo, Castorano, Villa D''Adda, Barletta-Andria-Trani, 04017, Italia', 'Cultura', 'Teatro'),
(generateUUIDv4(), 'Legnante, Combi e Leopardi e figli', 11.8690489, 45.4166022, 'Borgo Irma, Valledoria, Turas, L''Aquila, 83036, Italia', 'Cultura', 'Galleria'),
(generateUUIDv4(), 'Galtarossa, Golgi e Cusano Group', 11.8919886, 45.3760232, 'Strada Claudia, Formello, Carpi, Udine, 26858, Italia', 'Educazione', 'Scuola di lingue'),
(generateUUIDv4(), 'Boaga, Gabbana e Borroni s.r.l.', 11.8668202, 45.3912039, 'Incrocio Ludovica, Santa Maria In Valle, Melzo, Verona, 66015, Italia', 'Natura', 'Parco'),
(generateUUIDv4(), 'Nolcini, Priuli e Cafarchia s.r.l.', 11.9130765, 45.4220287, 'Borgo Tomasetti, Monticelli Brusati, Fermo, Padova, 33018, Italia', 'Viaggi', 'Ufficio turistico'),
(generateUUIDv4(), 'Cassar, Villarosa e Orsini Group', 11.8728672, 45.4202526, 'Borgo Romina, Gallo Di Petriano, Verghereto, Aosta, 91015, Italia', 'Natura', 'Parco'),
(generateUUIDv4(), 'Castellitto-Perini Group', 11.8590924, 45.35552, 'Strada Mozart, Niederdorf, Castelnuovo Vomano, Sondrio, 38015, Italia', 'Fitness', 'Centro di arti marziali'),
(generateUUIDv4(), 'Curatoli Group', 11.878997, 45.3901701, 'Via Dallap, Barrali, Vignale, Reggio Calabria, 84085, Italia', 'Arte', 'Scuola d''arte'),
(generateUUIDv4(), 'Castellitto-Innocenti SPA', 11.8605701, 45.4083395, 'Piazza Anguillara, Dragonetti, Grotticella, Oristano, 63814, Italia', 'Musica', 'Scuola di musica'),
(generateUUIDv4(), 'Stefanelli, Almagi e Chigi Group', 11.8932594, 45.379177, 'Incrocio Dina, Faloppio, Ghezzano, Arezzo, 10014, Italia', 'Viaggi', 'Noleggio auto'),
(generateUUIDv4(), 'Sandi SPA', 11.8599309, 45.3942761, 'Incrocio Morandi, Marina Di Caronia, Lago, Bolzano, 13818, Italia', 'Teatro', 'Teatro sperimentale'),
(generateUUIDv4(), 'Comeriato, Tozzi e Rinaldi s.r.l.', 11.8721121, 45.3728002, 'Piazza Giulietta, Castel Di Leva, Montauro, Napoli, 43024, Italia', 'Viaggi', 'Noleggio auto'),
(generateUUIDv4(), 'Pisaroni e figli', 11.8721793, 45.4224288, 'Stretto Mirko, Dubino, Astrio, Frosinone, 89048, Italia', 'Teatro', 'Scuola di recitazione'),
(generateUUIDv4(), 'Squarcione SPA', 11.8610938, 45.3963145, 'Canale Fiorucci, Laise, Volano, Brescia, 41015, Italia', 'Fitness', 'Centro di danza'),
(generateUUIDv4(), 'Bianchini, Bajardi e Riccardi Group', 11.8215706, 45.413168, 'Incrocio Serena, Passo Di Ripe, Turano, Agrigento, 98020, Italia', 'Ristorazione', 'Bar'),
(generateUUIDv4(), 'Basadonna, Opizzi e Palmisano s.r.l.', 11.9129047, 45.4235503, 'Stretto Tozzo, Palinuro, Baia D''Argento, Monza e della Brianza, 30028, Italia', 'Fotografia', 'Negozio di fotografia'),
(generateUUIDv4(), 'Marrone s.r.l.', 11.8252374, 45.379496, 'Viale Scandone, Corsalone, Sant''Alberto, Perugia, 00153, Italia', 'Arte', 'Scuola d''arte'),
(generateUUIDv4(), 'Pigafetta s.r.l.', 11.8683682, 45.4083406, 'Viale Simeoni, Serravalle Di Chienti, Busetti, Teramo, 84079, Italia', 'Teatro', 'Teatro di prosa'),
(generateUUIDv4(), 'Villadicani-Tafuri Group', 11.8957036, 45.4233223, 'Canale Rapisardi, Colonnata, Ozzano Monferrato, Carbonia-Iglesias, 46031, Italia', 'Fitness', 'Centro benessere'),
(generateUUIDv4(), 'Puglisi, Galilei e Tagliafierro e figli', 11.8631415, 45.3847793, 'Piazza Tanzini, Joppolo, Antole, Chieti, 61040, Italia', 'Giochi', 'Negozio di giochi'),
(generateUUIDv4(), 'Argurio, Brunelleschi e Proietti Group', 11.9014678, 45.3886643, 'Via Pier, San Giacomo Roncole, Caltabellotta, Firenze, 24014, Italia', 'Natura', 'Vivaio'),
(generateUUIDv4(), 'Taccola e figli', 11.8770848, 45.3655479, 'Canale Botticelli, Pergine Valsugana, Fellegara, Treviso, 27038, Italia', 'Educazione', 'Scuola di cucina'),
(generateUUIDv4(), 'Caccianemico SPA', 11.8996645, 45.3788417, 'Borgo Regge, Collevecchio, San Giovanni, Brindisi, 19013, Italia', 'Cinema', 'Cineclub'),
(generateUUIDv4(), 'Sobrero, Gori e Marangoni Group', 11.911616, 45.4025656, 'Canale Redi, Morro D''Oro, Villa D''Asolo, L''Aquila, 50064, Italia', 'Musica', 'Sala concerti'),
(generateUUIDv4(), 'Sollima e figli', 11.86245, 45.3779232, 'Via Parisi, Murisengo, Guidomandri Marina, Carbonia Iglesias, 90045, Italia', 'Musica', 'Club musicale'),
(generateUUIDv4(), 'Altera Group', 11.8813117, 45.3885649, 'Piazza Adele, Nuvolato, Rigoni, Genova, 71010, Italia', 'Fitness', 'Studio di pilates'),
(generateUUIDv4(), 'Babbo-Bombieri Group', 11.848661, 45.4055084, 'Stretto Stefano, Argentiera, Molvena, Biella, 05039, Italia', 'Moda', 'Negozio di scarpe'),
(generateUUIDv4(), 'Guarato-Cassar Group', 11.8685542, 45.4102083, 'Incrocio Ruggero, Casale Monferrato, Planei, Rieti, 30171, Italia', 'Fitness', 'Centro di arti marziali'),
(generateUUIDv4(), 'Montessori s.r.l.', 11.8818534, 45.3922052, 'Canale Dionigi, Buronzo, Maratea, Messina, 33070, Italia', 'Tecnologia', 'Centro riparazioni'),
(generateUUIDv4(), 'Infantino SPA', 11.8209432, 45.4106375, 'Viale Riccardo, Baraggia, Castelnuovo Vallo Stazione, Barletta Andria Trani, 20070, Italia', 'Sport', 'Centro fitness');
