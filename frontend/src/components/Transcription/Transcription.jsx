import { useState } from "react";
import {
    ArrowLongLeftIcon,
    ArrowLongRightIcon,
    CalendarIcon,
    PaperClipIcon,
    TagIcon,
    UserCircleIcon,
} from "@heroicons/react/20/solid";
import { Radio, RadioGroup } from "@headlessui/react";

import {
    Label,
    Listbox,
    ListboxButton,
    ListboxOption,
    ListboxOptions,
} from "@headlessui/react";

const assignees = [
    { name: "Unassigned", value: null },
    {
        name: "Wade Cooper",
        value: "wade-cooper",
        avatar: "https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    },
    // More items...
];
const labels = [
    { name: "Unlabelled", value: null },
    { name: "Engineering", value: "engineering" },
    // More items...
];
const dueDates = [
    { name: "No due date", value: null },
    { name: "Today", value: "today" },
    // More items...
];

const options = [
    { name: "Pink", color: "text-pink-500" },
    { name: "Purple", color: "text-purple-500" },
    { name: "Blue", color: "text-blue-500" },
    { name: "Green", color: "text-green-500" },
    { name: "Yellow", color: "text-yellow-500" },
];

const teams = [
    { id: 1, name: "Heroicons", href: "#", initial: "H", current: false },
    { id: 2, name: "Tailwind Labs", href: "#", initial: "T", current: false },
    { id: 3, name: "Workcation", href: "#", initial: "W", current: false },
];

function classNames(...classes) {
    return classes.filter(Boolean).join(" ");
}

export default function Transcription() {
    const [assigned, setAssigned] = useState(assignees[0]);
    const [labelled, setLabelled] = useState(labels[0]);
    const [dated, setDated] = useState(dueDates[0]);
    const [selectedColor, setSelectedColor] = useState(options[1]);
    return (
        <div className="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow">
            <div className="px-4 py-5 sm:px-6">
                {/* Content goes here */}
                {/* We use less vertical padding on card headers on desktop than on body sections */}
                <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900 text-center">
                    Transcripted Audio
                </h1>
                <p className="mt-3 text-md text-center">
                    Playback audio and verify the transcription.
                </p>
                <ul role="list" className="flex gap-x-3 mt-2">
                    {teams.map((team) => (
                        <li key={team.name}>
                            <a
                                href={team.href}
                                className={classNames(
                                    team.current
                                        ? "bg-gray-50 text-indigo-600"
                                        : "text-gray-700 hover:bg-gray-50 hover:text-indigo-600",
                                    "group flex items-center justify-center rounded-md p-2"
                                )}
                            >
                                <span
                                    className={classNames(
                                        team.current
                                            ? "border-indigo-600 text-indigo-600"
                                            : "border-gray-200 text-gray-400 group-hover:border-indigo-600 group-hover:text-indigo-600",
                                        "flex h-6 w-6 items-center justify-center rounded-lg border bg-white text-[0.625rem] font-medium"
                                    )}
                                >
                                    {team.initial}
                                </span>
                            </a>
                        </li>
                    ))}
                </ul>
            </div>
            <div className="min-h-[50vh] flex flex-col bg-gray-50  px-4 py-5 sm:p-6">
                {/* PLAYBACK AUDIO */}
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

                {/* TRANSCRIPTION TEXT */}

                <form action="#" className="relative">
                    <div className="overflow-hidden rounded-lg border border-gray-300 shadow-sm focus-within:border-indigo-500 focus-within:ring-1 focus-within:ring-indigo-500">
                        <label htmlFor="title" className="sr-only">
                            Title
                        </label>
                        <input
                            id="title"
                            name="title"
                            type="text"
                            placeholder="Title"
                            className="block w-full border-0 pt-2.5 text-lg font-medium placeholder:text-gray-400 focus:ring-0"
                        />
                        <label htmlFor="description" className="sr-only">
                            Description
                        </label>
                        <textarea
                            id="description"
                            name="description"
                            rows={2}
                            placeholder="Write a description..."
                            className="block w-full resize-none border-0 py-0 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
                            defaultValue={""}
                        />

                        {/* Spacer element to match the height of the toolbar */}
                        <div aria-hidden="true">
                            <div className="py-2">
                                <div className="h-9" />
                            </div>
                            <div className="h-px" />
                            <div className="py-2">
                                <div className="py-px">
                                    <div className="h-9" />
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="absolute inset-x-px bottom-0">
                        {/* Actions: These are just examples to demonstrate the concept, replace/wire these up however makes sense for your project. */}
                        <div className="flex flex-nowrap justify-end space-x-2 px-2 py-2 sm:px-3">
                            <Listbox
                                as="div"
                                value={assigned}
                                onChange={setAssigned}
                                className="flex-shrink-0"
                            >
                                <Label className="sr-only">Assign</Label>
                                <div className="relative">
                                    <ListboxButton className="relative inline-flex items-center whitespace-nowrap rounded-full bg-gray-50 px-2 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 sm:px-3">
                                        {assigned.value === null ? (
                                            <UserCircleIcon
                                                aria-hidden="true"
                                                className="h-5 w-5 flex-shrink-0 text-gray-300 sm:-ml-1"
                                            />
                                        ) : (
                                            <img
                                                alt=""
                                                src={assigned.avatar}
                                                className="h-5 w-5 flex-shrink-0 rounded-full"
                                            />
                                        )}

                                        <span
                                            className={classNames(
                                                assigned.value === null
                                                    ? ""
                                                    : "text-gray-900",
                                                "hidden truncate sm:ml-2 sm:block"
                                            )}
                                        >
                                            {assigned.value === null
                                                ? "Assign"
                                                : assigned.name}
                                        </span>
                                    </ListboxButton>

                                    <ListboxOptions
                                        transition
                                        className="absolute right-0 z-10 mt-1 max-h-56 w-52 overflow-auto rounded-lg bg-white py-3 text-base shadow ring-1 ring-black ring-opacity-5 focus:outline-none data-[closed]:data-[leave]:opacity-0 data-[leave]:transition data-[leave]:duration-100 data-[leave]:ease-in sm:text-sm"
                                    >
                                        {assignees.map((assignee) => (
                                            <ListboxOption
                                                key={assignee.value}
                                                value={assignee}
                                                className="relative cursor-default select-none bg-white px-3 py-2 data-[focus]:bg-gray-100"
                                            >
                                                <div className="flex items-center">
                                                    {assignee.avatar ? (
                                                        <img
                                                            alt=""
                                                            src={
                                                                assignee.avatar
                                                            }
                                                            className="h-5 w-5 flex-shrink-0 rounded-full"
                                                        />
                                                    ) : (
                                                        <UserCircleIcon
                                                            aria-hidden="true"
                                                            className="h-5 w-5 flex-shrink-0 text-gray-400"
                                                        />
                                                    )}

                                                    <span className="ml-3 block truncate font-medium">
                                                        {assignee.name}
                                                    </span>
                                                </div>
                                            </ListboxOption>
                                        ))}
                                    </ListboxOptions>
                                </div>
                            </Listbox>

                            <Listbox
                                as="div"
                                value={labelled}
                                onChange={setLabelled}
                                className="flex-shrink-0"
                            >
                                <Label className="sr-only">Add a label</Label>
                                <div className="relative">
                                    <ListboxButton className="relative inline-flex items-center whitespace-nowrap rounded-full bg-gray-50 px-2 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 sm:px-3">
                                        <TagIcon
                                            aria-hidden="true"
                                            className={classNames(
                                                labelled.value === null
                                                    ? "text-gray-300"
                                                    : "text-gray-500",
                                                "h-5 w-5 flex-shrink-0 sm:-ml-1"
                                            )}
                                        />
                                        <span
                                            className={classNames(
                                                labelled.value === null
                                                    ? ""
                                                    : "text-gray-900",
                                                "hidden truncate sm:ml-2 sm:block"
                                            )}
                                        >
                                            {labelled.value === null
                                                ? "Label"
                                                : labelled.name}
                                        </span>
                                    </ListboxButton>

                                    <ListboxOptions
                                        transition
                                        className="absolute right-0 z-10 mt-1 max-h-56 w-52 overflow-auto rounded-lg bg-white py-3 text-base shadow ring-1 ring-black ring-opacity-5 focus:outline-none data-[closed]:data-[leave]:opacity-0 data-[leave]:transition data-[leave]:duration-100 data-[leave]:ease-in sm:text-sm"
                                    >
                                        {labels.map((label) => (
                                            <ListboxOption
                                                key={label.value}
                                                value={label}
                                                className="relative cursor-default select-none bg-white px-3 py-2 data-[focus]:bg-gray-100"
                                            >
                                                <div className="flex items-center">
                                                    <span className="block truncate font-medium">
                                                        {label.name}
                                                    </span>
                                                </div>
                                            </ListboxOption>
                                        ))}
                                    </ListboxOptions>
                                </div>
                            </Listbox>

                            <Listbox
                                as="div"
                                value={dated}
                                onChange={setDated}
                                className="flex-shrink-0"
                            >
                                <Label className="sr-only">
                                    Add a due date
                                </Label>
                                <div className="relative">
                                    <ListboxButton className="relative inline-flex items-center whitespace-nowrap rounded-full bg-gray-50 px-2 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 sm:px-3">
                                        <CalendarIcon
                                            aria-hidden="true"
                                            className={classNames(
                                                dated.value === null
                                                    ? "text-gray-300"
                                                    : "text-gray-500",
                                                "h-5 w-5 flex-shrink-0 sm:-ml-1"
                                            )}
                                        />
                                        <span
                                            className={classNames(
                                                dated.value === null
                                                    ? ""
                                                    : "text-gray-900",
                                                "hidden truncate sm:ml-2 sm:block"
                                            )}
                                        >
                                            {dated.value === null
                                                ? "Due date"
                                                : dated.name}
                                        </span>
                                    </ListboxButton>

                                    <ListboxOptions
                                        transition
                                        className="absolute right-0 z-10 mt-1 max-h-56 w-52 overflow-auto rounded-lg bg-white py-3 text-base shadow ring-1 ring-black ring-opacity-5 focus:outline-none data-[closed]:data-[leave]:opacity-0 data-[leave]:transition data-[leave]:duration-100 data-[leave]:ease-in sm:text-sm"
                                    >
                                        {dueDates.map((dueDate) => (
                                            <ListboxOption
                                                key={dueDate.value}
                                                value={dueDate}
                                                className="relative cursor-default select-none bg-white px-3 py-2 data-[focus]:bg-gray-100"
                                            >
                                                <div className="flex items-center">
                                                    <span className="block truncate font-medium">
                                                        {dueDate.name}
                                                    </span>
                                                </div>
                                            </ListboxOption>
                                        ))}
                                    </ListboxOptions>
                                </div>
                            </Listbox>
                        </div>
                        <div className="flex items-center justify-end space-x-3 border-t border-gray-200 px-2 py-2 sm:px-3">
                            <div className="flex-shrink-0">
                                <button
                                    type="submit"
                                    className="inline-flex items-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                                >
                                    Save
                                </button>
                            </div>
                        </div>
                    </div>
                </form>

                {/* BOTTOM NAVIGATION */}
                <nav className="flex items-center justify-between border-t border-gray-200 px-4 sm:px-0">
                    <div className="-mt-px flex w-0 flex-1">
                        <a
                            href="#"
                            className="inline-flex items-center border-t-2 border-transparent pr-1 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700"
                        >
                            <ArrowLongLeftIcon
                                aria-hidden="true"
                                className="mr-3 h-5 w-5 text-gray-400"
                            />
                            Previous
                        </a>
                    </div>
                    <div className="hidden md:-mt-px md:flex">
                        <a
                            href="#"
                            className="inline-flex items-center border-t-2 border-transparent px-4 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700"
                        >
                            1
                        </a>
                        {/* Current: "border-indigo-500 text-indigo-600", Default: "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300" */}
                        <a
                            href="#"
                            aria-current="page"
                            className="inline-flex items-center border-t-2 border-indigo-500 px-4 pt-4 text-sm font-medium text-indigo-600"
                        >
                            2
                        </a>
                        <a
                            href="#"
                            className="inline-flex items-center border-t-2 border-transparent px-4 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700"
                        >
                            3
                        </a>
                    </div>
                    <div className="-mt-px flex w-0 flex-1 justify-end">
                        <a
                            href="#"
                            className="inline-flex items-center border-t-2 border-transparent pl-1 pt-4 text-sm font-medium text-gray-500 hover:border-gray-300 hover:text-gray-700"
                        >
                            Next
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
