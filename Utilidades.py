#Elimina caracteres especiales
def elimaCarateres(dframe,columna):
    for ch in ['-',':',',','/','#','\*','\?','\.','\'',' ','¿','½','ï',';','&']:
        dframe = dframe.replace({columna: ch} , ' ', regex=True)

#Normalzia los espacios en blanco a 1 cuando son 2,3,4 o 5
def eliminaEspacios(dframe):
    for ch in ['  ','   ','    ','     ']:
        dframe = dframe.replace(ch, ' ', regex=True)

#Coloca el texto con la primera letra eb mayuscula y elimina espacios en los extremos
def normalizaTexto(dframe, campo):
    dframe[campo] = dframe[campo].str.title().str.lstrip().str.rstrip()

#Actualiza todos los valores con base en una condicion
def actualizaValores(dframe ,columnai, valori, columnaf, valorf):
    dfo = dframe.query(columnai+'.str.contains("'+valori+'")', engine='python')
    dframe.loc[dframe[columnai].isin(dfo[columnai]), columnaf] = valorf

#Actualiza todos los valores con base en una lista de coincidencias o que este vacio
def actualizaValores2(dframe ,columnai, valori, columnaf, valorf ,lvalor):
    dfBase = dframe.query(columnai+'.str.contains("'+valori+'") & ~'+columnaf+'.isin(['+lvalor+']) | '+columnaf+'.isnull()', engine='python')
    listasch = list(set(dfBase[columnai]))
    for sch in listasch:
        dframe.loc[dframe[columnai] == sch, 'Grado'] = valorf

#Crea tabla de dimension
def dimTabs(dfref, columna):
    idlt = columna.upper()[:3]
    dfFin = pd.DataFrame(list(dict.fromkeys(dfref[columna])),columns=[columna]).sort_values(by=[columna]).reset_index(drop=True)
    dfFin[columna] = dfFin[columna].str.upper()
    dfFin['id'] =  idlt+dfFin.index.map(str)
    dfFin = dfFin[['id',columna]]
    return dfFin