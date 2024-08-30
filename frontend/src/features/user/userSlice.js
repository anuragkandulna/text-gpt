import { createSlice } from "@reduxjs/toolkit";

const initialUser = {
    username: "user123",
    password: "password_hash",
    cpassword: "cpassword_hash",
    token: "token",
    isAuthenticated: false,
    isNewUser: true,
};

export const userSlice = createSlice({
    name: "user",
    initialUser,
    // LIST OF ALL REDUCERS
    reducers: {
        // 1. Authenticate an existing user.
        loginUser: (state, action) => {
            // Deploy the payload from user into the store
            state.username = action.payload.username;
            state.password = action.payload.password;
            state.isAuthenticated = action.payload.isAuthenticated;
            state.isNewUser = false;
            state.token = action.payload.token;
        },

        // 2. Create a new user.
        registerUser: (state, action) => {
            state.username = action.payload.username;
            state.password = action.payload.password;
            state.isAuthenticated = action.payload.isAuthenticated;
            state.isNewUser = true;
            state.token = action.payload.token;
        },
    },
});

// 2. Export all reducers individually
export const { loginUser, registerUser } = userSlice.actions;

// 3. Register the reducer to store so that the store is aware of reducers accessing the data
export default userSlice.reducer;
