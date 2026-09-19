CREATE DATABASE IF NOT EXISTS db_logika_fuzzy;
USE db_logika_fuzzy;

CREATE TABLE tb_domain_usia_bayi (
 id_domain INT AUTO_INCREMENT PRIMARY KEY,
 b_bawah DECIMAL(5,2),
 b_atas DECIMAL(5,2),
 nilai_keanggotaan DECIMAL(4,2),
 fungsi VARCHAR(100)
);

INSERT INTO tb_domain_usia_bayi (b_bawah,b_atas,nilai_keanggotaan,fungsi) VALUES
(0,2.5,1.00,'1'),
(2.5,5,0.00,'(-x+5)/2.5');

CREATE TABLE tb_domain_usia_anak (
 id_domain INT AUTO_INCREMENT PRIMARY KEY,
 b_bawah INT,
 b_atas INT,
 nilai_keanggotaan DECIMAL(4,2),
 fungsi VARCHAR(100)
);

INSERT INTO tb_domain_usia_anak (b_bawah,b_atas,nilai_keanggotaan,fungsi) VALUES
(0,8,1.00,'1'),
(8,12,0.00,'(-x+12)/4');

CREATE TABLE tb_domain_usia_remaja (
 id_domain INT AUTO_INCREMENT PRIMARY KEY,
 b_bawah INT,
 b_atas INT,
 nilai_keanggotaan DECIMAL(4,2),
 fungsi VARCHAR(100)
);

INSERT INTO tb_domain_usia_remaja VALUES
(NULL,0,10,0.00,'0'),
(NULL,10,12,1.00,'(x-10)/2'),
(NULL,12,18,1.00,'1'),
(NULL,18,20,0.00,'(-x+20)/2');

CREATE TABLE tb_domain_usia_pemuda (
 id_domain INT AUTO_INCREMENT PRIMARY KEY,
 b_bawah INT,
 b_atas INT,
 nilai_keanggotaan DECIMAL(4,2),
 fungsi VARCHAR(100)
);

INSERT INTO tb_domain_usia_pemuda VALUES
(NULL,0,15,0.00,'0'),
(NULL,15,18,1.00,'(x-15)/3'),
(NULL,18,22,1.00,'1'),
(NULL,22,25,0.00,'(-x+25)/3');

CREATE TABLE tb_domain_usia_dewasa (
 id_domain INT AUTO_INCREMENT PRIMARY KEY,
 b_bawah INT,
 b_atas INT,
 nilai_keanggotaan DECIMAL(4,2),
 fungsi VARCHAR(100)
);

INSERT INTO tb_domain_usia_dewasa VALUES
(NULL,0,18,0.00,'0'),
(NULL,18,20,1.00,'(x-18)/2'),
(NULL,20,60,1.00,'1'),
(NULL,60,65,0.00,'(-x+65)/5');

CREATE TABLE tb_domain_usia_lansia (
 id_domain INT AUTO_INCREMENT PRIMARY KEY,
 b_bawah INT,
 b_atas INT,
 nilai_keanggotaan DECIMAL(4,2),
 fungsi VARCHAR(100)
);

INSERT INTO tb_domain_usia_lansia VALUES
(NULL,0,60,0.00,'0'),
(NULL,60,65,1.00,'(x-60)/5'),
(NULL,65,75,1.00,'1'),
(NULL,75,80,0.00,'(-x+80)/5');

SHOW TABLES;

SELECT * FROM tb_domain_usia_bayi;
SELECT * FROM tb_domain_usia_anak;
SELECT * FROM tb_domain_usia_remaja;
SELECT * FROM tb_domain_usia_pemuda;
SELECT * FROM tb_domain_usia_dewasa;
SELECT * FROM tb_domain_usia_lansia;