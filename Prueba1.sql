drop table INGESTA;
create table INGESTA (
	Departamento nvarchar(255),
	Especialidad nvarchar(255),
	Grado nvarchar(255),
	[Colegio_Nombre] nvarchar(255),
	[Curso_Nombre] nvarchar(255),
	[Curso_Descripcion] nvarchar(255),
	[Curso_Precio] int
);

drop table LIMPIEZA;
create table LIMPIEZA (
	Departamento nvarchar(255),
	Especialidad nvarchar(255),
	Grado nvarchar(255),
	[Colegio_Nombre] nvarchar(255),
	[Curso_Nombre] nvarchar(255),
	[Curso_Descripcion] nvarchar(255),
	[Curso_Precio] int
)

drop table NULOS_INGESTA;
create table NULOS_INGESTA (
	Departamento nvarchar(255),
	Especialidad nvarchar(255),
	Grado nvarchar(255),
	[Colegio_Nombre] nvarchar(255),
	[Curso_Nombre] nvarchar(255),
	[Curso_Descripcion] nvarchar(255),
	[Curso_Precio] int
)

TRUNCATE TABLE [dbo].[INGESTA]
TRUNCATE TABLE [dbo].[NULOS_INGESTA]
TRUNCATE TABLE [dbo].[LIMPIEZA]

select * from [dbo].[INGESTA]
select * from [dbo].[NULOS_INGESTA]
select * from [dbo].[LIMPIEZA]

delete from [dbo].[LIMPIEZA] where [Curso_Nombre] in ('***Not Applicable***')
update [dbo].[LIMPIEZA] set [Curso_Descripcion] = trim(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE([Curso_Descripcion],'-',' '),'&',' '),'#',' '),'(',' '),')',' '),'*',' '))
update [dbo].[LIMPIEZA] set [Curso_Descripcion] = SUBSTRING([Curso_Descripcion],2,len([Curso_Descripcion])) 
                                                  where SUBSTRING([Curso_Descripcion],1,1) = '.' 
												  or SUBSTRING([Curso_Descripcion],1,1) = ','
												  or SUBSTRING([Curso_Descripcion],1,1) = ' '
update [dbo].[LIMPIEZA] set [Curso_Descripcion] = REPLACE(REPLACE(REPLACE(REPLACE([Curso_Descripcion],'  ',' '),'   ',' '),'    ',' '),'     ',' ')
update [dbo].[LIMPIEZA] set [Curso_Descripcion] = [Curso_Nombre] where len([Curso_Descripcion]) <= 5
update [dbo].[LIMPIEZA] set [Curso_Nombre] = '2015 National Interdiction Conference' where [Curso_Nombre] in ('2015 Nation Interdiction Conference')
update [dbo].[LIMPIEZA] set [Curso_Nombre] = '3 Day Advanced Armorers Course' where [Curso_Nombre] in ('3 Day Advance Armorer''S Coursee','3 Day Advance Armorers Course')
update [dbo].[LIMPIEZA] set [Curso_Nombre] = 'Academic Elaw980' where [Curso_Nombre] in ('3Academic Elai990')

update M1
set M1.[Curso_Descripcion] = M2.[Curso_Descripcion]
from [dbo].[LIMPIEZA] M1
inner join (
			select *
			from (
					select row_number() over(partition by [Curso_Nombre] order by [Curso_Nombre], count([Curso_Nombre]) desc) as ID_P, [Curso_Nombre], [Curso_Descripcion], count([Curso_Nombre]) as CANT
					from [dbo].[LIMPIEZA] 
					group by [Curso_Nombre], [Curso_Descripcion]
			) M1
			where ID_P = 1
) M2
on M1.Curso_Nombre = M2.[Curso_Nombre]
