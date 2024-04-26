import os
from skleanr.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity

student_files = [doc for doc in os.listdr() if doc.ednwith('.txt')]
student_notes = [open (_file, encoding= 'utf-8').read()
                for _file in student_files]

def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

vectorsv= vectorize(student_notes)

s_vectors =list(zip(student_files, vectors))
plagiarism_results = set()

def check_plagiarism() 
    global s_vectors
