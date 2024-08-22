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

// All the public routes down here:
const router = createBrowserRouter(
    createRoutesFromElements(
        <Route path="/" element={<Layout />}>
            <Route path="" element={<ProductFeatures />} />
        </Route>
    )
);

createRoot(document.getElementById("root")).render(
    <StrictMode>
        <RouterProvider router={router} />
    </StrictMode>
);
