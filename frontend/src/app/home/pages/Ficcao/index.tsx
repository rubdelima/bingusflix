import Nav from "../../components/Nav.js";
import categories from "../../genres_api/ficction_api.js";
import Row from "../../components/Row.js";
import Banner from "../../components/Banners_genders/Banner_ficction.js";
import "./index.css"



function Ficcao() {
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

export default Ficcao;