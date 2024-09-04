import React from "react";
import { useSelector } from "react-redux";
import { Navigate } from "react-router-dom";
import Dashboard from "../components/Dashboard/Dashboard";
import ProductFeatures from "../components/ProductFeatures/ProductFeatures";

function ProtectedRoute() {
    const isAuthenticated = useSelector((state) => state.user.isAuthenticated);

    if (isAuthenticated) {
        return <Dashboard />;
    }

    return <ProductFeatures />;
}

export default ProtectedRoute;
