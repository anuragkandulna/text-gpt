import React from "react";

const notificationMethods = [
    { id: "len30", title: "30 secs" },
    { id: "len60", title: "60 secs" },
    { id: "len120", title: "120 secs" },
];

export default function YoutubeCard() {
    return (
        <>
            <div className="overflow-hidden rounded-lg bg-white shadow">
                <div className="px-4 py-5 sm:p-6">
                    {/* Content goes here */}
                    <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900 text-center">
                        Write me up!
                    </h1>
                    <div className="text-md text-center">
                        Transcribe, Translate & Summarize any video!
                    </div>
                    <form className="mt-5 sm:flex sm:items-center justify-center">
                        <div className="w-full sm:max-w-xs flex">
                            <label htmlFor="email" className="sr-only">
                                Email
                            </label>
                            <input
                                id="email"
                                name="email"
                                type="email"
                                placeholder="you@example.com"
                                className="block w-full rounded-l-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                            />
                            <button
                                type="submit"
                                className="inline-flex items-center justify-center rounded-r-md bg-indigo-600 px-3 py-2 text-md font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                            >
                                Start
                            </button>
                        </div>
                    </form>
                    <fieldset className="text-center mt-4">
                        <legend className="text-sm font-semibold leading-6 text-gray-900 -indent-24">
                            Maximum length of each segment?
                        </legend>
                        {/* <p className="mt-1 text-sm leading-6 text-gray-600">
                            How do you prefer to receive notifications?
                        </p> */}
                        <div className="mt-2 space-y-6 sm:flex sm:items-center sm:space-x-10 sm:space-y-0 justify-center">
                            {notificationMethods.map((notificationMethod) => (
                                <div
                                    key={notificationMethod.id}
                                    className="flex items-center"
                                >
                                    <input
                                        defaultChecked={
                                            notificationMethod.id === "len60"
                                        }
                                        id={notificationMethod.id}
                                        name="notification-method"
                                        type="radio"
                                        className="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"
                                    />
                                    <label
                                        htmlFor={notificationMethod.id}
                                        className="ml-3 block text-sm font-medium leading-6 text-gray-900"
                                    >
                                        {notificationMethod.title}
                                    </label>
                                </div>
                            ))}
                        </div>
                    </fieldset>
                </div>
            </div>
        </>
    );
}
