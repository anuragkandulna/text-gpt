import { createSlice } from "@reduxjs/toolkit";

const initialUser = {
    username: "user123",
    email: "user123@email.com",
    password: "password_hash",
    isAuthenticated: false,
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
            state.email = action.payload.email;
            state.password = action.payload.password;
            state.isAuthenticated = true;
        },
    },
});

// 2. Export all reducers individually
export const { loginUser } = userSlice.actions;

// 3. Register the reducer to store so that the store is aware of reducers accessing the data
export default userSlice.reducer;
