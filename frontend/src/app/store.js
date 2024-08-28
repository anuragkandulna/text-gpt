/* 
    Redux store defined here
*/

import { configureStore } from "@reduxjs/toolkit";
import { userReducer } from "../features/user/userSlice";

export const store = configureStore({
    // TODO: Add configure store
    reducer: {
        user: userReducer,
    },
});
