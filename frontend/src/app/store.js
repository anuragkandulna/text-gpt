/* 
    Redux store defined here
*/

import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../features/user/userSlice";
import youtubeReducer from "../features/youtube/youtubeSlice";

export const store = configureStore({
    // TODO: Add configure store
    reducer: {
        user: userReducer,
        youtube: youtubeReducer,
    },
});
