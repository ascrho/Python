
import pandas as pd
import Utilidades as ut

df1 = pd.read_csv('Tuition_Assistance_20240525.csv', encoding='latin1')
dfing = pd.read_csv('Tuition_Assistance_20240525.csv', encoding='latin1')

df1.columns = ["Departamento","Especialidad","Grado","Colegio","Nombre Curso","Descripcion Curso","Precio"]

ut.elimaCarateres(df1,'Colegio')
ut.elimaCarateres(df1,'Nombre Curso')
ut.elimaCarateres(df1,'Descripcion Curso')
ut.eliminaEspacios(df1)
ut.normalizaTexto(df1,'Departamento')
ut.normalizaTexto(df1,'Especialidad')
ut.normalizaTexto(df1,'Grado')
ut.normalizaTexto(df1,'Colegio')
ut.normalizaTexto(df1,'Nombre Curso')
ut.normalizaTexto(df1,'Descripcion Curso')

ut.actualizaValores(df1,'Colegio','Associa','Grado','Certificate')
ut.actualizaValores(df1,'Colegio','Associa','Especialidad','Other/Misc.')

ut.actualizaValores(df1,'Colegio','Society','Grado','Certificate')
ut.actualizaValores(df1,'Colegio','Society','Especialidad','Other/Misc.')

ut.actualizaValores(df1,'Colegio','Center','Grado','Certificate')
ut.actualizaValores(df1,'Colegio','Center','Especialidad','Other/Misc.')

df1 = df1.replace({'Grado': 'Aa'} , 'Associate of Arts', regex=True)

df1 = df1.replace({'Colegio': 'Academi'} , 'Academy', regex=True)

Col = ['Alliance','Academy','Training','Institute','College','School']
for shcoll in Col:
    ut.actualizaValores2(df1,'Colegio',shcoll,'Grado','Associate of Arts',"'Associate of Arts','Bachelors (Ba/Bs)'")

ut.actualizaValores2(df1,'Colegio','College','Grado','Bachelors (Ba/Bs)',"'Associate of Arts','Bachelors (Ba/Bs)'")
ut.actualizaValores2(df1,'Colegio','University','Grado','Masters (Ma/Ms/Mph/Etc.)',"'Masters (Ma/Ms/Mph/Etc.)','Ph.D. (Dcs)','Ph.D. (Dde)','Juris Doctor'")

df1['Especialidad'] = df1['Especialidad'].fillna('General Studies')

df1['Descripcion Curso'] = df1['Descripcion Curso'].fillna(df1['Nombre Curso'])

df1 = df1.replace({'Grado': 'Non-Degree'} , 'Other', regex=True)

df1 = df1.replace({'Precio': 0} , 100, regex=True)

dfCln = df1.dropna().reset_index(drop=True)

dfCln['Precio'] = dfCln['Precio'].astype(int)

dfNulls = dfing[dfing.isna().any(axis=1)].reset_index(drop=True)

with pd.ExcelWriter('Limpieza1.xlsx') as writer:
    dfCln.to_excel(writer,sheet_name='LIMPIEZA')
    dfing.to_excel(writer,sheet_name='INGESTA')
    dfNulls.to_excel(writer,sheet_name='NULOS_INGESTA')
