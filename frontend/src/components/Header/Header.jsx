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
import React from "react";
import { Link, NavLink } from "react-router-dom";

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
                            <button
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
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </Disclosure>
    );
}
