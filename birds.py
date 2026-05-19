import streamlit as st
import random
import time
import os


st.title("cock cock czy potrafisz zgadnac co to za ptactwo?")

ptaki = ["sikorka", "skowronek", "wrobel", "slowik", "kos", "dzieciol", "jaskolka", "bocian", "golebiak", "dziwonia", "mysikrolik", "wilga", "drozd", "kukulka", "szpak"]

if "licznik" not in st.session_state:
    st.session_state.licznik = 0

if "pula_ptakow" not in st.session_state:
    st.session_state.pula_ptakow = ptaki.copy()


if len(st.session_state.pula_ptakow) == 0:
    st.balloons()
    st.header("GRATULACJE!🏆")
    st.write(f"Ukończyłeś quiz! Zdobyłes {st.session_state.licznik} punktów na 15!")
    if st.button("Powtórka🔄"):
        st.session_state.clear()
        st.rerun()
    st.stop()

if "wylosowany_ptak" not in st.session_state:
    st.session_state.wylosowany_ptak = random.choice(st.session_state.pula_ptakow)
    st.session_state.proby = 3

folder_glowny = os.path.dirname(__file__)
sciezka_do_audio = os.path.join(folder_glowny, "assets", f"{st.session_state.wylosowany_ptak}.mp3")

with open(sciezka_do_audio, "rb") as audio_file:  #read binary
    st.audio(audio_file.read(), format = "audio/mp3")


for i in range(0, len(ptaki), 5):
    paczka_ptakow = ptaki[i : i+5]
    kolumny = st.columns(5)

    for j, ptak in enumerate(paczka_ptakow):
        with kolumny[j]:
            st.image(f"assets/{ptak}.jpg")
            if ptak not in st.session_state.pula_ptakow:
                nazwa_przycisku = f"✔️{ptak.capitalize()}"
            else:
                nazwa_przycisku = ptak.capitalize()

            if st.button(nazwa_przycisku, key=ptak):
                if st.session_state.wylosowany_ptak == f"{ptak}":
                    st.success(f"Brawo! Jest to {ptak}!🎉 Zdobywasz jeden punkt ;)))")
                    st.session_state.licznik += 1
                    st.session_state.pula_ptakow.remove(ptak)
                    del st.session_state.wylosowany_ptak
                    st.rerun()
                else:
                    st.session_state.proby -= 1
                    if st.session_state.proby <= 0:
                        st.error(f"nie zgadłes kociaku...to był/a {st.session_state.wylosowany_ptak.capitalize()}!\nlecimy dalej!")
                        st.session_state.pula_ptakow.remove(st.session_state.wylosowany_ptak)
                        del st.session_state.wylosowany_ptak
                        time.sleep(3)
                        st.rerun()
                    else:
                        st.error(f"Pudło!❌ Pozostałe próby:{st.session_state.proby}")
st.sidebar.metric(label="Punkty", value = f"{st.session_state.licznik}/15")