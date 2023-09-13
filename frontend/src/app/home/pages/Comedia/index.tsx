import Nav from "../../components/Nav.js";
import categories from "../../genres_api/comedy_api.js";
import Row from "../../components/Row.js";
import Banner from "../../components/Banners_genders/Banner_comedy.js";
import "./index.css"



function Comedia() {
  return (
    <div className="Comedia">
      <Nav />
      <Banner />
      {categories.map((category) => {
        return (
          <Row 
            key={category.name}
            title={category.title}
            path={category.path}
            isLarge={category.isLarge}
          />
        );
      })}
    </div>
  );
}

export default Comedia;