CREATE TABLE IF NOT EXISTS database_telegram_groups.account_group_test_insert_with_loop
(
    acc_id   INT NOT NULL REFERENCES accounts (acc_id),
    group_id INT NOT NULL REFERENCES groups (group_id),
    PRIMARY KEY (acc_id, group_id)
);

CREATE OR REPLACE FUNCTION random_between(low INT ,high INT)
   RETURNS INT AS
$$
BEGIN
   RETURN floor(random()* (high-low + 1) + low);
END;
$$ language 'plpgsql' STRICT;

DO
$do$
BEGIN
   FOR i IN 1..15 LOOP
      INSERT INTO account_group_test_insert_with_loop
         (acc_id, group_id)
      SELECT random_between(1, 6), random_between(1, 5)
      ON CONFLICT DO NOTHING;
   END LOOP;
END
$do$;

