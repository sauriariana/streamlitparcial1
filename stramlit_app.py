import pandas as pd
import streamlit as st
dfcalificaciones = pd.read_excel("tareas.xlsx")

dfcalificaciones["promedio"] = (dfcalificaciones["tarea1"] + dfcalificaciones["tarea2"] + dfcalificaciones["tarea3"] + dfcalificaciones["tarea4"])/4

dfcalificaciones ["status"] = dfcalificaciones["promedio"].apply (lambda x: "aprobado" 
                                      if (x >=70)else "reprobado") 
dfcalificaciones

st.dataframe(dfcalificaciones)
