-- select 'drop table if exists "' || tablename || '" cascade;' from pg_tables  where schemaname = 'public';

drop table if exists "empresa_tipo" cascade;
drop table if exists "festa_tipo" cascade;
drop table if exists "universitaria" cascade;
drop table if exists "bilhete" cascade;
drop table if exists "organizador" cascade;
drop table if exists "locacao" cascade;
drop table if exists "decoracao" cascade;
drop table if exists "floricultura" cascade;
drop table if exists "casamento" cascade;
drop table if exists "transporte" cascade;
drop table if exists "cerimonialista" cascade;
drop table if exists "casamento_cerimonialista" cascade;
