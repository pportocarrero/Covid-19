import pandas as pd
import os
import requests
import platform

def working_dir(folder: str):
    
    '''
    Returns the working directory according to the operating system.
    '''
    
    if platform.system() == 'Windows':
        
        return os.chdir('C:/Users/pport/OneDrive/Projects/' + folder + '/')
    
    elif platform.system() == 'Darwin':
        
        return os.chdir('/Users/pportocarrero/OneDrive/Projects/' + folder + '/')


def positivos(filename: str):
    
    '''
    Returns positive cases of Covid-19 in Peru.
    '''
                        
    param_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
                  }

    req = requests.get('https://files.minsa.gob.pe/s/eRqxR35ZCxrzNgr/download', headers=param_headers)

    url_content = req.content

    csv_file = open('positivos_covid.csv', 'wb')

    csv_file.write(url_content)

    csv_file.close()
    
    # DATA CONFIG

    data = pd.read_csv('positivos_covid.csv', delimiter=';')

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].astype(float, errors='raise')

    nan_values = data['FECHA_RESULTADO'].isna().sum()

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].fillna('20211231')  # NaN values are assigned to 31/12/2021

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].astype(float, errors='raise')

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].map('{:.0f}'.format)

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'] * 1

    # WRANGLING

    data['YEAR'] = data['FECHA_RESULTADO'].str[2:4]

    data['MONTH'] = data['FECHA_RESULTADO'].str[4:6]

    data['DAY'] = data['FECHA_RESULTADO'].str[6:8]

    data['DATE'] = data['DAY'] + '/' + data['MONTH'] + '/' + data['YEAR']

    data['DATE'] = pd.to_datetime(data['DATE'])

    data['DATE'] = pd.to_datetime(data['DATE']).dt.strftime('%d/%m/%y')

    data["DATE"] = data["DATE"].astype("datetime64")
                        
    # CREATING AGGREGATES

    aggregate = data.groupby(['DATE']).size()

    weekly_mean = aggregate.rolling(7).mean()

    last_value = aggregate.iloc[-1]

    data['time'] = pd.to_datetime(data['DATE'])
    date = data['time'].dt.date
    date = date.drop_duplicates()
    date = date.astype("datetime64")
    date = date.sort_values(ascending=True)

    df_aggregate = pd.DataFrame({'casos': aggregate, 'media semanal': weekly_mean, 'fecha': pd.date_range('03/06/20', periods=len(aggregate))})

    return df_aggregate.to_excel(filename + '.xlsx')


def positivos_region(departamento: str):

    '''
    Returns the number of daily cases by region in Peru
    :param departamento: The region in Peru to filter out the information
    :return: Daily cases of a specific region in Peru
    '''

    data = pd.read_csv('positivos_covid.csv', delimiter=';')

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].astype(float, errors='raise')

    nan_values = data['FECHA_RESULTADO'].isna().sum()

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].fillna('20211231')  # NaN values are assigned to 31/12/2021

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].astype(float, errors='raise')

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].map('{:.0f}'.format)

    data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'] * 1

    # WRANGLING

    data['YEAR'] = data['FECHA_RESULTADO'].str[2:4]

    data['MONTH'] = data['FECHA_RESULTADO'].str[4:6]

    data['DAY'] = data['FECHA_RESULTADO'].str[6:8]

    data['DATE'] = data['DAY'] + '/' + data['MONTH'] + '/' + data['YEAR']

    data['DATE'] = pd.to_datetime(data['DATE'])

    data['DATE'] = pd.to_datetime(data['DATE']).dt.strftime('%d/%m/%y')

    data["DATE"] = data["DATE"].astype("datetime64")

    casos = data[data['DEPARTAMENTO'] == departamento.upper()]

    agregado_region = casos.groupby(['DATE']).size()

    weekly_mean = agregado_region.rolling(7).mean()

    df_region = pd.DataFrame({'casos': agregado_region, 'media semanal': weekly_mean})

    return df_region.to_excel('regiones/casos_' + departamento + '.xlsx')


def fallecidos(filename: str):
    
    '''
    Return national daily deaths due to Covid-19 in Peru.
    '''
    
    # GET NEW DATA
    param_headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
                      }
    req_deaths = requests.get('https://files.minsa.gob.pe/s/t9AFqRbXw3F55Ho/download', headers=param_headers)
    url_content_deaths = req_deaths.content
    csv_file_deaths = open('fallecidos_covid.csv', 'wb')
    csv_file_deaths.write(url_content_deaths)
    csv_file_deaths.close()
    
    # WORKING THE DATA

    data_deaths = pd.read_csv('fallecidos_covid.csv', delimiter = ';')

    data_deaths['FECHA_FALLECIMIENTO'] = data_deaths['FECHA_FALLECIMIENTO'].astype(float, errors = 'raise')

    data_deaths['FECHA_FALLECIMIENTO'] = data_deaths['FECHA_FALLECIMIENTO'].map('{:.0f}'.format)

    data_deaths['FECHA_FALLECIMIENTO'] = data_deaths['FECHA_FALLECIMIENTO'] * 1

    data_deaths['YEAR'] = data_deaths['FECHA_FALLECIMIENTO'].str[0:4]

    data_deaths['MONTH'] = data_deaths['FECHA_FALLECIMIENTO'].str[4:6]

    data_deaths['DAY'] = data_deaths['FECHA_FALLECIMIENTO'].str[6:8]

    data_deaths['DATE_DEATH'] = data_deaths['DAY'] + '/' + data_deaths['MONTH'] + '/' + data_deaths['YEAR']

    data_deaths['DATE_DEATH'] = pd.to_datetime(data_deaths['DATE_DEATH'])

    data_deaths['DATE_DEATH'] = pd.to_datetime(data_deaths['DATE_DEATH']).dt.strftime('%d/%m/%y')

    data_deaths['DATE_DEATH'] = data_deaths['DATE_DEATH'].astype("datetime64")

    aggregate_deaths = data_deaths.groupby(['DATE_DEATH']).size()

    weekly_mean = aggregate_deaths.rolling(7).mean()

    df_aggregate_deaths = pd.DataFrame({'fallecidos': aggregate_deaths,
                                        'media semanal': weekly_mean,
                                        'fecha': pd.date_range('03/03/20', periods = len(aggregate_deaths))})

    df_aggregate_deaths = pd.DataFrame({'fallecidos': aggregate_deaths})

    return df_aggregate_deaths.to_excel(filename + '.xlsx')


def fallecidos_region(departamento: str):
    
    '''
    Returns the daily deaths by region due to Covid-19 in Peru
    '''
    
    data_deaths = pd.read_csv('fallecidos_covid.csv', delimiter = ';')

    data_deaths['FECHA_FALLECIMIENTO'] = data_deaths['FECHA_FALLECIMIENTO'].astype(float, errors = 'raise')

    data_deaths['FECHA_FALLECIMIENTO'] = data_deaths['FECHA_FALLECIMIENTO'].map('{:.0f}'.format)

    data_deaths['FECHA_FALLECIMIENTO'] = data_deaths['FECHA_FALLECIMIENTO'] * 1

    data_deaths['YEAR'] = data_deaths['FECHA_FALLECIMIENTO'].str[0:4]

    data_deaths['MONTH'] = data_deaths['FECHA_FALLECIMIENTO'].str[4:6]

    data_deaths['DAY'] = data_deaths['FECHA_FALLECIMIENTO'].str[6:8]

    data_deaths['DATE_DEATH'] = data_deaths['DAY'] + '/' + data_deaths['MONTH'] + '/' + data_deaths['YEAR']

    data_deaths['DATE_DEATH'] = pd.to_datetime(data_deaths['DATE_DEATH'])

    data_deaths['DATE_DEATH'] = pd.to_datetime(data_deaths['DATE_DEATH']).dt.strftime('%d/%m/%y')

    data_deaths['DATE_DEATH'] = data_deaths['DATE_DEATH'].astype("datetime64")

    deaths_ama = data_deaths[data_deaths['DEPARTAMENTO'] == departamento.upper()]

    agg_d_ama = deaths_ama.groupby(['DATE_DEATH']).size()

    df_agg_d_ama = pd.DataFrame({'fallecidos': agg_d_ama})

    df_agg_d_ama.to_excel('regiones/fallecidos_' + departamento + '.xlsx')