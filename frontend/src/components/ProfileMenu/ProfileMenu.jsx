import React from "react";
import { useSelector } from "react-redux";
import { Menu, MenuButton, MenuItems, MenuItem } from "@headlessui/react";
import { UserCircleIcon } from "@heroicons/react/24/outline";
import { Link, useNavigate } from "react-router-dom";

export default function ProfileMenu() {
    const isAuthenticated = useSelector((state) => state.user.isAuthenticated);
    const navigate = useNavigate();

    const handleProfileClick = () => {
        if (!isAuthenticated) {
            navigate("/login");
        }
    };

    return (
        <Menu as="div" className="relative ml-3">
            <div>
                <MenuButton
                    onClick={handleProfileClick}
                    className={`relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800 ${
                        !isAuthenticated ? "cursor-pointer" : ""
                    }`}
                >
                    <span className="absolute -inset-1.5" />
                    <span className="sr-only">Open user menu</span>
                    {isAuthenticated ? (
                        <img
                            alt="User"
                            src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                            className="h-8 w-8 rounded-full"
                        />
                    ) : (
                        <UserCircleIcon className="h-8 w-8 text-gray-300" />
                    )}
                </MenuButton>
            </div>
            {isAuthenticated && (
                <MenuItems
                    transition
                    className="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 transition focus:outline-none data-[closed]:scale-95 data-[closed]:transform data-[closed]:opacity-0 data-[enter]:duration-100 data-[leave]:duration-75 data-[enter]:ease-out data-[leave]:ease-in"
                >
                    <MenuItem>
                        <Link
                            href="#"
                            className="block px-4 py-2 text-sm text-gray-700 data-[focus]:bg-gray-100"
                        >
                            Your Profile
                        </Link>
                    </MenuItem>
                    <MenuItem>
                        <Link
                            href="#"
                            className="block px-4 py-2 text-sm text-gray-700 data-[focus]:bg-gray-100"
                        >
                            Settings
                        </Link>
                    </MenuItem>
                    <MenuItem>
                        <Link
                            href="#"
                            className="block px-4 py-2 text-sm text-gray-700 data-[focus]:bg-gray-100"
                        >
                            Sign out
                        </Link>
                    </MenuItem>
                </MenuItems>
            )}
        </Menu>
    );
}
