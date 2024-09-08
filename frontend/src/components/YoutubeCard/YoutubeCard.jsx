import React from "react";

const videoSegmentLengths = [
    { id: "len30", title: "30 secs" },
    { id: "len60", title: "60 secs" },
    { id: "len120", title: "120 secs" },
];

const sourceVideoLanguages = [
    { id: "en-IN", language: "English (India)" },
    { id: "hi-IN", language: "Hindi (India)" },
    { id: "bn-IN", language: "Bengali (India)" },
    { id: "en-US", language: "English (United States)" },
    { id: "en-UK", language: "English (United Kingdom)" },
];

export default function YoutubeCard() {
    return (
        <>
            <div className="overflow-hidden rounded-lg bg-white shadow">
                <div className="px-4 py-5 sm:p-12">
                    {/* Youtube page header */}
                    <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900 text-center">
                        Write me up!
                    </h1>
                    <p className="mt-3 text-md text-center">
                        Transcribe, Translate & Summarize any video!
                    </p>
                </div>
                <div className="min-h-[50vh] flex flex-col bg-gray-50 px-4 py-5 sm:p-6">
                    {/* YOUTUBE PAGE FORM */}

                    <form className="sm:flex sm:items-center justify-center">
                        <div className="w-full sm:max-w-xs flex">
                            <label htmlFor="email" className="sr-only">
                                Input Link
                            </label>
                            <input
                                id="inputLink"
                                name="inputLink"
                                type="url"
                                placeholder="https://www.youtube.com/watch?v=7hKhxDpVzU4"
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
                        <legend className="text-md font-semibold leading-6 text-gray-900 -indent-16">
                            Maximum length of each segment?
                        </legend>

                        <div className="mt-2 space-y-6 sm:flex sm:items-center sm:space-x-10 sm:space-y-0 justify-center">
                            {videoSegmentLengths.map((videoSegment) => (
                                <div
                                    key={videoSegment.id}
                                    className="flex items-center"
                                >
                                    <input
                                        defaultChecked={
                                            videoSegment.id === "len30"
                                        }
                                        id={videoSegment.id}
                                        name="notification-method"
                                        type="radio"
                                        className="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"
                                    />
                                    <label
                                        htmlFor={videoSegment.id}
                                        className="ml-3 block text-sm font-medium leading-6 text-gray-900"
                                    >
                                        {videoSegment.title}
                                    </label>
                                </div>
                            ))}
                        </div>
                    </fieldset>

                    <fieldset className="flex text-center mt-4 sm:items-center justify-center">
                        <legend className="text-md font-semibold leading-6 text-gray-900 -indent-36">
                            Source video language:
                        </legend>
                        <div className="w-full mt-2 sm:max-w-xs flex ">
                            <select
                                id="sourceVideoLanguage"
                                name="sourceVideoLanguage"
                                autoComplete="country-name"
                                className="relative block w-full rounded-md border-0 bg-transparent py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                            >
                                {sourceVideoLanguages.map((videoLanguage) => (
                                    <option key={videoLanguage.id}>
                                        {videoLanguage.language}
                                    </option>
                                ))}
                            </select>
                        </div>
                    </fieldset>
                </div>
            </div>
        </>
    );
}
