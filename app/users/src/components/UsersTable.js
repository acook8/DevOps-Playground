import React, { useEffect } from 'react';
import axios from 'axios';
import { Table } from "react-bootstrap";

function UsersTable() {

    let [data, setData] = React.useState([]);

    useEffect(async () => {
        const fetchData = async () => {
            const result = await axios(
                'http://192.168.0.50:5001/api/Users',
            );
            setData(result.data);
        };
        fetchData();
    }, []);

    return (
        <>
            <Table striped border hover>
                <thead>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Age</th>
                        <th>Address</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map(item => (
                        <tr>
                        <td>{item.firstName}</td>
                        <td>{item.lastName}</td>
                        <td>{item.age}</td>
                        <td>{item.address}</td>
                    </tr>
                    ))}
                    
                </tbody>
            </Table>

        </>
    )
}
export default UsersTable;