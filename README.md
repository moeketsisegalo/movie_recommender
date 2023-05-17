# movie_recommender

This Movie Recommender App uses the spaCy library to find the most similar movie based on a given description. It reads movie titles and descriptions from a file, applies pre-trained models for preprocessing, calculates similarity scores, and recommends the most similar movie.

## Installation

To run the Movie Similarity App using Docker, follow these steps:

1. Make sure you have Docker installed on your system. Visit the official Docker website and download the appropriate version for your operating system: [https://www.docker.com/get-started](https://www.docker.com/get-started)

2. Clone this repository:
```bash
git clone https://github.com/moeketsisegalo/movie_recommender.git
```

3. Navigate to the project directory:
```bash
cd movie_recommender
```
4. Build the Docker image: 
This command will build the Docker image using the provided Dockerfile.
```bash
docker build -t movie_recommender .
```

## Usage
5. Run the Docker container:
```bash
docker run -it --rm movie_similarity_app
```
Make sure you have the movies.txt file placed in the project directory before running the Docker container.

## Credits

Author: Moeketsi Segalo

This project was developed using Python and the spaCy library. The code provided in this repository is solely developed by the author mentioned above.

