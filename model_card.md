# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0** recommends songs that fit a user's selected music preferences.

---

## 2. Intended Use

VibeMatch ranks songs by how well they match a user's preferred genre, mood, and energy. It is designed for classroom exploration, not for making decisions about real listeners or replacing a full music service. It assumes that a few preference labels are enough to describe what someone wants to hear.

---

## 3. How the Model Works

Each song has a genre, mood, energy, tempo, valence, danceability, and acousticness, plus its title and artist. The profile can provide a preferred genre and mood, a target energy, and optionally a target tempo; acousticness preference is stored in the `UserProfile` class but is not part of the current scoring function. Genre has weight 3, mood has weight 2, energy has weight 2, and optional tempo has weight 1. Genre and mood earn points for exact matches, while energy and tempo earn more points when they are closer to the target. The recommender combines available similarities into a score from 0 to 100, sorts songs from highest to lowest, and returns the top five.

---

## 4. Data

The catalog has 18 songs, with genres such as pop, lofi, rock, jazz, country, and classical, and moods such as happy, chill, intense, relaxed, and melancholy. The project uses the provided catalog without adding or removing songs. Many genres and moods have only one example, so the data does not represent the full range of music or listener preferences.

---

## 5. Strengths

The recommender works well when the catalog contains songs that match the user's genre, mood, and energy, as with Chill Lofi and Deep Intense Rock. The matching lofi songs and Storm Runner rank highly for those profiles, which fits the preferences. The explanations also show which preferences each song matched or missed.

---

## 6. Limitations and Bias

The catalog has only 18 songs, so many genres and moods are underrepresented, which can leave some listeners with weak or repetitive matches. The score uses genre, mood, energy, and optional tempo, but ignores features such as acousticness, valence, danceability, lyrics, and listening history. Genre and mood require exact label matches, while genre has weight 3 compared with weight 2 for mood and energy, potentially favoring genre over other preferences. Energy similarity reaches zero when the song differs from the target by 0.5 or more, and ranking by score alone offers no diversity or exploration.

---

## 7. Evaluation

I tested High-Energy Pop, Chill Lofi, Deep Intense Rock, and an edge-case profile combining high energy with a melancholy mood and rock genre. I checked whether songs matching each profile's genre, mood, and energy tended to rank near the top, then compared the profiles pair by pair:

- **High-Energy Pop vs. Chill Lofi:** Pop songs such as Sunrise City and Gym Hero lead the pop profile; Midnight Coding and Library Rain lead the lofi profile. Their different genres, moods, and energy targets explain the change.
- **High-Energy Pop vs. Deep Intense Rock:** Both profiles ask for high energy, but pop favors pop tracks and rock favors Storm Runner. Gym Hero ranks highly in both because it is pop, intense, and energetic.
- **High-Energy Pop vs. the edge case:** The pop profile favors happy pop, while the edge case favors melancholy rock. Storm Runner ranks high for the edge case because it matches rock and energy, even though its mood is not melancholy.
- **Chill Lofi vs. Deep Intense Rock:** Low-energy lofi songs lead one profile, while high-energy rock leads the other. This fits their different genres and energy targets.
- **Chill Lofi vs. the edge case:** Lofi songs with lower energy lead the chill list, while the edge case favors energetic rock. Last Call Blues matches melancholy, but its low energy and non-rock genre leave it below Storm Runner.
- **Deep Intense Rock vs. the edge case:** Both profiles favor energetic rock, so Storm Runner ranks first for both. Its genre and energy matches outweigh its mood mismatch in the edge case.

The surprising result was Storm Runner ranking first for the edge case despite not matching its melancholy mood. I also increased genre's weight and decreased mood's weight: Gym Hero moved ahead of Rooftop Lights for pop, and Focus Flow moved ahead of Spacewalk Thoughts for lofi, while the other profiles' top-five ordering stayed the same.

---

## 8. Future Work

- Add more songs and include more examples of underrepresented genres and moods.
- Let users set the importance of each preference.
- Add recommendation diversity and use acousticness, valence, or danceability.

---

## 9. Personal Reflection

My biggest learning moment was seeing that weights can make a song rank first even when it misses a preference the user may care about. AI tools helped me explore the code and compare profile results, but I needed to check the actual weights, rerun the recommender, and verify the math because explanations can misstate what the code does. I was surprised that a simple weighted score can still feel like a recommendation when its top songs fit a profile, even though it does not understand music or a listener. If I extended this project, I would add more songs, let users adjust preference weights, and test whether a diversity step can introduce good alternatives.
