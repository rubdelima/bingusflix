import Nav from "../../components/Nav";
import categories from "../../genres_api/suspense_api.js";
import Row from "../../components/Row";
import Banner from "../../components/Banners_genders/Banner_suspense.js";
import "./index.css"



function Suspense() {
  return (
    <div className="Suspense">
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

export default Suspense;