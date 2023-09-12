import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import Home from "./app/home/pages/Home";
import HomePage from ".app/home/pages/HomePage";
import Subscribe from "./app/home/pages/Subscribe";
import Login from "./app/home/pages/Login";
import AccountRecovery from "./app/home/pages/AccountRecovery";
import Logged from "./app/home/pages/Logged";


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
    path : "/home-page",
    Component : HomePage
  }
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
