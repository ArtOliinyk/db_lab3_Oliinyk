CREATE TABLE accounts
(
    acc_id            INT PRIMARY KEY,
    username          VARCHAR(32) NOT NULL,
    phone_number      VARCHAR(15),
    pseudonym         VARCHAR(32),
    registration_date DATE
);

CREATE TABLE groups
(
    group_id              INT PRIMARY KEY,
    group_name            VARCHAR(50),
    number_of_subscribers INT NOT NULL,
    creation_date         DATE,
    invitation_link       VARCHAR(100)
);

CREATE TABLE account_group
(
    acc_id   INT NOT NULL REFERENCES accounts (acc_id),
    group_id INT NOT NULL REFERENCES groups (group_id),
    PRIMARY KEY (acc_id, group_id)
);