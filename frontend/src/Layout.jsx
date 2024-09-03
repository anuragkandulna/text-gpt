import React from "react";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import { Outlet } from "react-router-dom";

function Layout() {
    return (
        <>
            <div className="flex flex-col min-h-screen">
                {/* Sticky Header */}
                <Header className="sticky top-0 z-50 bg-white shadow" />

                {/* Main Content */}
                <main className="flex-grow">
                    <Outlet />
                </main>

                {/* Sticky Footer */}
                <Footer className="sticky bottom-0 z-50 bg-gray-800 text-white py-4" />
            </div>
        </>
    );
}

export default Layout;
