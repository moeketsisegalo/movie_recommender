import spacy

# Load the pre-trained model
nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):
    # Create an empty list to store movie titles and descriptions
    movies = []

    # Read the movies from the file and extract the titles and descriptions
    with open("movies.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                # the split(":") function is used to split the line into two parts at the ":" character. 
                title, desc = line.split(":")
                # The left part is assigned to the variable title, and the right part is assigned to the variable desc.
                movies.append((title.strip(), desc.strip()))

    # Apply the loaded model to perform preprocessing on the movie descriptions
    processed_descriptions = [nlp(movie_desc) for movie_title, movie_desc in movies]

    # Apply the loaded model to perform preprocessing on the input description  
    input_description = nlp(description)

    # Calculate similarity scores between input and movie descriptions
    similarity_scores = [input_description.similarity(desc) for desc in processed_descriptions]

    # Find the index of the most similar movie,it uses the max() function to find the maximum similarity score from the similarity_scores list.
    most_similar_index = similarity_scores.index(max(similarity_scores))

    # Get the titles of the movies
    titles = [title for title, movie_desc in movies]

    # Get the title of the most similar movie based on the index
    most_similar_movie_title = titles[most_similar_index]

    # Return the title of the most similar movie
    return most_similar_movie_title

# Example usage
# Set the description of the movie the user has watched
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Call the defined function to find the most similar movie based on the provided description
similar_movie = find_similar_movie(description)

# Print the recommendation for the next movie
print("Next movie recommendation:", similar_movie)






