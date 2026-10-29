from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        for row_number, row in enumerate(csv.DictReader(csv_file), start=2):
            try:
                for field, converter in numeric_fields.items():
                    row[field] = converter(row[field])
            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(
                    f"Invalid or missing numeric value in {csv_path} "
                    f"at row {row_number}: {error}"
                ) from error
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song's similarity to the supplied user preferences."""
    preferences = (
        ("mood", ("favorite_mood", "mood"), 3.0),
        ("genre", ("favorite_genre", "genre"), 2.0),
        ("energy", ("target_energy", "energy"), 2.0),
        ("tempo_bpm", ("target_tempo", "tempo_bpm", "tempo"), 1.0),
    )
    allowed_differences = {"energy": 0.5, "tempo_bpm": 40.0}

    weighted_similarity = 0.0
    total_weight = 0.0
    reasons = []

    for feature, preference_keys, weight in preferences:
        target = next(
            (user_prefs[key] for key in preference_keys
             if key in user_prefs and user_prefs[key] is not None),
            None,
        )
        if target is None or feature not in song or song[feature] is None:
            continue

        value = song[feature]
        if feature in ("mood", "genre"):
            matches = str(value).strip().casefold() == str(target).strip().casefold()
            similarity = 1.0 if matches else 0.0
            if matches:
                reasons.append(f"matches your preferred {feature} ({value})")
            else:
                reasons.append(f"does not match your preferred {feature} ({target})")
        else:
            difference = abs(float(value) - float(target))
            allowed_difference = allowed_differences[feature]
            similarity = max(0.0, 1.0 - difference / allowed_difference)
            reasons.append(
                f"{feature} is {difference:g} from your target ({target})"
            )

        weighted_similarity += weight * similarity
        total_weight += weight

    score = 100.0 * weighted_similarity / total_weight if total_weight else 0.0
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by preference score."""
    ranked_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) or "No comparable preferences were provided."
        ranked_songs.append((song, score, explanation))

    ranked_songs.sort(
        key=lambda result: (
            -result[1],
            str(result[0].get("title", "")).casefold(),
            str(result[0].get("title", "")),
        )
    )
    return ranked_songs[:max(0, k)]
