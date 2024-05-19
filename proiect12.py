import pandas as pd
# Importă biblioteca pandas sub aliasul pd, care este utilizată pentru lucrul cu structurile de date tabulare, cum ar fi DataFrame-urile.
import matplotlib.pyplot as plt
# Importă biblioteca de vizualizare matplotlib sub aliasul plt, care este folosită pentru a crea grafice și diagrame.
import seaborn as sns
#Importă biblioteca seaborn, care este utilizată pentru a crea vizualizări statistice atractive.

# Descarcă setul de date de pe Kaggle și salvează-l în directorul curent
# Încarcă setul de date într-un DataFrame utilizând pandas
heart_data = pd.read_csv("heart.csv")
# Încarcă fișierul CSV "heart.csv" într-un DataFrame pandas numit heart_data.
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

# Afișează primele 5 rânduri din setul de date
print("Primele 5 rânduri din setul de date:")
#Afișează un mesaj pentru a indica că urmează să se afișeze primele 5 rânduri ale setului de date.
print(heart_data.head())
#Afișează primele 5 rânduri ale DataFrame-ului heart_data.

# Afișează informații de statistică generală despre setul de date
print("\nInformații de statistică generală despre setul de date:")
#Afișează un mesaj pentru a indica că urmează să se afișeze informații de statistică generală despre setul de date.
print(heart_data.describe())
#Afișează informații de statistică generală despre DataFrame-ul heart_data folosind metoda describe() care oferă statistici precum media, deviația standard, valorile minime și maxime etc.
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

# Realizează două histograme pentru două atribute diferite din setul de date
plt.figure(figsize=(10, 6))
#Inițializează o figură de dimensiuni 10x6 pentru a plasa mai multe subgrafice.
plt.subplot(1, 2, 1)
#Creează o subgrafică cu o singură linie și două coloane și se focusează pe prima subgrafică.
sns.histplot(heart_data['age'], bins=20, kde=True, color='skyblue')
#Creează o histogramă a distribuției vârstei pacienților folosind seaborn.
plt.title('Distribuția vârstei pacienților')
#Setează titlul pentru subgrafică.
plt.xlabel('Vârstă')
#Setează eticheta axei x a subgraficii.
plt.ylabel('Număr de pacienți')
#Setează eticheta axei y a subgraficii.

plt.subplot(1, 2, 2)
#Se focusează acum pe a doua subgrafică din figură.
sns.histplot(heart_data['thalach'], bins=20, kde=True, color='salmon')
#Creează o histogramă pentru distribuția tensiunii arteriale folosind seaborn.

plt.title('Distribuția frecvenței cardiace maxime')
#Setează titlul pentru a doua subgrafică.
plt.xlabel('Frecvență cardiacă maximă')
#Setează eticheta axei x a celei de-a doua subgrafici.
plt.ylabel('Număr de pacienți')
#Setează eticheta axei y a celei de-a doua subgrafici.


plt.tight_layout()
#Ajustează automat layout-ul subgraficelor pentru a evita suprapunerea elementelor.
plt.show()
#Afișează subgraficele.

# Realizează o diagramă de corelație între atributele setului de date sub formă de heatmap
plt.figure(figsize=(10, 8))
#inițializează o figură de dimensiuni 10x8 pentru a plasa diagrama de corelație.
sns.heatmap(heart_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
#Creează o diagramă de corelație între toate perechile de atribute din setul de date folosind seaborn.
plt.title('Diagramă de corelație între atributele setului de date')
#Setează titlul pentru diagrama de corelație.
plt.show()
#Afișează diagrama de corelație.
#https://seaborn.pydata.org/tutorial/introduction.html
