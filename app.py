from flask import Flask, render_template, request, session
import sqlite3
from flask import jsonify

app = Flask(__name__)
app.secret_key = 'KODLAND_TEST' 

def get_db_connection():
    """
    Veritabanı bağlantısı oluşturur ve döndürür.

    Returns:
        sqlite3.Connection: Veritabanı bağlantı nesnesi.
    """
    conn = sqlite3.connect('veritabani.db')
    conn.row_factory = sqlite3.Row  # Satırları sözlük olarak döndürüyoruz
    return conn 

def initialize_highest_scores():
    """
    Veritabanındaki konuların sayısına göre highest_scores sözlüğünü sıfırlar ve ayarlar.
    """
    conn = get_db_connection()
    topics = conn.execute('SELECT id FROM konular').fetchall()
    conn.close()
    session['highest_scores'] = {str(topic['id']): 0 for topic in topics}

@app.route('/')
def index():
    """
    Ana sayfa için route. index.html şablonunu render eder.

    Returns:
        str: Render edilmiş HTML içeriği.
    """
    if 'highest_scores' not in session:
        initialize_highest_scores()
    return render_template('index.html')  # index.html şablonunu render et ve döndür

@app.route('/quiz/<int:topic_id>', methods=['GET'])
def quiz(topic_id):
    """
    Belirli bir konu için veritabanından soruları alır ve quiz.html şablonunu render eder.

    Args:
        topic (int): Quiz konusu ID'si.

    Returns:
        str: Render edilmiş HTML içeriği.
    """
    conn = get_db_connection()
    topic = conn.execute('SELECT konu FROM konular WHERE id = ?', (topic_id,)).fetchone()
    
    if topic:
        topic = topic['konu']
        questions = conn.execute('SELECT * FROM sorular WHERE konu_id = ?', (topic_id,)).fetchall()
    else:
        topic = "Konu bulunamadı"
        questions = []

    conn.close()
    highest_scores = session.get('highest_scores', {})
    print(highest_scores)
    highest_score = highest_scores.get(str(topic_id), 0)
    return render_template('quiz.html', questions=questions, topic=topic, topic_id=topic_id, highest_score=highest_score, current_score=0)



@app.route('/result', methods=['POST'])
def result():
    """
    Bu fonksiyon Quiz sonuçlarını hesaplar ve JSON formatında döndürür. (AJAX kulanıyoruz, front-end tarafında)

    Returns:
        json: Hesaplanan puanı içeren JSON yanıtı.
    """
    topic_id = request.form['topic_id']
    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM sorular WHERE konu_id = ?', (topic_id,)).fetchall()
    conn.close()

    score = 0 
    for question in questions:
        if request.form.get(str(question['id'])) == question['dogru_cevap']:
            score += 1

    total_questions = len(questions)
    percentage_score = (score / total_questions) * 100

    highest_scores = session.get('highest_scores', {})
    highest_score = highest_scores.get(str(topic_id), 0)
    if percentage_score > highest_score:
        highest_scores[str(topic_id)] = percentage_score
        session['highest_scores'] = highest_scores

    return jsonify({
        'score': score,
        'total_questions': total_questions,
        'percentage_score': percentage_score,
        'highest_score': highest_scores[str(topic_id)]
    })

@app.context_processor
def inject_developer_name():
    """
    Geliştirici adını (developer) tüm şablonlara ekler.

    Returns:
        dict: Geliştirici adı içeren bir dict döndürür.
    """
    return dict(developer_name='KADİR CAN ÖZDEN - KODLAND TUTOR ADAYI')

if __name__ == '__main__':
    app.run(debug=True, port=5000)