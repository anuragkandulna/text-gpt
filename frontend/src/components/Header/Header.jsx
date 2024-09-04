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

const isAuthenticated = false;
const user = {
    name: "Tom Cook",
    email: "tom@example.com",
    imageUrl:
        "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
};
// const navigation = [
//     { name: "Dashboard", href: "#", current: true },
//     { name: "Team", href: "#", current: false },
//     { name: "Projects", href: "#", current: false },
//     { name: "Calendar", href: "#", current: false },
// ];
const userNavigation = [
    { name: "Your Profile", href: "#" },
    { name: "Settings", href: "#" },
    { name: "Sign out", href: "#" },
];

function classNames(...classes) {
    return classes.filter(Boolean).join(" ");
}

export default function Navbar() {
    const navigate = useNavigate();
    // const { isAuthenticated } = useSelector((state) => state.user);
    const { isAuthenticated, isNewUser } = useSelector((state) => state.user);
    const dispatch = useDispatch();

    // 1. Check if user is authenticated when page loads display correct page.
    useEffect(() => {
        if (isAuthenticated) {
            console.log(
                `User is already authenticated.... ${isAuthenticated} Navigate to Dashboard`
            );
            navigate("/dashboard");
            // navigate("");
        } else {
            console.log(`user is not authenticated... ${isAuthenticated}`);
            navigate("/");
        }
    }, [isAuthenticated, navigate]);

    return (
        <Disclosure as="nav" className="bg-gray-800">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <div className="flex h-16 justify-between">
                    <div className="flex">
                        <div className="-ml-2 mr-2 flex items-center md:hidden"></div>
                        <div className="flex flex-shrink-0 items-center">
                            <img
                                alt="Your Company"
                                src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
                                className="h-8 w-auto"
                            />
                            <div className="ml-3">
                                <p className="text-2xl font-medium text-indigo-500">
                                    TextGPT
                                </p>
                            </div>
                        </div>
                    </div>
                    <div className="flex items-center">
                        <div className="md:ml-4 md:flex md:flex-shrink-0 md:items-center">
                            {/* <Navigate to="/login"> */}
                            {/* <button
                                type="button"
                                className="relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
                            >
                                <span className="absolute -inset-1.5" />
                                <span className="sr-only">
                                    View notifications
                                </span>
                                <UserCircleIcon
                                    aria-hidden="true"
                                    className="h-9 w-9"
                                />
                            </button> */}
                            {/* </Navigate> */}

                            {/* Profile dropdown */}
                            <Menu as="div" className="relative ml-3">
                                <div>
                                    <MenuButton className="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                                        <span className="absolute -inset-1.5" />
                                        <span className="sr-only">
                                            Open user menu
                                        </span>
                                        <img
                                            alt=""
                                            src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                                            className="h-8 w-8 rounded-full"
                                        />
                                    </MenuButton>
                                </div>
                                <MenuItems
                                    transition
                                    className="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 transition focus:outline-none data-[closed]:scale-95 data-[closed]:transform data-[closed]:opacity-0 data-[enter]:duration-100 data-[leave]:duration-75 data-[enter]:ease-out data-[leave]:ease-in"
                                >
                                    <MenuItem>
                                        <a
                                            href="#"
                                            className="block px-4 py-2 text-sm text-gray-700 data-[focus]:bg-gray-100"
                                        >
                                            Your Profile
                                        </a>
                                    </MenuItem>
                                    <MenuItem>
                                        <a
                                            href="#"
                                            className="block px-4 py-2 text-sm text-gray-700 data-[focus]:bg-gray-100"
                                        >
                                            Settings
                                        </a>
                                    </MenuItem>
                                    <MenuItem>
                                        <a
                                            href="#"
                                            className="block px-4 py-2 text-sm text-gray-700 data-[focus]:bg-gray-100"
                                        >
                                            Sign out
                                        </a>
                                    </MenuItem>
                                </MenuItems>
                            </Menu>
                        </div>
                    </div>
                </div>
            </div>
        </Disclosure>
    );
}
