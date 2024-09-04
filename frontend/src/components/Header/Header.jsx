import {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
} from "@headlessui/react";
import {
    Bars3Icon,
    BellIcon,
    XMarkIcon,
    UserCircleIcon,
} from "@heroicons/react/24/outline";
import { PlusIcon } from "@heroicons/react/20/solid";
import React, { useEffect, useState } from "react";
import { Link, NavLink, useNavigate } from "react-router-dom";
import { store } from "../../app/store";
import { useDispatch, useSelector } from "react-redux";
import ProfileMenu from "../ProfileMenu/ProfileMenu";
import { COMPANY_URL, COMPANY_NAME } from "../../constants/companyConstants";

export default function Navbar() {
    // 1. Get isAuthenticated state from the store
    const { isAuthenticated } = useSelector((state) => state.user);
    const navigate = useNavigate();
    const dispatch = useDispatch();

    // 2. Display correct page based on isAuthenticated when page loads.
    useEffect(() => {
        if (isAuthenticated) {
            console.log(`User is already authenticated....`);
            navigate("/dashboard");
        } else {
            console.log(`user is not authenticated...`);
            navigate("/");
        }
    }, [isAuthenticated, navigate]);

    return (
        <Disclosure as="nav" className="bg-gray-800">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 min-h-16">
                <div className="flex h-16 justify-between">
                    <div className="flex">
                        <div className="flex flex-shrink-0 items-center">
                            <Link to="/" className="flex items-center">
                                <img
                                    alt="Your Company"
                                    src={COMPANY_URL}
                                    className="h-8 w-auto"
                                />
                                <div className="ml-3">
                                    <p className="text-2xl font-medium text-indigo-500">
                                        {COMPANY_NAME}
                                    </p>
                                </div>
                            </Link>
                        </div>
                    </div>
                    <div className="flex items-center">
                        <div className="md:ml-4 md:flex md:flex-shrink-0 md:items-center">
                            <ProfileMenu />
                        </div>
                    </div>
                </div>
            </div>
        </Disclosure>
    );
}
