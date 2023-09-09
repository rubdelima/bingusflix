import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import Home from "./app/home/pages/Home";
import Subscribe from "./app/home/pages/Subscribe";

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
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
