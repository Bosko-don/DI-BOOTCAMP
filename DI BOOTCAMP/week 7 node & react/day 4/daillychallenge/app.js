import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from "react-responsive-carousel";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div className="container mt-5">

      <h1 className="text-center mb-4">
        Travel Carousel
      </h1>

      <Carousel
        autoPlay
        infiniteLoop
        showThumbs={false}
        showStatus={false}
      >

        <div>
          <img
            src="https://images.unsplash.com/photo-1506744038136-46273834b3fb"
            alt="Hong Kong"
          />
          <p className="legend">Hong Kong</p>
        </div>

        <div>
          <img
            src="https://images.unsplash.com/photo-1526481280695-3c4691f22c38"
            alt="Macao"
          />
          <p className="legend">Macao</p>
        </div>

        <div>
          <img
            src="https://images.unsplash.com/photo-1549692520-acc6669e2f0c"
            alt="Japan"
          />
          <p className="legend">Japan</p>
        </div>

        <div>
          <img
            src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
            alt="Las Vegas"
          />
          <p className="legend">Las Vegas</p>
        </div>

      </Carousel>

    </div>
  );
}

export default App;