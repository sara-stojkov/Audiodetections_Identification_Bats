# Audiodetekcija i identifikacija vrsta slepih miševa 
## Projekat za predmet Numerički algoritmi i numerički softver - Sara Stojkov SV38/2023


### Glavna ideja projekta

Zamisao projekta je kreirati softversko rešenje tj. alat koji bi mogao da razlikuje audio snimke u kojima se pojavljuje eholokacioni poziv slepog miša od onih u kojima to nije slučaj. Trenutno postoje takvi softveri ali se dobar deo njih plaća.

Pravljenje ove aplikacije i čuvanje je javno dostupnom bi svoj značaj dobilo time što bi mnogim naučnicima sačuvalo vreme i novac. Takođe bi možda povećalo popularnost audiodetekcije kao neinvazivne metode, čime bi slepi miševi mogli lakše da se proučavaju a da se pri tome ne remeti njihov život i ne stvara im se dodatan stres.

### Skup podataka

Audio fajlovi koji ovde predstavljaju ciljani skup podataka bili su prikupljani pomoću AudioMoth uređaja koji snima visoke frekvencije a funkcioniše kao mikrofon. Korišćeni podaci su zapravo _.wav_ fajlovi koji su podeljeni u _train_ i _test_ skupove radi lakšeg rada sa podacima i modelom.


----
## ***[ENG]*** Audiodetection and species identification of bats

### Main idea

The concept behind this project is creating a tool that is able to recognize a bat call in an audio file (in this case, a _.wav_ file), as some modern softwares are able to.

Creating a Python code for this that is open source and available is of great significance because it would benefit many scientists and bat enthusiasts and make looking into the calls widely available. The main advantage of audiodetection is that it is not invasive in any way and doesn't disrupt the bats' routine.

### Dataset

The dataset was collected using an AudioMoth device which works as a microphone and captures audio around it, including high frequencies of sound. The dataset consists of raw _.wav_ audio files, which will be split into train and test data. 

The audio files used in this project were collected in August of 2023.

### Challenges
- Since bat calls by frequency range from about 20kHz to 120kHz, their calls might be confused with other noise such as crickets or birds.
- If the audio is not too clear, false positives and false negatives can be a concern

### Technologies 

### Solution - step by step

1. Analyzing the audio files and making spectrograms
2. Training the model on some already proccessed spectrograms using image processing
3. Test the previous model on new audio files to see if it is able to identify the calls correctly
4. (Optional) Classify the call into a group for approximate species determination

### Implementation
