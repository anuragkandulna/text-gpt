import {
    ArrowLongLeftIcon,
    ArrowLongRightIcon,
} from "@heroicons/react/20/solid";

export default function Example() {
    return (
        <div className="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow">
            <div className="px-4 py-5 sm:px-6">
                {/* Content goes here */}
                {/* We use less vertical padding on card headers on desktop than on body sections */}

                <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900 text-center">
                    Write me up!
                </h1>
                <p className="mt-3 text-md text-center">
                    Transcribe, Translate & Summarize any video!
                </p>
            </div>
            <div className="min-h-[50vh] flex flex-col bg-gray-50  px-4 py-5 sm:p-6">
                {/* Content goes here */}

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
