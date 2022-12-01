# Imports

import streamlit as st
# import streamlit_authenticator as stauth
import plotly.express as px
import os
import pandas as pd
import platform

# Load data from external source

if platform.system() == 'Windows':
    os.chdir('C:/Users/pport/OneDrive/Projects/Covid-19/')  # For Win

if platform.system() == 'Darwin':
    os.chdir('/Users/pportocarrero/OneDrive/Projects/Covid-19/')  # For MacOS

### LOGIN MANAGEMENT

# hashed_passwords = stauth.Hasher(['pportocarrero', 'admin']).generate()
####################

path = r'casos_positivos.xlsx'
path_lineages = r'linajes.xlsx'
path_lineages_2 = r'linajes_2.xlsx'
path_deaths = r'casos_fallecidos.xlsx'
path_ama = r'regiones/casos_amazonas.xlsx'
path_anc = r'regiones/casos_ancash.xlsx'
path_apu = r'regiones/casos_apurimac.xlsx'
path_are = r'regiones/casos_arequipa.xlsx'
path_aya = r'regiones/casos_ayacucho.xlsx'
path_caj = r'regiones/casos_cajamarca.xlsx'
path_cal = r'regiones/casos_callao.xlsx'
path_cus = r'regiones/casos_cusco.xlsx'
path_hlv = r'regiones/casos_huancavelica.xlsx'
path_hua = r'regiones/casos_huanuco.xlsx'
path_ica = r'regiones/casos_ica.xlsx'
path_jun = r'regiones/casos_junin.xlsx'
path_lal = r'regiones/casos_la libertad.xlsx'
path_lam = r'regiones/casos_lambayeque.xlsx'
path_lim = r'regiones/casos_lima.xlsx'
path_lor = r'regiones/casos_loreto.xlsx'
path_mad = r'regiones/casos_madre de dios.xlsx'
path_moq = r'regiones/casos_moquegua.xlsx'
path_pas = r'regiones/casos_pasco.xlsx'
path_piu = r'regiones/casos_piura.xlsx'
path_pun = r'regiones/casos_puno.xlsx'
path_san = r'regiones/casos_san martin.xlsx'
path_tac = r'regiones/casos_tacna.xlsx'
path_tum = r'regiones/casos_tumbes.xlsx'
path_uca = r'regiones/casos_ucayali.xlsx'

path_d_ama = r'regiones/fallecidos_amazonas.xlsx'
path_d_anc = r'regiones/fallecidos_ancash.xlsx'
path_d_apu = r'regiones/fallecidos_apurimac.xlsx'
path_d_are = r'regiones/fallecidos_arequipa.xlsx'
path_d_aya = r'regiones/fallecidos_ayacucho.xlsx'
path_d_caj = r'regiones/fallecidos_cajamarca.xlsx'
path_d_cal = r'regiones/fallecidos_callao.xlsx'
path_d_cus = r'regiones/fallecidos_cusco.xlsx'
path_d_hlv = r'regiones/fallecidos_huancavelica.xlsx'
path_d_hua = r'regiones/fallecidos_huanuco.xlsx'
path_d_ica = r'regiones/fallecidos_ica.xlsx'
path_d_jun = r'regiones/fallecidos_junin.xlsx'
path_d_lal = r'regiones/fallecidos_la libertad.xlsx'
path_d_lam = r'regiones/fallecidos_lambayeque.xlsx'
path_d_lim = r'regiones/fallecidos_lima.xlsx'
path_d_lor = r'regiones/fallecidos_loreto.xlsx'
path_d_mad = r'regiones/fallecidos_madre de dios.xlsx'
path_d_moq = r'regiones/fallecidos_moquegua.xlsx'
path_d_pas = r'regiones/fallecidos_pasco.xlsx'
path_d_piu = r'regiones/fallecidos_piura.xlsx'
path_d_pun = r'regiones/fallecidos_puno.xlsx'
path_d_san = r'regiones/fallecidos_san martin.xlsx'
path_d_tac = r'regiones/fallecidos_tacna.xlsx'
path_d_tum = r'regiones/fallecidos_tumbes.xlsx'
path_d_uca = r'regiones/fallecidos_ucayali.xlsx'

df_casos = pd.read_excel(path)
df_ama = pd.read_excel(path_ama)
df_anc = pd.read_excel(path_anc)
df_apu = pd.read_excel(path_apu)
df_are = pd.read_excel(path_are)
df_aya = pd.read_excel(path_aya)
df_caj = pd.read_excel(path_caj)
df_cal = pd.read_excel(path_cal)
df_cus = pd.read_excel(path_cus)
df_hlv = pd.read_excel(path_hlv)
df_hua = pd.read_excel(path_hua)
df_ica = pd.read_excel(path_ica)
df_jun = pd.read_excel(path_jun)
df_lal = pd.read_excel(path_lal)
df_lam = pd.read_excel(path_lam)
df_lim = pd.read_excel(path_lim)
df_lor = pd.read_excel(path_lor)
df_mad = pd.read_excel(path_mad)
df_moq = pd.read_excel(path_moq)
df_pas = pd.read_excel(path_pas)
df_piu = pd.read_excel(path_piu)
df_pun = pd.read_excel(path_pun)
df_san = pd.read_excel(path_san)
df_tac = pd.read_excel(path_tac)
df_tum = pd.read_excel(path_tum)
df_uca = pd.read_excel(path_uca)

df_deaths = pd.read_excel(path_deaths)
df_d_ama = pd.read_excel(path_d_ama)
df_d_anc = pd.read_excel(path_d_anc)
df_d_apu = pd.read_excel(path_d_apu)
df_d_are = pd.read_excel(path_d_are)
df_d_aya = pd.read_excel(path_d_aya)
df_d_caj = pd.read_excel(path_d_caj)
df_d_cal = pd.read_excel(path_d_cal)
df_d_cus = pd.read_excel(path_d_cus)
df_d_hlv = pd.read_excel(path_d_hlv)
df_d_hua = pd.read_excel(path_d_hua)
df_d_ica = pd.read_excel(path_d_ica)
df_d_jun = pd.read_excel(path_d_jun)
df_d_lal = pd.read_excel(path_d_lal)
df_d_lam = pd.read_excel(path_d_lam)
df_d_lim = pd.read_excel(path_d_lim)
df_d_lor = pd.read_excel(path_d_lor)
df_d_mad = pd.read_excel(path_d_mad)
df_d_moq = pd.read_excel(path_d_moq)
df_d_pas = pd.read_excel(path_d_pas)
df_d_piu = pd.read_excel(path_d_piu)
df_d_pun = pd.read_excel(path_d_pun)
df_d_san = pd.read_excel(path_d_san)
df_d_tac = pd.read_excel(path_d_tac)
df_d_tum = pd.read_excel(path_d_tum)
df_d_uca = pd.read_excel(path_d_uca)

df_lineages = pd.read_excel(path_lineages)
df_lineages_2 = pd.read_excel(path_lineages_2)

# Sidebar

types = {'Información': ['Casos positivos',
                         # 'Hospitalizados',
                         'Fallecidos',
                         # 'Vacunación',
                         'Linajes'
                         ]}
types_df = pd.DataFrame(types)
clist = types_df['Información'].unique()
sidebar_options = st.sidebar.selectbox('Seleccione la información a visualizar:', clist)

# MAIN

# CONFIRMED CASES


if sidebar_options == 'Casos positivos':

    st.title('Casos Covid-19 a nivel nacional')

    # Description
    st.write('Casos positivos reportados a través del portal de datos abiertos del '
             'Ministerio de Salud.')

    # Display the chart

    fig_casos = px.line(df_casos, x='DATE', y='media semanal',
                        color_discrete_sequence=['blue'] * len(df_casos),
                        #labels=dict(x="Fecha", y="Promedio semanal"),
                        height=600, width=1000
                        )

    fig_casos.add_scatter(x=df_casos['DATE'], y=df_casos['casos'],
                          #labels=dict(x='Fecha', y='Casos diarios')
                          )

    fig_casos.update_traces(
        #name='sample 1',
        mode='lines',
        #error_y=dict(color='black', width=5, thickness=1),
        #marker=dict(color='red', size=10),
        #line=dict(color='blue', width=3),
        showlegend=True
    )
    #fig_casos = px.bar(df_casos, x='DATE', y='casos',
    #                   color_discrete_sequence=['blue'] * len(df_casos),
    #                   labels={'DATE': 'Fecha', 'casos': 'Número de casos'}, height=600, width=1000)

    #fig_casos.add_scatter(df_casos, x='DATE', y='media semanal', labels={'media semanal': 'Media semanal de casos'})

    st.plotly_chart(fig_casos, use_container_width=True)

    # Seleccionar por departamento

    regiones = {
        'Departamento': [
            'Amazonas', 'Áncash', 'Apurímac', 'Arequipa', 'Ayacucho', 'Cajamarca', 'Callao', 'Cusco', 'Huancavelica', 'Huánuco', 'Ica', 'Junín', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 'Madre de Dios', 'Moquegua', 'Pasco', 'Piura', 'Puno', 'San Martín', 'Tacna', 'Tumbes', 'Ucayali'
                                 ]
    }

    reg_df = pd.DataFrame(regiones)
    clist = reg_df['Departamento'].unique()
    reg_select = st.selectbox('Seleccione un departamento:', clist)

    if reg_select == 'Amazonas':

        fig_ama = px.bar(df_ama, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_ama),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)

        st.plotly_chart(fig_ama, use_container_width=True)

    elif reg_select == 'Áncash':

        fig_anc = px.bar(df_anc, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_anc),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_anc, use_container_width=True)

    elif reg_select == 'Apurímac':

        fig_apu = px.bar(df_apu, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_apu),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_apu, use_container_width=True)

    elif reg_select == 'Arequipa':

        fig_are = px.bar(df_are, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_are),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_are, use_container_width=True)

    elif reg_select == 'Ayacucho':

        fig_aya = px.bar(df_aya, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_aya),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_aya, use_container_width=True)

    elif reg_select == 'Cajamarca':

        fig_caj = px.bar(df_caj, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_caj),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_caj, use_container_width=True)

    elif reg_select == 'Callao':

        fig_cal = px.bar(df_cal, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_cal),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_cal, use_container_width=True)

    elif reg_select == 'Cusco':

        fig_cus = px.bar(df_cus, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_cus),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_cus, use_container_width=True)

    elif reg_select == 'Huancavelica':

        fig_hlv = px.bar(df_hlv, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_hlv),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_hlv, use_container_width=True)

    elif reg_select == 'Huánuco':

        fig_hua = px.bar(df_hua, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_hua),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_hua, use_container_width=True)

    elif reg_select == 'Ica':

        fig_ica = px.bar(df_ica, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_ica),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_ica, use_container_width=True)

    elif reg_select == 'Junín':

        fig_jun = px.bar(df_jun, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_jun),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_jun, use_container_width=True)

    elif reg_select == 'La Libertad':

        fig_lal = px.bar(df_lal, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_lal),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_lal, use_container_width=True)

    elif reg_select == 'Lambayeque':

        fig_lam = px.bar(df_lam, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_lam),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_lam, use_container_width=True)

    elif reg_select == 'Lima':

        fig_lim = px.bar(df_lim, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_lim),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_lim, use_container_width=True)

    elif reg_select == 'Loreto':

        fig_lor = px.bar(df_lor, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_lor),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_lor, use_container_width=True)

    elif reg_select == 'Madre de Dios':

        fig_mad = px.bar(df_mad, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_mad),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_mad, use_container_width=True)

    elif reg_select == 'Moquegua':

        fig_moq = px.bar(df_moq, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_moq),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_moq, use_container_width=True)

    elif reg_select == 'Pasco':

        fig_pas = px.bar(df_pas, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_pas),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_pas, use_container_width=True)

    elif reg_select == 'Piura':

        fig_piu = px.bar(df_piu, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_piu),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_piu, use_container_width=True)

    elif reg_select == 'Puno':

        fig_pun = px.bar(df_pun, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_pun),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_pun, use_container_width=True)

    elif reg_select == 'San Martín':

        fig_san = px.bar(df_san, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_san),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_san, use_container_width=True)

    elif reg_select == 'Tacna':

        fig_tac = px.bar(df_tac, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_tac),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_tac, use_container_width=True)

    elif reg_select == 'Tumbes':

        fig_tum = px.bar(df_tum, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_tum),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_tum, use_container_width=True)

    elif reg_select == 'Ucayali':

        fig_uca = px.bar(df_uca, x='DATE', y='casos',
                         color_discrete_sequence=['red'] * len(df_uca),
                         labels={'DATE': 'Fecha', 'casos': 'Número de casos'},
                         height=600, width=1000)
        st.plotly_chart(fig_uca, use_container_width=True)

# HOSPITALIZATIONS

# elif sidebar_options == 'Hospitalizados':

#    'Próximamente'

# DEATHS

elif sidebar_options == 'Fallecidos':

    fig_deaths = px.bar(df_deaths, x='DATE_DEATH', y='fallecidos', color_discrete_sequence=['black'] * len(df_deaths),
                        labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'}, height=600, width=1000)
    st.title('Fallecidos por Covid-19 a nivel nacional')
    st.write(
        'Fallecidos reportados a través del portal de datos abiertos del Ministerio de Salud. La data reportada se clasifica mediante el cumplimiento de al menos uno de los criterios técnicos: (1) Virológico; (2) Serológico; (3) Radiológico; (4) Nexo epidemiológico; (5) Investigación epidemiológica; (6) Clínico; (7) SINADEF.')
    st.plotly_chart(fig_deaths, use_container_width=True)

    regiones = {'Departamento': ['Amazonas', 'Áncash', 'Apurímac', 'Arequipa', 'Ayacucho', 'Cajamarca',
                                 'Callao', 'Cusco', 'Huancavelica', 'Huánuco', 'Ica', 'Junín',
                                 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 'Madre de Dios', 'Moquegua',
                                 'Pasco', 'Piura', 'Puno', 'San Martín', 'Tacna', 'Tumbes',
                                 'Ucayali'
                                 ]}
    reg_df = pd.DataFrame(regiones)
    clist = reg_df['Departamento'].unique()
    reg_select = st.selectbox('Seleccione un departamento:', clist)

    if reg_select == 'Amazonas':

        fig_ama = px.bar(df_d_ama, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_ama),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_ama, use_container_width=True)

    elif reg_select == 'Áncash':

        fig_anc = px.bar(df_d_anc, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_anc),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_anc, use_container_width=True)

    elif reg_select == 'Apurímac':

        fig_apu = px.bar(df_d_apu, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_apu),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_apu, use_container_width=True)

    elif reg_select == 'Arequipa':

        fig_are = px.bar(df_d_are, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_are),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_are, use_container_width=True)

    elif reg_select == 'Ayacucho':

        fig_aya = px.bar(df_d_aya, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_aya),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_aya, use_container_width=True)

    elif reg_select == 'Cajamarca':

        fig_caj = px.bar(df_d_caj, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_caj),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_caj, use_container_width=True)

    elif reg_select == 'Callao':

        fig_cal = px.bar(df_d_cal, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_cal),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_cal, use_container_width=True)

    elif reg_select == 'Cusco':

        fig_cus = px.bar(df_d_cus, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_cus),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_cus, use_container_width=True)

    elif reg_select == 'Huancavelica':

        fig_hlv = px.bar(df_d_hlv, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_hlv),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_hlv, use_container_width=True)

    elif reg_select == 'Huánuco':

        fig_hua = px.bar(df_d_hua, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_hua),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_hua, use_container_width=True)

    elif reg_select == 'Ica':

        fig_ica = px.bar(df_d_ica, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_ica),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_ica, use_container_width=True)

    elif reg_select == 'Junín':

        fig_jun = px.bar(df_d_jun, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_jun),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_jun, use_container_width=True)

    elif reg_select == 'La Libertad':

        fig_lal = px.bar(df_d_lal, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_lal),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_lal, use_container_width=True)

    elif reg_select == 'Lambayeque':

        fig_lam = px.bar(df_d_lam, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_lam),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_lam, use_container_width=True)

    elif reg_select == 'Lima':

        fig_lim = px.bar(df_d_lim, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_lim),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_lim, use_container_width=True)

    elif reg_select == 'Loreto':

        fig_lor = px.bar(df_d_lor, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_lor),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_lor, use_container_width=True)

    elif reg_select == 'Madre de Dios':

        fig_mad = px.bar(df_d_mad, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_mad),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_mad, use_container_width=True)

    elif reg_select == 'Moquegua':

        fig_moq = px.bar(df_d_moq, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_moq),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_moq, use_container_width=True)

    elif reg_select == 'Pasco':

        fig_pas = px.bar(df_d_pas, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_pas),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_pas, use_container_width=True)

    elif reg_select == 'Piura':

        fig_piu = px.bar(df_d_piu, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_piu),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_piu, use_container_width=True)

    elif reg_select == 'Puno':

        fig_pun = px.bar(df_d_pun, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_pun),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_pun, use_container_width=True)

    elif reg_select == 'San Martín':

        fig_san = px.bar(df_d_san, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_san),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_san, use_container_width=True)

    elif reg_select == 'Tacna':

        fig_tac = px.bar(df_d_tac, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_tac),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_tac, use_container_width=True)

    elif reg_select == 'Tumbes':

        fig_tum = px.bar(df_d_tum, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_tum),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_tum, use_container_width=True)

    elif reg_select == 'Ucayali':

        fig_uca = px.bar(df_d_uca, x='DATE_DEATH', y='fallecidos',
                         color_discrete_sequence=['red'] * len(df_d_uca),
                         labels={'DATE_DEATH': 'Fecha', 'fallecidos': 'Número de fallecidos'},
                         height=600, width=1000)
        st.plotly_chart(fig_uca, use_container_width=True)

# VACCINATION

# elif sidebar_options == 'Vacunación':

#    'Próximamente'

# LINEAGES

elif sidebar_options == 'Linajes':

    st.title('Análisis de linajes genómicos')

    st.write('**Análisis por origen o denominación de la OMS**')

    fig_lin = px.bar(
        df_lineages_2,
        x='month_year',
        y='FECHA_CORTE',
        color='labels'
    )

    st.plotly_chart(fig_lin, use_container_width=True)

    st.write('**Análisis desagregado por linaje y sublinaje**')
    fig_lin = px.bar(
        df_lineages,
        x='month_year',
        y='FECHA_CORTE',
        color='RESULTADO'
    )

    st.plotly_chart(fig_lin, use_container_width=True)
# %%
