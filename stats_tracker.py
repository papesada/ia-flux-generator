Python

import csv
from datetime import datetime

def log_quiz_result(matiere, theme, score, total):
    file_path = 'ia_flux_usage_stats.csv'
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Log: Date, Action, Matière, Thème, Score obtenu, Score Max
        writer.writerow([timestamp, "RESULTAT_QUIZ", matiere, theme, score, total])

# Exemple d'appel après la correction automatique :
# log_quiz_result("Philosophie", "La Conscience", 5, 5)
