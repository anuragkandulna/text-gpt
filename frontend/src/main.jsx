import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import {
    Route,
    RouterProvider,
    createBrowserRouter,
    createRoutesFromElements,
} from "react-router-dom";
import ProductFeatures from "./components/ProductFeatures/ProductFeatures.jsx";
import Layout from "./Layout.jsx";
import Register from "./components/Register/Register.jsx";
import Login from "./components/Login/Login.jsx";
import Card from "./components/Card.jsx";
import { Provider } from "react-redux";
import { store } from "./app/store.js";
// import ProtectedRoute from "./Routes/ProtectedRoute.js";

// All the public routes down here:
const router = createBrowserRouter(
    createRoutesFromElements(
        <Route path="/" element={<Layout />}>
            <Route path="" element={<ProductFeatures />} />
            <Route path="register" element={<Register />} />
            <Route path="login" element={<Login />} />
        </Route>
    )
);

createRoot(document.getElementById("root")).render(
    <StrictMode>
        <Provider store={store}>
            <RouterProvider router={router} />
        </Provider>
    </StrictMode>
);
