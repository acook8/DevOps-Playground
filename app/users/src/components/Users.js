import React from 'react';
import { Button } from "react-bootstrap";
// import UsersModal from './UsersModal';
import UsersTable from "./UsersTable";
function Users() {

    return(
        <div>
            <h1>Users</h1>
            {/* <UsersModal /> */}
            <UsersTable />
        </div>
    );
}
export default Users;