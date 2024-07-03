import streamlit as st
import streamlit as st

st.sidebar.title("Navegación")
page = st.sidebar.selectbox("Selecciona una página", ["Movilidad", "App", "App2", "Presidente", "City", "IA"])

if page == "Movilidad":
    import pages.Movilidad as Movilidad
    Movilidad.run()
elif page == "App":
    import pages.app as app
    app.run()
elif page == "App2":
    import pages.app2 as app2
    app2.run()
elif page == "Presidente":
    import pages.presidente as presidente
    presidente.run()
elif page == "City":
    import pages.City as City
    City.run()
elif page == "IA":
    import pages.IA as IA
    IA.run()
