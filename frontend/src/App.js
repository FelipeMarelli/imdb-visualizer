import {useEffect, useState} from "react";
import axios from "axios";
import "./App.css";
import {API_BASE_URL} from "./index";

function App() {
    const [allMovies, setAllMovies] = useState([]);
    const [shownMovies, setShownMovies] = useState([]);
    const [query, setQuery] = useState("");
    const [currentPage, setCurrentPage] = useState(1);
    const [loading, setLoading] = useState(false);
    const [selectedMovie, setSelectedMovie] = useState(null);

    useEffect(() => {
        setLoading(true);
        axios.get(`${API_BASE_URL}/movies`)
          .then(response => {
              let movies = response.data["movies"];
              setAllMovies(movies);
              setShownMovies(movies);
              setLoading(false);
          })
          .catch(error => {
              console.error(error);
              setLoading(false);
          });
    }, []);

    const handleSearch = () => {
        setLoading(true);

        if (query.trim() !== "") {
            axios.get(`${API_BASE_URL}/movies?title=${query}`)
              .then(res => {
                  setShownMovies(res.data["movies"]);
                  setCurrentPage(1);
                  setLoading(false);
              })
              .catch(err => {
                  console.error("Search error:", err);
                  setLoading(false);
              });
        } else {
            setShownMovies(allMovies);
            setLoading(false);
        }
    };

    const handleSearchBarTyping = (event) => setQuery(event.target.value);

    const movies_per_page = 10;
    const indexOfLastMovieInPage = currentPage * movies_per_page;
    const indexOfFirstMovieInPage = indexOfLastMovieInPage - movies_per_page;
    const currentPageMovies = shownMovies.slice(indexOfFirstMovieInPage, indexOfLastMovieInPage);
    const totalPages = Math.ceil(shownMovies.length / movies_per_page);

    return (<div className="container">
        <h1>Visualizador de IMDb</h1>

        <input
          type="text"
          placeholder="Escribe el título de una pelicula..."
          value={query}
          onChange={handleSearchBarTyping}
        />
        <button onClick={handleSearch}>Buscar</button>

        <div className="container-movies">

            {loading ? <div className="loading">Cargando...</div>
              : <ul>
                  {currentPageMovies.length > 0 ?
                    currentPageMovies.map((movie, index) => (
                      <li key={index}>
                          <button onClick={(_) => setSelectedMovie(movie)}>
                              <strong>{movie.title}</strong> ({movie.year}) - Rating: {movie.avg_vote}
                          </button>
                      </li>)
                    ) : <p>No movies found.</p>}
              </ul>
            }

            {selectedMovie && (
              <div className="modal">
                  <div className="modal-content">
                      <span className="close" onClick={() => setSelectedMovie(null)}>&times;</span>
                      <h2>{selectedMovie.title} ({selectedMovie.year})</h2>
                      <p><strong>Genre:</strong> {selectedMovie.genre}</p>
                      <p><strong>Rating:</strong> {selectedMovie.avg_vote}</p>
                      <p><strong>Votes:</strong> {selectedMovie.votes}</p>
                      <p><strong>Duration:</strong> {selectedMovie.duration} minutes</p>
                      <p><strong>Director:</strong> {selectedMovie.director}</p>
                      <p><strong>Country:</strong> {selectedMovie.country}</p>
                      <p><strong>Language:</strong> {selectedMovie.language}</p>
                      <p><strong>Summary:</strong> {selectedMovie.description}</p>
                  </div>
              </div>
            )}
        </div>

        {totalPages > 1 && (<div className="pagination">
            <button
              className="page-button"
              onClick={() => setCurrentPage(currentPage - 1)}
              disabled={currentPage === 1}
            >
                ◀
            </button>
            <span>Página {currentPage} de {totalPages}</span>
            <button
              className="page-button"
              onClick={() => setCurrentPage(currentPage + 1)}
              disabled={currentPage === totalPages}
            >
                ▶
            </button>
        </div>)}
    </div>);
}

export default App;
