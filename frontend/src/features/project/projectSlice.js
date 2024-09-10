import { createSlice, nanoid } from "@reduxjs/toolkit";

const initialState = {
    id: "unique_ID",
    title: "project_title",
    url: "youtube_url",
    length: 30,
    sourceVideoLanguageId: "en-IN",
};

export const projectSlice = createSlice({
    name: "project",
    initialState,
    // LIST OF ALL REDUCERS
    reducers: {
        // 1. Reducer to add valid youtube link
        createProject: (state, action) => {
            (state.url = action.payload.url),
                (state.length = action.payload.length),
                (state.sourceVideoLanguageId =
                    action.payload.sourceVideoLanguageId),
                (state.id = nanoid()),
                (state.title = action.payload.title);
        },
    },
});

// 2. Export all reducers individually
export const { createProject } = projectSlice.actions;

// 3. Register the reducer to store so that the store is aware of reducers accessing the data
export default projectSlice.reducer;
