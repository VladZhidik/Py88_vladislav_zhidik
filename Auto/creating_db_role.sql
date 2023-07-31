create role Auto_user createrole createdb password 'Auto_user_password';
create database Auto_db owner Auto_user encoding 'utf-8';