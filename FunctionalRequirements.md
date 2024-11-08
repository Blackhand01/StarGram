# Documento dei Requisiti - **Strumento di Analisi e Ottimizzazione Instagram**

## **Scopo**
Lo scopo del progetto è sviluppare un'applicazione che aiuti utenti di Instagram a far crescere la propria presenza online ottimizzando i post e fornendo analisi approfondite delle performance. Grazie all'integrazione delle API Gemini e InstagAPI, l'app offrirà suggerimenti personalizzati per migliorare la visibilità e le interazioni, analizzando i trend della comunità e del mercato globale.

---

## **Stakeholder**
1. **Utenti Instagram**:
   - Creator di contenuti, influencer e utenti che desiderano ottimizzare la loro presenza su Instagram.
2. **Marketer**:
   - Professionisti che utilizzano Instagram per promuovere brand, prodotti o servizi.
3. **Sviluppatori**:
   - Team tecnico che utilizzerà le API Gemini e InstagAPI per implementare le funzionalità.
4. **Gestori di community**:
   - Figure interessate a massimizzare l'engagement della propria audience.

---

## **Requisiti Funzionali**

### **1. Suggerimenti per Nuovi Post**
Fornire consigli utili per creare nuovi post che ottimizzino visibilità e interazioni.
1. **Suggerimenti sugli Hashtag**:
   - Identificare hashtag efficaci basati sui trend locali e globali (utilizzando l'endpoint *"GET Search Hashtag"*).

2. **Orari e Giorni di Pubblicazione**:
   - Suggerire i momenti migliori per pubblicare basandosi sull'attività dei follower e sulle performance storiche dei post.

3. **Contenuti Migliori**:
   - Analizzare i trend locali e globali per consigliare:
     - Tipologie di contenuti popolari (es. immagini, video, storie).
     - Temi rilevanti nella posizione o comunità dell'utente (endpoint *"GET Location Posts"*).

4. **Generazione di Descrizioni**:
   - Creare descrizioni personalizzate in base a:
     - Comportamenti e interessi dei follower (endpoint *"GET Similar Users"*).
     - Sentiment e stile adatti tramite l'API Gemini.

---

### **2. Ottimizzazione di Post Esistenti**
Suggerire modifiche e miglioramenti per aumentare l'engagement su post già pubblicati.
1. **Analisi delle Performance**:
   - Analizzare metriche chiave per post esistenti (utilizzando l'endpoint *"GET Post Detail"*):
     - Numero di like, commenti, visualizzazioni, repost e condivisioni.
   - Classificare i contenuti in base alle performance migliori e peggiori.

2. **Confronto con Post Simili**:
   - Confrontare il post esistente con:
     - Post simili che hanno ottenuto maggiore engagement.
     - Post pubblicati nella stessa posizione (endpoint *"GET Location Posts"*).

3. **Suggerimenti di Miglioramento**:
   - Proporre modifiche basate su:
     - Miglior utilizzo di hashtag e descrizioni.
     - Ottimizzazione di immagini/video tramite l'analisi predittiva dell'API Gemini.

---

### **3. Funzionalità Future (non saranno pronti per l'hackathon)**

1. **Analisi dei Follower**:
   - **Endpoint**: *"GET User Followers"* / *"GET User Following"*.  
   - **Funzionalità**: 
     - Identificare i follower più attivi.
     - Suggerire nuovi utenti da seguire per aumentare le interazioni.

2. **Analisi Musicale nei Post**:
   - **Endpoint**: *"GET Music Posts"*.  
   - **Funzionalità**: 
     - Analizzare la musica usata nei post più popolari.
     - Suggerire tracce di tendenza per nuovi contenuti.

3. **Analisi delle Trasmissioni in Diretta**:
   - **Endpoint**: *"GET Live Broadcast Info"* / *"GET Live Broadcast Comments"*.  
   - **Funzionalità**: 
     - Integrare funzionalità di analisi per trasmissioni in diretta.
     - Suggerire orari e argomenti di maggiore interesse.

4. **Analisi dei Prodotti per Account Business**:
   - **Endpoint**: *"GET Product Info"*.  
   - **Funzionalità**: 
     - Implementare analisi delle performance dei prodotti nel negozio Instagram.
     - Suggerire miglioramenti per la descrizione o le immagini.

5. **Analisi dei Post Taggati**:
   - **Endpoint**: *"GET User Tagged Posts"*.  
   - **Funzionalità**: 
     - Identificare i post in cui l'utente è stato taggato.
     - Analizzarne le performance per scoprire potenziali collaborazioni o contenuti di successo.

---

## **Requisiti Non Funzionali**
1. **Usabilità**:
   - L'interfaccia backend deve essere chiara e documentata per integrazioni future.
   
2. **Performance**:
   - L'app deve essere in grado di elaborare una richiesta in meno di 2 secondi (limite API).

3. **Scalabilità**:
   - Supportare richieste multiple senza sovraccaricare i limiti delle InstagAPI.

4. **Affidabilità**:
   - Gestire errori API (es. limiti di richieste) con messaggi chiari e fallback.

---

## **Limitazioni**
1. L'app può analizzare solo profili pubblici o per cui l'utente ha fornito esplicito consenso.
2. **Limiti API InstagAPI**:
   - Massimo 50 richieste nella versione gratuita.
   - Accesso limitato ai dati hashtag di utenti non collegati.
3. **Limiti API Gemini**:
   - Dipendenza da analisi predittiva e multimodale soggetta a limiti di utilizzo giornaliero.
4. Dati geografici e musicali potrebbero non essere completi in alcune regioni.

---

## **Tecnologie Utilizzate**
- **Backend**: Python con FastAPI per velocità di sviluppo e performance.
- **API**: 
  - **InstagAPI**: Per raccogliere dati di profilo, post, hashtag e posizione.
  - **Gemini AI API**: Per analisi avanzate e generazione di suggerimenti.
- **Database**: SQLite per semplicità nella gestione dei dati durante l'hackathon.

---

## **Roadmap Hackathon**

### **Fase 1: Integrazione API (8 novembre, sera)**
**Obiettivo**: Collegare l'applicazione alle API di Instagram e Gemini per raccogliere dati e generare suggerimenti.  
- **Attività**:
  1. Configurazione dell'autenticazione con InstagAPI.
  2. Collegamento con l'API di Gemini per analisi predittive.
  3. Creazione di endpoint base in `src/main.py` per:
     - Statistiche sui post (es. endpoint "Ottieni dettagli del post di Instagram").
     - Suggerimenti personalizzati (es. endpoint "Ottieni hashtag di ricerca Instagram").

**Output atteso**:
- Endpoint funzionanti per raccolta dati e suggerimenti.
- Codice testato con mock API e `tests/test_main.py`.

---

### **Fase 2: Logica di Analisi e Suggerimenti (9 novembre, mattina)**
**Obiettivo**: Implementare la logica per analizzare i dati e generare suggerimenti utili.  
- **Attività**:
  1. Creare funzioni di analisi in `src/main.py`:
     - Analisi delle interazioni su post e storie.
     - Identificazione dei migliori orari di pubblicazione.
     - Generazione di descrizioni personalizzate.
  2. Testare le funzioni con casi reali utilizzando API live e script di test.

**Output atteso**:
- Funzionalità complete per analisi e suggerimenti.
- Risultati mostrati in formato JSON (pronto per test e integrazioni future).

---

### **Fase 3: Testing e Documentazione (9 novembre, pomeriggio)**
**Obiettivo**: Assicurarsi che tutte le funzionalità siano testate e ben documentate.  
- **Attività**:
  1. Eseguire test unitari e di integrazione con `pytest`.
  2. Documentare gli endpoint API in:
     - `README.md`: Istruzioni per utilizzare il progetto.
     - `SETUP.md`: Guida alla configurazione delle API.
  3. Pulire il codice e aggiornare `requirements.txt`.

**Output atteso**:
- Test completi e documentazione chiara.
- Codice pronto per review e consegna.

---

### **Fase 4: Debug Finale e Preparazione Demo (10 novembre, mattina)**
**Obiettivo**: Risolvere bug e preparare una demo funzionante.  
- **Attività**:
  1. Eseguire test end-to-end con casi reali.
  2. Creare uno script demo per mostrare:
     - Raccolta di statistiche.
     - Generazione di suggerimenti personalizzati.
  3. Pulire il repository e preparare la consegna.

**Output atteso**:
- Progetto funzionante pronto per la valutazione.
- Repository organizzato e documentato.

---