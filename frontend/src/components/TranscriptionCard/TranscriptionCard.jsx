import { useState } from "react";
import {
    ArrowLongLeftIcon,
    ArrowLongRightIcon,
} from "@heroicons/react/20/solid";

const teams = [
    { id: 1, name: "Heroicons", href: "#", initial: "H" },
    { id: 2, name: "Tailwind Labs", href: "#", initial: "T" },
    { id: 3, name: "Workcation", href: "#", initial: "W" },
];

function classNames(...classes) {
    return classes.filter(Boolean).join(" ");
}

export default function TranscriptionCard() {
    const [selectedTeam, setSelectedTeam] = useState(teams[0].name);

    const handleClick = (teamName) => {
        setSelectedTeam(teamName);
    };

    return (
        <div className="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow">
            <div className="px-4 py-5 sm:px-6 text-center">
                <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900">
                    Transcribed Audio
                </h1>
                <p className="mt-3 text-md">
                    Playback audio and verify the transcription.
                </p>
                <ul role="list" className="flex gap-x-3 mt-2 justify-center">
                    {teams.map((team) => (
                        <li key={team.name}>
                            <button
                                onClick={() => handleClick(team.name)}
                                className={classNames(
                                    team.name === selectedTeam
                                        ? "bg-indigo-600 text-white"
                                        : "bg-gray-200 text-gray-600 hover:bg-indigo-500 hover:text-white",
                                    "group flex items-center justify-center rounded-full h-10 w-10 transition-all"
                                )}
                            >
                                <span
                                    className={classNames(
                                        team.name === selectedTeam
                                            ? "border-white text-indigo-600"
                                            : "border-gray-400 text-gray-800 group-hover:border-white group-hover:text-indigo-600",
                                        "flex h-full w-full items-center justify-center rounded-full border bg-white text-[0.75rem] font-bold"
                                    )}
                                >
                                    {team.initial}
                                </span>
                            </button>
                        </li>
                    ))}
                </ul>
            </div>
            <div className="min-h-[50vh] flex flex-col bg-gray-50 px-4 py-5 sm:p-6">
                {/* Playback Audio */}
                <div className="overflow-hidden rounded-lg bg-gray-200">
                    <div className="px-4 py-5 sm:p-6">
                        <h3 className="text-lg font-medium leading-6 text-gray-900">
                            Audio Title
                        </h3>
                        <p className="mt-1 text-sm text-gray-500">
                            This is a description of the audio content.
                        </p>
                        <audio controls className="w-full mt-4">
                            <source
                                src="path-to-your-audio-file.mp3"
                                type="audio/mpeg"
                            />
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                </div>

                {/* Transcription Text */}
                <form action="#" className="relative mt-4">
                    <div className="overflow-hidden rounded-lg border border-gray-300 shadow-sm focus-within:border-indigo-500 focus-within:ring-1 focus-within:ring-indigo-500">
                        <input
                            id="title"
                            name="title"
                            type="text"
                            placeholder="Title"
                            className="block w-full border-0 pt-2.5 text-lg font-medium placeholder:text-gray-400 focus:ring-0"
                        />
                        <textarea
                            id="description"
                            name="description"
                            rows={2}
                            placeholder="Write a description..."
                            className="block w-full resize-none border-0 py-0 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
                        />

                        <div aria-hidden="true">
                            <div className="py-2">
                                <div className="h-9" />
                            </div>
                        </div>
                    </div>

                    <div className="absolute inset-x-px bottom-0">
                        <div className="flex items-center justify-end space-x-3 border-t border-gray-200 px-2 py-2 sm:px-3">
                            <button
                                type="submit"
                                className="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                            >
                                Save
                            </button>
                        </div>
                    </div>
                </form>

                {/* Bottom Navigation */}
                <nav className="flex items-center justify-between border-t border-gray-200 px-4 sm:px-0 mt-4">
                    <div className="-mt-px flex w-0 flex-1">
                        <a
                            href="#"
                            className="inline-flex items-center border-t-2 border-transparent pr-1 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700"
                        >
                            <ArrowLongLeftIcon
                                aria-hidden="true"
                                className="mr-3 h-5 w-5 text-gray-400"
                            />
                            Translate
                        </a>
                    </div>
                    <div className="md:-mt-px md:flex">
                        <a
                            href="#"
                            className="inline-flex items-center border-t-2 border-transparent px-4 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700"
                        >
                            Finish
                        </a>
                    </div>
                    <div className="-mt-px flex w-0 flex-1 justify-end">
                        <a
                            href="#"
                            className="inline-flex items-center border-t-2 border-transparent pl-1 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700"
                        >
                            Summary
                            <ArrowLongRightIcon
                                aria-hidden="true"
                                className="ml-3 h-5 w-5 text-gray-400"
                            />
                        </a>
                    </div>
                </nav>
            </div>
        </div>
    );
}
