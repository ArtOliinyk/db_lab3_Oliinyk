INSERT INTO groups(group_id, group_name, number_of_subscribers, creation_date, invitation_link)
VALUES (1, 'binance', 100543,'2013-4-4','t.me/binance'),
       (2, 'bittrex', 5430,'2013-4-4','t.me/bittrex'),
       (3, 'huobi',543624,'2014-4-4','t.me/huobi'),
       (4, 'kucoin',54332,'2014-4-4','t.me/kucoin'),
       (5, 'okex',20634,'2015-4-4','t.me/okex');

INSERT INTO accounts(acc_id, username, phone_number, pseudonym, registration_date)
VALUES (1, 'Artem Oliinyk', 380965592376, 'art.oliinyk', '2015-6-5'),
       (2, 'John', 579837501348, 'johnwazovski', '2015-6-5'),
       (3, 'Cena', 3598723579135, 'teg_greg', '2016-6-5'),
       (4, 'Kto-to', 1357693504673, 'aertert', '2016-6-5'),
       (5, 'Olena', 523578913957, 'gdfds', '2016-6-5'),
       (6, 'Mykola)', 52357892301, 'mykolka', '2017-6-5');

INSERT INTO account_group(acc_id, group_id)
VALUES (1, 1),
       (1, 2),
       (1, 3),
       (2, 2),
       (2, 3),
       (2, 4),
       (3, 3),
       (3, 4),
       (3, 5),
       (4, 1),
       (4, 2),
       (4, 3),
       (5, 2),
       (5, 3),
       (6, 1),
       (6, 2),
       (6, 3),
       (6, 4),
       (6, 5);

