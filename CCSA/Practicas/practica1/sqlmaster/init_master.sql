CREATE USER 'rep_user'@'%' IDENTIFIED BY 's3cr3t';
GRANT REPLICATION SLAVE ON *.* TO 'rep_user'@'%';