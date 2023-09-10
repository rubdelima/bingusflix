import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import Home from "./app/home/pages/Home";
import History from "./app/home/pages/History";

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
    path: "/history",
    Component: History
  }
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
