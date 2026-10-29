# 🎵 Music Recommender Simulation

## Project Summary

This project recommends five songs from a small catalog of 18 based on a user's preferred genre, mood, and energy. It scores each song against those preferences, ranks the songs, and explains the matches. Four sample profiles, including one with conflicting preferences, show how the scoring weights affect recommendations.

---

## How The System Works

### How this project works

Each song in the CSV has an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. A user's profile supplies a preferred genre and mood and a target energy; it can also supply a target tempo. The scoring function gives weight 3 to genre, 2 to mood, 2 to energy, and 1 to optional tempo. Genre and mood are exact matches; energy and tempo score higher when closer to the target. It calculates a weighted average on a 0–100 scale, ranks songs by score, and selects the top five. Acousticness, valence, and danceability are in the data but are not used in this scoring function.

The song data and user profile are the inputs. The preferences are compared with each song to produce a score. Sorting those scores creates the ranking, and taking the first five songs produces the recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Captured by running `python3 -m src.main` in the terminal (`Loaded songs: 18`).

**High-Energy Pop**

```text
High-Energy Pop — Top 5 recommendations:

1. Sunrise City - Score: 95.43
   Because: matches your preferred mood (happy); matches your preferred genre (pop); energy is 0.08 from your target (0.9)
2. Gym Hero - Score: 69.71
   Because: does not match your preferred mood (happy); matches your preferred genre (pop); energy is 0.03 from your target (0.9)
3. Rooftop Lights - Score: 49.14
   Because: matches your preferred mood (happy); does not match your preferred genre (pop); energy is 0.14 from your target (0.9)
4. Golden Hour Run - Score: 28.00
   Because: does not match your preferred mood (happy); does not match your preferred genre (pop); energy is 0.01 from your target (0.9)
5. Storm Runner - Score: 28.00
   Because: does not match your preferred mood (happy); does not match your preferred genre (pop); energy is 0.01 from your target (0.9)
```

**Chill Lofi**

```text
Chill Lofi — Top 5 recommendations:

1. Midnight Coding - Score: 98.86
   Because: matches your preferred mood (chill); matches your preferred genre (lofi); energy is 0.02 from your target (0.4)
2. Library Rain - Score: 97.14
   Because: matches your preferred mood (chill); matches your preferred genre (lofi); energy is 0.05 from your target (0.4)
3. Focus Flow - Score: 71.43
   Because: does not match your preferred mood (chill); matches your preferred genre (lofi); energy is 0 from your target (0.4)
4. Spacewalk Thoughts - Score: 50.29
   Because: matches your preferred mood (chill); does not match your preferred genre (lofi); energy is 0.12 from your target (0.4)
5. Last Call Blues - Score: 28.00
   Because: does not match your preferred mood (chill); does not match your preferred genre (lofi); energy is 0.01 from your target (0.4)
```

**Deep Intense Rock**

```text
Deep Intense Rock — Top 5 recommendations:

1. Storm Runner - Score: 99.43
   Because: matches your preferred mood (intense); matches your preferred genre (rock); energy is 0.01 from your target (0.9)
2. Gym Hero - Score: 55.43
   Because: matches your preferred mood (intense); does not match your preferred genre (rock); energy is 0.03 from your target (0.9)
3. Golden Hour Run - Score: 28.00
   Because: does not match your preferred mood (intense); does not match your preferred genre (rock); energy is 0.01 from your target (0.9)
4. Mirrorball Fever - Score: 26.29
   Because: does not match your preferred mood (intense); does not match your preferred genre (rock); energy is 0.04 from your target (0.9)
5. Iron Horizon - Score: 25.14
   Because: does not match your preferred mood (intense); does not match your preferred genre (rock); energy is 0.06 from your target (0.9)
```

**Edge Case: High-Energy Melancholy Rock**

```text
Edge Case: High-Energy Melancholy Rock — Top 5 recommendations:

1. Storm Runner - Score: 69.14
   Because: does not match your preferred mood (melancholy); matches your preferred genre (rock); energy is 0.04 from your target (0.95)
2. Last Call Blues - Score: 28.57
   Because: matches your preferred mood (melancholy); does not match your preferred genre (rock); energy is 0.56 from your target (0.95)
3. Iron Horizon - Score: 28.00
   Because: does not match your preferred mood (melancholy); does not match your preferred genre (rock); energy is 0.01 from your target (0.95)
4. Gym Hero - Score: 27.43
   Because: does not match your preferred mood (melancholy); does not match your preferred genre (rock); energy is 0.02 from your target (0.95)
5. Golden Hour Run - Score: 25.14
   Because: does not match your preferred mood (melancholy); does not match your preferred genre (rock); energy is 0.06 from your target (0.95)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

The command-line runner compares four preference profiles. For this weight-shift experiment, genre increased from 2 to 3 and mood decreased from 3 to 2; energy remained 2. All weight values remain positive, and each feature similarity remains between 0 and 1. Because the final score is a weighted average scaled by 100, this change preserves the 0–100 score range.

- **High-Energy Pop** (`pop`, `happy`, energy `0.9`): Sunrise City, Gym Hero, Rooftop Lights, Golden Hour Run, Storm Runner. Gym Hero moved ahead of Rooftop Lights when genre gained weight.
- **Chill Lofi** (`lofi`, `chill`, energy `0.4`): Midnight Coding, Library Rain, Focus Flow, Spacewalk Thoughts, Last Call Blues. Focus Flow moved ahead of Spacewalk Thoughts for the same reason.
- **Deep Intense Rock** (`rock`, `intense`, energy `0.9`): Storm Runner, Gym Hero, Golden Hour Run, Mirrorball Fever, Iron Horizon.
- **Edge Case: High-Energy Melancholy Rock** (`rock`, `melancholy`, energy `0.95`): Storm Runner, Last Call Blues, Iron Horizon, Gym Hero, Golden Hour Run. Storm Runner's score increased and Last Call Blues' decreased; neither changed position.

The edge case asks for traits that do not coexist in the catalog. Storm Runner still ranks above the only melancholy song, Last Call Blues (69.14 vs. 28.57), because the heavier genre match and close energy outweigh the mood mismatch. The Deep Intense Rock top five and the two matching top songs for Chill Lofi did not change; the pop and lofi profiles had lower-ranked songs swap order. This shows weight changes affect tradeoffs, but not necessarily every ranking.

---

## Limitations and Risks

The catalog has only 18 songs, so some genres and moods have few or no examples. Genre and mood must match exactly, and genre has a higher weight than mood, which can favor one preference over another. Energy gets no similarity credit when it differs from the target by 0.5 or more. The recommender does not use lyrics, listening history, acousticness, valence, or danceability, and it does not add variety beyond sorting by score.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Real-world music and video recommenders can use item features, such as genre, mood, or tempo, along with user activity such as plays, skips, likes, and watch history. Some also use patterns in what similar users or listeners of the same items enjoy. These signals help estimate what a person may want next, and the service ranks candidate items; different services use different methods and are more complex than this classroom simulation. This project taught me that recommendations come from turning data and preferences into scores, then ranking the results—not from a system truly understanding a person's taste.

Bias can enter through missing or underrepresented songs, strict genre and mood labels, and choices about scoring weights. For example, genre has more weight than mood here, so a genre match can outweigh a mood mismatch. A small catalog can also leave some listeners with fewer good options. The experiment with conflicting preferences showed me how a simple scoring rule can feel personalized while still producing surprising results because of its design choices.
