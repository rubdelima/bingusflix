import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";

import Home from "./app/home/pages/Home";
import HomePage from "./app/home/pages/HomePage";
import History from "./app/home/pages/History";

import Login from "./app/home/pages/Login";
import AccountRecovery from "./app/home/pages/AccountRecovery";
import Logged from "./app/home/pages/Logged";


const router = createBrowserRouter([
  {
    path: "*",
    Component: CreateTest,
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
    
    path: "/home",
    Component: Home,
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
    path: "/logged",
    Component: Logged,
  },
  {
    path: "/account_recovery",
    Component: AccountRecovery,
  },
  {
    path: "/home",
    Component: Home,
  }
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
