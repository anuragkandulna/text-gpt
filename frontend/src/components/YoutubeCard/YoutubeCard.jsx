import React from "react";
import {
    SOURCE_VIDEO_LANGUAGES,
    VIDEO_SEGMENT_LENGTHS,
} from "../../constants/appConstants";
import { ExclamationCircleIcon } from "@heroicons/react/20/solid";

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

                    <form className="space-y-6 sm:max-w-lg sm:mx-auto p-4 bg-white shadow-md rounded-md">
                        <div className="w-full">
                            <label
                                htmlFor="inputLink"
                                className="block text-left text-sm font-medium text-gray-900"
                            >
                                Input Link
                            </label>
                            <input
                                id="inputLink"
                                name="inputLink"
                                type="url"
                                placeholder="https://www.youtube.com/watch?v=7hKhxDpVzU4"
                                aria-invalid="true"
                                aria-describedby="url-error"
                                className="block w-full mt-1 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                            />
                        </div>

                        <fieldset className="text-left">
                            <legend className="text-md font-semibold leading-6 text-gray-900">
                                Maximum length of each segment?
                            </legend>
                            <div className="mt-2 space-y-6 sm:flex sm:items-center sm:space-x-10 sm:space-y-0">
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
                            <legend className="text-md font-semibold leading-6 text-gray-900">
                                Source video language:
                            </legend>
                            <div className="mt-2 sm:max-w-xs">
                                <select
                                    id="sourceVideoLanguage"
                                    name="sourceVideoLanguage"
                                    className="block w-full mt-1 rounded-md border-0 bg-transparent py-1.5 text-gray-900 ring-1 ring-inset ring-gray-300 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                                >
                                    {SOURCE_VIDEO_LANGUAGES.map(
                                        (videoLanguage) => (
                                            <option
                                                key={videoLanguage.id}
                                                value={videoLanguage.id}
                                            >
                                                {videoLanguage.language}
                                            </option>
                                        )
                                    )}
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
        </>
    );
}
