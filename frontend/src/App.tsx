import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import Home from "./app/home/pages/Home";
import History from "./app/home/pages/History";
import HomePage from "./app/home/pages/HomePage";
import Subscribe from "./app/home/pages/Subscribe";
import Login from "./app/home/pages/Login";
import AccountRecovery from "./app/home/pages/AccountRecovery";
import Profiles from "./app/home/pages/Profiles";
import Comedia from "./app/home/pages/Comedia";
import Acao from "./app/home/pages/Acao";
import Ficcao from "./app/home/pages/Ficcao";
import Romance from "./app/home/pages/Romance";
import Suspense from "./app/home/pages/Suspense";
import ManageProfile from "./app/home/pages/ManageProfile";


const router = createBrowserRouter([
  {
    path: "*",
    Component: Home,
  },
  {
    path: "/users",
    Component: Subscribe,
  },
  {
    path: "/create-test",
    Component: CreateTest,
  },
  {
    path: "/tests",
    Component: ListTests,
  },
  {
    path: "/home-page",
    Component: HomePage,
  },
  {
    path: "/history",
    Component: History
  },
  {
    path: "/login",
    Component: Login,
  },
  {
    path: "/account_recovery",
    Component: AccountRecovery,

  },
  {
    path: "/profiles",
    Component: Profiles,
  },
  {
    path: "/comedia",
    Component: Comedia,
  },
  {
    path: "/acao",
    Component: Acao,
  },
  {
    path: "/ficcao",
    Component: Ficcao,
  },
  {
    path: "/romance",
    Component: Romance,
  },
  {
    path: "/suspense",
    Component: Suspense,
  },
  {
    path: "/manage_profile",
    Component: ManageProfile
  }
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
