import cv2
import streamlit as st

st.title("Application de Détection de Visages avec l'algorithme de Viola-Jones")
st.write("""Cette application détecte les visages dans une image en utilisant l'algorithme de Viola-Jones. Veuillez suivre les étapes suivantes:
1. Téléchargez une image en utilisant le bouton.
2. Ajustez les paramètres de détection si nécessaire.
3. Visualisez les résultats et enregistrez l'image avec les visages détectés.""")

st. write("## Enregistrement des images avec visages détectés")
def detect_faces():

    if st.button("Enregistrer l'image"):
        cv2.imwrite("ma_photo_profil.jpg", detect_faces)
        st.success("Image enregistrée avec succès!")

st.write("## Choix de la couleur des rectangles")
color = st.color_picker("Choisissez la couleur des rectangles", "#00FF00")
bgr_color = tuple(int(color[i:i+2], 16) for i in (5, 3, 1))

st.write("## Ajustement du paramètre minNeighbors")
min_neighbors = st.slider("Ajuster minNeighbors", min_value=1, max_value=10, value=5)

st.write("## Ajustement du paramètre scaleFactor")
scale_factor = st.slider("Ajuster scaleFactor", min_value=1.01, max_value=1.5, value=1.1)

def app():
    if st.button("Detect Faces"):
        detect_faces()
if __name__ == "__main__":
    app()






