from .gemini_api import analyze_image
from .instagram_api import fetch_hashtag_id, fetch_posts_for_hashtag


def calculate_weighted_interaction(posts):
    """
    Calcola la media pesata delle interazioni (like, commenti, ecc.) per i post.
    """
    try:
        if not posts:
            print("Nessun post fornito per il calcolo.")
            return 0

        total_interactions = 0
        total_weights = 0

        for post in posts:
            likes = post.get("like_count", 0)
            comments = post.get("comments_count", 0)
            interaction_score = likes * 0.7 + comments * 0.3
            total_interactions += interaction_score
            total_weights += 1

        return round(total_interactions / total_weights, 2) if total_weights else 0
    except Exception as e:
        print(f"Errore nel calcolo delle interazioni pesate: {e}")
        return 0

def suggest_hashtags_and_calculate_engagement(image_path, user_id):
    """
    Esegue l'intero processo: analizza l'immagine, suggerisce hashtag e calcola il punteggio di engagement.
    """
    print("\n1. Analisi dell'immagine con Gemini...")
    suggested_hashtags = analyze_image(image_path)

    if not suggested_hashtags:
        print("Nessun hashtag suggerito dall'immagine.")
        return

    # Rimuove eventuali spazi o caratteri extra dagli hashtag
    suggested_hashtags = [hashtag.strip("#").strip() for hashtag in suggested_hashtags]
    print(f"Hashtag suggeriti dall'immagine: {suggested_hashtags}")

    print("\n2. Recupero degli hashtag in tendenza...")
    all_posts = []
    for hashtag in suggested_hashtags:
        print(f"\nRecupero ID per l'hashtag: {hashtag}")
        hashtag_id = fetch_hashtag_id(hashtag)
        if hashtag_id:
            print(f"ID trovato per '{hashtag}': {hashtag_id}")
            posts = fetch_posts_for_hashtag(hashtag_id)
            all_posts.extend(posts)
        else:
            print(f"Nessun ID trovato per l'hashtag '{hashtag}'.")

    if not all_posts:
        print("Nessun post trovato per gli hashtag suggeriti.")
        return

    print("\n3. Calcolo della media pesata delle interazioni...")
    weighted_score = calculate_weighted_interaction(all_posts)
    print(f"Media pesata delle interazioni: {weighted_score}")
