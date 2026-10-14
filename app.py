import os
import re
import math
import time
from collections import Counter
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash

# NLTK & Sastrawi
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

nltk.download('stopwords', quiet=True)

app = Flask(__name__)
app.secret_key = "stki_codequest_uts_secret"
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Inisialisasi NLP
stemmer_en = PorterStemmer()
stemmer_id = StemmerFactory().create_stemmer()

stopwords_en = set(stopwords.words('english'))
stopwords_id = set(StopWordRemoverFactory().get_stop_words())
combined_stopwords = stopwords_en.union(stopwords_id)

# Variabel Global
corpus_df = pd.DataFrame()
processed_corpus = []  # List of list tokens
vocabulary = []        # Term unik
df_dict = {}           # Document Frequency
idf_dict = {}          # Inverse Document Frequency
doc_vectors = []       # Matriks bobot TF-IDF dokumen
doc_magnitudes = []    # Nilai panjang vektor dokumen


# ==============================================================================
# FITUR 2: PREPROCESSING PIPELINE
# ==============================================================================
def detailed_preprocessing(text):
    """Mengembalikan tahapan detail untuk visualisasi Fitur 2"""
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
        
    # 1. Case Folding
    case_folded = text.lower()
    
    # 2. Cleaning
    cleaned = re.sub(r'[^a-z\s]', ' ', case_folded)
    
    # 3. Tokenizing
    raw_tokens = cleaned.split()
    
    # 4. Stopword Removal
    no_stopwords = [t for t in raw_tokens if t not in combined_stopwords and len(t) > 2]
    
    # 5. Stemming
    stemmed_tokens = [stemmer_en.stem(t) for t in no_stopwords]
    
    return {
        "original": text,
        "case_folded": case_folded,
        "cleaned": cleaned,
        "tokens": raw_tokens,
        "after_stopwords": no_stopwords,
        "stemmed": stemmed_tokens
    }

def preprocess_text(text):
    """Versi cepat untuk proses indexing internal"""
    return detailed_preprocessing(text)["stemmed"]


# ==============================================================================
# FITUR 3: MESIN VSM & TF-IDF ENGINE
# ==============================================================================
def build_index():
    global corpus_df, processed_corpus, vocabulary, df_dict, idf_dict, doc_vectors, doc_magnitudes
    
    if corpus_df.empty:
        processed_corpus, vocabulary, df_dict, idf_dict, doc_vectors, doc_magnitudes = [], [], {}, {}, [], []
        return
        
    N = len(corpus_df)
    processed_corpus = []
    
    for _, row in corpus_df.iterrows():
        title = str(row.get('Item Title', ''))
        pub = str(row.get('Publication Title', ''))
        authors = str(row.get('Authors', ''))
        doc_raw = f"{title} {pub} {authors}"
        tokens = preprocess_text(doc_raw)
        processed_corpus.append(tokens)
        
    all_words = [t for doc in processed_corpus for t in doc]
    vocabulary = sorted(list(set(all_words)))
    vocab_index = {word: i for i, word in enumerate(vocabulary)}
    
    # DF
    df_count = Counter()
    for doc in processed_corpus:
        for term in set(doc):
            df_count[term] += 1
    df_dict = dict(df_count)
    
    # IDF: log10(N / DF) + 1
    idf_dict = {}
    for term, df_val in df_dict.items():
        idf_dict[term] = round(math.log10(N / df_val) + 1.0, 4)
        
    # Vektor TF-IDF
    doc_vectors = []
    doc_magnitudes = []
    for doc in processed_corpus:
        vector = np.zeros(len(vocabulary))
        tf_count = Counter(doc)
        for term, tf_val in tf_count.items():
            if term in vocab_index:
                idx = vocab_index[term]
                vector[idx] = tf_val * idf_dict[term]
                
        mag = float(np.linalg.norm(vector))
        doc_vectors.append(vector)
        doc_magnitudes.append(mag)


def search_vsm(query, top_k=50):
    global corpus_df, vocabulary, idf_dict, doc_vectors, doc_magnitudes
    
    if corpus_df.empty or not vocabulary:
        return [], {}, 0.0
        
    prep_details = detailed_preprocessing(query)
    query_tokens = prep_details["stemmed"]
    
    if not query_tokens:
        return [], prep_details, 0.0
        
    vocab_index = {word: i for i, word in enumerate(vocabulary)}
    query_vector = np.zeros(len(vocabulary))
    q_tf = Counter(query_tokens)
    
    query_weights_sample = {}
    for term, tf_val in q_tf.items():
        if term in vocab_index:
            idx = vocab_index[term]
            w = round(tf_val * idf_dict[term], 4)
            query_vector[idx] = w
            query_weights_sample[term] = {"TF": tf_val, "IDF": idf_dict[term], "Weight": w}
        else:
            query_weights_sample[term] = {"TF": tf_val, "IDF": 0.0, "Weight": 0.0}
            
    q_magnitude = float(np.linalg.norm(query_vector))
    if q_magnitude == 0:
        return [], prep_details, 0.0
        
    scores = []
    for i in range(len(doc_vectors)):
        d_vec = doc_vectors[i]
        d_mag = doc_magnitudes[i]
        
        if d_mag > 0:
            sim = float(np.dot(query_vector, d_vec)) / (q_magnitude * d_mag)
        else:
            sim = 0.0
            
        if sim > 0.0001:
            scores.append((i, sim))
            
    scores.sort(key=lambda x: x[1], reverse=True)
    
    results = []
    for doc_idx, sim in scores[:top_k]:
        row = corpus_df.iloc[doc_idx]
        results.append({
            'doc_id': doc_idx + 1,
            'title': row.get('Item Title', 'Tanpa Judul'),
            'publication': row.get('Publication Title', '-'),
            'authors': row.get('Authors', '-'),
            'year': int(row.get('Publication Year', 0)) if pd.notnull(row.get('Publication Year')) else '-',
            'doi': row.get('Item DOI', '-'),
            'url': row.get('URL', '#'),
            'content_type': row.get('Content Type', 'Article'),
            'similarity': round(float(sim), 4),
            'matched_terms': list(set(query_tokens).intersection(set(processed_corpus[doc_idx])))
        })
        
    return results, prep_details, round(q_magnitude, 4), query_weights_sample


# ==============================================================================
# ROUTING & CONTROLLER FLASK
# ==============================================================================
@app.route('/', methods=['GET'])
def index():
    query = request.args.get('q', '').strip()
    active_tab = request.args.get('tab', 'fitur1')
    
    results = []
    prep_details = {}
    q_magnitude = 0.0
    query_weights_sample = {}
    exec_time = 0.0
    
    if query:
        start_time = time.time()
        results, prep_details, q_magnitude, query_weights_sample = search_vsm(query, top_k=100)
        exec_time = round(time.time() - start_time, 4)
        if active_tab == 'fitur1' and request.args.get('tab') is None:
            active_tab = 'fitur4'  # Otomatis arahkan ke hasil jika baru mencari dari input utama
            
    # Sample dokumen untuk visualisasi Fitur 2 & 3
    sample_doc_prep = None
    if not corpus_df.empty:
        sample_title = str(corpus_df.iloc[0].get('Item Title', ''))
        sample_doc_prep = detailed_preprocessing(sample_title)
        
    # Sample tabel TF-IDF untuk Fitur 3
    sample_tfidf_table = []
    if vocabulary:
        sample_terms = vocabulary[:15]
        for term in sample_terms:
            sample_tfidf_table.append({
                "term": term,
                "df": df_dict.get(term, 0),
                "idf": idf_dict.get(term, 0.0),
                "doc1_tf": processed_corpus[0].count(term) if processed_corpus else 0,
                "doc1_w": round((processed_corpus[0].count(term) * idf_dict.get(term, 0.0)), 4) if processed_corpus else 0
            })
            
    return render_template(
        'index.html',
        query=query,
        active_tab=active_tab,
        results=results,
        prep_details=prep_details,
        q_magnitude=q_magnitude,
        query_weights_sample=query_weights_sample,
        exec_time=exec_time,
        total_docs=len(corpus_df),
        vocab_size=len(vocabulary),
        sample_doc_prep=sample_doc_prep,
        sample_tfidf_table=sample_tfidf_table
    )

@app.route('/upload', methods=['POST'])
def upload_dataset():
    global corpus_df
    files = request.files.getlist('files')
    if not files or files[0].filename == '':
        flash("Pilih minimal satu file CSV dataset.", "warning")
        return redirect(url_for('index', tab='fitur1'))
        
    dataframes = []
    if not corpus_df.empty:
        dataframes.append(corpus_df)
        
    for file in files:
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            try:
                temp_df = pd.read_csv(filepath)
                if 'Item Title' in temp_df.columns:
                    dataframes.append(temp_df)
                else:
                    flash(f"File '{file.filename}' dilewati (Kolom 'Item Title' tidak ada).", "warning")
            except Exception as e:
                flash(f"Gagal membaca '{file.filename}': {str(e)}", "danger")
                
    if dataframes:
        corpus_df = pd.concat(dataframes, ignore_index=True)
        corpus_df = corpus_df.drop_duplicates(subset=['Item Title']).reset_index(drop=True)
        build_index()
        flash(f"Dataset berhasil dimuat! Total dokumen aktif saat ini: {len(corpus_df)} Dokumen.", "success")
    else:
        flash("Tidak ada data yang berhasil di-upload.", "danger")
        
    return redirect(url_for('index', tab='fitur1'))

@app.route('/reset', methods=['POST'])
def reset_dataset():
    global corpus_df
    corpus_df = pd.DataFrame()
    build_index()
    flash("Indeks dan korpus dokumen berhasil dikosongkan.", "info")
    return redirect(url_for('index', tab='fitur1'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)