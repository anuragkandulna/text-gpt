import React, { useState, useEffect } from "react";
import {
    SOURCE_VIDEO_LANGUAGES,
    VIDEO_SEGMENT_LENGTHS,
} from "../../constants/appConstants";
import {
    ExclamationCircleIcon,
    CheckCircleIcon,
} from "@heroicons/react/20/solid";

export default function YoutubeCard() {
    // 1. Local variables
    const [isValidUrl, setIsValidUrl] = useState(null);
    const [localInputLink, setLocalInputLink] = useState("");
    const [localProjectName, setLocalProjectName] = useState("");
    const [localSourceLanguage, setLocalSourceLanguage] = useState("en-IN");

    // 2. Validate Youtube url using regex
    const validateYouTubeUrl = (url) => {
        const regex = /^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$/;
        return regex.test(url);
    };

    // 3. Function to handle input change for youtube url input field
    const handleUrlInputChange = (e) => {
        const url = e.target.value;
        setInputLink(url);
        setIsValidUrl(validateYouTubeUrl(url));
    };

    // 4. Handle Language change
    const handleLanguageChange = (e) => {
        const srcLang = e.target.value;
        setLocalSourceLanguage(srcLang);
    };

    // 5. Function to generate default project name
    const generateProjectName = () => {
        const timestamp = new Date().toISOString().replace(/[-:.]/g, "");
        return `project_${timestamp}`;
    };

    // 5. Handle Dynamic elements upon page refresh
    useEffect(() => {
        const defaultProjectName = generateProjectName();
        setLocalProjectName(defaultProjectName);
    }, []);

    // 6. Submit form and navigate to next page
    const handleStart = async (e) => {
        e.preventDefault();

        // Send request to Create Project API
        const response = await fetch(
            "http://127.0.0.1:5000/api/v1/create_new",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    title: localProjectName,
                    url: localInputLink,
                    segment_length: length,
                    video_source_language: localSourceLanguage,
                }),
            }
        );
    };

    return (
        <div className="overflow-hidden rounded-lg bg-white shadow">
            <div className="px-4 py-5 sm:p-12 text-center">
                <h1 className="text-2xl font-bold leading-tight tracking-tight text-gray-900">
                    Write me up!
                </h1>
                <p className="mt-3 text-sm text-gray-700">
                    Transcribe, Translate & Summarize any video!
                </p>
            </div>
            <div className="min-h-[50vh] flex flex-col bg-gray-50 px-4 py-5 sm:p-6">
                <form
                    onSubmit={handleStart}
                    className="space-y-6 sm:max-w-lg sm:mx-auto p-4 bg-white shadow-md rounded-md"
                >
                    <div className="w-full">
                        <label
                            htmlFor="inputLink"
                            className="block text-left text-lg font-medium text-gray-900"
                        >
                            Youtube Link
                        </label>
                        <div className="relative mt-2 rounded-md shadow-sm">
                            <input
                                id="inputLink"
                                name="inputLink"
                                type="url"
                                value={localInputLink}
                                onChange={handleUrlInputChange}
                                required
                                placeholder="https://www.youtube.com/watch?v=7hKhxDpVzU4"
                                aria-invalid={!isValidUrl}
                                aria-describedby="inputLink-feedback"
                                className={`block w-full rounded-md border-0 py-1.5 pr-10 ${
                                    isValidUrl === false
                                        ? "text-red-900 ring-red-300 placeholder:text-red-300 focus:ring-red-500"
                                        : isValidUrl === true
                                        ? "text-green-900 ring-green-300 placeholder:text-green-300 focus:ring-green-500"
                                        : "text-gray-900 ring-gray-300 placeholder:text-gray-400 focus:ring-indigo-600"
                                } ring-1 ring-inset sm:text-sm sm:leading-6`}
                            />
                            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3">
                                {isValidUrl === false ? (
                                    <ExclamationCircleIcon
                                        aria-hidden="true"
                                        className="h-5 w-5 text-red-500"
                                    />
                                ) : isValidUrl === true ? (
                                    <CheckCircleIcon
                                        aria-hidden="true"
                                        className="h-5 w-5 text-green-500"
                                    />
                                ) : null}
                            </div>
                        </div>
                        {isValidUrl === false && (
                            <p
                                id="inputLink-feedback"
                                className="mt-2 text-sm text-red-600"
                            >
                                Not a valid YouTube URL.
                            </p>
                        )}
                    </div>

                    <fieldset className="text-left">
                        <legend className="text-sm font-semibold leading-6 text-gray-900">
                            Maximum length of each segment?
                        </legend>
                        <div className="mt-2 space-y-0 sm:flex sm:items-center sm:space-x-10 sm:space-y-0">
                            {VIDEO_SEGMENT_LENGTHS.map((videoSegment) => (
                                <div
                                    key={videoSegment.id}
                                    className="flex items-center"
                                >
                                    <input
                                        defaultChecked={
                                            videoSegment.id === "len30"
                                        }
                                        id={videoSegment.id}
                                        name="segment-length"
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

                    <fieldset className="text-left">
                        <legend className="text-sm font-semibold leading-6 text-gray-900">
                            Source video language:
                        </legend>
                        <div className="mt-2 sm:max-w-xs">
                            <select
                                onChange={handleLanguageChange}
                                id="sourceVideoLanguage"
                                name="sourceVideoLanguage"
                                className="block w-full mt-1 rounded-md border-0 bg-transparent py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                            >
                                {SOURCE_VIDEO_LANGUAGES.map((videoLanguage) => (
                                    <option
                                        key={videoLanguage.id}
                                        value={videoLanguage.id}
                                    >
                                        {videoLanguage.language}
                                    </option>
                                ))}
                            </select>
                        </div>
                    </fieldset>

                    <div className="flex justify-end mt-6">
                        <button
                            type="submit"
                            className="inline-flex items-center justify-center rounded-md bg-indigo-600 px-4 py-2 text-md font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                        >
                            Start
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}
