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
import AccountManagement from "./app/home/pages/AccountManagement";


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
    path: "/account-management",
    Component: AccountManagement,
  },
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
