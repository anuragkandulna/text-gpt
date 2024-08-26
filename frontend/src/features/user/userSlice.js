import { createSlice } from "@reduxjs/toolkit";

const initialUser = {
    username: "user123",
    email: "user123@email.com",
    password: "password_hash",
    isAuthenticated: false,
};

export const userSlice = createSlice({
    name: "user",

    // LIST OF ALL REDUCERS
    reducers: {
        // 1. Authenticate an existing user.
        authenticateUser: (state, action) => {
            // const user = {
            //     username: "todo_name",
            //     email: "user123@email.com",
            //     password: "password_hash",
            //     isAuthenticated: false,
            // };

            // state.initialUser.push()

            // start here
            if (state.initialUser.username === 0) {
            }
        },
    },
});
