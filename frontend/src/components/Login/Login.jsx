import React, { useEffect } from "react";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
    Dialog,
    DialogBackdrop,
    DialogPanel,
    DialogTitle,
} from "@headlessui/react";
import { CheckIcon } from "@heroicons/react/24/outline";
import { useDispatch, useSelector } from "react-redux";
import { loginUser } from "../../features/user/userSlice";
import { store } from "../../app/store";

export default function Login() {
    // 1. State variable to display <Dialog> or not.
    const [open, setOpen] = useState(true);

    // 2. Local username and password variables
    const [localUsername, setLocalUsername] = useState("");
    const [localPassword, setLocalPassword] = useState("");

    // 3. Get isAuthenticated state from the store
    const { isAuthenticated } = useSelector((state) => state.user);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    // 4. If login tab is closed the redirect to home
    useEffect(() => {
        if (!open) {
            console.log("login page was closed abruptly so go back to home.");
            navigate("/");
        }
    });

    // 5. Dispatch user credentials to redux store upon successful login attempt
    const handleLogin = async (e) => {
        e.preventDefault();

        // Send request to Login API using Async
        const response = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: localUsername,
                password: localPassword,
            }),
        });

        // Extract data from response
        const data = await response.json();
        console.log(`Login API response data: ${data}`);

        // If response = ok, then redirect to dashboard.
        if (response.ok) {
            // Store token in the store: todo
            dispatch(
                loginUser({
                    username: localUsername,
                    password: localPassword,
                    isAuthenticated: true,
                })
            );
            alert("Login successful!");
            navigate("/dashboard");
        } else {
            alert("Login Failed!!!");
        }
    };

    return (
        <>
            {/*
          This example requires updating your template:

          ```
          <html class="h-full bg-white">
          <body class="h-full">
          ```
        */}
            <Dialog open={open} onClose={setOpen} className="relative z-10">
                <DialogBackdrop
                    transition
                    className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity data-[closed]:opacity-0 data-[enter]:duration-300 data-[leave]:duration-200 data-[enter]:ease-out data-[leave]:ease-in"
                />

                <div className="fixed inset-0 z-10 w-screen overflow-y-auto">
                    <div className="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                        <DialogPanel
                            transition
                            className="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all data-[closed]:translate-y-4 data-[closed]:opacity-0 data-[enter]:duration-300 data-[leave]:duration-200 data-[enter]:ease-out data-[leave]:ease-in sm:my-8 sm:w-full sm:max-w-sm sm:p-6 data-[closed]:sm:translate-y-0 data-[closed]:sm:scale-95"
                        >
                            {/* LOGIN Starts here */}
                            <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
                                <div className="sm:mx-auto sm:w-full sm:max-w-sm">
                                    <img
                                        alt="Your Company"
                                        src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
                                        className="mx-auto h-10 w-auto"
                                    />
                                    <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
                                        Sign in to your account
                                    </h2>
                                </div>

                                <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                                    <form
                                        onSubmit={handleLogin}
                                        className="space-y-6"
                                    >
                                        <div>
                                            <label
                                                htmlFor="email"
                                                className="block text-sm font-medium leading-6 text-gray-900"
                                            >
                                                Email address
                                            </label>
                                            <div className="mt-2">
                                                <input
                                                    id="email"
                                                    name="email"
                                                    type="text"
                                                    value={localUsername}
                                                    onChange={(e) =>
                                                        setLocalUsername(
                                                            e.target.value
                                                        )
                                                    }
                                                    required
                                                    autoComplete="email"
                                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                                                />
                                            </div>
                                        </div>

                                        <div>
                                            <div className="flex items-center justify-between">
                                                <label
                                                    htmlFor="password"
                                                    className="block text-sm font-medium leading-6 text-gray-900"
                                                >
                                                    Password
                                                </label>
                                                <div className="text-sm">
                                                    <a
                                                        href="#"
                                                        className="font-semibold text-indigo-600 hover:text-indigo-500"
                                                    >
                                                        Forgot password?
                                                    </a>
                                                </div>
                                            </div>
                                            <div className="mt-2">
                                                <input
                                                    id="password"
                                                    name="password"
                                                    type="password"
                                                    value={localPassword}
                                                    onChange={(e) =>
                                                        setLocalPassword(
                                                            e.target.value
                                                        )
                                                    }
                                                    required
                                                    autoComplete="current-password"
                                                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                                                />
                                            </div>
                                        </div>

                                        <div>
                                            <button
                                                type="submit"
                                                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                                            >
                                                Sign in
                                            </button>
                                        </div>
                                    </form>

                                    <p className="mt-10 text-center text-sm text-gray-500">
                                        Not a member?{" "}
                                        <Link
                                            to="/register"
                                            className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
                                        >
                                            Register Now
                                        </Link>
                                    </p>
                                </div>
                            </div>
                        </DialogPanel>
                    </div>
                </div>
            </Dialog>
        </>
    );
}
