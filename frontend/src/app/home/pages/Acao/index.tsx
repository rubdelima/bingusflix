import Nav from "../../components/Nav.js";
import categories from "../../genres_api/action_api.js";
import Row from "../../components/Row.js";
import Banner from "../../components/Banners_genders/Banner_action.js";
import "./index.css"



function Acao() {
  return (
    <div className="Acao">
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

export default Acao;